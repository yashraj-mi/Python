from abc import ABC, abstractmethod


class Account(ABC):
    """Base abstract class for bank accounts."""

    bank_name = "ABC Bank"

    def __init__(self, owner: str, balance: float):
        self._owner = owner
        self._balance = balance

    @staticmethod
    def validate_amount(amount: float) -> bool:
        """Check if amount is valid (> 0)."""
        return amount > 0

    @property
    def balance(self) -> float:
        """Return current balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        """Deposit money into account."""
        if self.validate_amount(amount):
            self._balance += amount
        else:
            print("Invalid amount")

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw money (implemented by child classes)."""
        pass

    @classmethod
    def get_bank_name(cls) -> str:
        """Return bank name."""
        return cls.bank_name


class SavingsAccount(Account):
    """Savings account with balance protection."""

    def withdraw(self, amount: float) -> None:
        if amount <= self._balance and self.validate_amount(amount):
            self._balance -= amount
        else:
            print("Insufficient balance or invalid amount")


class CurrentAccount(Account):
    """Current account (can go negative with overdraft facility)."""

    def withdraw(self, amount):
        overdraft_limit = 2000

        if self.validate_amount(amount) and self._balance - amount >= -overdraft_limit:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded")


def main() -> None:
    acc1 = SavingsAccount("Rahul", 10000)
    acc2 = CurrentAccount("Priya", 5000)

    acc1.deposit(2000)
    acc1.withdraw(3000)

    acc2.withdraw(1000)

    print("Rahul Balance:", acc1.balance)
    print("Priya Balance:", acc2.balance)

    print("Bank:", Account.get_bank_name())


if __name__ == "__main__":
    main()
