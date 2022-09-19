from django.shortcuts import render
from googletrans import Translator


def index(request):
	translator = Translator()
	
	text = translator.translate('Olá Mundo', dest='en')

	context = {
		'text': text.text 
	}

	return render(request, 'core/index.html', context)
