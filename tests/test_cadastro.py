from CadastroSystem import Cadastro

def test_cadastro_email_valido():
    cadastro = Cadastro()
    resultado = cadastro.cadastrar_usuario("Carlos", "Carlos@email.com", "senha123")
    assert resultado == "Cadastro realizado com sucesso"

def test_cadastro_email_invalido():
    cadastro = Cadastro()
    resultado = cadastro.cadastrar_usuario("Carlos", "Carlosemail.com", "senha123")
    assert resultado == "Email inválido"

def test_cadastro_campos_obrigatorios():
    cadastro = Cadastro()
    resultado = cadastro.cadastrar_usuario("", "","")
    assert resultado == "Todos os campos são obrigatórios"