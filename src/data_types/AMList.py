"""
* Action Manager
* List Data Type
"""
from typing import Union

from photoshop.api import ActionList

from src._base import AMBaseObject, AMBase
from src._types import ActionObject


class AMList(AMBaseObject):
    """
    Builds a wrapper for applying an ActionList object from an action tree.

    Args:
        action (str | int): String ID or Type ID for applying this reference.
        tree (list): Tree of actions representing "Put" statements.
    """
    def __init__(self, action: Union[str, int], tree: Union[AMBase, list[AMBase]]):
        # Internal attributes
        super().__init__(action, tree, ActionList)
        self._func = 'putList'

    @property
    def args(self) -> list[Union[ActionObject, str, int]]:
        return [self.app.convert_id(self._action), self.get_descriptor()]
