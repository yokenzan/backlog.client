# -*- coding: utf-8 -*-

from typing import Union, List, Optional
from src.issue_type import *


class IssueTypeFactory:

    def generate(self, params: dict) -> IssueType:
        return IssueType(
            params['id'], params['name'], params['color'], params['displayOrder']
        )

