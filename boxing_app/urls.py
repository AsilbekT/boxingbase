from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('boxers_details/<int:id>/', views.boxers_details, name='boxers_details'),
    path("add_boxer/", views.add_boxer, name="add_boxer"),
    path("edit_boxer/<int:id>/", views.edit_boxer, name="edit_boxer"),
    path("change_lang/", views.change_lang, name="change_lang"),
]