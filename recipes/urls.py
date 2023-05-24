from django.urls import path

from . import views

# * A variavel "app_name" tem que receber o 
# nome em aspas simples * deixando recipe:(name path)
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]