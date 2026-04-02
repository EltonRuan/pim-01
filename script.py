# Dados e Informações:

# dados de login
login_data = {
    "usuario": "admin",
    "email": "admin@email.com",
    "senha": "123456",
}

# dados da empresa
all_company_data = {
    "nome": "Stampflex",
    "cnpj": "29.232.897/0001-60",
    "telefone": "(12)3351-6396",
    "email": "contato@stampflex.com",
    "bairro": "Jardim Terras de São João",
    "cidade": "Jacareí",
    "estado": "SP",
    "cep": "12324-784",
    "logradouro": "Av. José Carlos Fernandes",
    "numero": "56",
    "complemento": "Galpão",
}

#Funções:

# Valida o login do usuário, comparando os dados inseridos com os dados pré-definidos
def login(email, senha):
    if email == login_data["email"] and senha == login_data["senha"]:
        return True
    else:
        return False


# Exibir os dados da empresa de forma organizada
def show_company_data(data):
    # print("Dados da Empresa:")

    company_data = []

    for chave, valor in data.items():
        company_data.append(f"{chave.capitalize()}: {valor}")

    result = "Dados da empresa:" + " " + company_data[0] + ", " + company_data[1] + ", " + company_data[2] + ", " + company_data[3] + ", " + company_data[4] + ", " + company_data[5] + ", " + company_data[6] + ", " + company_data[7] + ", " + company_data[8] + ", " + company_data[9]

    return result

# Retornos visíveis no terminal:

print("Seja bem vindo ao sistema de controle de estoque da empresa Stampflex!")
print("Faça login para acessar as informações da empresa.")

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

validate_login = login(email, senha)

# se o login falhar, ele não retorna nenhum valor
if validate_login == False:
    print("Login falhou. Verifique suas credenciais.")

# se o login for bem-sucedido, ele retorna os dados de todas as funções
else:
    print("Login bem-sucedido.")
    print(show_company_data(all_company_data))
