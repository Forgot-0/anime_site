from django.urls import path
from .views import PersonsListView, PersonDetailView


urlpatterns = [
    path('', PersonsListView.as_view(), name='person_list'),
    path('<slug:slug>/', PersonDetailView.as_view(), name='person_detail')

]