from database.decoraters import with_session
from models.settlement import PaymentStatus
from schemas.helper import failure,success
from sqlalchemy import  select,func
from models import Settlement,User


@with_session
def get_total_owed(session,user_id: int) -> dict:

    user=session.get(User,user_id)
    if not user:
        return failure(
            f"User not exists with id {user_id}"
        )
    total_owed=session.scalar(select(func.sum(Settlement.amount)).where(Settlement.from_user==user_id,Settlement.status==PaymentStatus.UNPAID)) or 0

    return success(
        "Total Owened balance fetched successfully!",
        {"total_owed":total_owed}
    )
@with_session
def get_total_receivable(session,user_id: int) -> dict:
    user = session.get(User, user_id)
    if not user:
        return failure(
            f"User not exists with id {user_id}"
        )
    total_receivable=session.scalar(select(func.sum(Settlement.amount)).where(Settlement.to_user==user_id,Settlement.status==PaymentStatus.UNPAID)) or 0
    return  success(
        "Total receivable balance fetched successfully!",
        {"total_receivable":total_receivable}
    )
@with_session
def get_net_balance(session,user_id:int) -> dict:
    user = session.get(User, user_id)
    if not user:
        return failure(
            f"User not exists with id {user_id}"
        )
    net_balance=get_total_receivable(user_id)["data"]["total_receivable"]-get_total_owed(user_id)["data"]["total_owed"]
    return success(
        "Total net balance fetched succesfully!",
        {"net_balance":net_balance}
    )

