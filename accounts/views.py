from django.shortcuts import render
# Create your views here.
from accounts.forms import SignUpForm

def registration(request):
    forms = SignUpForm
    return render(request, 'register.html', {'forms':forms})
