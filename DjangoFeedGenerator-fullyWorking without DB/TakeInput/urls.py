from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.take_input_view, name='take_input_view'),
    url(r'^submit1/', views.submit1_view, name='submit1_view'),
    url(r'^submit2/', views.submit2_view, name='submit2_view'),

]