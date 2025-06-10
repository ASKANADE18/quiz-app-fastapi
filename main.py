from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import Base, engine
import models
from Routes import quiz
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown logic (optional)

app = FastAPI(lifespan=lifespan)

app.include_router(quiz.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quiz App"}

# Serve templates and static
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_quiz(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})
