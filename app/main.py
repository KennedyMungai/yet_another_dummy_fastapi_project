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


@app.get(
    '/license-plates/{_license}',
    tags=['License Plates'],
    name='License Plates',
    description='A simple API endpoint for retrieving license plate data'
)
async def get_license_plate(_license: str = Path(..., min_length=9, max_length=9)) -> dict[str: str]:
    """An API endpoint to get license places

    Returns:
        dict: Some simple placeholder text
    """
    return {'license': _license}
