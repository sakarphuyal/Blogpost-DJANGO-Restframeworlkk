from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace="blog")),
    url(r'^posts/',views.postList.as_view()),
]
  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


