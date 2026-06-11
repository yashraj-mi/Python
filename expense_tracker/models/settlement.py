from sqlalchemy import Integer,ForeignKey
from  datetime import  date
from  enum import  Enum
from sqlalchemy import  Enum as SQLEnum
from database.db import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class PaymentStatus(Enum):
    PAID = "PAID"
    UNPAID = "UNPAID"

class Settlement(Base):
    __tablename__ = "settlement"

    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    from_user:Mapped[int]=mapped_column(ForeignKey("users.id"))
    to_user:Mapped[int]=mapped_column(ForeignKey("users.id"))
    amount:Mapped[float]=mapped_column(nullable=False)
    status:Mapped[PaymentStatus]=mapped_column(SQLEnum(PaymentStatus),nullable=False)
    created_at:Mapped[date]=mapped_column(default=date.today,nullable=False)


    debtor=relationship(
        "User",
        foreign_keys=[from_user],
        back_populates="settlements_sent"
    )

    creditor=relationship(
        "User",
        foreign_keys=[to_user],
        back_populates="settlements_received"
    )