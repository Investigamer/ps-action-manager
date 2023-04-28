"""
* Action Manager
* Large Integer Data Type
"""
from typing import Union

from src._base import AMBase


class AMLargeInteger(AMBase):
    """
    Builds a wrapper for applying a "PutLargeInteger" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of this action.
        value (int): Large integer to apply in this action.
    """
    def __init__(self, action: Union[str, int], value: int):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._func = "putLargeInteger"

    @property
    def args(self) -> list[Union[str, int], int]:
        return [self.app.convert_id(self._action), self._value]
