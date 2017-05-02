from django.conf.urls import url

import views

urlpatterns = [
    url(r'^host_list', views.host_list, name='host_list'),
    url(r'^host_edit', views.host_edit, name='host_edit'),
    url(r'^host_delete', views.host_delete, name='host_delete'),
]