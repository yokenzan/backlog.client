#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from src.api       import BacklogPyClient
from src.config    import Config
from src.usercases import *
from src.commands  import AddIssue


# class IssuePrinter:
#
#     def sprint(self, issue: Union[Issue, List[Issue]]) -> str:
#         if not isinstance(issue, Issue):
#             return '\n'.join([self.sprint(i) for i in issue])
#
#         indentation = ' ' * 8
#         separator   = '-' * 100
#         description = '\n'.join([indentation + i for i in issue.description.split('\n')])
#
#         return (
#             f'\n{separator}\n'
#             f'〇 {issue.summary}\n\n'
#             f'## 状態:\n{indentation}{str(issue.status)}\n\n'
#             f'## 種別:\n{indentation}{str(issue.issueType)}\n\n'
#             f'## 内容:\n{description}\n\n'
#             f'## 担当:\n{indentation}{str(issue.assignee)}\n'
#         )
#
#     def sprint_row(self, issue: Issue) -> str:
#         keyId   = issue.keyId
#         summary = issue.summary[0:48] + '..'
#
#         return f'{keyId:<5} - {summary}'
#
#
# class UpdateStatus:
#
#     def __init__(self, timestamp: str, user: User):
#         self.timestamp = timestamp
#         self.user      = user
#
#     def __str__(self):
#         return 'UpdateStatus: ' + ', '.join([
#             self.timestamp,
#             str(self.user),
#         ])



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



def add_issue():

    with open('./config.json') as f: config = Config(json.load(f))

    client            = BacklogPyClient(config)
    add_issue_command = AddIssue(
        GetUsers(client,         UserFactory()),
        GetPriorities(client,    PriorityFactory()),
        GetIssueTypes(client,    IssueTypeFactory()),
        GetIssueStatuses(client, IssueStatusFactory())
    )

    add_issue_command.handle()


import os
import subprocess

preferred_editor = os.environ.get('EDITOR')

if preferred_editor is None:
    preferred_editor = subprocess.run(['which', 'vi'])

import tempfile

with tempfile.NamedTemporaryFile('a+')as f:
    subprocess.call([preferred_editor, f.name])
    print(f.read())


