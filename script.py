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

# dados dos items em estoque
all_stock_products = {
    "Juntas de expansão de Kevlar": {
        "nome": "Juntas de expansão de Kevlar",
        "descricao": "Junta de expansão fabricada em Kevlar, indicada para absorção de vibrações e dilatações em tubulações industriais.",
        "dimensoes": "30x30x5 cm",
        "peso": 1.2,
        "quantidade": 50,
        "preco": 185.0,
        "desperdicio": 0.15
    },
    "Juntas de expansão de Fibra de vidro": {
        "nome": "Juntas de expansão de Fibra de vidro",
        "descricao": "Junta de expansão em fibra de vidro, ideal para aplicações com alta temperatura e baixa pressão, oferecendo boa resistência térmica.",
        "dimensoes": "25x25x4 cm",
        "peso": 0.9,
        "quantidade": 70,
        "preco": 132.5,
        "desperdicio": 0.12
    },
    "Juntas de expansão de Fibra cerâmica": {
        "nome": "Juntas de expansão de Fibra cerâmica",
        "descricao": "Junta de expansão em fibra cerâmica, indicada para aplicações de altíssimas temperaturas, com excelente isolamento térmico e resistência química.",
        "dimensoes": "20x20x3 cm",
        "peso": 0.7,
        "quantidade": 120,
        "preco": 210.0,
        "desperdicio": 0.18
    },
    "Juntas de expansão de Sider": {
        "nome": "Juntas de expansão de Sider",
        "descricao": "Junta de expansão em material siderúrgico, indicada para sistemas industriais que exigem boa resistência mecânica e durabilidade.",
        "dimensoes": "28x28x6 cm",
        "peso": 1.6,
        "quantidade": 80,
        "preco": 165.0,
        "desperdicio": 0.14
    },
    "Juntas de expansão de Tecido de sílica": {
        "nome": "Juntas de expansão de Tecido de sílica",
        "descricao": "Junta de expansão em tecido de sílica, indicada para aplicações com altas temperaturas, oferecendo excelente resistência térmica e flexibilidade.",
        "dimensoes": "22x22x4 cm",
        "peso": 0.8,
        "quantidade": 90,
        "preco": 195.0,
        "desperdicio": 0.16
    },
    "Juntas de norma de Papelão hidráulico com tela": {
        "nome": "Juntas de norma de Papelão hidráulico com tela",
        "descricao": "Junta de vedação em papelão hidráulico com reforço interno em tela, indicada para aplicações com pressão moderada, garantindo maior resistência mecânica.",
        "dimensoes": "18x18x2 cm",
        "peso": 0.6,
        "quantidade": 150,
        "preco": 45.0,
        "desperdicio": 0.1
    },
    # "Juntas de norma de Papelão hidráulico sem tela": {
    #     "nome": "Juntas de norma de Papelão hidráulico sem tela",
    #     "descricao": "Junta de vedação em papelão hidráulico sem reforço, indicada para aplicações de baixa pressão, oferecendo boa vedação com custo reduzido.",
    #     "dimensoes": "18x18x2 cm",
    #     "peso": 0.5,
    #     "quantidade": 180,
    #     "preco": 32.0,
    #     "desperdicio": 0.08
    # },
    # "Juntas de norma de Grafite com tela": {
    #     "nome": "Juntas de norma de Grafite com tela",
    #     "descricao": "Junta de vedação em grafite com reforço interno em tela metálica, indicada para altas temperaturas e pressões, com excelente desempenho em ambientes industriais.",
    #     "dimensoes": "20x20x2.5 cm",
    #     "peso": 0.9,
    #     "quantidade": 110,
    #     "preco": 98.0,
    #     "desperdicio": 0.17
    # },
    # "Juntas de norma de Grafite sem tela": {
    #     "nome": "Juntas de norma de Grafite sem tela",
    #     "descricao": "Junta de vedação em grafite sem reforço interno, indicada para altas temperaturas com baixa a média pressão, oferecendo excelente conformabilidade.",
    #     "dimensoes": "20x20x2 cm",
    #     "peso": 0.7,
    #     "quantidade": 140,
    #     "preco": 72.0,
    #     "desperdicio": 0.13
    # },
    # "Juntas patentes de Kevlar": {
    #     "nome": "Juntas patentes de Kevlar",
    #     "descricao": "Junta patente em Kevlar, indicada para aplicações industriais que exigem alta resistência mecânica, abrasão e durabilidade em condições severas.",
    #     "dimensoes": "24x24x3 cm",
    #     "peso": 1.1,
    #     "quantidade": 95,
    #     "preco": 158.0,
    #     "desperdicio": 0.16
    # },
    # "Juntas patentes de Veda-rosca": {
    #     "nome": "Juntas patentes de Veda-rosca",
    #     "descricao": "Junta patente para vedação de roscas, indicada para sistemas hidráulicos e pneumáticos, garantindo vedação eficiente contra vazamentos.",
    #     "dimensoes": "15x15x1 cm",
    #     "peso": 0.3,
    #     "quantidade": 220,
    #     "preco": 18.0,
    #     "desperdicio": 0.09
    # },
    # "Juntas metálicas": {
    #     "nome": "Juntas metálicas",
    #     "descricao": "Junta metálica de alta resistência, indicada para aplicações que exigem vedação sob altas pressões e temperaturas extremas, oferecendo durabilidade prolongada.",
    #     "dimensoes": "22x22x2 mm",
    #     "peso": 0.5,
    #     "quantidade": 130,
    #     "preco": 120.0,
    #     "desperdicio": 0.15
    # },
    # "Protetores de flange de Sider": {
    #     "nome": "Protetores de flange de Sider",
    #     "descricao": "Protetor de flange em Sider, indicado para proteger superfícies de contato durante armazenamento e transporte, garantindo integridade das peças.",
    #     "dimensoes": "30x30x3 mm",
    #     "peso": 0.9,
    #     "quantidade": 160,
    #     "preco": 75.0,
    #     "desperdicio": 0.12
    # },
    # "Protetores de flange de Tecido de sílica com teflon": {
    #     "nome": "Protetores de flange de Tecido de sílica com teflon",
    #     "descricao": "Protetor de flange em tecido de sílica com camada de teflon, indicado para superfícies sensíveis, resistente a altas temperaturas e items químicos.",
    #     "dimensoes": "32x32x4 mm",
    #     "peso": 0.7,
    #     "quantidade": 140,
    #     "preco": 112.0,
    #     "desperdicio": 0.14
    # },
    # "Máquina de cortar juntas": {
    #     "nome": "Máquina de cortar juntas",
    #     "descricao": "Equipamento industrial para corte preciso de juntas em diversos materiais, garantindo acabamento uniforme e eficiência na produção.",
    #     "dimensoes": "120x80x150 cm",
    #     "peso": 85.0,
    #     "quantidade": 5,
    #     "preco": 12500.0,
    #     "desperdicio": 0.2
    # },
    # "Tromba sanfonada de Kevlar com estrutura interna de ferros circulares": {
    #     "nome": "Tromba sanfonada de Kevlar com estrutura interna de ferros circulares",
    #     "descricao": "Tromba sanfonada em Kevlar com reforço interno de ferros circulares, indicada para absorver vibrações e movimentos em sistemas industriais, com alta durabilidade e resistência mecânica.",
    #     "dimensoes": "50x50x40 cm",
    #     "peso": 7.5,
    #     "quantidade": 25,
    #     "preco": 850.0,
    #     "desperdicio": 0.18
    # },
    # "Fitas de PTFE expandido": {
    #     "nome": "Fitas de PTFE expandido",
    #     "descricao": "Fita de PTFE expandido, utilizada para vedação e isolamento em tubulações, resistente a items químicos e altas temperaturas, com fácil aplicação.",
    #     "dimensoes": "10x0.5x5000 mm",
    #     "peso": 0.2,
    #     "quantidade": 300,
    #     "preco": 28.0,
    #     "desperdicio": 0.12
    # },
    # "Gaxetas de PTFE puro quadrada": {
    #     "nome": "Gaxetas de PTFE puro quadrada",
    #     "descricao": "Gaxeta quadrada em PTFE puro, indicada para vedação de equipamentos industriais, oferecendo alta resistência química e térmica com baixo atrito.",
    #     "dimensoes": "10x10x5 mm",
    #     "peso": 0.05,
    #     "quantidade": 250,
    #     "preco": 35.0,
    #     "desperdicio": 0.1
    # },
    # "Gaxetas de PTFE puro redonda": {
    #     "nome": "Gaxetas de PTFE puro redonda",
    #     "descricao": "Gaxeta redonda em PTFE puro, indicada para vedação de eixos e tubulações, com excelente resistência química e térmica, durabilidade elevada e baixo atrito.",
    #     "dimensoes": "10x5 mm",
    #     "peso": 0.04,
    #     "quantidade": 230,
    #     "preco": 38.0,
    #     "desperdicio": 0.11
    # },
    # "Gaxetas grafitada quadrada": {
    #     "nome": "Gaxetas grafitada quadrada",
    #     "descricao": "Gaxeta quadrada grafitada, indicada para vedação de equipamentos industriais sob altas temperaturas e pressão, oferecendo resistência química e durabilidade prolongada.",
    #     "dimensoes": "12x12x4 mm",
    #     "peso": 0.06,
    #     "quantidade": 180,
    #     "preco": 42.0,
    #     "desperdicio": 0.13
    # },
    # "Gaxetas grafitada redonda": {
    #     "nome": "Gaxetas grafitada redonda",
    #     "descricao": "Gaxeta redonda grafitada, indicada para vedação de eixos e tubulações sob altas temperaturas, com excelente resistência química, durabilidade e baixo atrito.",
    #     "dimensoes": "12x4 mm",
    #     "peso": 0.05,
    #     "quantidade": 190,
    #     "preco": 44.0,
    #     "desperdicio": 0.12
    # },
    # "Arruelas de cobre": {
    #     "nome": "Arruelas de cobre",
    #     "descricao": "Arruela de cobre, indicada para fixação e vedação em sistemas hidráulicos e mecânicos, oferecendo boa condutividade elétrica e resistência à corrosão.",
    #     "dimensoes": "15x2 mm",
    #     "peso": 0.02,
    #     "quantidade": 500,
    #     "preco": 1.5,
    #     "desperdicio": 0.1
    # },
    # "Arruelas de aço": {
    #     "nome": "Arruelas de aço",
    #     "descricao": "Arruela de aço, indicada para fixação em sistemas mecânicos e estruturas, oferecendo alta resistência mecânica e durabilidade em ambientes industriais.",
    #     "dimensoes": "15x2 mm",
    #     "peso": 0.03,
    #     "quantidade": 450,
    #     "preco": 1.2,
    #     "desperdicio": 0.1
    # }
}

