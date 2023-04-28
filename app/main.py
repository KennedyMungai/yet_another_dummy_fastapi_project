"""The entrypoint for the FastAPI application"""
from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    """The template for the Post data

    Args:
        BaseModel (A class from pydantic ): No clue
    """
    title: str
    nb_views: int


# Dummy Database
posts = {
    1: Post(title="First Post", nb_views=100),
}


@app.get(
    "/posts/{_id: int}",
    tags=["Posts"],
    name='Fetch Posts',
    description='This endpoint fetches posts from the database',
    response_model=Post,
    status_code=status.HTTP_200_OK
)
async def get_post(_id: int) -> dict[int, Post]:
    """An endpoint for getting posts from the database

    Returns:
        dict[int, Post]: _description_
    """

    return posts[_id]
