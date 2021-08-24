from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import
from django.conf import settings
from django.conf.urls.static import static


app_name = 'image_classification'

urlpatterns = [
    # path('', views.first_view, name='first_view'),
    path('', views.image_upload, name='image_upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
