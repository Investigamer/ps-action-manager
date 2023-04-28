"""
* Action Manager
* Property Data Type
"""
from typing import Union

from src._base import AMBase


class AMProperty(AMBase):
    """
    Builds a wrapper for applying a "PutProperty" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of the action class.
        value (str): String ID or Type ID of the property to apply to this action.
    """
    def __init__(self, action: Union[str, int], value: Union[str, int]):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._func = "putProperty"

    @property
    def args(self) -> list[int]:
        return [self.app.convert_id(self._action), self.app.convert_id(self._value)]
