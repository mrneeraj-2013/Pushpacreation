from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Pushpa Creation"
admin.site.site_title = "Pushpa Creation Admin Portal"
admin.site.index_title = "Welcome to Pushpa Creation"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pihu.urls'))
]
