from  services.user_service import add_user,get_user,get_all_users,delete_user,update_user
USER_COMMANDS=[

{
    "name": "add-user",
    "help": "Add a new user",
    "handler": add_user,
    "arguments": [
        {"name": "--name", "required": True}
    ]
},
{
    "name": "list-users",
    "help": "List all users",
    "handler": get_all_users,
    "arguments": []
},
{
    "name": "get-user",
    "help": "Get user by id",
    "handler": get_user,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "update-user",
    "help": "Update user",
    "handler": update_user,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True},
        {"name": "--name", "required": True}
    ]
},
{
    "name": "delete-user",
    "help": "Delete user",
    "handler": delete_user,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
]