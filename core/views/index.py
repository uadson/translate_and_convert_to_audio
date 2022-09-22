from django.shortcuts import render, redirect
from googletrans import Translator
from django.contrib import messages


def index(request):
	if not request.POST:
		return render(request, 'core/index.html')

	# clearing previous session
	try:
		del request.session['data']
	except KeyError:
		pass

	translator = Translator()

	input_text = request.POST.get('inputText')
	output_lang = request.POST.getlist('lang[]')
	
	if len(output_lang) == 1:
		for lang in output_lang:
			data = translator.translate(input_text, dest=lang)
			
			request.session['data'] = data.text
			# creating session
			response = request.session.get('data')
			# accessing session
			
			context = {'response': response}

			return render(request, 'core/index.html', context)

	else:
		messages.add_message(
			request, messages.ERROR,
			'Select only one language'
		)
		return redirect('core:index')
