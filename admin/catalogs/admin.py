from django.contrib import admin
from django.db.models import Model as Modelo
from . import models
import inspect
# Register your models here.
for x in dir(models):
	item = getattr(models, x)
	if inspect.isclass(item) and issubclass(item, Modelo) and x != 'User' and not admin.site.is_registered(item):
		admin.site.register(item)