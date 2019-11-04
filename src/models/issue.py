# -*- coding: utf-8 -*-


from typing import Optional

from .user         import User
from .issue_type   import IssueType
from .issue_status import IssueStatus
from .priority     import Priority

class Issue:

    def __init__(
            self,
            id:          int,
            issueKey:    str,
            keyId:       int,
            issueType:   IssueType,
            summary:     str,
            description: str,
            assignee:    Optional[User],
            priority:    Priority,
            status:      IssueStatus
        ):
        self.id          = id
        self.issueKey    = issueKey
        self.keyId       = keyId
        self.issueType   = issueType
        self.summary     = summary
        self.description = description
        self.assignee    = assignee
        self.priority    = priority
        self.status      = status

    def __str__(self):
        return 'Issue: ' + ', '.join([
            str(self.id),
            self.issueKey,
            str(self.keyId),
            str(self.issueType),
            self.summary,
            self.description,
            str(self.assignee) if isinstance(self.assignee, User) else '',
            str(self.priority),
            str(self.status)
        ])

