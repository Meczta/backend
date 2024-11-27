from fastapi import FastAPI
from .routes import user
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "root"}
