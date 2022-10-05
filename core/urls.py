from django.urls import path
from core.views import index, clean


app_name = "core"


urlpatterns = [
	path('', index, name='index'),
	path('clean/', clean, name='clean'),
]