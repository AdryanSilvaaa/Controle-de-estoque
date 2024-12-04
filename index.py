import mysql.connector


# Estabelecendo a conexão com o banco de dados

def conectar():
    
    return mysql.connector.connect(
    host='127.0.0.1',  # Endereço do servidor MySQL
    user='root',  # Seu usuário MySQL
    password='lindo243020',  # Sua senha MySQL
    database='controle_de_estoque'  # Nome do banco de dados
) 

#Função para obter o nome da categoria ao inves do id
def obter_categoria_id(nome_categoria):
    conn = conectar()
    cursor = conn.cursor()
    sql_select = "SELECT id_categoria FROM categorias WHERE nome_categoria = %s"
    cursor.execute(sql_select, (nome_categoria,))
    resultado = cursor.fetchone()
    cursor.fetchall()  # Certificar que todos os resultados são lidos
    cursor.close()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        raise ValueError("Categoria não encontrada")
    
#Função para obter o nome da localizaçao ao inves do id
def obter_localizacao_id(descricao):
    conn = conectar()
    cursor = conn.cursor()
    sql_select = "SELECT id_localizacao FROM localizacoes WHERE descricao = %s"
    cursor.execute(sql_select, (descricao,))
    resultado = cursor.fetchone()
    cursor.fetchall()  # Certificar que todos os resultados são lidos
    cursor.close()
    conn.close()
    if resultado:
        return resultado[0]
    else:
        raise ValueError("Localização não encontrada")

#FUNÇÃO PARA INSERIR UM NOVO PRODUTO A TABELA PRODUTOS
def inserir_produto(nome_produto, descricao, preco, quantidade, categoria_id, localizacao_id):
    conn = conectar()
    cursor = conn.cursor()
    sql_insert = """
    INSERT INTO produtos (nome_produto, descricao, preco, quantidade, categoria_id, localizacao_id)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql_insert, (nome_produto, descricao, preco, quantidade, categoria_id, localizacao_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Produto inserido com sucesso!")
    

#FUNÇÃO PARA INSERIR UMA NOVA CATEGORIA
def inserir_categoria(nome_categoria, descricao):
    conn = conectar()   
    cursor = conn.cursor()
    sql_insert = """ 
    INSERT INTO categorias(nome_categoria, descricao) 
    VALUES(%s, %s)"""
    cursor.execute(sql_insert,(nome_categoria, descricao))
    conn.commit()
    cursor.close()
    conn.close()    
    print("Categoria inserida com sucesso !!!")
    
    
#FUNÇÃO PARA PODER INSERIR UMA NOVA LOCALIZAÇAO
def inserir_localizacao(descricaoDaLocalizacao, deposito):
    conn = conectar()
    cursor = conn.cursor()
    sql_insert = """
    INSERT INTO localizacoes(descricao, deposito)
    VALUES (%s, %s)"""
    cursor.execute(sql_insert,(descricaoDaLocalizacao, deposito))
    conn.commit()
    cursor.close()
    conn.close()
    print ("Nova localização inserida com sucesso !!")    
    
    
#FUNÇÃO PARA VER ITEN NA TABELA
def consultar_produtos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos"
        cursor.execute(sql_select)
        produtos = cursor.fetchall()
        cursor.close()
        conn.close()
        return produtos
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return []
    
    
#FUNÇAO DO MENU PARA ESCOLHER OQUE FAZER
def mostrar_menu():
    print("1. Ver estoque")
    print("2. Cadastrar produto")
    print('3. Cadastrar nova categoria')
    print('4. Cadastrar nova localização')
    print("3. Sair")
    
    
#FUNÇÃO PRINCIPAL QUE CHAMA AS OUTRAS FUNÇÕES 
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            produtos = consultar_produtos()
            for produto in produtos:
                print(produto)
        elif escolha == '2':
            nome_produto = input("Nome do produto: ")
            descricao = input("Descrição: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            nome_categoria = input("Nome da categoria: ")
            descricao_localizacao = input("Descrição da localização: ")
            try:
                categoria_id = obter_categoria_id(nome_categoria)
                localizacao_id = obter_localizacao_id(descricao_localizacao)
                inserir_produto(nome_produto, descricao, preco, quantidade, categoria_id, localizacao_id)
            except ValueError as e:
                print(e)
        elif escolha == '3':
            nome_categoria = input("Digite o nome da nova categoria : ")
            descricao = input('Digite uma descrição sobre a nova categoria')
            inserir_categoria(nome_categoria, descricao)
        elif escolha == '4':
            deposito = input("Digite um nome para o novo deposito")
            descricaoDaLocalizacao = input("Digite a descrição da localização")
            inserir_localizacao( deposito,descricaoDaLocalizacao )
            
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()


