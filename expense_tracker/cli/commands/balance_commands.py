from services.balance_service import get_net_balance,get_total_owed,get_total_receivable

BALANCE_COMMANDS=[

{
    "name": "get-total-owed",
    "help": "Get total amount user owes",
    "handler": get_total_owed,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "get-total-receivable",
    "help": "Get total amount receivable",
    "handler": get_total_receivable,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "get-net-balance",
    "help": "Get net balance",
    "handler": get_net_balance,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
]