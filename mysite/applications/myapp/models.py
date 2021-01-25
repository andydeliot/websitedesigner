from django.db import models

# Import ajoutés.
from django.conf import settings
from django.utils import timezone
from django.contrib import admin


# Liste des fields disponibles :
# https://docs.djangoproject.com/en/3.1/ref/models/fields/

# Lorsque les modèles sont créés ou modifiés :
# python3 manage.py makemigrations myapp

class MyModel(models.Model):
    my_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    my_char = models.CharField(max_length=200)
    my_text = models.TextField()
    my_date = models.DateTimeField(default=timezone.now)
    my_int = models.IntegerField(defaut=0)

    def save_me(self):
        self.save()
admin.site.register(MyModel)

