import json

import quart

app = quart.Quart(__name__)


@app.get("/")
async def index():
    return {"Hello": "World!"}
