from django.contrib import admin
from django.urls import path, include
from tasks.views import task_list  # ✅ アプリから import
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', task_list, name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),

    # JWT トークン
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
