"""
Test out the App
"""
# Local Imports
from src._action_manager import ActionManager
from src.data_types.AMList import AMList
from src.data_types.AMName import AMName
from src.data_types.AMReference import AMReference


def example_func():
    ActionManager(
        "show",
        AMList(
            "target",
            AMReference(
                tree=AMName(
                    "layer",
                    "Layer 1"
                )
            )
        )
    )
