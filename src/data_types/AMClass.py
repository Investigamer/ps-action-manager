"""
* Action Manager
* Class Data Type
"""
from typing import Union

from src._base import AMBase


class AMClass(AMBase):
    """
    Builds a wrapper for applying a "PutClass" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of the action or class.
        value (str): The class ID to set as the action's value, if required.
    """
    def __init__(self, action: Union[str, int], value: Union[str, int, None] = None):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._func = "putClass"

    @property
    def args(self) -> list[int]:
        # Value is optional
        if self._value:
            return [
                self.app.convert_id(self._action),
                self.app.convert_id(self._value)
            ]
        return [self.app.convert_id(self._action)]
