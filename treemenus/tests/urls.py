from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    (r'^test_treemenus_admin/', include(admin.site.urls)),
]

handler500 = 'django.views.defaults.server_error'
