"""The entry point for the application."""
from fastapi import FastAPI

app = FastAPI()


@app.get('/',  tags=['Root'], description='The root endpoint for the application', response_model=dict[str, str], response_model_exclude_unset=True, name='Root')
async def root() -> dict[str, str]:
    """The root endpoint for the application

    Returns:
        Dict: A dictionary containing a simple message for testing purposes
    """
    return {'Working': 'Like a butterfly, crash like a bee'}
