from django.contrib.auth import views as auth_views
from django.urls import path
from.import views
app_name = 'accounts'


urlpatterns = [
    
    path('login', views.login_view, name='login'),
    # login
    path('logout', views.logout_view, name='logout'),
    # logout
    path('signup/', views.signup_view, name='signup'),
    # registration / signup
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # password reset
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # password reset done
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # reset token
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # reset done

    

]