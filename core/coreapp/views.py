from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm


def index(request):
    submitted = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = UserForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'coreapp/index.html', {'form':form, 'submitted':submitted})