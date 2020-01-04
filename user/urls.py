from django.conf.urls import include, url
from .views import RegisterView, LoginView, HomeView, EditView, DeleteView, PageNotFound, LogoutView

urlpatterns = [
	url(r'^login/', LoginView, name = 'login'),
	url(r'^logout/', LogoutView, name = 'logout'),
	url(r'^register/', RegisterView, name = 'register'),
	url(r'^home/', HomeView, name = 'home'),
	url(r'404/', PageNotFound, name='404'),
	url(r'^edit/(?P<username>\w+)/', EditView, name='edit'),
	url(r'^delete/(?P<username>\w+)/', DeleteView, name='delete')
]