from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='Authentication:login')
def index(request):
    diction = {'sample_text': 'This is a text'}
    return render(request, 'index.html', context=diction)
