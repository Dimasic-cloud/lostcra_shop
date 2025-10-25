from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.templates import templates


router = APIRouter()


@router.get("/")
async def home(request: Request):
    context = {
        "request": request,
        "title": "home",
        "message": "success!"
    }

    return templates.TemplateResponse("index.html", context=context)