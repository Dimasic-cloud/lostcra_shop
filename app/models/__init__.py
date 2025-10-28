from .database import engine, Base
from .users import Users

Base.metadata.create_all(bind=engine)