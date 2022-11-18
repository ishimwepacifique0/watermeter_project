from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Admin)
admin.site.register(Employer)
admin.site.register(Customer)
admin.site.register(watermeter)
admin.site.register(Bill)