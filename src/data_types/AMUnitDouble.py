"""
* Action Manager
* Unit Double Data Type
"""
from typing import Union

from src._base import AMBase


class AMUnitDouble(AMBase):
    """
    Builds a wrapper for applying a "PutUnitDouble" statement to an action tree.

    Args:
        action (str | int): String ID or Type ID of this action.
        unit (str | int): Units this double should be represented in.
        value (float): Double to apply in this action.
    """
    def __init__(
        self, action: Union[str, int],
        unit: Union[str, int] = 'pixelsUnit',
        value: float = 0.000000
    ):
        # Internal attributes
        super().__init__(action)
        self._value = value
        self._unit = unit
        self._func = "putUnitDouble"

    @property
    def args(self) -> list[Union[str, int], float]:
        return [
            self.app.convert_id(self._action),
            self.app.convert_id(self._unit),
            self._value
        ]
