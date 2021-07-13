from django.urls import path
from .views import SnacksView,SnacksDetials,SnacksCreate,SnacksUpdate,SnacksDelete
urlpatterns = [
    path('', SnacksView.as_view(),name='snackslist'),
    path('<int:pk>/', SnacksDetials.as_view(),name='snackdetials'),
    path('create/', SnacksCreate.as_view(),name='snackscreate'),
    path('<int:pk>/update/', SnacksUpdate.as_view(),name='snacksupdate'),
    path('<int:pk>/delete/', SnacksDelete.as_view(),name='snacksdelete'),
]
