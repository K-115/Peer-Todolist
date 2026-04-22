# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todos = []

    def add(self, todo):
        # Parameters: 
        #   todo: an instance of Todo

        self.todos.append(todo)
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [todo for todo in self.todos if not todo.complete]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete


        return [todo for todo in self.todos if todo.complete]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete

        for todo in self.todos:
            todo.remove()


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        self.task = task
        self.complete = False
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False


    def mark_complete(self):
        # Returns:
        #   Nothing
        self.complete = True
        # Side-effects:
        #   Sets the complete property to True
