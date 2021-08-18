from abc import abstractmethod
from models.media_item import MediaItem


class MediaDataProvider:
    """Abstract class for Media data providers"""

    def __init__(self):
        pass

    @abstractmethod
    def find_movies(self, name: str) -> list[MediaItem]:
        """Find a movie"""

    @abstractmethod
    def find_shows(self, name: str) -> list[MediaItem]:
        """Find a TV show"""

    @abstractmethod
    def tag(self) -> str:
        """String to use for a source id"""
