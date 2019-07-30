
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import internalapp
from .forms import appForm, tryoutform
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.views.generic.list import ListView
# Create your views here.


def testhome(request):
    submitted = False
    if request.method == 'POST' :
        form = appForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/testhome/?submitted=True')
    else:
        form = appForm()

        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'tryout/testhome.html', {'form': form, 'submitted': submitted})

def tryout(request):
    print(request.GET)
    if request.method == 'POST' :
        tryform = tryoutform(request.POST)
        print(request.POST)
        if tryform.is_valid():
            return HttpResponseRedirect('/tryform/')
    else:
        tryform = tryoutform(initial={'email':'johndoe@coffeehouse.com','name':'yeashin'})
    return render(request,'tryout/dualList.html',{'form':tryform})

class applist(ListView):
    model = internalapp


    