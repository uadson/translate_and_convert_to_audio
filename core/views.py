from django.shortcuts import render, redirect
from googletrans import Translator
from django.contrib import messages
from gtts import gTTS
import os
from pathlib import Path
import uuid
from utils.digger import delete_file


def index(request):
	"""
		Translator

		#1 received text typed by user and translate it
		#2 the text is converted in a audio file
	"""
	if not request.POST:
		return render(request, 'core/index.html')

	# clearing previous session
	try:
		delete_file(request.session['id'])
		del request.session['data']
		del request.session['id']
	except KeyError:
		pass

	translator = Translator()

	input_text = request.POST.get('inputText')
	output_lang = request.POST.getlist('lang[]')
	
	if len(output_lang) == 1:
		for lang in output_lang:
			# generating key
			key = uuid.uuid4()
			# translating
			data = translator.translate(input_text, dest=lang)
			# converting and saving the converted audio
			audio = gTTS(text=data.text, lang=lang, slow=False)
			audio.save(f"./media/{key}.mp3")

			# creating session
			request.session['data'] = data.text
			request.session['id'] = f"{key}"

			# accessing session
			response = request.session.get('data')
			
			context = {'response': response}

			return render(request, 'core/index.html', context)

	else:
		messages.add_message(
			request, messages.ERROR,
			'Select only one language'
		)
		return redirect('core:index')
