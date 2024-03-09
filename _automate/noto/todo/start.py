from zrb import StrInput, Task, python_task, runner
from zrb.helper.accessories.color import colored
from zrb.helper.python_task import show_lines

from _automate.noto.log._helper import append_log, get_log_lines
from _automate.noto.todo._group import TODO_GROUP
from _automate.noto.todo._helper import get_items, get_pretty_item_lines, start_item


@python_task(
    name="start",
    group=TODO_GROUP,
    inputs=[
        StrInput(
            name="task",
            prompt="Search pattern (regex)",
            prompt_required=True,
            default="",
        ),
    ],
    retry=0,
)
def start(*args, **kwargs):
    task: Task = kwargs.get("_task")
    search = kwargs.get("task")
    items = get_items(search=search, completed=False)
    if len(items) == 0:
        show_lines(
            task,
            colored("⚠️  NOT STARTED: Task not found", color="light_red"),
            "List of available tasks:",
            *get_pretty_item_lines(get_items(completed=False)),
        )
        return
    if len(items) > 1:
        show_lines(
            task,
            colored("⚠️  NOT STARTED: Multiple task found", color="light_red"),
            "List of matched tasks:",
            *get_pretty_item_lines(items),
        )
        return
    item = items[0]
    start_item(item)
    append_log(f"__START__ {item.description}")
    show_lines(task, *get_log_lines(), "", *get_pretty_item_lines(get_items()))


runner.register(start)
