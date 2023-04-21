from django.conf.urls import url
import views
#from views

urlpatters = [
    url(r'^api/customer$', views.customer),
]

