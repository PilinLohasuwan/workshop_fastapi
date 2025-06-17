from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def roof():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
    return [
        {"id": 1, "detail": "first todos"},
        {"id": 2, "detail": "seconds todos"}
    ]

counter = 0
@app.get("/counter")
async def get_conuter():
    global counter
    counter += 1
    return {"message": f"counter = {counter}"}