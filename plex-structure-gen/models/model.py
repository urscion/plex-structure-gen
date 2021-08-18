from pathlib import Path
from PySide2.QtCore import QObject, Signal
import logging

from .media_item import MediaItem
from .media_collections import MediaLibrary, MediaCollection, Movie, TvShow

logger = logging.getLogger(__name__)


class Model(QObject):
    library_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.library = None

    def set_media_library(self, path: Path):
        self.library = MediaLibrary(path=path)

    def add_media_collection(self, item: MediaItem):
        """Add a new media collection.

        Args:
            name: name of media to add

        Emits:
            library_changed
        """
        new_collection = MediaCollection.from_mediaitem(item)
        if new_collection not in self.library.collection:
            self.library.collection.append(new_collection)
            self.library_changed.emit(new_collection.name)
        else:
            logger.warning(f"{item.name} already in collection!")
        logger.info(self.library.collection)
