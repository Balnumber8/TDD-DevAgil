
from CadastroSystem import Cadastro

def test_login_com_credenciais_validas():
    cadastro = Cadastro()
    cadastro.cadastrar_usuario("Carlos", "carlos@email.com", "senha123")
    resultado = cadastro.login("carlos@email.com", "senha123")
    assert resultado == "Login bem-sucedido"

def test_login_com_email_incorreto():
    cadastro = Cadastro()
    cadastro.cadastrar_usuario("Carlos", "carlos@email.com", "senha123")
    resultado = cadastro.login("errado@email.com", "senha123")
    assert resultado == "Credenciais inválidas"

def test_login_com_senha_incorreta():
    cadastro = Cadastro()
    cadastro.cadastrar_usuario("Carlos", "carlos@email.com", "senha123")
    resultado = cadastro.login("carlos@email.com", "senhaerrada")
    assert resultado == "Credenciais inválidas"