#Funções:

# Valida o login do usuário, comparando os dados inseridos com os dados pré-definidos
def login(email, senha):
    """Função para validar o login do usuário, comparando os dados inseridos com os dados pré-definidos. """

    if email == login_data["email"] and senha == login_data["senha"]:
        return True
    else:
        return False

# Exibir os dados da empresa de forma organizada
def show_company_data(data):

    """Função para exibir os dados da empresa de forma organizada. """

    company_data = []

    # percorre os dados da empresa e adiciona cada dado formatado à lista company_data
    for key, value in data.items():
        company_data.append(f"{key.capitalize()}: {value}")

    # concatena os dados formatados em uma string
    result = "Dados da empresa:" + " " + company_data[0] + ", " + company_data[1] + ", " + company_data[2] + ", " + company_data[3] + ", " + company_data[4] + ", " + company_data[5] + ", " + company_data[6] + ", " + company_data[7] + ", " + company_data[8] + ", " + company_data[9] + ", " + company_data[10]

    return result

def show_stock_products(products):

    """Função para exibir os produtos em estoque de forma organizada. """

    stock_products = []

    # percorre os produtos em estoque e adiciona cada produto formatado à lista stock_products
    for key in products.keys():
        stock_products.append(key)

    # result = "items em estoque: " + stock_products[0] + ", " + stock_products[1] + ", " + stock_products[2] + ", " + stock_products[3] + ", " + stock_products[4] + ", " + stock_products[5] + ", " + stock_products[6] + ", " + stock_products[7] + ", " + stock_products[8] + ", " + stock_products[9] + ", " + stock_products[10] + ", " + stock_products[11] + ", " + stock_products[12] + ", " + stock_products[13] + ", " + stock_products[14] + ", " + stock_products[15] + ", " + stock_products[16] + ", " + stock_products[17] + ", " + stock_products[18] + ", " + stock_products[19] + ", " + stock_products[20] + ", " + stock_products[21] + ", " + stock_products[22]

    result = "items em estoque: " + stock_products[0] + ", " + stock_products[1] + ", " + stock_products[2] + ", " + stock_products[3] + ", " + stock_products[4] + ", " + stock_products[5] 

    return result

