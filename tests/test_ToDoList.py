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
    task1.mark_complete()
    completelist.add(task1)
    assert completelist.complete() == [task1]



def test_given_up_a_task():
    incompletelist = TodoList()
    incompletetask = Todo("Wash Dog")
    assert incompletelist.give_up() == None

'''
def test_if_given_empty_task():
    with pytest.raises Value Error as e:    
    
def test_if_an_empty_list():
    raise Exception(String)

def test_give_up_task_that_doesnt_exist():
    raise Exception(String)


'''