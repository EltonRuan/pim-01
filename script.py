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
    "numero": 56,
    "complemento": "Galpão",
}

all_stock_products = {
    "produto1": {
        "nome": "Produto A",
        "descricao": "Descrição do Produto A",
        "dimensoes": "10x20x30 cm",
        "peso": "2kg",
        "quantidade": 100,
        "preco": 10.0,
        "margem_sobra": 0.1,
    },
    "produto2": {
        "nome": "Produto B",
        "descricao": "Descrição do Produto B",
        "dimensoes": "10x20x30 cm",
        "peso": "2kg",
        "quantidade": 100,
        "preco": 10.0,
        "margem_sobra": 0.1,
    },
    "produto3": {
        "nome": "Produto C",
        "descricao": "Descrição do Produto C",
        "dimensoes": "10x20x30 cm",
        "peso": "2kg",
        "quantidade": 200,
        "preco": 5.0,
        "margem_sobra": 0.1,
    },
    "produto4": {
        "nome": "Produto D",
        "descricao": "Descrição do Produto D",
        "dimensoes": "10x20x30 cm",
        "peso": "2kg",
        "quantidade": 200,
        "preco": 5.0,
        "margem_sobra": 0.1,
    },
    "produto5": {
        "nome": "Produto E",
        "descricao": "Descrição do Produto E",
        "dimensoes": "10x20x30 cm",
        "peso": "2kg",
        "quantidade": 200,
        "preco": 5.0,
        "margem_sobra": 0.1,
    },
    "produto6": {
        "nome": "Produto F",
        "descricao": "Descrição do Produto F",
        "dimensoes": "10x20x30 cm",
        "peso": "2kg",
        "quantidade": 200,
        "preco": 5.0,
        "margem_sobra": 0.1,
    },
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

    company_data = []

    for key, value in data.items():
        company_data.append(f"{key.capitalize()}: {value}")

    result = "Dados da empresa:" + " " + company_data[0] + ", " + company_data[1] + ", " + company_data[2] + ", " + company_data[3] + ", " + company_data[4] + ", " + company_data[5] + ", " + company_data[6] + ", " + company_data[7] + ", " + company_data[8] + ", " + company_data[9]

    return result

def show_stock_products(products):
    stock_products = []

    for key in products.keys():
        stock_products.append(key)

    result = "Produtos em estoque: " + stock_products[0] + ", " + stock_products[1] + ", " + stock_products[2] + ", " + stock_products[3] + ", " + stock_products[4] + ", " + stock_products[5]

    return result

def show_data_product(key, value):
    product_data = []

    for key, value in value.items():
        product_data.append(f"{key.capitalize()}: {value}")

    result = "Dados do produto: " + product_data[0] + ", " + product_data[1] + ", " + product_data[2] + ", " + product_data[3] + ", " + product_data[4] + ", " + product_data[5]

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
    print("Login bem-sucedido." + "\n")
    print(show_company_data(all_company_data) + "\n")
    print(show_stock_products(all_stock_products) + "\n")
    for key, value in all_stock_products.items():
        print(show_data_product(key, value) + "\n")