def show_data_product(key, value):

    """Função para exibir os dados de um produto de forma organizada. """

    product_data = []

    # percorre os dados do produto e adiciona cada dado formatado à lista product_data
    for key, value in value.items():
        product_data.append(f"{key.capitalize()}: {value}")

    # result = product_data[0] + ", " + product_data[1] + ", " + product_data[2] + ", " + product_data[3] + ", " + product_data[4] + ", " + product_data[5] + ", " + product_data[6] + ", " + product_data[7] + ", " + product_data[8] + ", " + product_data[9] + ", " + product_data[10] + ", " + product_data[11] + ", " + product_data[12] + ", " + product_data[13] + ", " + product_data[14] + ", " + product_data[15] + ", " + product_data[16] + ", " + product_data[17] + ", " + product_data[18] + ", " + product_data[19] + ", " + product_data[20] + ", " + product_data[21] + ", " + product_data[22]

    result = product_data[0] + ", " + product_data[1] + ", " + product_data[2] + ", " + product_data[3] + ", " + product_data[4] + ", " + product_data[5] 

    return result

def calculate_total_stock(products):

    """Função para calcular a quantidade total dos itens em estoque, o peso total dos itens em estoque e o valor total dos itens em estoque. """

    total_quantity = 0
    total_weight = 0
    total_value = 0

    # percorre os produtos em estoque e soma a quantidade, o peso e o valor
    for product in products.values():
        total_quantity += product["quantidade"]
        total_weight += product["peso"]
        total_value += product["preco"] * product["quantidade"]

    return total_quantity, total_weight, total_value

