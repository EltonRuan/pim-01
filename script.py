# dados da empresa, preenchidos manualmente, para serem usados posteriormente

# uso de dicionário para armazenar os dados da empresa
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

# função para exibir os dados da empresa de forma organizada
def show_company_data(data):
    # print("Dados da Empresa:")

    company_data = []

    for chave, valor in data.items():
        company_data.append(f"{chave.capitalize()}: {valor}")

    result = "Dados da empresa:" + " " + company_data[0] + ", " + company_data[1] + ", " + company_data[2] + ", " + company_data[3] + ", " + company_data[4] + ", " + company_data[5] + ", " + company_data[6] + ", " + company_data[7] + ", " + company_data[8] + ", " + company_data[9]

    return result


# Retorno das funções para exibir os dados
print(show_company_data(all_company_data))