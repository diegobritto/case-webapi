# customerAPI


## 🛠️ Abrir e rodar o projeto
:warning: Atenção, antes de rodar o programa, siga as instruções abaixo:warning:
- Abra o `Terminal` na `pasta do projeto`
- Certifique-se que a `virtualenv` esteja ativada, caso não tenha, siga os passos abaixo para instalação e ativação
- Instalando a virtualenv `pip install virtualenv`
- Criando uma nova virtualenv `virtualenv nome_da_virtualenv`
- Ativando uma virtualenv `source nome_da_virtualenv/bin/activate`  (Linux ou macOS)
- Ativando uma virtualenv `nome_da_virtualenv/Scripts/Activate`  (Windows)
- Execute o comando `pip install -r requirements.txt`

**Funcionalidades**

- `[GET]/cliente/`: Consulta de todos os clientes da base
- `[GET]/cliente/{Email}`: Consulta de cliente através do e-mail
- `[POST]/cliente/{Email}`: Cadastro de cliente informando o nome completo e e-mail;
- `[PUT]/cliente/{Email}`: Atualização de nome e e-mail (você deve fazer um método que atualize o nome
e e-mail de um cliente registrado).
- `[DELETE]/cliente/{Email}`: Exclusão de um cliente através do e-mail.



 [<img src="https://avatars.githubusercontent.com/u/62968318?s=96&v=4" width=115><br><sub>Diego Britto</sub>](https://github.com/diegobritto) 
