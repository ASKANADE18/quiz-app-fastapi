from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import engine
import models
from routes import quiz

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quiz App API")

# Add these lines for serving static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Add this route to serve your HTML page
@app.get("/", response_class=HTMLResponse)
async def serve_quiz_page(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})

# Include your existing quiz routes
app.include_router(quiz.router)
