from abc import ABC, abstractmethod
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

from .media_item import Movie


@dataclass
class LibraryItem(ABC):
    """Class for filesystem objects in the library"""

    path: Optional[Path] = field(default=None, init=False)

    def is_real(self) -> bool:
        """Determines if the file exists on the file system"""
        return self.path is not None and self.path.exists()

    def rename(self, basename: str) -> None:
        """Rename the file on the filesystem

        Args:
            basename: Basename of the media
        """
        if self.path is not None and self.is_real():
            self.path.rename(self.path.with_name(basename))


class MediaFile(LibraryItem, ABC):
    @classmethod
    @abstractmethod
    def allowed_file_names(cls) -> tuple[str]:
        """Allowed file names"""

    @classmethod
    @abstractmethod
    def allowed_file_exts(cls) -> tuple[str]:
        """Allowed file extensions"""

    def is_real(self):
        return LibraryItem.is_real(self) and self.path.is_file()


class VideoFile(MediaFile, ABC):
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def quality(self) -> str:
        """Quality of the"""
        # TODO Create enum or something


class MovieFile(VideoFile, Movie):
    """Movie file"""

    def __init__(self):
        super().__init__()


class AssetFile(MediaFile):
    """Related asset file"""

    def __init__(self):
        super().__init__()


class MediaImageAsset(ABC):
    """Image asset"""

    def __init__(self):
        self.use_simple_name = False


class Poster(AssetFile, MediaImageAsset):
    """Poster for the media"""

    def __init__(self):
        AssetFile.__init__(self)
        MediaImageAsset.__init__(self)

    def rename(self, basename: str):
        if self.use_simple_name and self.path is not None and self.is_real():
            self.path.rename(self.path.with_name("poster"))
        else:
            super().rename(basename=basename)
