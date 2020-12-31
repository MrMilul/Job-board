from django.contrib import admin
from django.urls import path, include
from apps.core import views as v
from apps.job import views as vv
from django.contrib.auth import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', v.frontpage, name='frontpage'),
    path('signup/', v.singup, name='signup'),
    path('admin/', admin.site.urls),
    path('logout/', views.LogoutView.as_view(), name="logout"), 
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'), 
    path('jobs/<int:job_id>/', vv.detail_job, name='detail_job'), 
    path('dashboard/',include('apps.userprofile.urls')), 
    # path('jobs/add/', vv.add_job, name='add_job')
    path('apply/<int:id>/', vv.apply_for_job, name='apply_for_job')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


