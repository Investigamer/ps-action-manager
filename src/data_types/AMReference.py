"""
* Action Manager
* Reference Data Type
"""
from typing import Union

from photoshop.api import ActionReference

from src._base import AMBaseObject, AMBase
from src._types import ActionObject


class AMReference(AMBaseObject):
    """
    Builds a wrapper for applying an ActionReference object from an action tree.

    Args:
        action (str | int): String ID or Type ID for applying this reference.
        tree (list): Tree of actions representing "Put" statements.
    """
    def __init__(self, action: Union[str, int, None] = None, tree: Union[AMBase, list[AMBase]] = None):
        # Internal attributes
        super().__init__(action, tree, ActionReference)
        self._func = 'putReference'

    @property
    def args(self) -> list[Union[str, int, ActionObject]]:
        # Do we have a valid action ID?
        if self._action:
            return [self.app.convert_id(self._action), self.get_descriptor()]
        # Return only the ActionReference
        return [self.get_descriptor()]
