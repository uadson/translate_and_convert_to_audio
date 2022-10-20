### Tradutor e Conversor de Texto em Áudio - [english version here](####-ENGLISH-VERSION)


Esta é uma aplicação que tem como objetivo a tradução de textos entre os seguintes idiomas (por enquanto):

Português, Espanhol e Inglês


O texto traduzido é convertido em um arquivo de áudio que pode ser executado pelo player de mídia no navegador e ou baixado pelo usuário.


##### Funcionalidades (parte do usuário):

1 - Campo para digitar o texto o qual será traduzido (input).

2 - Por padrão o idioma inglês está selecionado.

3 - No campo abaixo (output) será apresentado a tradução do texto digitado, após clicar no botão "Translate".

4 - Além da tradução, será gerado um arquivo de áudio que poderá ser executado no player de mídia ao lado do campo de resposta (tradução) e que poderá ser baixado.

5 - O botão "Clear", limpa os campos para que o usuário insira novos dados.
O uso do botão é opcional, uma vez que o texto digitado poder ser subscrito.


##### Funcionalidades (parte do backend):

###### Dependências

O primeiro passo é fazer o isolamento das dependências do projeto criando um ambiente virtual, para isso basta executar:

	python -m venv .venv

	obs.: o nome dado ao ambiente virtual foi .venv mas pode ser qualquer outro.

Para instalar todas as dependências utilizadas no projeto basta executar:

	pip install -r requirements.txt

Abaixo estão listadas de forma independente cada biblioteca e o framework, caso deseje instalar um de cada vez.

O framework python utilizado é o Django em sua versão mais recente.
Para instalação do framework:

	pip install django

Para tradução dos textos é necessário a utilização da biblioteca googletrans em sua versão 3.1.0a0:

	pip install googletrans==3.1.0a0

E por último, para conversão dos textos em áudio, a API Google Text to Speech:

	pip install gTTS


###### Execução do programa

Após o clique no botão "Translate", os dados do formulário (template) são coletados através da requisição e os seguintes processos são executados:

1 - uma session é iniciada - django.sessions;

2 - uma string hexadecimal randomizada é gerada;

3 - uma variável (data) recebe a tradução gerada;

4 - uma outra variável então (audio) recebe o áudio da tradução;

5 - o áudio é salvo em formato .mp3 em um diretório de identificação media, e o nome do arquivo de áudio será a string hexadecimal gerada conforme dito no ítem 2;

6 - uma session do django recebe os dados da tradução - request.session['data'] e uma outra recebe a string hexadecimal como o id - request.session['id'];

7 - uma variável recebe uma string (nome do áudio) para ser retornada no template - audio = f"{request.session['id']}.mp3";

8 - os dados retornados para o template são: os dados coletados do formulário (texto digitado pelo usuário), o texto traduzido através de uma session - response = request.session.get('data') e o audio, identificado através da string "request.session['id'].mp3".

#### ENGLISH VERSION

Text to Audio Translator and Converter

This is an application that aims to translate texts between the following languages ​​(for now):

Portuguese, Spanish and English

The translated text is converted into an audio file that can be played by the media player in the browser and or downloaded by the user.
Features (user part):

1 - Field to type the text which will be translated (input).

2 - By default the English language is selected.

3 - In the field below (output) the translation of the typed text will be displayed, after clicking on the "Translate" button.

4 - In addition to the translation, an audio file will be generated that can be played in the media player next to the answer field (translation) and that can be downloaded.

5 - The "Clear" button, clears the fields for the user to enter new data. The use of the button is optional, as the text entered can be subscripted.
Features (backend part):
dependencies

The first step is to isolate the project's dependencies by creating a virtual environment, just run:

python -m venv .venv

obs.: the name given to the virtual environment was .venv but it can be any other.

To install all the dependencies used in the project just run:

pip install -r requirements.txt

Below are listed independently each library and framework, in case you want to install one at a time.

The python framework used is Django in its latest version. To install the framework:

pip install django

To translate the texts, it is necessary to use the googletrans library in its version 3.1.0a0:

pip install googletrans==3.1.0a0

And finally, for converting texts into audio, the Google Text to Speech API:

pip install gTTS

program execution

After clicking the "Translate" button, the form data (template) is collected through the request and the following processes are performed:

1 - a session is started - django.sessions;

2 - a random hexadecimal string is generated;

3 - a variable (data) receives the generated translation;

4 - then another variable (audio) receives the translation audio;

5 - the audio is saved in .mp3 format in a media identification directory, and the name of the audio file will be the hexadecimal string generated as stated in item 2;

6 - one django session receives the translation data - request.session['data'] and another receives the hexadecimal string as the id - request.session['id'];

7 - a variable receives a string (audio name) to be returned in the template - audio = f"{request.session['id']}.mp3";

8 - the data returned to the template are: the data collected from the form (text typed by the user), the text translated through a session - response = request.session.get('data') and the audio, identified through the string "request.session['id'].mp3".

Note: clicking on "Translate", starts a verification, so that there is not more than one audio file in the directory, and deletes all existing sessions, generating new sessions with the new requests.

Obs.: o clique em "Translate", inicia uma verificação, para que não haja mais de um arquivo de áudio no diretório, e deleta todas sessions existentes, gerando novas sessions com as novas requisições.
