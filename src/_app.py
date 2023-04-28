"""
* AM Photoshop Application
* Maintains a singular Photoshop entity for use with the Action Manager and related classes.
"""
from functools import cache
from typing import Union

from _ctypes import COMError
from photoshop.api import Application


class AMPhotoshop(Application):
    _instance = None

    def __new__(cls):
        """Always return the same Photoshop Application instance on successive calls."""
        if cls._instance is None or not cls._instance.is_running(cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def is_running(cls) -> bool:
        """Check if the current Photoshop Application instance is still valid."""
        try:
            _ = cls._instance.name
            return True
        except (AttributeError, COMError):
            pass
        return False

    @cache
    def convert_id(self, index: Union[str, int]):
        """
        Converts strings using stringIDToTypeID, assumes integers are already TypeID.

        Args:
            index (str | int): StringID or TypeID.
        Returns:
            The converted ID.
        """
        if isinstance(index, str):
            return self.stringIDToTypeID(index)
        return index

    """
    CACHED CONVERSION METHODS
    """

    @cache
    def charIDToTypeID(self, index: str):
        """
        Caching handler for charIDToTypeID.
        @param index: ID to convert to TypeID.
        """
        return super().charIDToTypeID(index)

    @cache
    def stringIDToTypeID(self, index: str):
        """
        Caching handler for stringIDToTypeID.
        @param index: ID to convert to TypeID.
        """
        return super().stringIDToTypeID(index)

    @cache
    def CharIDToTypeID(self, index: str):
        """
        Caching handler for charIDToTypeID.
        @param index: ID to convert to TypeID.
        """
        return super().charIDToTypeID(index)

    @cache
    def StringIDToTypeID(self, index: str):
        """
        Caching handler for StringIDToTypeID.
        @param index: ID to convert to TypeID.
        """
        return super().stringIDToTypeID(index)
