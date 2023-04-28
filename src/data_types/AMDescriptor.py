"""
* Action Manager
* Descriptor Data Type
"""
from typing import Union

from photoshop.api import ActionDescriptor

from src._base import AMBaseObject, AMBase
from src._types import ActionObject


class AMDescriptor(AMBaseObject):
    """
    Builds a wrapper for applying an ActionDescriptor object from an action tree.

    Args:
        action (str | int): String ID or Type ID for applying this action.
        action_class (str | int): String ID or Type ID for this action's class.
        tree (list): Tree of actions representing "Put" statements.
    """
    def __init__(
        self,
        action: Union[str, int],
        action_class: Union[str, int, None] = None,
        tree: Union[AMBase, list[AMBase]] = None
    ):
        # Internal attributes
        super().__init__(action, tree, ActionDescriptor)
        self._func = 'putObject'
        self._action_class = action_class

    @property
    def args(self) -> list[Union[str, int, ActionObject]]:
        # Action class is optional
        if self._action_class:
            return [
                self.app.convert_id(self._action),
                self.app.convert_id(self._action_class),
                self.get_descriptor()
            ]
        return [self.app.convert_id(self._action), self.get_descriptor()]
