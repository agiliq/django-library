from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.conf import settings
from django.shortcuts import render

from diglib.models import Books, Author, Publisher, Transaction

model_dict = {'book': Books, 'author':Author, 'publisher':Publisher}

def index(request):
    books = Books.objects.all()
    return render(request, 'index.html', {'books': books})

def detail(request, var_name, var_id=None):
    model = model_dict.get(var_name, "")
    obj = get_object_or_404(model, pk=var_id)
    return render(request, 'detail.html', {'detail':var_name, var_name:obj})

    
def status(request, book_id):
    tr = Transaction.objects.filter(book__id=book_id)
    return render(request, 'status.html', {'status_data': tr})
