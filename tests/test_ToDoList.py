import pytest
from lib.ToDoList import *

def test_add_todo_to_incomplete_list():
    incompletelist = TodoList()
    task1 = Todo("Wash Dishes")
    incompletelist.add(task1)
    assert incompletelist.incomplete() == [task1]

def test_add_todo_to_complete_list():
    completelist = TodoList()
    task1 = Todo("Wash Dishes")
    completelist.add(task1)
    assert completelist.complete() == [task1]

def test_add_task_as_complete():
    completetask = Todo()
    completelist = TodoList()
    assert Todo.mark_complete("Clean Dog") == completelist.complete("Clean Dog")

def test_add_task_as_incomplete():
    incompletetask = Todo()
    incompletelist = TodoList()
    assert Todo("Clean Dog") == incompletelist.incomplete("Clean Dog")

def test_given_up_a_task():
    incompletetask = Todo()
    incompletelist = TodoList()
    assert TodoList.give_up("Wash Dog") == incompletelist([])

