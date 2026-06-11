from services.expense_service import add_expense,update_expense,delete_expense,get_expense,get_all_expenses
EXPENSE_COMMANDS=[

{
    "name": "add-expense",
    "help": "Add expense",
    "handler": add_expense,
    "arguments": [
        {"name": "--description", "required": True},
        {"name": "--category"},
        {"name": "--amount", "type": float, "required": True},
        {"name": "--paid-by", "type": int, "required": True},
        {
            "name": "--participants",
            "type": int,
            "nargs": "+",
            "required": True
        }
    ]
},
{
    "name": "get-expense",
    "help": "Get expense by id",
    "handler": get_expense,
    "arguments": [
        {"name": "--expense-id", "type": int, "required": True}
    ]
},
{
    "name": "get-all-expenses",
    "help": "Get all expenses",
    "handler": get_all_expenses,
    "arguments": []
},
{
    "name": "update-expense",
    "help": "Update expense",
    "handler": update_expense,
    "arguments": [
        {"name": "--expense-id", "type": int, "required": True},
        {"name": "--description"},
        {"name": "--category"},
    ]
},
{
    "name": "delete-expense",
    "help": "Delete expense",
    "handler": delete_expense,
    "arguments": [
        {"name": "--expense-id", "type": int, "required": True}
    ]
},
]