import argparse
from cli.command_config import COMMANDS


REQUIRED_KEYS = {
    "name",
    "help",
    "handler",
    "arguments"
}

def register_command(subparsers, config):
    """
    Register a command and its arguments
    with argparse.
    """

    try:

        missing = REQUIRED_KEYS - config.keys()

        if missing:
            raise ValueError(
                f"Command {config.get('name')} "
                f"is missing keys: {missing}"
            )


        parser = subparsers.add_parser(
            config["name"],
            help=config["help"]
        )

        for arg in config.get("arguments", []):

            arg_name = arg["name"]

            options = {
                key: value
                for key, value in arg.items()
                if key != "name"
            }

            parser.add_argument(
                arg_name,
                **options
            )

        parser.set_defaults(
            handler=config["handler"]
        )

    except KeyError as e:
        raise ValueError(
            f"Invalid command configuration. Missing key: {e}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Failed to register command "
            f"{config.get('name', 'UNKNOWN')}: {e}"
        )


def create_parser():
    """
    Create and configure the root parser.
    """

    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="Splitwise Style Expense Tracker CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    for command in COMMANDS:
        register_command(
            subparsers,
            command
        )

    return parser