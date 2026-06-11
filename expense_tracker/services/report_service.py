from datetime import date
from sqlalchemy import select, extract
from database.decoraters import with_session
from models import Expense, Participant, User
from schemas.helper import success, failure


@with_session
def get_user_expenses(session, user_id: int) -> dict:
    """
    Get all expenses in which a user participated.
    """

    user = session.get(User, user_id)

    if not user:
        return failure(
            f"User not found with user id: {user_id}"
        )

    expenses = []

    for participation in user.participations:

        expense = participation.expense

        expenses.append(
            {
                "expense_id": expense.id,
                "description": expense.description,
                "category": expense.category,
                "amount": expense.amount,
                "share_amount": participation.share_amount,
                "paid_by": expense.payer.name,
                "created_at": expense.created_at.isoformat()
            }
        )

    return success(
        "User expenses fetched successfully.",
        expenses
    )


@with_session
def get_monthly_expenses(session, month: int) -> dict:
    """
    Get all expenses for a given month
    in the current year.
    """

    current_year = date.today().year

    expenses = session.scalars(
        select(Expense).where(
            extract("month", Expense.created_at) == month,
            extract("year", Expense.created_at) == current_year
        )
    ).all()

    data = [
        {
            "expense_id": expense.id,
            "description": expense.description,
            "category": expense.category,
            "amount": expense.amount,
            "paid_by": expense.payer.name,
            "created_at": expense.created_at.isoformat()
        }
        for expense in expenses
    ]

    return success(
        f"Expenses for month {month}",
        data
    )


@with_session
def get_category_report(session, category: str) -> dict:
    """
    Get all expenses belonging to a category.
    """

    expenses = session.scalars(
        select(Expense).where(
            Expense.category == category
        )
    ).all()

    data = [
        {
            "expense_id": expense.id,
            "description": expense.description,
            "amount": expense.amount,
            "paid_by": expense.payer.name,
            "created_at": expense.created_at.isoformat()
        }
        for expense in expenses
    ]

    return success(
        f"{category} expenses fetched successfully",
        data
    )


@with_session
def get_expenses_paid_by_user(session, user_id: int) -> dict:
    """
    Get all expenses paid by a user.
    """

    user = session.get(User, user_id)

    if not user:
        return failure(
            f"User not found with user id: {user_id}"
        )

    data = [
        {
            "expense_id": expense.id,
            "description": expense.description,
            "category": expense.category,
            "amount": expense.amount,
            "created_at": expense.created_at.isoformat()
        }
        for expense in user.expenses_paid
    ]

    return success(
        "Expenses paid by user fetched successfully",
        data
    )


@with_session
def get_group_summary(session, expense_id: int) -> dict:
    """
    Get complete expense breakdown:
    who participated and their share.
    """

    expense = session.get(Expense, expense_id)

    if not expense:
        return failure(
            f"Expense not found with id: {expense_id}"
        )

    participants = [
        {
            "user_id": participant.user.id,
            "name": participant.user.name,
            "share_amount": participant.share_amount
        }
        for participant in expense.participants
    ]

    return success(
        "Expense summary fetched successfully",
        {
            "expense_id": expense.id,
            "description": expense.description,
            "category": expense.category,
            "amount": expense.amount,
            "paid_by": expense.payer.name,
            "created_at": expense.created_at.isoformat(),
            "participants": participants
        }
    )