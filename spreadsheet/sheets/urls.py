from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, SpreadsheetViewSet, CellViewSet

# DRF Router for API endpoints
router = DefaultRouter()
router.register(r'spreadsheets', SpreadsheetViewSet)
router.register(r'cells', CellViewSet)

urlpatterns = [
    path('', index, name='spreadsheet_index'),  # Web UI
    path('api/', include(router.urls)),  # API endpoints
]
