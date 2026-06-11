
from services.report_service import get_category_report,get_group_summary,get_monthly_expenses,get_user_expenses,get_expenses_paid_by_user

REPORT_COMMANDS=[
{
    "name": "get-user-expenses",
    "help": "Get all expenses of a user",
    "handler": get_user_expenses,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "get-monthly-expenses",
    "help": "Get expenses of a month",
    "handler": get_monthly_expenses,
    "arguments": [
        {"name": "--month", "type": int, "required": True}
    ]
},
{
    "name": "get-category-report",
    "help": "Get expenses by category",
    "handler": get_category_report,
    "arguments": [
        {"name": "--category", "required": True}
    ]
},
{
    "name": "get-expenses-paid-by-user",
    "help": "Get expenses paid by user",
    "handler": get_expenses_paid_by_user,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "get-group-summary",
    "help": "Get expense participant summary",
    "handler": get_group_summary,
    "arguments": [
        {"name": "--expense-id", "type": int, "required": True}
    ]
},
]