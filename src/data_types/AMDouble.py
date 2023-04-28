"""
* Action Manager
* Double Data Type
"""
from typing import Union

from src._base import AMBase


class AMDouble(AMBase):
    """
    Builds a wrapper for applying a "PutDouble" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of this action.
        value (float): Double to apply in this action.
    """
    def __init__(self, action: Union[str, int], value: float):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._func = "putDouble"

    @property
    def args(self) -> list[Union[str, int], float]:
        return [self.app.convert_id(self._action), self._value]
