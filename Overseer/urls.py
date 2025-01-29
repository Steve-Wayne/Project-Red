from django.urls import path 
from .views import  (create_board , BoardListView , BoardDetailView,ListCreationView)

urlpatterns = [
    path('' ,BoardListView.as_view( template_name = 'Overseer/home.html') , name="home") , 
    path('create/' , create_board , name="create_board"),
    path('board/<int:pk>/' , BoardDetailView.as_view( template_name = 'Overseer/board_detail.html') , name="board_detail"),
    path('board/<int:pk>/create_list/' , ListCreationView.as_view( template_name = 'Overseer/create_list.html') , name="create_list")
]