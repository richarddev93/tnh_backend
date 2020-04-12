from django.urls import path
from .views import home
# from rest_framework.authtoken import views
# router = routers.DefaultRouter()

# router.register('cadastro',cadastro_usuario_view)
app_name = 'frontend'

urlpatterns = [
   
    path('/',home,name ='home.html'), 
 
     

]