from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field


@dataclass
class MediaItem(ABC):
    name: str
    year: str
    source: str
    source_id: str

    @property
    def display_name(self) -> str:
        return f"{self.name} ({self.year})"


@dataclass
class Movie(MediaItem):
    """Movie"""


@dataclass
class Show(MediaItem):
    """TV Show"""

    seasons: list[Season] = field(default_factory=list)


@dataclass
class Season(MediaItem):
    """TV Season"""

    number: int
    episodes: list[Episode] = field(default_factory=list)


@dataclass
class Episode(MediaItem):
    """TV Episode"""
