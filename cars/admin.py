from django.contrib import admin
from .models import User
from .models import Login
from .models import Vehicle

# Register your models here.
admin.site.register(User)
admin.site.register(Login)
admin.site.register(Vehicle)