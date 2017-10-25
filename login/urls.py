from . import views
from django.conf.urls import url


app_name = 'login'
urlpatterns = [
    # url(r'^upload/', views.upload_csv, name="upload"),
    url(r'^app/', views.index_view, name="index"),
    url(r'^login/', views.login_view, name="login"),
    url(r'^logout/', views.logout_view, name="logout"),
    url(r'^register/', views.register_view, name="register"),
    url(r'^validate/', views.validate_view, name="validate_view"),
    url(r'^profile/$', views.list_file, name='list_file')

]
