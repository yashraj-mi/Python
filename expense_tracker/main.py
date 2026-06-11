from cli.parser import create_parser

def main():
    try:
        parser = create_parser()
        args = parser.parse_args()

        arguments = vars(args).copy()

        handler = arguments.pop("handler")
        arguments.pop("command", None)

        if handler.__name__ == "add_expense":

            expense_data = {
                "description": arguments["description"],
                "amount": arguments["amount"],
                "category": arguments.get("category"),
                "paid_by": arguments["paid_by"],
                "participants": arguments["participants"]
            }

            result = handler(expense_data)

        elif handler.__name__ == "update_expense":

            update_data = {}

            if arguments.get("description") is not None:
                update_data["description"] = arguments["description"]

            if arguments.get("category") is not None:
                update_data["category"] = arguments["category"]


            result = handler(
                arguments["expense_id"],
                update_data
            )

        else:
            result = handler(**arguments)

        if result["success"] ==False:
            print(result["message"])
        else:
            print(result["message"])
            print(result["data"])

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(
            {
                "success": False,
                "message": f"Unexpected error: {str(e)}",
                "data": None
            }
        )

if __name__ == "__main__":
    main()