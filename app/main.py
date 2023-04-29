"""The entrypoint for the application"""
from typing import Tuple

from fastapi import Depends, FastAPI

app = FastAPI()


async def pagination(skip: int = 0, limit: int = 0) -> Tuple[int, int]:
    """A simple function that imitates pagination

    Args:
        skip (int, optional): The number of db items to be skipped. Defaults to 0.
        limit (int, optional): The number of items to be shown on screen at any given time. Defaults to 0.

    Returns:
        Tuple[int, int]: Returns a tuple of both numbers
    """
    return (skip, limit)


@app.get('/items')
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    """A simple function that lists items

    Args:
        p (Tuple[int, int], optional): A tuple of two integers. Defaults to Depends(pagination).

    Returns:
        dict: A dictionary of two integers
    """
    skip, limit = p
    return {"skip": skip, "limit": limit}
