from datetime import date, timedelta
from enum import StrEnum, auto


class TaskStatus(StrEnum):
    planned = auto()
    in_progress = auto()
    blocked = auto()
    done = auto()


def is_overdue(due_date, status):
    if due_date is None:
        return False
    if (status != TaskStatus.done) and (due_date < date.today()):
        return True
    else:
        return False


def next_status(current):
    match current:
        case TaskStatus.planned:
            return TaskStatus.in_progress
        case TaskStatus.in_progress:
            return TaskStatus.done
        case TaskStatus.done | TaskStatus.blocked:
            return current


def main():
    print("Hello from learn-python!")
    yesterday = date.today() - timedelta(days=1)

    print(is_overdue(None, TaskStatus.planned))  # False
    print(is_overdue(yesterday, TaskStatus.done))  # False
    print(is_overdue(yesterday, TaskStatus.in_progress))  # True

    print(next_status(TaskStatus.planned))  # TaskStatus.in_progress
    print(next_status(TaskStatus.in_progress))  # TaskStatus.done
    print(next_status(TaskStatus.done))  # TaskStatus.done
    print(next_status(TaskStatus.blocked))  # TaskStatus.blocked


if __name__ == "__main__":
    main()
