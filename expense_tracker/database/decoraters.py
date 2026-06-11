# database/decorators.py
from database.db import get_session
from functools import  wraps
def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with get_session() as session:
            return func(session, *args, **kwargs)
    return wrapper