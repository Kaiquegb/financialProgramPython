# Criar uma lista de transações para que todos os dados/entradas sejam armazenados nela.
transactions = []
# Abrir o arquivo no modo append, a fim de criar sem modificar o arquivo caso ele já exista.
open("transactions.csv", "a").close()
# Abrir o arquivo no modo de leitura, para ler as informações do mesmo.
file = open("transactions.csv", "r")
# Salvar o texto do arquivo em uma variável.
file_data = file.read()
# Fechar o arquivo.
file.close()

# Passar por cada linha do arquivo, separadas por espaço.
for line in file_data.split("\n"):
    # Checar se a linha não está vazia.
    if line != "":
        # Separar a linha por vírgula.
        values = line.split(",")
        # Adicionar um item (correspondendo a cada linha do arquivo) na lista de transações. Cada entrada será separada por vírgula, os valores correspodem por cada informação presente no espaço entre as vírgulas.
        transactions.append(
            {
                "name": values[0],
                "category": values[1],
                # Declarar o "value" para ser lido com 'float', pois no arquivo se mantém como 'string'.
                "value": float(values[2]),
                "type": values[3],
                "date": values[4]
            }
        )


# Função "save_data" criada para salvar a lista de transações num arquivo CSV.
def save_data(transactions):
    # Abrir o arquivo CSV no modo de escrita, apagando todos os dados que tinham antes.
    file = open("transactions.csv", "w")

    # Escrever/reconhecer os dados de cada item da lista no arquivo.
    for item in transactions:
        name = item["name"]
        category = item["category"]
        value = item["value"]
        type = item["type"]
        date = item["date"]
        # Escrever os dados separados por ",".
        file.write(f"{name},{category},{value},{type},{date}\n")

    # Fechar o arquivo CSV.
    file.close()


# Função "add" criada para adicionar as transações no sistema. Serão pedidos os dados necessários para cada transação.
def add(transactions):
    # Receber os dados necessários da transação a ser adicionada.
    name = input("Digite o nome da transação: ")
    category = input("Digite a categoria da transação: ")
    value = input("Digite o valor da transação: ")
    type = input("Digite o tipo da transação (ex.: débito ou crédito): ")
    # Receber a data da transação no formato ano-mês-dia para que o programa identifique.
    date = input("Digite a data da transação (ex.: ano-mês-dia): ")

    # Adicionar a transação na lista.
    transactions.append(
        {
            # Criar um dicionário para que as entradas sejam identificadas pelos nomes das variáveis, ao invés do seu "índice/valor".
            "name": name,
            "category": category,
            # Converter o "valor" para float, assim, ao invés de ser lido como str, será lido como número.
            "value": float(value),
            "type": type,
            "date": date
        }
    )

    print("Transação registrada com sucesso!")
    print("\n-------------------------\n")


# Função "print_data" criada pra printar os dados de uma transação.
def print_data(transaction):
    # Reconhecer os dados de entrada existentes na lista "transactions".
    name = transaction["name"]
    category = transaction["category"]
    value = transaction["value"]
    type = transaction["type"]
    date = transaction["date"]
    
    # Para encurtar o código, ao invés de adicionar o bloco de prints, só será escrito o "print_data".
    print(f"Nome - {name}")
    print(f"Categoria - {category}")
    print(f"Valor - {value:.2f}")
    print(f"Tipo - {type}")
    print(f"Data - {date}\n")

# Função "update" criada para alterar os dados de um transação já existente.
def update(transactions):
    # Receber o nome da transação que o usuário deseja alterar.
    name = input("Digite o nome da transação que deseja atualizar: ")
    print("\n-------------------------\n")

    for item in transactions:
        # Checar o nome da transação na lista de transações. Caso tenha achado a transação em questão, o programa pedirá os novos dados.
        if item["name"].lower() == name.lower():
            # Receber os novos dados para atualização.
            new_name = input("Digite o novo nome da transação: ")
            new_category = input("Digite a nova categoria da transação: ")
            new_value = input("Digite o novo valor da transação: ")
            new_type = input("Digite o novo tipo da transação (ex.: débito ou crédito): ")
            new_date = input("Digite a nova data da transação (ex.: ano-mês-dia): ")

            # Alterar os dados, modificando os antigos dados, pelas novas entradas.
            item["name"] = new_name
            item["category"] = new_category
            item["value"] = float(new_value)
            item["type"] = new_type
            item["date"] = new_date

    print("Transação atualizada com sucesso!")
    print("\n-------------------------\n")


# Função "delete" criada para deletar uma transação cadastrada na lista.
def delete(transactions):
    # Receber o nome da transação que o usuário deseja deletar.
    name = input("Digite o nome da transação que deseja deletar: ")
    print("\n-------------------------\n")

    for item in transactions:
        # Checar o nome da transação na lista de transações. Caso tenha achado a transação em questão, o programa removerá a transação.
        if item["name"].lower() == name.lower():
            transactions.remove(item)
            break

    print("Transação deletada com sucesso!")
    print("\n-------------------------\n")


# Funcão "list_transactions" criada para listar os dados de todos os itens da lista, caso exista pelo menos uma transação já cadastrada.
def list_transactions(transactions):
    # Checar se a lista tá vazia.
    if (len(transactions) == 0):
        print("Lista de transações vazia!")
        print("\n-------------------------\n")
        return

    # Caso a lista não esteja vazia, o programa se direciona para o loop e lista os dados das transações cadastradas.
    for item in transactions:
        print_data(item)

    print("-------------------------\n")


