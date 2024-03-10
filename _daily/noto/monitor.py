from typing import Any

from zrb import Task, python_task, runner
from zrb.helper.python_task import show_lines

from _daily.noto._group import NOTO_GROUP
from _daily.noto.log._helper import get_log_lines
from _daily.noto.todo._helper import get_items, get_pretty_item_lines
from _daily.noto.todo.kanban._helper import get_kanban_lines


@python_task(
    name="monitor",
    group=NOTO_GROUP,
    retry=0,
)
def monitor(*args: Any, **kwargs: Any):
    task: Task = kwargs.get("_task")
    items = get_items()
    show_lines(
        task,
        *get_log_lines(),
        "",
        *get_kanban_lines(items),
        "",
        *get_pretty_item_lines(items)
    )


runner.register(monitor)
