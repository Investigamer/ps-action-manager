"""
Action Manager Module
"""
# Standard Imports
from typing import Union

# Third Party
from photoshop.api import DialogModes, ActionDescriptor

# Local Imports
from src._base import AMBaseObject, AMBase


class ActionManager(AMBaseObject):
    """
    Builds a Photoshop Action Manager execution tree.

    Args:
        action (str | int): String ID or Type ID for this action.
        tree (dict): Tree of actions representing "Put" statements.
        dialog (DialogModes): Dialog mode to use for this action execution.
    """
    def __init__(
            self,
            action: Union[str, int],
            tree: Union[AMBase, list[AMBase]],
            dialog: DialogModes = DialogModes.DisplayNoDialogs
    ):
        # Internal attributes
        super().__init__(action, tree, ActionDescriptor)
        self._dialog = dialog or DialogModes.DisplayNoDialogs
        self.execute()

    def execute(self):
        """Executes the full action tree."""
        self.app.executeAction(
            self.app.convert_id(self._action),
            self.get_descriptor(),
            self._dialog
        )