# Funcão "list_by_category" criada para listar os dados de todas as transações de uma categoria específica, caso exista pelo menos uma cadastrada.
def list_by_category(transactions):
    # Receber a categoria desejada para procurar as transações existentes.
    category = input("Digite a categoria das transações que deseja listar: ")
    print("\n-------------------------\n")
    
    # Criar lista auxiliar para armazenar os dados e permitir printar a listagem, por serem várias informações diferentes.
    items_list = []
    # Passar por cada item da lista de transações.
    for item in transactions:
        # Checar se a categoria do item é a categoria escolhida pelo usuário. Adicionar a função .lower para deixar todas as letras em minúsculo, evitando que um item não seja achado por ter uma letra maiúscula.
        if item["category"].lower() == category.lower():
            # Caso seja compatível, adicionar transação na lista auxiliar.
            items_list.append(item)

    # Checar se a lista auxiliar está vazia (não existir nenhuma transação daquela categoria).
    if (len(items_list) == 0):
        print("Nenhuma transação com a categoria escolhida foi encontrada!")
        print("\n-------------------------\n")
        return

    # Caso a lista não esteja vazia, o programa se direciona para o loop e lista os dados das transações cadastradas naquela categoria.
    for item in items_list:
        print_data(item)

    print("-------------------------\n")


# Função "list_debits" criada para listar todas as transações do tipo débito (saídas de dinheiro).
def list_debits(transactions):
    items_list = []
    for item in transactions:
        # Checar se o tipo da transação é débito. Adicionar a função .lower para deixar todas as letras em minúsculo, evitando que um item não seja achado por ter uma letra maiúscula.
        if item["type"].lower() == "débito":
            # Caso seja, adicionar na lista auxiliar.
            items_list.append(item)

    # Checar se a lista auxiliar está vazia (não existe nenhuma transação do tipo débito).
    if len(items_list) == 0:
        print("Não há nenhuma transação de débito")
        print("\n-------------------------\n")
        return
    
    # Caso a lista não esteja vazia, o programa se direciona para o loop e lista os dados das transações cadastradas do tipo débito.
    for item in items_list:
        print_data(item)

    print("-------------------------\n")


# Função "list_credits" criada para listar todas as transações do tipo crédito (entradas de dinheiro).
def list_credits(transactions):
    items_list = []
    for item in transactions:
        # Checar se o tipo da transação é crédito. Adicionar a função .lower para deixar todas as letras em minúsculo, evitando que um item não seja achado por ter uma letra maiúscula.
        if item["type"].lower() == "crédito":
            # Caso seja, adicionar na lista auxiliar.
            items_list.append(item)

    # Checar se a lista auxiliar está vazia (não existe nenhuma transação do tipo crédito).
    if len(items_list) == 0:
        print("Não há nenhuma transação de crédito")
        print("\n-------------------------\n")
        return

    # Caso a lista não esteja vazia, o programa se direciona para o loop e lista os dados das transações cadastradas do tipo crédito.
    for item in items_list:
        print_data(item)

    print("-------------------------\n")


# Função "list_by_date" criada para listar as transações realizadas em um dado período de tempo.
def list_by_date(transactions):
    # Receber a data de início do período desejado pelo usuário. 
    start_date = input("Digite a data de início do período (ex.: ano-mês-dia): ")
    # Receber a data final do período desejado pelo usuário.
    end_date = input("Digite a data final do período (ex.: ano-mês-dia): ")
    print("\n-------------------------\n")

    items_list = []
    # Passar por cada item da lista auxiliar de transações.
    for item in transactions:
        # Checar se a data do item pertence ao período de tempo estabelecido nas entradas.
        if item["date"] >= start_date and item["date"] <= end_date:
            # Caso pertença, adicionar transação na lista auxiliar.
            items_list.append(item)

    # Checar se a lista auxiliar está vazia (não existe nenhuma transação no dado período de tempo).
    if len(items_list) == 0:
        print("Não há transações realizadas nesse período de tempo!")
        print("\n-------------------------\n")
        return
    
    # Caso a lista não esteja vazia, o programa se direciona para o loop e lista os dados das transações cadastradas no dado período.
    for item in items_list:
        print_data(item)

    print("-------------------------\n")



# Criar um loop para que o Menu sempre apareça para o usuário, a fim de realizar as ações desejadas.
while True:
    # Criar um Menu de opções. 
    print("<1> - Adicionar")
    print("<2> - Listar transações")
    print("<3> - Listar por categoria")
    print("<4> - Listar transações por data")
    print("<5> - Listar transações de débito")
    print("<6> - Listar transações de crédito")
    print("<7> - Atualizar")
    print("<8> - Deletar")
    print("<0> - Sair")

    # Receber a escolha do usuário.
    option = int(input("\nDigite sua escolha: "))
    print("\n-------------------------\n")

    # Checar qual foi a opção selecionada pelo usuário e chamar a função correspondente a cada uma delas. 
    if option == 1:
        add(transactions)
    elif option == 2:
        list_transactions(transactions)
    elif option == 3:
        list_by_category(transactions)
    elif option == 4:
        list_by_date(transactions)
    elif option == 5:
        list_debits(transactions)
    elif option == 6:
        list_credits(transactions)
    elif option == 7:
        update(transactions)
    elif option == 8:
        delete(transactions)
    elif option == 0:
        print("Até a próxima!")
        # Salvar todas as movimentações realizadas, a fim de manter no arquivo e permitir que o usuário tenha acesso ao seu histórico de utilização.
        save_data(transactions)
        break
    else:
        print("Escolha inválida, selecione outra opção")
        print("\n-------------------------\n")