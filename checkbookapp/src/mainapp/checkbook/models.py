from django.db import models

TRANSACTION_CHOICES = {
    ("Credit", "Credit"),
    ("Debit", "Debit"),
    ("Withdrawal", "Withdrawal"),
    ("Deposit", "Deposit"),
}
TITLE_CHOICE = {
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Mrs.', 'Mrs.'),
}


# Create your models here.
class Account(models.Model):  # Model for Users
    title = models.CharField(max_length=5, choices=TITLE_CHOICE, blank=True, null=False)
    firstName = models.CharField("First Name", max_length=15)
    lastName = models.CharField("Last Name", max_length=15)
    startBal = models.DecimalField("Starting Balance", default=0.00, decimal_places=2, max_digits=10)

    Accounts = models.Manager()

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Transaction(models.Model):  # Transaction model
    date = models.DateTimeField("Date of Transaction", auto_now_add=True)
    type = models.CharField("Type of Transaction", max_length=10, choices=TRANSACTION_CHOICES, default="---")
    amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, default="", blank=True, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()

