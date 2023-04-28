"""
* Action Manager
* Boolean Data Type
"""
from typing import Union

from src._base import AMBase


class AMBoolean(AMBase):
    """
    Builds a wrapper for applying a "PutBoolean" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of the action.
        value (bool): The truth value of this action.
    """
    def __init__(self, action: Union[str, int], value: bool = True):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._func = "putBoolean"

    @property
    def args(self) -> list[Union[str, int], bool]:
        return [self.app.convert_id(self._action), self._value]
