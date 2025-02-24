from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from users.views.registration_views import UserRegistrationView
from users.views.users_views import UsersListView, UserDetailsView


urlpatterns = [
    path('users-list/', UsersListView.as_view(), name='users_list'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('user-details/', UserDetailsView.as_view(), name='user_details'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    # Путь для стандартных логина и логаута встроенных в Джанго
    path('auth/', include('django.contrib.auth.urls')),
]
