from fastapi import FastAPI

from .routers import users, items, models


app = FastAPI()
app.include_router(users.router)
app.include_router(items.router)
app.include_router(models.router)

@app.get('/')
async def root():
  return {'message': 'Hello World'}