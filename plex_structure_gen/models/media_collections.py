"""Contains media collections"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union
import logging

from .media_file import MediaFile, LibraryItem
from . import media_item

logger = logging.getLogger(__name__)


@dataclass
class MediaCollection(LibraryItem, metaclass=ABCMeta):
    """Media Collection representing a folder"""

    name: str
    year: str
    source: str = ""
    source_id: str = ""
    items: list[Union[MediaCollection, MediaFile]] = field(default_factory=list)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MediaCollection):
            return NotImplemented
        if self.name == other.name:
            return True
        return False

    def is_real(self):
        return LibraryItem.is_real(self) and self.path.is_dir()

    @property
    @abstractmethod
    def qualified_name(self):
        """Returns fully qualified name for the media"""

    @property
    def display_name(self):
        """Returns display name"""
        if self.year > 0:
            return f"{self.name} ({self.year})"
        else:
            return f"{self.name}"

    @staticmethod
    def from_mediaitem(item: media_item.MediaItem) -> MediaCollection:
        if isinstance(item, media_item.Movie):
            return Movie(
                name=item.name,
                year=item.year,
                source=item.source,
                source_id=item.source_id,
            )
        elif isinstance(item, media_item.Show):
            newshow = TvShow(
                name=item.name,
                year=item.year,
                source=item.source,
                source_id=item.source_id,
            )
            for season in item.seasons:
                newshow.seasons.append(
                    TvSeason(
                        name=season.name,
                        year=season.year,
                        source=season.source,
                        source_id=season.source_id,
                        number=season.number,
                    )
                )
            return newshow
        else:
            raise NotImplementedError(
                f"Cannot create a MediaCollection from Media item of type {str(type(item))}."
            )


@dataclass
class Movie(MediaCollection):
    """Movie (collection of files)"""

    @property
    def qualified_name(self):
        rstr = f"{self.name}"
        if self.year > 0:
            rstr += f" ({self.year})"
        rstr = (
            f"{rstr} {{{self.source}-{self.source_id}}}"
            if self.source
            else rstr
        )
        rstr = rstr.replace(":", " -")
        return rstr


@dataclass
class TvShow(MediaCollection):
    """Collection of Seasons"""

    seasons: list[TvSeason] = field(default_factory=list)

    @property
    def qualified_name(self):
        rstr = f"{self.name}"
        if self.year > 0:
            rstr += f" ({self.year})"
        rstr = (
            f"{rstr} {{{self.source}-{self.source_id}}}"
            if self.source
            else rstr
        )
        rstr = rstr.replace(":", " -")
        return rstr


@dataclass
class TvSeason(MediaCollection):
    """Collection of Episodes"""

    number: int = 0

    @property
    def qualified_name(self):
        return f"Season {self.number:02d}"


@dataclass
class MediaLibrary:
    path: Path
    collection: list[Union[MediaCollection, MediaFile]] = field(
        default_factory=list
    )

    def add_media_collection(self, name: str):
        """Add a new media collection"""
        self.collection.append(MediaCollection(name=name, year="2021"))
