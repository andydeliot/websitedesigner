from django.shortcuts import render

from .models import *

# Il est nécéssaire de rajouter les vues dans le fichier urls.py

def myview(request):
    my_models = MyModel.objects.all().order_by('my_date')
    return render(request, 'myapp/mypage.html', {'my_models': my_models})

