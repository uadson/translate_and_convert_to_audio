from django.urls import path, include
from . import index
from . import sessions


app_name = 'core'

urlpatterns = [
	path('', include(index)),
	path('', include(sessions)),
]