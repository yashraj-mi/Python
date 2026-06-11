from sqlalchemy import select
from models import User
from database.decoraters import with_session
from schemas.helper import success, failure


@with_session
def add_user(session, name: str) -> dict:
    """
    Create a new user.

    Args:
        name (str): User name.

    Returns:
        dict: Standard service response.
    """

    try:

        user = User(name=name)

        session.add(user)
        session.flush()

        return success(
            "User added successfully.",
            {
                "id": user.id,
                "name": user.name
            }
        )

    except Exception as e:
        return failure(str(e))


@with_session
def get_user(session, user_id: int) -> dict:
    """
    Fetch a single user by ID.

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

    return success(
        "User fetched successfully.",
        {
            "id": user.id,
            "name": user.name
        }
    )


@with_session
def get_all_users(session) -> dict:
    """
    Fetch all users.

    Returns:
        dict: Standard service response.
    """

    users = session.scalars(
        select(User).order_by(User.id)
    ).all()

    return success(
        "Users fetched successfully.",
        [
            {
                "id": user.id,
                "name": user.name
            }
            for user in users
        ]
    )


@with_session
def update_user(
        session,
        user_id: int,
        name: str
) -> dict:
    """
    Update user name.

    Args:
        user_id (int): User ID.
        name (str): New name.

    Returns:
        dict: Standard service response.
    """

    try:

        user = session.get(
            User,
            user_id
        )

        if not user:
            return failure(
                f"User with id={user_id} not found."
            )

        user.name = name

        return success(
            "User updated successfully.",
            {
                "id": user.id,
                "name": user.name
            }
        )

    except Exception as e:
        return failure(str(e))


@with_session
def delete_user(
        session,
        user_id: int
) -> dict:
    """
    Delete a user.

    Args:
        user_id (int): User ID.

    Returns:
        dict: Standard service response.
    """

    try:

        user = session.get(
            User,
            user_id
        )

        if not user:
            return failure(
                f"User with id={user_id} not found."
            )

        deleted_user = {
            "id": user.id,
            "name": user.name
        }

        session.delete(user)

        return success(
            "User deleted successfully.",
            deleted_user
        )

    except Exception as e:
        return failure(str(e))
