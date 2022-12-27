from django.urls import path
from . import views
urlpatterns = [
    path('sk/', views.skill, name="skill"),
]