def calculate_product(product):

    """Função para calcular os dados de um produto de forma organizada. """
    
    # valor unitário do item, ou seja, o valor de 1 unidade do item
    item_value = product["preco"]

    # quantidade total dos itens em estoque
    total_quantity = product["quantidade"]

    # peso total dos itens em estoque
    total_weight = product["peso"] * product["quantidade"]

    # valor total dos itens, sem contar o desperdício
    total_value = product["preco"] * product["quantidade"]

    # % do desperdício do item
    waste_percentage = product["desperdicio"]

    # valor do item com o desperdício, ou seja, o valor do item subtraindo o valor do desperdício
    item_final_value_unit = product["preco"] - (product["preco"] * waste_percentage)

    # valor total do desperdício, ou seja, o desperdício multiplicado pela quantidade total dos itens em estoque
    total_waste = product["preco"] * product["desperdicio"] * product["quantidade"]

    # valor total dos itens, contando o desperdício, ou seja, o valor do item com o desperdício multiplicado pela quantidade total dos itens em estoque
    total_value_final = item_final_value_unit * product["quantidade"]


    return item_value, total_quantity, total_weight, total_value, waste_percentage, item_final_value_unit, total_waste, total_value_final

# Retornos visíveis no terminal:

print("\n")

print("Seja bem vindo ao sistema de controle de estoque da empresa Stampflex! " + "\n")
print("Faça login para acessar as informações da empresa.")

email = input("Digite seu email: ")
senha = input("Digite sua senha: ")

validate_login = login(email, senha)

# se o login falhar, ele não retorna nenhum valor
if validate_login == False:
    print("Login falhou. Verifique suas credenciais." + "\n")

# se o login for bem-sucedido, ele retorna os dados de todas as funções
else:
    print("Login bem-sucedido." + "\n")

    print("---------------------------------------------------------------------------" + "\n")

    print(show_company_data(all_company_data) + "\n")

    print("---------------------------------------------------------------------------" + "\n")
    
    print(show_stock_products(all_stock_products) + "\n")

    print("---------------------------------------------------------------------------" + "\n")

    # retorna os dados de cada item
    for key, value in all_stock_products.items():
        print(show_data_product(key, value) + "\n")

    print("---------------------------------------------------------------------------" + "\n")

    # retorna os dados gerais dos itens
    total_quantity, total_weight, total_value = calculate_total_stock(all_stock_products)
    print(f"Quantidade total dos itens em estoque: {total_quantity}")
    print(f"Peso total dos itens em estoque: {total_weight:.2f} kg")
    print(f"Valor total dos itens em estoque: R$ {total_value:.2f}" + "\n")

    print("---------------------------------------------------------------------------" + "\n")


    # retorna os dados do item, um de cada vez para acessar individualmente 
    for key, value in all_stock_products.items():
        item_value, total_quantity, total_weight, total_value, waste_percentage, item_final_value_unit, total_waste, total_value_final = calculate_product(value)
        print(f"Item: {value['nome']}")
        print(f"Valor unitário (1 item): R$ {item_value:.2f}")
        print(f"Estoque total: {total_quantity}")
        print(f"Valor total (valor total do estoque do item): R$ {total_value:.2f}")
        print(f"Peso total (soma o peso de todas os items do item): {total_weight:.2f} kg")

        print(f"% do desperdício: {waste_percentage:.2%}")
        print(f"Valor do item final (subtrai o valor do item com o desperdício): R$ {item_final_value_unit:.2f}")
        print(f"Valor total do desperdício (soma o valor do desperdício de todos os items): - R$ {total_waste:.2f}")
        print(f"Valor final do estoque (soma o valor dos items com o desperdício): R$ {total_value_final:.2f}"  + "\n")

    print("---------------------------------------------------------------------------" + "\n")

    print("Obrigado por utilizar o sistema de controle de estoque da empresa Stampflex!")
    print("\n")