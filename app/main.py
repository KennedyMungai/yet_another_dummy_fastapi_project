"""The entrypoint for the FastAPI application"""
from os import path
from fastapi import FastAPI, status, Response
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    """The template for the Post data

    Args:
        BaseModel (A class from pydantic ): No clue
    """
    title: str
    nb_views: int


class PublicPost(BaseModel):
    """The template for the public Post data

    Args:
        BaseModel (Pydantic): Base class for Pydantic models
    """
    title: str


# Dummy Database
posts = {
    1: Post(title="First Post", nb_views=100),
}


@app.get(
    "/posts/{_id: int}",
    tags=["Posts"],
    name='Fetch Posts',
    description='This endpoint fetches posts from the database',
    response_model=PublicPost,
    status_code=status.HTTP_200_OK
)
async def get_post(_id: int) -> dict[int, Post]:
    """An endpoint for getting posts from the database

    Returns:
        dict[int, Post]: _description_
    """

    return posts[_id]


@app.put('/posts/{id: int}')
async def update_or_create_post(_id: int, _post: Post, _response: Response):
    """The creating ir updating posts endpoint

    Args:
        _id (int): The id of the post
        _post (Post): The post
        _response (Response): The response in a predetermined template

    Returns:
        Post: A post
    """
    if _id not in posts:
        response.status_code = status.HTTP_201_CREATED

    posts[id] = post
    return posts[id]


@app.get('/redirect')
async def redirect():
    """The redirect endpoint

    Returns:
        RedirectResponse: A redirect response
    """
    return RedirectResponse('/new-url', status_code=status.HTTP_301_MOVED_PERMANENTLY)


@app.get('/cat', tags=['Files'], name='Cat Pic', description='Downloading a cat pic', response_class=FileResponse)
async def get_cat():
    """The cat pic download endpoint

    Returns:
        FileResponse: The file download class
    """
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = path.join(root_directory, 'assets', 'cat.jpg')

    return FileResponse(picture_path)
