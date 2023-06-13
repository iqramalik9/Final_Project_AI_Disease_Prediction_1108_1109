from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('predict_disease', views.predict_disease, name='predict_disease'),
    path('predict_symptoms', views.predict_symptoms, name='predict_symptoms'),
     
]