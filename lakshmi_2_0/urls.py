from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from page.views import customhandler404

admin.site.site_header = "Laskshmi888"
admin.site.site_title = "Laskshmi888 администрирование"
admin.site.index_title = "Laskshmi888 администрирование"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('item/', include('item.urls')),
    path('cart/', include('cart.urls')),
    path('user/', include('customuser.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = customhandler404
