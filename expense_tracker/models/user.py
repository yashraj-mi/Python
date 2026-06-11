from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(30),nullable=False)

    expenses_paid = relationship(
        "Expense",
        back_populates="payer",

    )

    participations=relationship(
        "Participant",
        back_populates="user"
    )

    settlements_sent=relationship(
        "Settlement",
        foreign_keys="Settlement.from_user",
        back_populates="debtor"
    )
    settlements_received=relationship(
        "Settlement",
        foreign_keys="Settlement.to_user",
        back_populates="creditor"
    )

