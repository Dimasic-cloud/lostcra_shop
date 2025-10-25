from fastapi.templating import Jinja2Templates
import os

current_dir = os.path.dirname(__file__)
templates_path = os.path.join(current_dir, "routes", "templates")
templates = Jinja2Templates(directory=templates_path)