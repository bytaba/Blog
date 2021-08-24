from django.urls import path
from . import views

urlpatterns = [
    path( ''             , views.index        , name= 'index'       ),
    path( 'posts'        , views.posts        , name='posts'        ),
    path( 'post/<slug>'  , views.post_detail  ,  name='post-detail' )

]