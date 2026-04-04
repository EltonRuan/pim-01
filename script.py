# Dados e Informações:

# dados de login
login_data = {
    "usuario": "admin",
    # "email": "admin@email.com",
    # "senha": "123456",
    "email": "",
    "senha": "",
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

# dados dos produtos em estoque
all_stock_products = {
    "produto1": {
        "nome": "Juntas de expansão de Kevlar",
        "descricao": "Junta de expansão fabricada em Kevlar, indicada para absorção de vibrações e dilatações em tubulações industriais.",
        "dimensoes": "30x30x5 cm",
        "peso": 1.2,
        "quantidade": 50,
        "preco": 185.0,
        "margem_sobra": 0.15
    },
    "produto2": {
        "nome": "Juntas de expansão de Fibra de vidro",
        "descricao": "Junta de expansão em fibra de vidro, ideal para aplicações com alta temperatura e baixa pressão, oferecendo boa resistência térmica.",
        "dimensoes": "25x25x4 cm",
        "peso": 0.9,
        "quantidade": 70,
        "preco": 132.5,
        "margem_sobra": 0.12
    },
    "produto3": {
        "nome": "Juntas de expansão de Fibra cerâmica",
        "descricao": "Junta de expansão em fibra cerâmica, indicada para aplicações de altíssimas temperaturas, com excelente isolamento térmico e resistência química.",
        "dimensoes": "20x20x3 cm",
        "peso": 0.7,
        "quantidade": 120,
        "preco": 210.0,
        "margem_sobra": 0.18
    },
    "produto4": {
        "nome": "Juntas de expansão de Sider",
        "descricao": "Junta de expansão em material siderúrgico, indicada para sistemas industriais que exigem boa resistência mecânica e durabilidade.",
        "dimensoes": "28x28x6 cm",
        "peso": 1.6,
        "quantidade": 80,
        "preco": 165.0,
        "margem_sobra": 0.14
    },
    "produto5": {
        "nome": "Juntas de expansão de Tecido de sílica",
        "descricao": "Junta de expansão em tecido de sílica, indicada para aplicações com altas temperaturas, oferecendo excelente resistência térmica e flexibilidade.",
        "dimensoes": "22x22x4 cm",
        "peso": 0.8,
        "quantidade": 90,
        "preco": 195.0,
        "margem_sobra": 0.16
    },
    "produto6": {
        "nome": "Juntas de norma de Papelão hidráulico com tela",
        "descricao": "Junta de vedação em papelão hidráulico com reforço interno em tela, indicada para aplicações com pressão moderada, garantindo maior resistência mecânica.",
        "dimensoes": "18x18x2 cm",
        "peso": 0.6,
        "quantidade": 150,
        "preco": 45.0,
        "margem_sobra": 0.1
    },
    "produto7": {
        "nome": "Juntas de norma de Papelão hidráulico sem tela",
        "descricao": "Junta de vedação em papelão hidráulico sem reforço, indicada para aplicações de baixa pressão, oferecendo boa vedação com custo reduzido.",
        "dimensoes": "18x18x2 cm",
        "peso": 0.5,
        "quantidade": 180,
        "preco": 32.0,
        "margem_sobra": 0.08
    },
    "produto8": {
        "nome": "Juntas de norma de Grafite com tela",
        "descricao": "Junta de vedação em grafite com reforço interno em tela metálica, indicada para altas temperaturas e pressões, com excelente desempenho em ambientes industriais.",
        "dimensoes": "20x20x2.5 cm",
        "peso": 0.9,
        "quantidade": 110,
        "preco": 98.0,
        "margem_sobra": 0.17
    },
    "produto9": {
        "nome": "Juntas de norma de Grafite sem tela",
        "descricao": "Junta de vedação em grafite sem reforço interno, indicada para altas temperaturas com baixa a média pressão, oferecendo excelente conformabilidade.",
        "dimensoes": "20x20x2 cm",
        "peso": 0.7,
        "quantidade": 140,
        "preco": 72.0,
        "margem_sobra": 0.13
    },
    "produto10": {
        "nome": "Juntas patentes de Kevlar",
        "descricao": "Junta patente em Kevlar, indicada para aplicações industriais que exigem alta resistência mecânica, abrasão e durabilidade em condições severas.",
        "dimensoes": "24x24x3 cm",
        "peso": 1.1,
        "quantidade": 95,
        "preco": 158.0,
        "margem_sobra": 0.16
    },
    "produto11": {
        "nome": "Juntas patentes de Veda-rosca",
        "descricao": "Junta patente para vedação de roscas, indicada para sistemas hidráulicos e pneumáticos, garantindo vedação eficiente contra vazamentos.",
        "dimensoes": "15x15x1 cm",
        "peso": 0.3,
        "quantidade": 220,
        "preco": 18.0,
        "margem_sobra": 0.09
    },
    "produto12": {
        "nome": "Juntas metálicas",
        "descricao": "Junta metálica de alta resistência, indicada para aplicações que exigem vedação sob altas pressões e temperaturas extremas, oferecendo durabilidade prolongada.",
        "dimensoes": "22x22x2 mm",
        "peso": 0.5,
        "quantidade": 130,
        "preco": 120.0,
        "margem_sobra": 0.15
    },
    "produto13": {
        "nome": "Protetores de flange de Sider",
        "descricao": "Protetor de flange em Sider, indicado para proteger superfícies de contato durante armazenamento e transporte, garantindo integridade das peças.",
        "dimensoes": "30x30x3 mm",
        "peso": 0.9,
        "quantidade": 160,
        "preco": 75.0,
        "margem_sobra": 0.12
    },
    "produto14": {
        "nome": "Protetores de flange de Tecido de sílica com teflon",
        "descricao": "Protetor de flange em tecido de sílica com camada de teflon, indicado para superfícies sensíveis, resistente a altas temperaturas e produtos químicos.",
        "dimensoes": "32x32x4 mm",
        "peso": 0.7,
        "quantidade": 140,
        "preco": 112.0,
        "margem_sobra": 0.14
    },
    "produto15": {
        "nome": "Máquina de cortar juntas",
        "descricao": "Equipamento industrial para corte preciso de juntas em diversos materiais, garantindo acabamento uniforme e eficiência na produção.",
        "dimensoes": "120x80x150 cm",
        "peso": 85.0,
        "quantidade": 5,
        "preco": 12500.0,
        "margem_sobra": 0.2
    },
    "produto16": {
        "nome": "Tromba sanfonada de Kevlar com estrutura interna de ferros circulares",
        "descricao": "Tromba sanfonada em Kevlar com reforço interno de ferros circulares, indicada para absorver vibrações e movimentos em sistemas industriais, com alta durabilidade e resistência mecânica.",
        "dimensoes": "50x50x40 cm",
        "peso": 7.5,
        "quantidade": 25,
        "preco": 850.0,
        "margem_sobra": 0.18
    },
    "produto17": {
        "nome": "Fitas de PTFE expandido",
        "descricao": "Fita de PTFE expandido, utilizada para vedação e isolamento em tubulações, resistente a produtos químicos e altas temperaturas, com fácil aplicação.",
        "dimensoes": "10x0.5x5000 mm",
        "peso": 0.2,
        "quantidade": 300,
        "preco": 28.0,
        "margem_sobra": 0.12
    },
    "produto18": {
        "nome": "Gaxetas de PTFE puro quadrada",
        "descricao": "Gaxeta quadrada em PTFE puro, indicada para vedação de equipamentos industriais, oferecendo alta resistência química e térmica com baixo atrito.",
        "dimensoes": "10x10x5 mm",
        "peso": 0.05,
        "quantidade": 250,
        "preco": 35.0,
        "margem_sobra": 0.1
    },
    "produto19": {
        "nome": "Gaxetas de PTFE puro redonda",
        "descricao": "Gaxeta redonda em PTFE puro, indicada para vedação de eixos e tubulações, com excelente resistência química e térmica, durabilidade elevada e baixo atrito.",
        "dimensoes": "10x5 mm",
        "peso": 0.04,
        "quantidade": 230,
        "preco": 38.0,
        "margem_sobra": 0.11
    },
    "produto20": {
        "nome": "Gaxetas grafitada quadrada",
        "descricao": "Gaxeta quadrada grafitada, indicada para vedação de equipamentos industriais sob altas temperaturas e pressão, oferecendo resistência química e durabilidade prolongada.",
        "dimensoes": "12x12x4 mm",
        "peso": 0.06,
        "quantidade": 180,
        "preco": 42.0,
        "margem_sobra": 0.13
    },
    "produto21": {
        "nome": "Gaxetas grafitada redonda",
        "descricao": "Gaxeta redonda grafitada, indicada para vedação de eixos e tubulações sob altas temperaturas, com excelente resistência química, durabilidade e baixo atrito.",
        "dimensoes": "12x4 mm",
        "peso": 0.05,
        "quantidade": 190,
        "preco": 44.0,
        "margem_sobra": 0.12
    },
    "produto22": {
        "nome": "Arruelas de cobre",
        "descricao": "Arruela de cobre, indicada para fixação e vedação em sistemas hidráulicos e mecânicos, oferecendo boa condutividade elétrica e resistência à corrosão.",
        "dimensoes": "15x2 mm",
        "peso": 0.02,
        "quantidade": 500,
        "preco": 1.5,
        "margem_sobra": 0.1
    },
    "produto23": {
        "nome": "Arruelas de aço",
        "descricao": "Arruela de aço, indicada para fixação em sistemas mecânicos e estruturas, oferecendo alta resistência mecânica e durabilidade em ambientes industriais.",
        "dimensoes": "15x2 mm",
        "peso": 0.03,
        "quantidade": 450,
        "preco": 1.2,
        "margem_sobra": 0.1
    }
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

    result = "Produtos em estoque: " + stock_products[0] + ", " + stock_products[1] + ", " + stock_products[2] + ", " + stock_products[3] + ", " + stock_products[4] + ", " + stock_products[5] + ", " + stock_products[6] + ", " + stock_products[7] + ", " + stock_products[8] + ", " + stock_products[9] + ", " + stock_products[10] + ", " + stock_products[11] + ", " + stock_products[12] + ", " + stock_products[13] + ", " + stock_products[14] + ", " + stock_products[15] + ", " + stock_products[16] + ", " + stock_products[17] + ", " + stock_products[18] + ", " + stock_products[19] + ", " + stock_products[20] + ", " + stock_products[21] + ", " + stock_products[22]

    return result

def show_data_product(key, value):
    product_data = []

    for key, value in value.items():
        product_data.append(f"{key.capitalize()}: {value}")

    result = "Dados do produto: " + product_data[0] + ", " + product_data[1] + ", " + product_data[2] + ", " + product_data[3] + ", " + product_data[4] + ", " + product_data[5]

    return result

def calculate_total_stock(products):
    total_quantity = 0
    total_weight = 0
    total_value = 0

    for product in products.values():
        total_quantity += product["quantidade"]
        total_weight += product["peso"]
        total_value += product["preco"] * product["quantidade"]

    return total_quantity, total_weight, total_value

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


total_quantity, total_weight, total_value = calculate_total_stock(all_stock_products)
print(f"Quantidade total em estoque: {total_quantity}")
print(f"Peso total em estoque: {total_weight:.2f} kg")
print(f"Valor total em estoque: R$ {total_value:.2f}")
