from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm


# Create view functions to render templates
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


def create_account(request):
    form = AccountForm(data=request.POST or None)  # Store the requested AccountForm in form, weather the form was
    if request.method == 'POST':                   # POSTed or no data was received
        if form.is_valid():
            form.save()                            # If the form we receive is valid, save the form
            return redirect('index')               # Return HTTP response to the index URL
    content = {'form': form}                   # Store form dictionary in content
    return render(request, 'checkbook/CreateNewAccount.html', content)  # Render CreateNewAccount with form in content


def balance(request, pk):       # Pass pk to view to render view for specific account
    account = get_object_or_404(Account, pk=pk)    # Store Account object & pk in account, if no object exists: 404
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.startBal
    table_contents = { }
    for t in transactions:
        if t.type == 'Deposit' or t.type == 'Credit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance' : current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
