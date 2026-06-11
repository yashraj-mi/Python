from sqlalchemy import Integer, ForeignKey
from database.db import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Participant(Base):

    def __repr__(self):
        return (
            f"Participant("
            f"user_id={self.user_id}, "
            f"expense_id={self.expense_id}, "
            f"share={self.share_amount})"
        )

    __tablename__ = "expense_participant"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    expense_id:Mapped[int]=mapped_column(ForeignKey("expenses.id"))
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))
    share_amount:Mapped[float]=mapped_column(nullable=False)

    expense=relationship(
        "Expense",
        back_populates="participants"
    )

    user=relationship(
        "User",
        back_populates="participations"
    )