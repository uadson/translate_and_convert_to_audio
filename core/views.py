from django.shortcuts import render
from googletrans import Translator


def index(request):
	translator = Translator()

	if not request.POST:
		return render(request, 'core/index.html')

	if request.POST:
		input_text = request.POST.get('inputText')
		
		output_lang = request.POST.getlist('lang[]')
		
		try:
			if len(output_lang) == 1:
				for lang in output_lang:
					data = translator.translate(input_text, dest=lang)

					print(data.text)

					context = {
						'data': data.text,
					}
		except:


		return render(request, 'core/index.html', context)
