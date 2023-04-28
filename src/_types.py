"""
Type Definitions
"""
from typing import Union, Type

from photoshop.api import ActionDescriptor, ActionReference, ActionList

ActionObject = Type[Union[ActionDescriptor, ActionReference, ActionList]]
