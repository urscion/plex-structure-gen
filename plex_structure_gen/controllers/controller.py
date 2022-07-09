import logging
import pathlib
from typing import Type
from typing import Sequence

from models.model import Model
from models.media_collections import (
    MediaLibrary,
    MediaCollection,
    TvShow,
)
from models.media_item import MediaItem
from services.base import MediaDataProvider

logger = logging.getLogger(__name__)


class Controller:
    def __init__(self, model: Model):
        self.model = model

    def set_media_library(self, directory: str) -> None:
        """Set the Media Library root"""
        lib_path = pathlib.Path(directory)
        if directory and lib_path.exists() and lib_path.is_dir():
            self.model.library = MediaLibrary(lib_path)
        else:
            self.model.library = None
            logger.warning("No Media Library selected")

    def add_media(self, item: MediaItem):
        self.model.add_media_collection(item)

    def search_movie(
        self, provider: MediaDataProvider, input: str
    ) -> Sequence[Type[MediaItem]]:
        if not input:
            return []
        return provider.find_movies(input)

    def search_shows(
        self, provider: MediaDataProvider, input: str
    ) -> Sequence[Type[MediaItem]]:
        if not input:
            return []
        return provider.find_shows(input)

    def create_collection(self):
        """Create the collection on the filesystem"""
        for media in self.model.library.collection:
            # Media Collection folder does not exist. MediaFiles are not created.
            if isinstance(media, MediaCollection):
                if not media.is_real():
                    logger.info(
                        f"Creating {media.qualified_name} for {str(type(media))}"
                    )
                    media.path = self.model.library.path / media.qualified_name
                    media.path.mkdir(parents=True, exist_ok=True)

                # For TV Shows, need to create Seasons directories
                if isinstance(media, TvShow):
                    for season in media.seasons:
                        if not season.is_real():
                            logger.info(
                                f"Creating {season.qualified_name} for {str(type(media))}"
                            )
                            season.path = media.path / season.qualified_name
                            season.path.mkdir(parents=True, exist_ok=True)
