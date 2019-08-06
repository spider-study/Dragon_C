
from django.contrib import admin
from django.urls import path,include

from home import views
# from jianli import jianliviews
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('jianli/', include('jianli.urls')),
    # path('book/',include('polls.urls'))
    
]
