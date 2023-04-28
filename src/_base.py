"""
* Action Manager Base Class
* Includes essential functionality shared by all AM classes.
"""
from functools import cached_property
from typing import Union, Type

from src._app import AMPhotoshop
from src._types import ActionObject


class AMBase:
    """
    Class with a universal Photoshop app object.

    Args:
        action (str | int): String ID or Type ID for applying this action.
    """
    app = AMPhotoshop()

    def __init__(self, action: Union[str, int, None]):
        # Initial attributes
        self._action = action
        self._func = 'putObject'

    @property
    def func(self) -> str:
        """Name of the function called to make this action's "Put" statement."""
        return self._func

    @property
    def args(self) -> list:
        """Args passed to this action's "Put" statement."""
        return []


class AMBaseObject(AMBase):
    """
    AMBase class with additional object data type functionality.
    Used for classes representing an ActionDescriptor, ActionList, or ActionReference.

    Args:
        action (str | int): String ID or Type ID for applying this action object.
        tree (list): Tree of actions representing "Put" statements.
        descriptor_type (ActionObject): ActionDescriptor, ActionReference, or ActionList.
    """
    def __init__(
        self,
        action: Union[str, int, None],
        tree: Union[AMBase, list[AMBase]],
        descriptor_type: ActionObject
    ):
        # Initial attributes
        super().__init__(action)
        self._descriptor_type = descriptor_type
        tree = tree or []
        self._tree = [tree] if not isinstance(tree, list) else tree

    @cached_property
    def descriptor(self) -> Type[ActionObject]:
        return self._descriptor_type()

    def get_descriptor(self) -> Type[ActionObject]:
        """Applies the action tree to the descriptor object returns it."""
        # Apply each object in the tree
        for action in self._tree:
            getattr(self.descriptor, action.func)(*action.args)
        return self.descriptor
