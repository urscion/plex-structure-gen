import tmdbsimple as tmdb
import __main__
import json
from pathlib import Path
import logging

from .base import MediaDataProvider
from models.media_item import Movie, Show, Season

CREDS_PATH = Path(__main__.__file__).parent.parent / "credentials.json"
try:
    tmdb.API_KEY = json.loads(CREDS_PATH.read_text())["tmdb"]["key"]
except Exception as e:
    raise Exception("Failed to load the TMDB credentials") from e


logger = logging.getLogger(__name__)


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
        response = search.movie(query=query)
        movies = []
        for s in search.results:
            movies.append(
                Movie(
                    name=s["title"],
                    year=s["release_date"].split("-")[0],
                    source=self.tag(),
                    source_id=s["id"],
                )
            )
        return sorted(movies, key=lambda x: x.year)

    def find_shows(self, query: str) -> list[Show]:
        search = tmdb.Search()
        search.tv(query=query)
        shows = []
        for s in search.results:
            show_item = tmdb.TV(s["id"])
            try:
                show = Show(
                    name=s["name"],
                    year=s["first_air_date"].split("-")[0],
                    source=self.tag(),
                    source_id=show_item.id,
                )
                for season in show_item.info()["seasons"]:
                    try:
                        show.seasons.append(
                            Season(
                                name=season["name"],
                                number=season["season_number"],
                                year=season["air_date"].split("-")[0],
                                source=self.tag(),
                                source_id=season["id"],
                            )
                        )
                    except (AttributeError, KeyError):
                        logger.exception(
                            f"Skipping Season {season['season_number']} of {show.name}."
                        )
                shows.append(show)
            except (AttributeError, KeyError):
                logger.exception(
                    f"Skipping Show {show_item.info()['name']}: {show_item.info()}"
                )
        return shows

    def tag(self) -> str:
        return "tmdb"
