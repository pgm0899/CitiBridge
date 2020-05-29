from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.display_output_view, name='display_output_view'),

    url(r'^$/all.csv', views.display_all_view,
        name='display_all_view'),

]
