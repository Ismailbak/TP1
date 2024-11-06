from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contacts, name='liste_contacts'),
    path('ajouter/', views.ajouter_contact, name='ajouter_contact'),
    path('supprimer/<int:contact_id>/', views.supprimer_contact, name='supprimer_contact'),
]
