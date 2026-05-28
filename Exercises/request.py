import requests


BASE_URL = "https://dummyjson.com"


def fetch_users():
    try:
        response = requests.get(f"{BASE_URL}/users")
        response.raise_for_status()

        return response.json()['users']

    except Exception as e:
        print("Error:", e)
        return []


def list_users():
    users = fetch_users()

    if not users:
        print("No users found")
        return

    print("\n===== USER LIST =====")

    for user in users:
        print(
            f"{user['id']} | "
            f"{user['firstName']} {user['lastName']} | "
            f"{user['email']}"
        )


def login_user(username, password):

    data = {
        "username": username,
        "password": password,
        "expiresInMins": 30
    }

    try:

        response = requests.post(
            f"{BASE_URL}/auth/login",
            json=data
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:
        print("Login Error:", e)
        return None


def get_current_user(access_token):

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    try:

        response = requests.get(
            f"{BASE_URL}/auth/me",
            headers=headers
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:
        print("Error:", e)
        return None


def search_user(name):

    try:

        response = requests.get(
            f"{BASE_URL}/users/search",
            params={"q": name}
        )

        response.raise_for_status()

        return response.json()['users']

    except Exception as e:
        print("Search Error:", e)
        return []


while True:

    print("\n===== MENU =====")
    print("1. List Users")
    print("2. Login User")
    print("3. Search User")
    print("4. Quit")

    try:
        choice = int(input("Enter Choice: "))

    except ValueError:
        print("Please enter a valid number")
        continue

    match choice:

        case 1:

            list_users()

        case 2:

            print("\n===== LOGIN =====")

            username = input("Enter Username: ")
            password = input("Enter Password: ")

            result = login_user(username, password)

            if result:

                print("\nLogin Successful!")

                print("User:", result['firstName'])
                print("Email:", result['email'])

                token = result['accessToken']

                print("\nFetching current user...\n")

                current_user = get_current_user(token)

                if current_user:
                    print(
                        f"{current_user['firstName']} "
                        f"{current_user['lastName']}"
                    )

        case 3:

            print("\n===== SEARCH USER =====")

            name = input("Enter Name: ")

            users = search_user(name)

            if users:

                print("\nSearch Results:\n")

                for user in users:
                    print(
                        f"{user['id']} | "
                        f"{user['firstName']} "
                        f"{user['lastName']} | "
                        f"{user['email']}"
                    )

            else:
                print("No users found")

        case 4:

            print("Goodbye!")
            break

        case _:

            print("Invalid choice!")