from django.shortcuts import render
from .models import Page
from .forms import PageForm

def infoPage(request):

        form = PageForm()
        information = Page.objects.all()
        return render(request, 'app/infoPage.html', context={'form':form, 'information':information})