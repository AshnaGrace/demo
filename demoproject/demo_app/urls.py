from django.urls import path
from .import views
urlpatterns=[
path('',views.demo,name="demo"),
path('shop/<int:book_id>',views.details,name='details'),
path('add/',views.add,name='add'),
path('update/<int:id>',views.update,name='update'),
path('delete/<int:taskid>',views.delete,name='delete'),
     ]
