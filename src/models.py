"""
Task dataclass for the Rich Todo Console Application
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with attributes:
    id (auto-incrementing integer), title (string),
    description (string), completed (boolean with default False)
    """
    id: int
    title: str
    description: str
    completed: bool = False