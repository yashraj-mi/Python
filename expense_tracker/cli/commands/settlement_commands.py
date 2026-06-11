from services.settlement_service import mark_paid,get_paid_settlements,get_all_settlements,get_pending_settlements

SETTLEMENT_COMMANDS=[

{
    "name": "mark-paid",
    "help": "Mark settlement as paid",
    "handler": mark_paid,
    "arguments": [
        {"name": "--settlement-id", "type": int, "required": True}
    ]
},
{
    "name": "get-pending-settlements",
    "help": "Get pending settlements",
    "handler": get_pending_settlements,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "get-paid-settlements",
    "help": "Get paid settlements",
    "handler": get_paid_settlements,
    "arguments": [
        {"name": "--user-id", "type": int, "required": True}
    ]
},
{
    "name": "get-all-settlements",
    "help": "Get all settlements",
    "handler": get_all_settlements,
    "arguments": []
},
]