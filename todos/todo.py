# API for interacting with Todo
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Union, List

router = APIRouter()
todos = []


class Todo(BaseModel):
    """Todo model"""
    id: str
    title: str
    status: str
    time: str = None


class TodoError(BaseModel):
    """Todo error model"""
    error_msg: str
    error_details: str = None


@router.get("/")
def get_todos(limit: int = 10) -> List[Todo]:
    """
    Get list of todos
    :param limit: Number of todos. If 0 => get all the todos
    :return: List of todos
    """
    if limit == 0:
        return todos
    return todos[:limit]


@router.post("/")
def post_todo(
    *, todo_in: Union[Todo, Any]
) -> Union[Todo, TodoError]:
    """
    Create new todo or update
    :param todo_in: Todo to create or update
    :return: Todo object
    """
    global todos
    try:
        todo = Todo.model_validate(todo_in)
        todos = [todo for todo in todos if todo.id != todo_in.id]
        todos.append(todo)
        return todo
    except Exception as ex:
        error = {'error_msg': 'Error during creating or updating Todo',
                 'error_details': str(ex)}
        return error


@router.delete("/{todo_id}")
def del_todo(todo_id: str) -> str:
    """
    Delete todo
    :param todo_id: Todo Id
    :return: Todo Id of deleted todo
    """
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
    return todo_id
