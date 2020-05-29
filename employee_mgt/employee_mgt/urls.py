
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),
    path('employees/<int:emp_id>', views.employee_detail, name='employee_detail'),
    path('json_view/', include('json_view.urls')),
    path('', views.index, name='index')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#    path('', views.index, name='homepage'),