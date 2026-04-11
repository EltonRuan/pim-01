# pim-01

## 📑 Navegação

* [Integrantes do Projeto](#-integrantes-do-projeto)
* [Sobre o Projeto](#-sobre-o-projeto)
* [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
* [Objetivo da Solução](#-objetivo-da-solução)
* [Possíveis Melhorias Futuras](#-possíveis-melhorias-futuras)
* [Funcionamento do Sistema](#-funcionamento-do-sistema)

---

## Integrantes do Projeto

* ARTHUR DOS SANTOS MORAES
* BRUNNO MIRANDA DA SILVEIRA
* ELTON RUAN DA SILVA SANTOS
* JOÃO VITOR DE ALMEIDA PONTES
* NATÁLIA NUNES VIEIRA
* PAULO FERNANDES GERHARDT

---

## 📖 Sobre o Projeto

O projeto **pim-01** foi desenvolvido como parte do **Projeto Integrado Multidisciplinar (PIM)** do primeiro semestre da **UNIP – São José dos Campos**, com o tema **"Análise Ética, Socioambiental e Tecnológica da Infraestrutura de Tecnologia da Informação em uma Organização"**.

A proposta consiste no desenvolvimento de uma solução tecnológica para a empresa **Stampflex**, com foco na melhoria do controle de **estoque** e na gestão **financeira**.

A aplicação foi implementada utilizando a linguagem **Python**, buscando otimizar processos internos, reduzir erros e fornecer uma visão mais clara, organizada e eficiente dos dados relacionados aos produtos e seus respectivos valores.

---

## Tecnologias Utilizadas

* Python
* Git

---

## Objetivo da Solução

* Auxiliar no cálculo de valores e estoque total
* Organizar informações de forma simples e eficiente
* Servir como base para futuras expansões, como interfaces gráficas ou integração com sistemas

---

## Funcionamento do Sistema

O sistema foi desenvolvido com o objetivo de simular um controle de estoque e análise financeira, utilizando estruturas de dados como dicionários e funções para organização das informações.

### Sistema de Login

O acesso ao sistema é realizado por meio de um login simples, onde o usuário deve informar **email** e **senha**.  
Esses dados são validados com informações previamente definidas no sistema.

### Dados da Empresa

As informações da empresa são armazenadas em um dicionário contendo dados como:

- Nome  
- CNPJ  
- Telefone  
- Email  
- Endereço completo  

Esses dados são exibidos de forma organizada no terminal após o login.

### Controle de Estoque

O estoque é representado por um dicionário contendo diversos produtos.  
Cada produto possui atributos como:

- Nome  
- Descrição  
- Dimensões  
- Peso  
- Quantidade em estoque  
- Preço unitário  
- Percentual de desperdício  

O sistema permite listar todos os itens cadastrados e exibir suas informações detalhadas.

### Cálculos Gerais do Estoque

O sistema realiza automaticamente cálculos importantes para a gestão, como:

- Quantidade total de itens em estoque  
- Peso total dos produtos  
- Valor total do estoque  

Esses dados ajudam na tomada de decisão e no controle geral da empresa.

### Cálculo por Produto

Para cada item do estoque, o sistema também calcula:

- Valor unitário  
- Quantidade total disponível  
- Peso total do item  
- Valor total sem desperdício  
- Percentual de desperdício  
- Valor do item com desconto do desperdício  
- Valor total perdido com desperdício  
- Valor final do estoque considerando o desperdício  

### Fluxo de Execução

1. O sistema solicita o login do usuário  
2. Valida as credenciais  
3. Exibe os dados da empresa  
4. Lista os produtos em estoque  
5. Mostra os detalhes de cada produto  
6. Calcula os totais gerais do estoque  
7. Calcula os dados individuais de cada produto  

### Interface

O sistema funciona via **terminal (console)**, exibindo todas as informações por meio de `prints`.  
Atualmente, não possui interface gráfica, mas pode ser expandido futuramente para uma aplicação com interface visual.
