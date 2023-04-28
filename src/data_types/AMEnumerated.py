"""
* Action Manager
* Enumerated Data Type
"""
from typing import Union

from src._base import AMBase


class AMEnumerated(AMBase):
    """
    Builds a wrapper for applying a "PutEnumerated" statement to an action tree.

    Args:
        action_class (str | int): String ID or Type ID of this action's class.
        action (str | int): String ID or Type ID of this action.
        value (int): String ID or Type ID representing the enumerated value to apply to this action.
    """
    def __init__(
        self,
        action_class: Union[str, int],
        action: Union[str, int],
        value: Union[str, int, None]
    ):
        # Internal attributes
        super().__init__(action)
        self._action_class = action_class
        self._value = value
        self._func = "putEnumerated"

    @property
    def args(self) -> list[Union[str, int], int]:
        # Value is optional
        if self._value:
            return [
                self.app.convert_id(self._action_class),
                self.app.convert_id(self._action),
                self.app.convert_id(self._value)
            ]
        return [
            self.app.convert_id(self._action_class),
            self.app.convert_id(self._action)
        ]
