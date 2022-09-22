from django.shortcuts import redirect
from django.http import HttpResponse


def cookie_session(request):
	request.session.set_test_cookie()
	return HttpResponse('<h1>DataFlair</h1>')


def cookie_delete(request):
	if request.session.test_cookie_worked():
		request.session.delete_test_cookie()
		response = HttpResponse("DataFlair<br> cookie created")
	else:
		response = HttpResponse("DataFlair <br> Your browser doesnot accept cookies")
	return response


def create_session(request):
	request.session['name'] = 'username'
	request.session['password'] = 'password123'
	return HttpResponse("<h1>DataFlair<br> the session is set</h1>")


def access_session(request):
	response = "<h1>Welcome to Sessions of DataFlair</h1><br>"
	if request.session.get('name'):
		response += f"Name: {request.session.get('name')}<br>"

	if request.session.get('password'):
		response += f"Password: {request.session.get('password')}<br>"
		return HttpResponse(response)
	else:
		return redirect('create/')


def delete_session(request):
	try:
		del request.session['name']
		del request.session['password']
	except KeyError:
		pass
	return HttpResponse("<h1>DataFlair<br> Session Data Cleared</h1>")