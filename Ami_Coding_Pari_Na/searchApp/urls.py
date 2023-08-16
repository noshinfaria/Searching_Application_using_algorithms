from django.urls import path
from . import views


urlpatterns=[
  path('search/', views.search_element, name="search"),
  path('listview/', views.list_user_input, name="list_view"),

]