from fastapi import FastAPI

app = FastAPI()

# root
@app.get("/")
async def root():
    return { "message": "This is root"}

# premium-content
@app.get("/premium-content")
async def get_premium():
    return { "message": "This is premium content"}
