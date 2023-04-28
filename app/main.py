"""The entry point for the application."""
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    """The root endpoint for the application

    Returns:
        Dict: A dictionary containing a simple message for testing purposes
    """
    return {'Working': 'Like a butterfly, crash like a bee'}
