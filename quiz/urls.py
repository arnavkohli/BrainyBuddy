from django.conf.urls import include, url
# from .views import RegisterView, LoginView, HomeView, EditView, DeleteView, PageNotFound

# urlpatterns = [
# 	url(r'^login/', LoginView, name = 'login'),
# 	url(r'^register/', RegisterView, name = 'register'),
# 	url(r'^home/', HomeView, name = 'home'),
# 	url(r'404/', PageNotFound, name='404'),
# 	url(r'^edit/(?P<username>\w+)/', EditView, name='edit'),
# 	url(r'^delete/(?P<username>\w+)/', DeleteView, name='delete')
# ]


from .views import QuizCreateView, QuizEditView, QuizListView, QuizTakeView


urlpatterns = [
	url(r'^createQuiz/', QuizCreateView, name='createQuiz'),
	url(r'^editQuiz/(?P<quiz_id>\d+)/$', QuizEditView, name='editQuiz'),
	url(r'^allQuizzes/', QuizListView, name='allQuizzes'),
	url(r'^takeQuiz/(?P<quiz_id>\d+)/$', QuizTakeView, name='takeQuiz')
]