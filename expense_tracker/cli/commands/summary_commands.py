from services.summary_service import user_summary

SUMMARY_COMMAND=[
    {
        "name": "user-summary",
        "help": "User's expenses summary",
        "handler": user_summary,
        "arguments": [
            {
                "name": "--user-id",
                "type": int,
                "required": True
            }
        ]
    }
]