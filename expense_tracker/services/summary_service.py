from sqlalchemy import select, func

from database.decoraters import with_session
from models import User, Settlement
from models.settlement import PaymentStatus
from schemas.helper import success, failure


@with_session
def user_summary(session, user_id: int) -> dict:
    """
    Get a financial summary for a user.

    Summary includes:
    - Total amount user owes others.
    - Total amount others owe user.
    - Net balance.

    Args:
        user_id (int): User ID.

    Returns:
        dict: Standard service response.
    """

    user = session.get(User, user_id)

    if not user:
        return failure(
            f"User with id={user_id} not found."
        )

    total_owed = session.scalar(
        select(
            func.sum(Settlement.amount)
        ).where(
            Settlement.from_user == user_id,
            Settlement.status == PaymentStatus.UNPAID
        )
    ) or 0

    total_receivable = session.scalar(
        select(
            func.sum(Settlement.amount)
        ).where(
            Settlement.to_user == user_id,
            Settlement.status == PaymentStatus.UNPAID
        )
    ) or 0

    net_balance = total_receivable - total_owed

    return success(
        "User summary fetched successfully.",
        {
            "user": {
                "id": user.id,
                "name": user.name
            },
            "total_owed": float(total_owed),
            "total_receivable": float(total_receivable),
            "net_balance": float(net_balance)
        }
    )

