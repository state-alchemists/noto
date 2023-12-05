from typing import Any
from zrb import runner, CmdTask
from .._group import noto_git_group
from ..config import NOTO_GIT_REMOTE_NAME
from ._helper import get_current_branch
from .commit import git_commit
import os

CURRENT_DIR = os.path.dirname(__file__)
NOTO_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))


def _git_push_cmd(*args: Any, **kwargs: Any):
    current_branch = get_current_branch()
    return [
        f'git push -u {NOTO_GIT_REMOTE_NAME} {current_branch}'
    ]


git_push = CmdTask(
    name='push',
    group=noto_git_group,
    upstreams=[git_commit],
    cwd=NOTO_DIR,
    cmd=_git_push_cmd
)
runner.register(git_push)
