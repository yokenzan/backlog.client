#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, json
from typing import Union, List, Optional

from src.factories.issue_factory import *

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

# print('-' * 50)

# copied_config            = config.copy()
# copied_config['count']   = 30
# copied_config['keyword'] = "集計"
# del copied_config['workspace']
#
# issue_url = urlgen.generate('issues')
# response  = requests.get(issue_url, copied_config)
#
# factory = IssueFactory()
# issues  = [factory.generate(i) for i in response.json()]
# printer = IssuePrinter()
# print(printer.sprint(issues));



# import curses
#
# try:
#     stdscr = curses.initscr()
#
#     stdscr.clear()
#     stdscr.addstr(0, 0,  '課題一覧')
#     stdscr.addstr(1, 8, f'キーワード:{copied_config["keyword"]}')
#     for i, v in enumerate(issues): stdscr.addstr(i + 5, 2, printer.sprint_row(v))
#     stdscr.refresh()
#     stdscr.getkey()
# finally:
#     curses.nocbreak()
#     stdscr.keypad(False)
#     curses.echo()
#     curses.endwin()


category_url = urlgen.generate('projects/KS/categories')
response     = requests.get(category_url, config)
print(response.json())
print('-' * 50)


issue_type_factory = IssueTypeFactory()
issue_type_url     = urlgen.generate('projects/KS/issueTypes')
response           = requests.get(issue_type_url, config)
[print(issue_type_factory.generate(i).to_list_item()) for i in response.json()]
print('-' * 50)


status_factory = IssueStatusFactory()
status_url     = urlgen.generate('statuses')
response       = requests.get(status_url, config)
[print(status_factory.generate(i).to_list_item()) for i in response.json()]
print('-' * 50)


copied_config = config.copy()
del copied_config['workspace']

user_factory = UserFactory()
user_url     = urlgen.generate('projects/KS/users')
response     = requests.get(user_url, copied_config)
[print(user_factory.generate(i).to_list_item()) for i in response.json()]
print('-' * 50)


priority_factory = PriorityFactory()
priority_url     = urlgen.generate('priorities')
response         = requests.get(priority_url, config)
[print(priority_factory.generate(i).to_list_item()) for i in response.json()]
print('-' * 50)
