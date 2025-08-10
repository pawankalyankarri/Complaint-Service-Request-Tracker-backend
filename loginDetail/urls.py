from django.urls import path
from . import views

urlpatterns = [
    path('userlogin/',views.LoginUser.as_view(),name='loginuserurl'),
    path('techlogin/',views.LoginTech.as_view(),name='logintechurl'),
    path('requests/',views.RaiseRequests.as_view(),name='requestsurl'),
]