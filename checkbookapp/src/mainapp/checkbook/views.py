from django.shortcuts import render, redirect
from .forms import AccountForm, TransactionForm


# Create view functions to render templates
def home(request):
    return render(request, 'checkbook/index.html')


def create_account(request):
    form = AccountForm(data=request.POST or None)  # Store the requested AccountForm in form, weather the form was
    if request.method == 'POST':                   # POSTed or no data was received
        if form.is_valid():
            form.save()                            # If the form we receive is valid, save the form
            return redirect('index')               # Return HTTP response to the index URL
    content = {'form': form}                   # Store form dictionary in content
    return render(request, 'checkbook/CreateNewAccount.html', content)  # Render CreateNewAccount with form in content


def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')


def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
