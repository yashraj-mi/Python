from sqlalchemy import select

from database.decoraters import with_session
from models import Settlement, User
from models.settlement import PaymentStatus
from schemas.helper import success, failure


@with_session
def mark_paid(session, settlement_id: int) -> dict:
    """
    Mark a settlement as paid.

    Args:
        settlement_id (int): Settlement ID.

    Returns:
        dict: Standard service response.
    """

    settlement = session.get(Settlement, settlement_id)

    if not settlement:
        return failure(
            f"Settlement with id={settlement_id} not found."
        )

    if settlement.status == PaymentStatus.PAID:
        return failure(
            "Settlement is already marked as paid."
        )

    settlement.status = PaymentStatus.PAID

    return success(
        "Settlement marked as paid.",
        {
            "id": settlement.id,
            "amount": settlement.amount,
            "status": settlement.status.value
        }
    )


@with_session
def get_pending_settlements(session, user_id: int) -> dict:
    """
    Get all unpaid settlements for a user.

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

    settlements = session.scalars(
        select(Settlement).where(
            Settlement.status == PaymentStatus.UNPAID,
            (Settlement.from_user == user_id)
            | (Settlement.to_user == user_id)
        )
    ).all()

    return success(
        "Pending settlements fetched successfully.",
        [
            {
                "id": settlement.id,
                "from_user": settlement.debtor.name,
                "to_user": settlement.creditor.name,
                "amount": settlement.amount,
                "status": settlement.status.value,
                "created_at": settlement.created_at.isoformat()
            }
            for settlement in settlements
        ]
    )


@with_session
def get_paid_settlements(session, user_id: int) -> dict:
    """
    Get all paid settlements for a user.

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

    settlements = session.scalars(
        select(Settlement).where(
            Settlement.status == PaymentStatus.PAID,
            (Settlement.from_user == user_id)
            | (Settlement.to_user == user_id)
        )
    ).all()

    return success(
        "Paid settlements fetched successfully.",
        [
            {
                "id": settlement.id,
                "from_user": settlement.debtor.name,
                "to_user": settlement.creditor.name,
                "amount": settlement.amount,
                "status": settlement.status.value,
                "created_at": settlement.created_at.isoformat()
            }
            for settlement in settlements
        ]
    )


@with_session
def get_all_settlements(session) -> dict:
    """
    Get all settlements.

    Returns:
        dict: Standard service response.
    """

    settlements = session.scalars(
        select(Settlement)
        .order_by(Settlement.created_at.desc())
    ).all()

    return success(
        "Settlements fetched successfully.",
        [
            {
                "id": settlement.id,
                "from_user": settlement.debtor.name,
                "to_user": settlement.creditor.name,
                "amount": settlement.amount,
                "status": settlement.status.value,
                "created_at": settlement.created_at.isoformat()
            }
            for settlement in settlements
        ]
    )
