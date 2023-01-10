# Uma CLI em Python para consumir da API do ViaCEP e obter os dados mediante uma requisição http.
Esta é uma aplicação de linha de comando(CLI) bem simples com a função de obter os dados de um CEP enviado uma requisição HTTP para a API do ViaCEP.</br>
Os dados resultantes dessa consulta são exibidos na tela no formato JSON.</br>
É possível salvar todas as consultas em um arquivo `.txt` mantendo o formato das informações em JSON para posteriormente reutilizar em outras aplicações.

<div align="center">
<img width="455" src="https://i.imgur.com/C6Zk3VF.jpg">
</div>

## Este projeto utiliza:

* [Python](https://www.python.org/)
* [Requests](https://pypi.org/project/requests/)
* [ViaCEP](https://viacep.com.br/)

## Como executar localmente?

* Clone esse repositório: **git clone https://github.com/fspjonny/consulta_cep_viacep_api.git**<br>
* Tenha o **Python** instalado no computador ou tenha um ambiente virtual **(venv)** com Python funcionando e aceitando um desses comandos de terminal **`py --version`** ou **`python --version`**
* Instale os requerimentos no seu computador ou seu ambiente virtual.</br>
O terminal de comando deve estar aberto no mesmo lugar onde estão os arquivos da aplicação.</br>
**`pip install -r requirements.txt`**

* Se ocorreu tudo bem com a instalação dos requerimentos, então após isso a aplicação deve ser executada através desta linha de comando abaixo:</br>
**`python main.py`**


A tela da aplicação deve ser igual a da imagem exibida no topo deste documento.</br>
Caso queira salvar uma consulta feita, a aplicação vai criar na mesma pasta da plicação um arquivo chamado "**resultado.txt**" que é o local onde as consultas serão salvas.