from __future__ import annotations

from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass, field


class MediaItem(metaclass=ABCMeta):
    @property
    def display_name(self) -> str:
        if self.year > 0:
            return f"{self.name} ({self.year})"
        else:
            return f"{self.name}"

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


class Movie(MediaItem, metaclass=ABCMeta):
    """Movie"""


@dataclass
class _Show:
    seasons: list[Season] = field(default_factory=list)


class Show(_Show, metaclass=ABCMeta):
    """TV Show"""


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


class Episode(MediaItem):
    """TV Episode"""
