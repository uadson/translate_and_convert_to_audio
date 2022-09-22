from django.urls import path
from core.views.sessions import cookie_session
from core.views.sessions import cookie_delete
from core.views.sessions import create_session
from core.views.sessions import access_session
from core.views.sessions import delete_session


urlpatterns = [
	path('testcookie/', cookie_session),
	path('deletecookie/', cookie_delete),
	path('create/', create_session),
	path('access/', access_session),
	path('delete/', delete_session),
]
