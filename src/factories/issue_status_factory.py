# -*- coding: utf-8 -*-

from src.models import IssueStatus


class IssueStatusFactory:
    def generate(self, params: dict) -> IssueStatus:
        return IssueStatus(
            params["id"],
            params["name"],
            params["color"],
            params["displayOrder"]
        )
