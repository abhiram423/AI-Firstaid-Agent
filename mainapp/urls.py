from django.urls import path
from mainapp import views

urlpatterns = [
    path('',       views.home,   name='home'),
    path('guide/', views.guide,  name='guide'),
    path('report/',views.report, name='report'),
]