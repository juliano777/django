from django.urls import path

#
from recipes.views import about
from recipes.views import contact
from recipes.views import home

urlpatterns = (
    path('', home),
    path('about', about),
    path('contact', contact),
)

