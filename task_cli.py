import sys
import json
import os
from datetime import datetime

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def get_timestamp():
    return datetime.now().isoformat()
def add_task(description):
    tasks = load_tasks()
    new_id = max([t['id'] for t in tasks], default=0) + 1
    task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': get_timestamp(),
        'updatedAt': get_timestamp()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {new_id})')

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = get_timestamp()
            save_tasks(tasks)
            print(f'Task {task_id} updated.')
            return
    print(f'Task {task_id} not found.')

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    save_tasks(tasks)
    print(f'Task {task_id} deleted.')

def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = get_timestamp()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}.')
            return
    print(f'Task {task_id} not found.')

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t['status'] == filter_status]
    for t in tasks:
        print(f"{t['id']}: {t['description']} [{t['status']}] (Created: {t['createdAt']})")
if __name__ == '__main__':
    args = sys.argv[1:]

    if not args:
        print("Usage: task-cli <command> [args]")
        sys.exit(1)

    command = args[0]

    if command == 'add' and len(args) >= 2:
        add_task(' '.join(args[1:]))
    elif command == 'update' and len(args) >= 3:
        update_task(int(args[1]), ' '.join(args[2:]))
    elif command == 'delete' and len(args) == 2:
        delete_task(int(args[1]))
    elif command == 'mark-in-progress' and len(args) == 2:
        change_status(int(args[1]), 'in-progress')
    elif command == 'mark-done' and len(args) == 2:
        change_status(int(args[1]), 'done')
    elif command == 'list':
        status = args[1] if len(args) == 2 else None
        list_tasks(status)
    else:
        print("Invalid command or arguments.")
