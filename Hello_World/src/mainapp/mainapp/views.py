from django.http import HttpResponse
from django.shortcuts import render


# Create a view that displays the users name
def home(request):
    names = ["Nate", "Jake", "Alice", "Jerry", "Mike", "George"]
    context = {
        'names': names,
    }
    return render(request, "home.html", context)
