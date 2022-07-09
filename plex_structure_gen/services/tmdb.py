from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
import tmdbsimple as tmdbs
import __main__
import json
from pathlib import Path
import logging
import sys

from .base import MediaDataProvider
from models.media_item import MediaItem, Movie, Show, Season, Episode

logger = logging.getLogger(__name__)


def _set_api_key():
    if getattr(sys, "frozen", False):
        creds_path = Path(sys.executable).parent / "credentials.json"
    else:
        creds_path = Path(__main__.__file__).parent.parent / "credentials.json"

    try:
        tmdbs.API_KEY = json.loads(creds_path.read_text())["tmdb"]["key"]
    except Exception as e:
        raise Exception("Failed to load the TMDB credentials") from e


@dataclass
class _TmdbItemMixin:
    _data: dict = field(default_factory=dict)


class TmdbItemMixIn(_TmdbItemMixin, MediaItem):
    @property
    def source(self):
        return "tmdb"

    @property
    def source_id(self):
        return self._data["id"]

    @property
    def poster_url(self):
        return f"https://image.tmdb.org/t/p/w500{self._data['poster_path']}"


@dataclass
class TmdbMovie(Movie, TmdbItemMixIn):
    @property
    def name(self):
        return self._data["title"]

    @property
    def year(self) -> int:
        try:
            return int(self._data["release_date"].split("-")[0])
        except Exception:
            return 0


@dataclass
class TmdbShow(Show, TmdbItemMixIn):
    def __post_init__(self):
        show_item = tmdbs.TV(self.source_id)
        for season in show_item.info()["seasons"]:
            try:
                self.seasons.append(TmdbSeason(_data=season))
            except (AttributeError, KeyError):
                logger.exception(
                    f"Skipping Season {season['season_number']} of {self.name}."
                )

    @property
    def name(self):
        return self._data["name"]

    @property
    def year(self):
        return self._data["first_air_date"].split("-")[0]


@dataclass
class TmdbSeason(Season, TmdbItemMixIn):
    @property
    def name(self):
        return self._data["name"]

    @property
    def year(self):
        return self._data["air_date"].split("-")[0]

    @property
    def number(self) -> int:
        return int(self._data["season_number"])

    @property
    def episodes(self) -> list[Episode]:
        # TODO Implement
        return []


class TmdbProvider(MediaDataProvider):
    """Media data provider for The Movie DB"""

    def __init__(self):
        pass

    def find_movies(self, query: str) -> list[Type[Movie]]:
        """Find movies based on a query string.

        Args:
            query: Movie query string

        Returns:
            List of movies
        """
        search = tmdbs.Search()
        search.movie(query=query)
        movies = []
        for s in search.results:
            movies.append(TmdbMovie(_data=s))
        return sorted(movies, key=lambda x: x.year)

    def find_shows(self, query: str) -> list[Type[Show]]:
        search = tmdbs.Search()
        search.tv(query=query)
        shows: list[Type[Show]] = []
        for s in search.results:
            try:
                shows.append(TmdbShow(_data=s))
            except (AttributeError, KeyError):
                logger.exception(f"Skipping Show {s['name']}")
        return shows


_set_api_key()
