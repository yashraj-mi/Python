from sqlalchemy import Integer, String, ForeignKey
from  datetime import  date
from database.db import Base
from typing import Optional
from sqlalchemy.orm import Mapped,mapped_column,relationship

class Expense(Base):
    __tablename__ = "expenses"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    description:Mapped[str]=mapped_column(String,nullable=False)
    category:Mapped[Optional[str]]=mapped_column(String)
    amount:Mapped[float]=mapped_column(nullable=False)
    paid_by:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    created_at:Mapped[date]=mapped_column(default=date.today,nullable=False)

    payer = relationship(
        "User",
        back_populates="expenses_paid"
    )

    participants=relationship(
        "Participant",
        back_populates="expense",
        cascade="all, delete-orphan"
    )
