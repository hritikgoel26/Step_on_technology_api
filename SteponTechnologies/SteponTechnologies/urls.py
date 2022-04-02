from django.contrib import admin
from django.urls import path,include
from Family import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()


router.register('parents',views.ParentsViewSet, basename='parents')

router.register('child',views.ChildViewSet, basename='child')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
