from sqlalchemy import select
from database.decoraters import with_session
from models import Expense, Participant, Settlement
from models.settlement import PaymentStatus
from schemas.helper import success, failure


@with_session
def add_expense(session, expense_data: dict) -> dict:
    """
    Create a new expense and generate corresponding
    participant and settlement records.

    Args:
        expense_data (dict):
            {
                "description": str,
                "category": str,
                "amount": float,
                "paid_by": int,
                "participants": list[int]
            }

    Returns:
        dict: Standard service response.
    """

    try:
        participants = expense_data["participants"]

        if not participants:
            return failure(
                "At least one participant is required."
            )

        if expense_data["amount"]<0:
            return failure(
                "Expense amount can not be negative."
            )

        expense = Expense(
            description=expense_data["description"],
            category=expense_data.get("category"),
            amount=expense_data["amount"],
            paid_by=expense_data["paid_by"]
        )

        session.add(expense)
        session.flush()

        share_amount = expense.amount / len(participants)

        for user_id in participants:

            session.add(
                Participant(
                    expense_id=expense.id,
                    user_id=user_id,
                    share_amount=share_amount
                )
            )

        for user_id in participants:

            if user_id == expense.paid_by:
                continue

            session.add(
                Settlement(
                    from_user=user_id,
                    to_user=expense.paid_by,
                    amount=share_amount,
                    status=PaymentStatus.UNPAID
                )
            )

        return success(
            "Expense added successfully.",
            {
                "id": expense.id,
                "description": expense.description,
                "amount": expense.amount,
                "participant_count": len(participants)
            }
        )

    except Exception as e:
        return failure(str(e))


@with_session
def get_expense(session, expense_id: int) -> dict:
    """
    Fetch a single expense by ID.

    Args:
        expense_id (int): Expense ID.

    Returns:
        dict: Standard service response.
    """

    expense = session.scalar(
        select(Expense).where(
            Expense.id == expense_id
        )
    )

    if not expense:
        return failure(
            f"Expense with id={expense_id} not found."
        )

    return success(
        "Expense fetched successfully.",
        {
            "id": expense.id,
            "description": expense.description,
            "category": expense.category,
            "amount": expense.amount,
            "paid_by": {
                "id": expense.payer.id,
                "name": expense.payer.name
            },
            "created_at": expense.created_at.isoformat(),
            "participants": [
                {
                    "id": participant.user.id,
                    "name": participant.user.name,
                    "share_amount": participant.share_amount
                }
                for participant in expense.participants
            ]
        }
    )


@with_session
def get_all_expenses(session) -> dict:
    """
    Fetch all expenses.

    Returns:
        dict: Standard service response.
    """

    expenses = session.scalars(
        select(Expense).order_by(
            Expense.created_at.desc()
        )
    ).all()

    return success(
        "Expenses fetched successfully.",
        [
            {
                "id": expense.id,
                "description": expense.description,
                "category": expense.category,
                "amount": expense.amount,
                "paid_by": expense.payer.name,
                "created_at": expense.created_at.isoformat()
            }
            for expense in expenses
        ]
    )


@with_session
def update_expense(
    session,
    expense_id: int,
    update_data: dict
) -> dict:
    """
    Update an existing expense.

    Note:
        Amount updates are intentionally disabled
        because settlements and participant shares
        would need recalculation.

    Args:
        expense_id (int): Expense ID.
        update_data (dict): Fields to update.

    Returns:
        dict: Standard service response.
    """

    try:

        expense = session.get(
            Expense,
            expense_id
        )

        if not expense:
            return failure(
                f"Expense with id={expense_id} not found."
            )

        if "amount" in update_data:
            return failure(
                "Updating amount is not supported."
            )

        if  update_data["description"]:
            expense.description = update_data["description"]

        if update_data["category"]:
            expense.category = update_data["category"]

        return success(
            "Expense updated successfully.",
            {
                "id": expense.id,
                "description": expense.description,
                "category": expense.category,
                "amount": expense.amount
            }
        )

    except Exception as e:
        return failure(str(e))


@with_session
def delete_expense(
    session,
    expense_id: int
) -> dict:
    """
    Delete an expense.

    Args:
        expense_id (int): Expense ID.

    Returns:
        dict: Standard service response.
    """

    try:

        expense = session.get(
            Expense,
            expense_id
        )

        if not expense:
            return failure(
                f"Expense with id={expense_id} not found."
            )

        deleted_expense = {
            "id": expense.id,
            "description": expense.description,
            "amount": expense.amount
        }

        session.delete(expense)

        return success(
            "Expense deleted successfully.",
            deleted_expense
        )

    except Exception as e:
        return failure(str(e))