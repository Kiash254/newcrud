from turtle import update
from django.urls import path
from .views import Create, Updateview, home,Detailview,Deleteview

app_name="crud"

urlpatterns = [
    path("",home,name="home"),
    path("create/",Create,name="create"),
    path("crud/<int:pk>/",Detailview, name='detail'),
    path('crud/<int:pk>/update',Updateview,name='update'),
    path('crud/<int:pk>/delete',Deleteview,name='delete')
]
