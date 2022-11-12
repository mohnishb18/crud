
from django.urls import path,include

from .views import *
from rest_framework import routers
#Token Authentictaion
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router = routers.DefaultRouter()
router.register(r'employee',EmployeeViewSet)


urlpatterns = [
     path('web',webpage),
     path('hm',index),
     path('form',EmpEntry),
     path('data',EmpData),
     path('update/<int:id>',UpdateEmp),
     path('delete/<int:id>',Empdelete),
     path('search',SearchEmp),
     path('',include(router.urls)),
     path('home1',home),
     # # path('get_user_credentials', views.UserCredentials.as_view()),
     # path('generate_credentials', views.GenerateCredentials.as_view()),
     path('ind',index1),
     path('home',home1),
     path('post',post_emp),
     path('update-emp/<int:eid>',update_employee),
     path('auth/',include('rest_framework.urls')),
     #Token Authentication
     path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
     #jwt Authentication
     path('gettoken',TokenObtainPairView.as_view()),
     path('refreshtoken',TokenRefreshView.as_view()),
     path('verifytoken',TokenVerifyView.as_view())


]