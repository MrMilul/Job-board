from django.urls import path, include
from .views import dashboard, delete_job, view_dashboard_job



urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<int:id>/', dashboard, name="update"),
    path('del/<int:id>/', delete_job, name="delete"),
    path('dashboard-job/<int:id>', view_dashboard_job, name="view_dashboard_job")
]