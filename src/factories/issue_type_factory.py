# -*- coding: utf-8 -*-

from src.models import IssueType


class IssueTypeFactory:

    def generate(self, params: dict) -> IssueType:
        return IssueType(
            params['id'], params['name'], params['color'], params['displayOrder']
        )

