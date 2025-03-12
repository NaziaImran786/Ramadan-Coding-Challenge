import streamlit as st
import json
import os

TODO_FILE = "todo.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add Task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    st.success(f"Task added successfully: {task}")

# Complete Task
def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        st.success(f"Task {task_number} marked as completed.")
    else:
        st.error("Invalid task number.")

# Remove Task
def remove_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        st.success(f"Removed task: {removed['task']}")
    else:
        st.error("Invalid task number.")

# Streamlit UI
st.title("✅ ToDo-CLI List")

# Add Task Section
task_input = st.text_input("Add a new task")
if st.button("Add Task") and task_input:
    add_task(task_input)

# List Tasks
st.subheader("Your Tasks")
tasks = load_tasks()
if not tasks:
    st.info("No tasks available.")
else:
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        st.write(f"{index}. {task['task']} [{status}]")

# Complete Task
task_number = st.number_input("Task number to complete", min_value=1, step=1)
if st.button("Complete Task"):
    complete_task(task_number)

# Remove Task
remove_number = st.number_input("Task number to remove", min_value=1, step=1)
if st.button("Remove Task"):
    remove_task(remove_number)

st.write("---")
st.caption("Built by Nazia Imran using UV and Streamlit")





# import click  # to create a CLI
# import json  # to save and load tasks from a file
# import os  # to check if the file exists

# TODO_FILE = "todo.json"

# def load_tasks():
#     if not os.path.exists(TODO_FILE):  # Fix the condition
#         return []
#     with open(TODO_FILE, "r") as file:
#         return json.load(file)

# def save_tasks(tasks):
#     with open(TODO_FILE, "w") as file:
#         json.dump(tasks, file, indent=4)

# @click.group()
# def cli():
#     """Simple Todo List Manager"""
#     pass

# @click.command()
# @click.argument("task")
# def add(task):
#     """Add a new task to the list"""
#     tasks = load_tasks()
#     tasks.append({"task": task, "done": False})
#     save_tasks(tasks)
#     click.echo(f"Task added successfully: {task}")

# @click.command(name="list")
# def list_tasks():
#     """List all the tasks"""
#     tasks = load_tasks()
#     if not tasks:
#         click.echo("No tasks found.")
#         return
#     for index, task in enumerate(tasks, 1):
#         status = "✅" if task['done'] else '❌'
#         click.echo(f"{index}. {task['task']} [{status}]")

# @click.command()
# @click.argument("task_number", type=int)
# def complete(task_number):
#     """Mark a task as completed"""
#     tasks = load_tasks()
#     if 0 < task_number <= len(tasks):
#         tasks[task_number - 1]["done"] = True
#         save_tasks(tasks)
#         click.echo(f"Task {task_number} marked as completed.")
#     else:
#         click.echo(f"Invalid task number: {task_number}")

# @click.command()
# @click.argument("task_number", type=int)
# def remove(task_number):
#     """Remove a task from the list"""
#     tasks = load_tasks()
#     if 0 < task_number <= len(tasks):
#         removed_task = tasks.pop(task_number - 1)
#         save_tasks(tasks)
#         click.echo(f"Removed task: {removed_task['task']}")
#     else:
#         click.echo(f"Invalid task number: {task_number}")

# cli.add_command(add)
# cli.add_command(list_tasks, name="list")
# cli.add_command(complete)
# cli.add_command(remove)

# if __name__ == "__main__":
#     cli()













