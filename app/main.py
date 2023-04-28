"""The entry point for the application."""
from fastapi import FastAPI, Path, status, Form, File, UploadFile
from pydantic import BaseModel
from typing import List


app = FastAPI()


class User(BaseModel):
    """A class for the users

    Args:
        BaseModel (Pydantic import): No Idea
    """
    name: str
    age: int


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
async def get_license_plate(
    _license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")
) -> dict[str: str]:
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
async def create_user(_user: User) -> User:
    """A simple API endpoint for creating users

    Args:
        name (str): The name of the user
        age (int): The age of the user

    Returns:
        Dict: A dictionary containing the user's name and age
    """
    return _user


@app.post(
    '/create-user-post',
    tags=['Users'],
    name='Create User Post',
    status_code=status.HTTP_201_CREATED,
    description='A simple API endpoint for creating users using form data'
)
async def create_user_form(
    _name: str = Form(...),
    _age: int = Form(...)
):
    """A simple API endpoint for creating users using form data

    Args:
        name (str): The name of the user
        age (int): The age of the user

    Returns:
        Dict: A dictionary containing the user's name and age
    """
    return {'name': _name, 'age': _age}


@app.post(
    '/files',
    tags=['File Upload'],
    name='A simple endpoint for uploading files',
    description='A simple file uploading endpoint',
    status_code=status.HTTP_201_CREATED
)
async def upload_file(file: bytes = File(...)):
    """A simple API endpoint for uploading files

    Args:
        file (bytes): The file to be uploaded

    Returns:
        Dict: A dictionary containing the file's size
    """
    return {'file_size': len(file)}


@app.post(
    '/upload-file',
    status_code=status.HTTP_201_CREATED,
    name='Upload A file',
    description='A better way to upload files',
    tags=['File Upload']
)
async def upload_file_alternative(file: UploadFile = File(...)):
    """A simple API endpoint for uploading files

    Args:
        file (UploadFile): The file to be uploaded

    Returns:
        Dict: A dictionary containing the file's size
    """
    return {'file_name': file.filename, 'content_type': file.content_type}


@app.post('upload-many-files', tags=['File Upload'], name='Multiple Uploads', description='An endpoint to upload a bunch of files', status_code=status.HTTP_201_CREATED)
async def upload_many_files(_files: List[UploadFile] = File(...)):
    """An endpoint to upload a bunch of files to the database

    Args:
        files (list[UploadFile], optional): Uploads a bunch of files. Defaults to File(...).
    """
    return [
        for file in files:
            {"file_name": file.filename, "content_type": file.content_type}
    ]
