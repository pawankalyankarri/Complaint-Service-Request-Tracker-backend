from django.contrib import admin
from .models import UserLogin,TechLogin,Requests,Departments,AcceptedRequests
# Register your models here.

admin.site.register(UserLogin)
admin.site.register(TechLogin)
admin.site.register(Requests)
admin.site.register(Departments)
admin.site.register(AcceptedRequests)