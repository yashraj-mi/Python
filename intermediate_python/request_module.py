import logging
from typing import Any

import requests

BASE_URL = "https://dummyjson.com"
REQUEST_TIMEOUT = 10

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def make_request(method: str, endpoint: str, **kwargs) -> dict[str, Any]:
    """
    Make an HTTP request and return JSON data.

    Args:
        method: HTTP method (GET, POST, etc.)
        endpoint: API endpoint.
        **kwargs: Additional arguments passed to requests.

    Returns:
        Parsed JSON response.

    Raises:
        requests.RequestException: If the request fails.
    """
    response = requests.request(
        method=method,
        url=f"{BASE_URL}{endpoint}",
        timeout=REQUEST_TIMEOUT,
        **kwargs,
    )

    response.raise_for_status()
    return response.json()


def fetch_users() -> list[dict[str, Any]]:
    """
    Fetch all users from the API.

    Returns:
        List of users.
    """
    try:
        data = make_request("GET", "/users")
        return data.get("users", [])

    except requests.RequestException as error:
        logger.error("Failed to fetch users: %s", error)
        return []


def login_user(username: str, password: str) -> dict[str, Any] | None:
    """
    Authenticate a user.

    Args:
        username: User's username.
        password: User's password.

    Returns:
        User data if login succeeds, otherwise None.
    """
    payload = {
        "username": username,
        "password": password,
        "expiresInMins": 30,
    }

    try:
        return make_request(
            "POST",
            "/auth/login",
            json=payload,
        )

    except requests.RequestException as error:
        logger.error("Login failed: %s", error)
        return None


def get_current_user(access_token: str) -> dict[str, Any] | None:
    """
    Fetch the currently authenticated user.

    Args:
        access_token: JWT access token.

    Returns:
        Current user data or None.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
    }

    try:
        return make_request(
            "GET",
            "/auth/me",
            headers=headers,
        )

    except requests.RequestException as error:
        logger.error("Failed to fetch current user: %s", error)
        return None


def search_user(name: str) -> list[dict[str, Any]]:
    """
    Search users by name.

    Args:
        name: Search query.

    Returns:
        Matching users.
    """
    try:
        data = make_request(
            "GET",
            "/users/search",
            params={"q": name},
        )

        return data.get("users", [])

    except requests.RequestException as error:
        logger.error("Search failed: %s", error)
        return []


def print_users(users: list[dict[str, Any]]) -> None:
    """
    Display users in a formatted manner.

    Args:
        users: List of user dictionaries.
    """
    if not users:
        print("No users found.")
        return

    print("\n===== USERS =====")

    for user in users:
        print(
            f"{user['id']} | "
            f"{user['firstName']} {user['lastName']} | "
            f"{user['email']}"
        )


def handle_list_users() -> None:
    """Handle user listing."""
    users = fetch_users()
    print_users(users)


def handle_login() -> None:
    """Handle user login."""
    print("\n===== LOGIN =====")

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    result = login_user(username, password)

    if not result:
        print("Login failed.")
        return

    print("\nLogin successful!")
    print(f"User : {result.get('firstName')}")
    print(f"Email: {result.get('email')}")

    access_token = result.get("accessToken")

    if not access_token:
        print("Access token not found.")
        return

    current_user = get_current_user(access_token)

    if current_user:
        print("\n===== CURRENT USER =====")
        print(
            f"{current_user['firstName']} "
            f"{current_user['lastName']}"
        )


def handle_search_user() -> None:
    """Handle user search."""
    print("\n===== SEARCH USER =====")

    name = input("Enter name: ").strip()

    users = search_user(name)
    print_users(users)


def display_menu() -> None:
    """Display the application menu."""
    print("\n===== MENU =====")
    print("1. List Users")
    print("2. Login User")
    print("3. Search User")
    print("4. Exit")


def main() -> None:
    """Application entry point."""
    while True:
        display_menu()

        try:
            choice = int(input("Enter choice: ").strip())

        except ValueError:
            print("Please enter a valid number.")
            continue

        match choice:
            case 1:
                handle_list_users()

            case 2:
                handle_login()

            case 3:
                handle_search_user()

            case 4:
                print("Goodbye!")
                break

            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()

