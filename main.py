#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json
from typing import Union, List, Optional

from src.user         import *
from src.issue_status import *
from src.issue_type   import *
from src.issue        import *
from src.priority     import *
from src.project      import *


class UrlGenerator:

    def __init__(self, workspace: str):
        self.base_url = 'https://' + workspace + '.backlog.jp/api/v2/'

    def generate(self, action: str) -> str:
        return self.base_url + action


class IssuePrinter:

    def sprint(self, issue: Union[Issue, List[Issue]]) -> str:
        if not isinstance(issue, Issue):
            return '\n'.join([self.sprint(i) for i in issue])

        indentation = ' ' * 8
        separator   = '-' * 100
        description = '\n'.join([indentation + i for i in issue.description.split('\n')])

        return (
            f'\n{separator}\n'
            f'〇 {issue.summary}\n\n'
            f'## 状態:\n{indentation}{str(issue.status)}\n\n'
            f'## 種別:\n{indentation}{str(issue.issueType)}\n\n'
            f'## 内容:\n{description}\n\n'
            f'## 担当:\n{indentation}{str(issue.assignee)}\n'
        )

    def sprint_row(self, issue: Issue) -> str:
        keyId   = issue.keyId
        summary = issue.summary[0:48] + '..'

        return f'{keyId:<5} - {summary}'


class IssueFactory:

    def generate(self, row: dict) -> Issue:
        return Issue(
            row['id'],
            row['issueKey'],
            row['keyId'],
            self.generateIssueType(row['issueType']),
            row['summary'],
            row['description'],
            self.generateUser(row['assignee']),
            self.generatePriority(row['priority']),
            self.generateIssueStatus(row['status'])
        )

    def generateIssueType(self, params: dict) -> IssueType:
        return IssueType(
            params['id'], params['name'], params['color'], params['displayOrder']
        )

    def generateIssueStatus(self, params: dict) -> IssueStatus:
        return IssueStatus(
            params['id'], params['name'], params['color'], params['displayOrder']
        )

    def generatePriority(self, params: dict) -> Priority:
        return Priority(params['id'], params['name'])

    def generateUser(self, params: Optional[dict]) -> Optional[User]:
        if params is None:
            return None
        else:
            return User(params['id'], params['userId'], params['name'], params['roleType'])


class UpdateStatus:

    def __init__(self, timestamp: str, user: User):
        self.timestamp = timestamp
        self.user      = user

    def __str__(self):
        return 'UpdateStatus: ' + ', '.join([
            self.timestamp,
            str(self.user),
        ])



with open('./config.json') as f: config = json.load(f)

urlgen    = UrlGenerator(config.get('workspace'))

# url       = urlgen.generate('users/myself')
# response  = requests.get(url, config)
# items     = response.json()
# myself    = User(items.get('id'), items.get('userId'), items.get('name'), items.get('roleType'))
# print(myself)
# print('-' * 50)


# project_url = urlgen.generate('projects')
# [print(Project(i.get('id'), i.get('projectKey'), i.get('name'))) for i in requests.get(project_url, config).json()]
#
# print('-' * 50)

copied_config            = config.copy()
copied_config['count']   = 30
copied_config['keyword'] = "集計"
del copied_config['workspace']

issue_url = urlgen.generate('issues')
response  = requests.get(issue_url, copied_config)

factory = IssueFactory()
issues  = [factory.generate(i) for i in response.json()]
printer = IssuePrinter()



import curses

try:
    stdscr = curses.initscr()

    stdscr.clear()
    stdscr.addstr(0, 0,  '課題一覧')
    stdscr.addstr(1, 8, f'キーワード:{copied_config["keyword"]}')
    for i, v in enumerate(issues): stdscr.addstr(i + 5, 2, printer.sprint_row(v))
    stdscr.refresh()
    stdscr.getkey()
finally:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

