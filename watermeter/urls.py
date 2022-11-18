from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.login,name='login'),
   path('',views.logout,name='logout'),
   path('dashboard/',views.dashboard,name="dashboard"),
   path('new_employer/',views.new_employer,name = "new_employer"),
   path('delete_employer/<int:id>',views.delete_employer,name="delete_employer"),
   path('manage_employer/',views.manage_employer,name="manage_employer"),
   path('new_customer/',views.new_customer,name = "new_customer"),
   path('manage_customer/',views.manage_customer,name="manage_customer"),
   path('delete_customer/<int:id>',views.delete_customer,name="delete_customer"),
   path('add_watermeter/',views.add_watermeter,name="add_watermeter"),
   path('manage_watermeter/',views.manage_watermeter,name="manage_watermeter"),
   path('delete_watermeter/<int:id>',views.delete_watermeter,name="delete_watermeter"),
   path('new_bill/',views.new_bill,name="new_bill"),
   path('manage_bill/',views.manage_bill,name="manage_bill"),
   path('delete_bill/<int:id>',views.delete_bill,name="delete_bill"),

   ######### frontend  ###############
   path('watermeter/',views.home,name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)