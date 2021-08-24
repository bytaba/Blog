from django.urls import path
from . import views

urls_pattern = [
    path( ''             , views.index        , name= 'index'       ),
    path( 'posts'        , views.posts        , name='posts'        ),
    path( 'post/<slug>'  , views.post_detail  ,  name='post-detail' )

]