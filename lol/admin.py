from django.contrib import admin
from .models import Languagecodes
from .models import Patches

# Register your models here.
admin.site.register(Languagecodes)
admin.site.register(Patches)