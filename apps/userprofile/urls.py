from django.urls import path, include
from .views import dashboard, delete_job

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<int:id>/', dashboard, name="update"),
    path('del/<int:id>/', delete_job, name="delete")
]