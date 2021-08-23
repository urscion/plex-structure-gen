from dataclasses import dataclass, field
import tmdbsimple as tmdb
import __main__
import json
from pathlib import Path
import logging
from abc import ABCMeta

from .base import MediaDataProvider
from models.media_item import MediaItem, Movie, Show, Season, Episode

CREDS_PATH = Path(__main__.__file__).parent.parent / "credentials.json"
try:
    tmdb.API_KEY = json.loads(CREDS_PATH.read_text())["tmdb"]["key"]
except Exception as e:
    raise Exception("Failed to load the TMDB credentials") from e


logger = logging.getLogger(__name__)


@dataclass
class TmdbMediaItem(MediaItem, metaclass=ABCMeta):
    _data: dict = field(default_factory=dict)

    @property
    def source(self):
        return "tmdb"

    @property
    def source_id(self):
        return self._data["id"]


@dataclass
class TmdbMovie(TmdbMediaItem, Movie):
    @property
    def name(self):
        return self._data["title"]

    @property
    def year(self):
        return self._data["release_date"].split("-")[0]


@dataclass
class TmdbShow(TmdbMediaItem, Show):
    def __post_init__(self):
        show_item = tmdb.TV(self.source_id)
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
class TmdbSeason(TmdbMediaItem, Season):
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

    def find_movies(self, query: str) -> list[Movie]:
        """Find movies based on a query string.

        Args:
            query: Movie query string

        Returns:
            List of movies
        """
        search = tmdb.Search()
        search.movie(query=query)
        movies = []
        for s in search.results:
            movies.append(TmdbMovie(_data=s))
        return sorted(movies, key=lambda x: x.year)

    def find_shows(self, query: str) -> list[Show]:
        search = tmdb.Search()
        search.tv(query=query)
        shows = []
        for s in search.results:
            try:
                shows.append(TmdbShow(_data=s))
            except (AttributeError, KeyError):
                logger.exception(f"Skipping Show {s['name']}")
        return shows
