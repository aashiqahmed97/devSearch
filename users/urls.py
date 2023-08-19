from django.urls import path
from users import  views



urlpatterns=[
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('account/', views.userAccount ,  name='account'),
    path('edit-account/', views.editAccount ,  name='edit-account'),




    path('', views.profiles, name='profiles'),
    path('profile/<uuid:pk>/', views.userProfile, name='user-profile'),
    path ('create-skill/', views.createSkill, name = 'create-skill'),
    path ('update-skill/<uuid:pk>/', views.updateSkill, name = 'update-skill'),
    path('delete-skill/<uuid:pk>/', views.deleteSkill, name='delete-skill'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<uuid:pk>/', views.viewMessage, name='message'),
    path('create-message/<uuid:pk>/', views.createMessage, name= 'create-message' ),


    
]