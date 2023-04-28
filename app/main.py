"""The entry point for the application."""
from fastapi import FastAPI, Path

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
