from cli.commands.user_commands import USER_COMMANDS
from cli.commands.expense_commands import EXPENSE_COMMANDS
from cli.commands.report_commands import REPORT_COMMANDS
from cli.commands.balance_commands import BALANCE_COMMANDS
from cli.commands.settlement_commands import SETTLEMENT_COMMANDS
from cli.commands.summary_commands import SUMMARY_COMMAND

COMMANDS = (
    USER_COMMANDS
    + EXPENSE_COMMANDS
    + REPORT_COMMANDS
    + BALANCE_COMMANDS
    + SETTLEMENT_COMMANDS
    + SUMMARY_COMMAND
)
