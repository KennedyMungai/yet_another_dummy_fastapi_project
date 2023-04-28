from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'Working': 'Like a butterfly, crash like a bee'}
