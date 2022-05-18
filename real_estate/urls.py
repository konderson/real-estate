
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

print(settings.MEDIA_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ReAL Estate Admin" 
admin.site.site_title = "ReAL Estate Admin Portal"  
admin.site.index_title = "Welcome to the Real Estate Portal" 
