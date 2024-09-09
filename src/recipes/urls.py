from django.urls import path

#
from recipes.views import about
from recipes.views import contact
from recipes.views import home
from recipes.views import recipe
from recipes.views import teste_local

urlpatterns = (
    path('', home),
    path('about', about),
    path('contact', contact),
    path('teste-local', teste_local),
    path('recipe/<int:id>/', recipe),
)
