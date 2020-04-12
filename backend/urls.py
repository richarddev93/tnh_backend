from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
   
    # REST FRAMEWORK URLS
    path('api/servico/', include('servicos.api.urls')),
    path('api/cadastro/', include('conta.api.urls')),
    path('account/',include('django.contrib.auth.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),


    # FRONTEND
    path('home/',include('frontend.urls')),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done_email.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_email.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done_email.html'),
     name='password_reset_done'),


    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', 
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form_email.html' ,
         email_template_name = 'registration/password_reset_email_template.html',
         subject_template_name = 'registration/password_reset_subject_email.txt')
         , name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_email.html'),
     name='password_reset_complete'),

     
     
]
