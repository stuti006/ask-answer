from django.urls import path
from . import views
urlpatterns=[

    path('', views.index, name='index'),
    path('bott/', views.bott, name='bott'),
    path('getResponse', views.getResponse, name='getResponse'),
    path('intership1/', views.internship1, name='internship1'),
    path('intership2/', views.internship2, name='internship2'),
    path('intership3/', views.internship2, name='internship3'),
    path('workshop1/', views.workshop1, name='workshop1'),
    path('workshop2/', views.workshop2, name='workshop2'),
    path('workshop3/', views.workshop3, name='workshop3'),
    path('workshop4/', views.workshop4, name='workshop4'),
    path('events1/', views.events1, name='events1'),
    path('events2/', views.events2, name='events2'),
    path('events3/', views.events3, name='events3'),
    #tthis is for qur=estiona ns
    path('home',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    # # User Register
    path('accounts/register/',views.register,name='register'),
    # # Profile
    # path('accounts/profile/',views.profile,name='profile'),
    # # Ask QUestion
    path('ask-question',views.ask_form,name='ask-question'),
    # # Tag Page
    path('tag/<str:tag>',views.tag,name='tag'),
    # # Tags Page
    path('tags',views.tags,name='tags'),
]