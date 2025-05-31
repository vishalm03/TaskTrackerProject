# Task Tracker CLI

A simple command-line application to track and manage your tasks.

## Features

- Add, update, and delete tasks
- Mark tasks as TODO, In Progress, or Done
- List tasks based on their status
- Stores tasks in a local JSON file

## Usage

```bash
# Add a new task
python task_cli.py add "Buy groceries"

# Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark task as in progress
python task_cli.py mark-in-progress 1

# Mark task as done
python task_cli.py mark-done 1

# List all tasks
python task_cli.py list

# List tasks by status
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

## 🔗 Project URL  
https://github.com/vishalm03/TaskTrackerProject
