# -*- coding: utf-8 -*-

from typing import Union, List, Optional
from src.priority import *


class PriorityFactory:

    def generate(self, params: dict) -> Priority:
        return Priority(params['id'], params['name'])

