from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
               path('createprofile',views.CreateProfile.as_view(),name="createprofile"),
               path('home',views.UserHome.as_view(),name="userhome"),
               path("register/", views.UserRegistrationApiView.as_view(), name='register'),
               path("login/", views.UserLoginApiView.as_view(), name='login'),
               path("logout/", views.UserLogoutView.as_view(), name='logout'),
               path("active/<uid64>/<token>/", views.activate, name='activate'),

               path('viewprofile',views.ViewProfile.as_view(),name="viewprofile"),
               path('editprofile',views.EditProfile.as_view(),name="editprofile"),
]