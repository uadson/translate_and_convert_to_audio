### Tradutor e Conversor de Texto em Áudio


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

Obs.: o clique em "Translate", inicia uma verificação, para que não haja mais de um arquivo de áudio no diretório, e deleta todas sessions existentes, gerando novas sessions com as novas requisições.

9 - O botão "Clear", limpa os campos do formulário e exclui o arquivo de áudio existente.