from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass, field


@dataclass
class MediaItem(metaclass=ABCMeta):
    @property
    def display_name(self) -> str:
        return f"{self.name} ({self.year})"

    @property
    @abstractmethod
    def name(self):
        """Media name"""

    @property
    @abstractmethod
    def year(self):
        """Media year"""

    @property
    @abstractmethod
    def source(self):
        """Media source"""

    @property
    @abstractmethod
    def source_id(self):
        """Media source_id"""


@dataclass
class Movie(MediaItem, metaclass=ABCMeta):
    """Movie"""


@dataclass
class Show(MediaItem, metaclass=ABCMeta):
    """TV Show"""

    seasons: list[Season] = field(default_factory=list)


@dataclass
class Season(MediaItem, metaclass=ABCMeta):
    """TV Season"""

    @property
    @abstractmethod
    def number(self) -> int:
        """Season number"""

    @property
    @abstractmethod
    def episodes(self) -> list[Episode]:
        """Episodes"""


@dataclass
class Episode(MediaItem):
    """TV Episode"""
