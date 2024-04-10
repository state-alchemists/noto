from zrb import Task, python_task, runner
from zrb.helper.task import show_lines

from ..sync import create_sync_noto_task
from ._group import noto_todo_group
from ._helper import get_todo_items, get_pretty_todo_item_lines


@python_task(
    name="list",
    group=noto_todo_group,
    retry=0,
)
def list_todo(*args, **kwargs):
    task: Task = kwargs.get("_task")
    show_lines(
        task,
        *get_pretty_todo_item_lines(get_todo_items()),
    )


create_sync_noto_task() >> list_todo
runner.register(list_todo)
