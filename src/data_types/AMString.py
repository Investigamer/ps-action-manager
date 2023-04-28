"""
* Action Manager
* String Data Type
"""
from typing import Union

from src._base import AMBase


class AMString(AMBase):
    """
    Builds a wrapper for applying a "PutName" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of this action.
        value (str): String to apply in this action.
    """
    def __init__(self, action: Union[str, int], value: str):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._func = "putString"

    @property
    def args(self) -> list[Union[str, int], str]:
        return [self.app.convert_id(self._action), self._value]
