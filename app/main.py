"""The entry point for the application."""
from fastapi import FastAPI, Path, Body, status

app = FastAPI()


@app.get(
    '/',
    tags=['Root'],
    description='The root endpoint for the application',
    response_model=dict[str, str],
    name='Root'
)
async def root() -> dict[str, str]:
    """The root endpoint for the application

    Returns:
        Dict: A dictionary containing a simple message for testing purposes
    """
    return {'Working': 'Like a butterfly, crash like a bee'}


@app.get(
    '/users/{_id: int}',
    tags=['Users'],
    name='Get User',
    description="A simple API endpoint for that emulates the structure of the real thing",
    response_model=dict[str, int]
)
async def get_user(_id: int = Path(..., ge=1)) -> dict[str: int]:
    """A simple API endpoint for that emulates the structure of the real thing

    Args:
        id (int): The id of the user

    Returns:
        Dict: A dictionary containing the user's id
    """
    return {'id': _id}


@app.get(
    '/license-plates/{_license}',
    tags=['License Plates'],
    name='License Plates',
    description='A simple API endpoint for retrieving license plate data'
)
async def get_license_plate(_license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")) -> dict[str: str]:
    """An API endpoint to get license places

    Returns:
        dict: Some simple placeholder text
    """
    return {'license': _license}


@app.post(
    '/users',
    tags=['Users'],
    name='Create User',
    description='A simple API endpoint for creating users',
    status_code=status.HTTP_201_CREATED
)
async def create_user(name: str = Body(...), age: int = Body(...)):
    """A simple API endpoint for creating users

    Args:
        name (str): The name of the user
        age (int): The age of the user

    Returns:
        Dict: A dictionary containing the user's name and age
    """
    return {"name": name, "age": age}
