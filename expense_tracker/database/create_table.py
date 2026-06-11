from models.user import User
from models.expense import Expense
from models.participant import Participant
from models.settlement import Settlement

from database.db import  engine,Base

def create_tables():
    Base.metadata.create_all(bind=engine)

