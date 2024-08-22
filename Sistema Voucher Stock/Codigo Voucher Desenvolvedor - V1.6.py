# produtos = {"Fone":[100,2], "Carregador":[101,3] , "Monitor":[102,4] , "Teclado":[103,3] , "Mouse":[104,2] , "GPU":[105,3] , "Gabinete":[106,2]} #aqui vem a predefinição
# escolha = int (input("\nBem Vindo ao Sistema de Controle de Estoque!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultas\nDigite 2 - para Adicionar itens ao estoque\nDigite 3 - para Retirar itens do estoque\nDigite 4 - para Gerar Relatorio\nDigite 5 - para Cadastrar um novo produto\nDigite 6 - para Remover um produto\nDigite 9 - para Sair\nDigite aqui:> ")) #menuzinho
# removed = []
# while escolha != 9:
#     if escolha == 1:
#         busca = input("Digite o nome ou o código do produto que você quer buscar: ")
#         if busca in removed:
#             print("O produto buscado foi excluido, caso necessario deve ser adicionado novamente!")
#         elif busca in produtos:
#             print("O produto é:", busca, "\nSeu código é:", produtos[busca][0], "\nA quantidade atual é:", produtos[busca][1]) #testando dicionario
#         else:  
#             for i, detalhes in produtos.items(): #testando posições, teoricamente ele percorre itens do indicie
#                 print(i)
#                 print(detalhes)
#                 if detalhes[0] == int(busca):
#                     print("O produto é:", i, "\nSeu código é:", detalhes[0], "\nA quantidade atual é:", detalhes[1])
#                     break
#             else:
#                 print("Produto não encontrado.")
#     elif escolha == 2:
#         print("Nomes dos produtos ja cadastrados: ")
#         for i, (chave, valor) in (produtos.items()): #exibir a lita dos nomes que ja tem
#             print("Produto:",chave)
#         adicionar = input ("Digite o nome do produto para adicionar: ")
#         if adicionar in produtos:
#            print("O produto é:", adicionar, "\nSeu código é:", produtos[adicionar][0], "\nA quantidade atual é:", produtos[adicionar][1])
#            print("Quantos itens você quer incluir em",adicionar,"?")
#            adc = int (input ("Digite a quantidade: "))
#            soma = produtos [adicionar][1]
#            result = soma + adc
#            produtos [adicionar][1] = result
#            print ("Foi adicionado",adc,"unidades no produto ", adicionar,", O estoque atualizado é: ", produtos [adicionar][1])
#         else:
#                 print("Produto não encontrado.")
#     elif escolha == 3:
#         print("Nomes dos Produtos ja cadastrados: ")
#         for i, (chave, valor) in enumerate(produtos.items()): #exibir a lita dos nomes que ja tem
#             print("Produto:",chave)
#         remover = input ("Digite o nome do produto para remover: ")
#         if remover in produtos:
#            print("O produto é:", remover, "\nSeu código é:", produtos[remover][0], "\nA quantidade atual é:", produtos[remover][1])
#            print("Quantos itens você quer remover em",remover,"?")
#            rem = int (input ("Digite a quantidade: "))
#            subtração = produtos [remover][1]
#            result = subtração - rem
#            produtos [remover][1] = result
#            print ("Foi removido",rem,"unidades no produto ", remover,", O estoque atualizado é: ", produtos [remover][1])
#         else:
#                 print("Produto não encontrado.")

#     elif escolha == 4:
#         print("Quer gerar o relatorio?")
#         relat = input("Digite Sim ou Não > ")
#         if relat == "Sim" or relat == "SIM" or relat == "sim":
#             print("Nomes dos Produtos ja cadastrados: ")
#             for i, (chave, valor) in enumerate(produtos.items()): #exibir a lita dos nomes que ja tem
#                 print(f"Produto: {chave}, O Código do produto é {valor[0]}, A quantidade atual no estoque é: {valor[1]}")            

#     elif escolha == 5:
#         nome_novo = input("Digite o nome do novo produto: ")
#         codigo_novo = int(input("Digite o código do novo produto: "))
#         quantidade_novo = int(input("Digite a quantidade do novo produto: "))
#         produtos[nome_novo] = [codigo_novo, quantidade_novo]
#         print("Novo produto" , nome_novo, "adicionado com sucesso!")

#     elif escolha == 6:
#         print("Nomes dos produtos ja cadastrados: ")
#         for i, (chave, valor) in enumerate(produtos.items()): #exibir a lita dos nomes que ja tem
#             print("Produto:",chave)
#         nome_remove = input("Digite o nome do produto a ser removido: ")
#         if nome_remove in produtos:
#             produtos.pop(nome_remove)
#             print("O Produto",nome_remove,"Foi removido com sucesso!")
#             removed.append(nome_remove)
#         else:
#             print("Produto não encontrado!")
#     else:
#         print("Opção inválida.")
#     escolhab = int(input("Digite 9 para finalizar ou 0 para voltar ao MENU: "))
#     if escolhab == 9:
#         break
#     elif escolhab == 0:
#         escolha = int (input("\nBem Vindo ao Sistema de Controle de Estoque!!!\n\nDigite uma das opções disponíveis:\nDigite 1 - para Consultas\nDigite 2 - para Adicionar itens ao estoque\nDigite 3 - para Retirar itens do estoque\nDigite 4 - para Gerar Relatorios\nDigite 5 - para Cadastrar um novo produto\nDigite 6 - para Remover um produto\nDigite 9 - para Sair\nDigite aqui:> "))
#     else:
#         print("Digite uma das opções válidas: 9 para finalizar ou 0 para voltar ao menu!")

# print("Saindo do programa...")






import tkinter as tk
from tkinter import messagebox, simpledialog

# Dados dos produtos
produtos = {"Fone": [100, 2], "Carregador": [101, 3], "Monitor": [102, 4], "Teclado": [103, 3], "Mouse": [104, 2], "GPU": [105, 3], "Gabinete": [106, 2]}
removed = []

# Funções do sistema
def consulta():
    busca = simpledialog.askstring("Consulta de Produto", "Digite o nome ou o código do produto:")
    if not busca:
        return
    if busca in removed:
        messagebox.showinfo("Consulta", "O produto buscado foi excluído, caso necessário deve ser adicionado novamente!")
    elif busca in produtos:
        messagebox.showinfo("Consulta", f"O produto é: {busca}\nSeu código é: {produtos[busca][0]}\nA quantidade atual é: {produtos[busca][1]}")
    else:
        for nome, detalhes in produtos.items():
            if str(detalhes[0]) == busca:
                messagebox.showinfo("Consulta", f"O produto é: {nome}\nSeu código é: {detalhes[0]}\nA quantidade atual é: {detalhes[1]}")
                break
        else:
            messagebox.showinfo("Consulta", "Produto não encontrado.")

def adicionar_item():
    listar_produtos()
    adicionar = simpledialog.askstring("Adicionar Produto", "Digite o nome do produto para adicionar:")
    if not adicionar:
        return
    if adicionar in produtos:
        adc = simpledialog.askinteger("Adicionar Produto", f"Quantos itens você quer incluir em {adicionar}?")
        if adc is not None:
            produtos[adicionar][1] += adc
            messagebox.showinfo("Adicionar Produto", f"Foi adicionado {adc} unidades no produto {adicionar}, o estoque atualizado é: {produtos[adicionar][1]}")
    else:
        messagebox.showinfo("Adicionar Produto", "Produto não encontrado.")

def remover_item():
    listar_produtos()
    remover = simpledialog.askstring("Remover Produto", "Digite o nome do produto para remover:")
    if not remover:
        return
    if remover in produtos:
        rem = simpledialog.askinteger("Remover Produto", f"Quantos itens você quer remover de {remover}?")
        if rem is not None:
            if rem <= produtos[remover][1]:
                produtos[remover][1] -= rem
                messagebox.showinfo("Remover Produto", f"Foi removido {rem} unidades do produto {remover}, o estoque atualizado é: {produtos[remover][1]}")
            else:
                messagebox.showinfo("Remover Produto", f"Quantidade a remover excede o estoque atual de {produtos[remover][1]} unidades.")
    else:
        messagebox.showinfo("Remover Produto", "Produto não encontrado.")

def gerar_relatorio():
    relatorio = "Nomes dos Produtos já cadastrados:\n"
    for nome, detalhes in produtos.items():
        relatorio += f"Produto: {nome}, Código: {detalhes[0]}, Quantidade: {detalhes[1]}\n"
    messagebox.showinfo("Relatório de Estoque", relatorio)

def cadastrar_produto():
    nome_novo = simpledialog.askstring("Cadastrar Produto", "Digite o nome do novo produto:")
    if not nome_novo:
        return
    codigo_novo = simpledialog.askinteger("Cadastrar Produto", "Digite o código do novo produto:")
    quantidade_novo = simpledialog.askinteger("Cadastrar Produto", "Digite a quantidade do novo produto:")
    if codigo_novo is not None and quantidade_novo is not None:
        produtos[nome_novo] = [codigo_novo, quantidade_novo]
        messagebox.showinfo("Cadastrar Produto", f"Novo produto {nome_novo} adicionado com sucesso!")

def remover_produto():
    listar_produtos()
    nome_remove = simpledialog.askstring("Remover Produto", "Digite o nome do produto a ser removido:")
    if not nome_remove:
        return
    if nome_remove in produtos:
        produtos.pop(nome_remove)
        removed.append(nome_remove)
        messagebox.showinfo("Remover Produto", f"O Produto {nome_remove} foi removido com sucesso!")
    else:
        messagebox.showinfo("Remover Produto", "Produto não encontrado!")

def listar_produtos():
    lista = "Nomes dos Produtos já cadastrados:\n"
    for nome, detalhes in produtos.items():
        lista += f"Produto: {nome}, Código: {detalhes[0]}, Quantidade: {detalhes[1]}\n"
    messagebox.showinfo("Lista de Produtos", lista)

# Interface gráfica
def main():
    root = tk.Tk()
    root.title("Sistema de Controle de Estoque")

    tk.Label(root, text="Bem Vindo ao Sistema de Controle de Estoque!!!").pack(pady=10)

    tk.Button(root, text="Consulta de Produtos", command=consulta).pack(pady=5)
    tk.Button(root, text="Adicionar Itens ao Estoque", command=adicionar_item).pack(pady=5)
    tk.Button(root, text="Retirar Itens do Estoque", command=remover_item).pack(pady=5)
    tk.Button(root, text="Gerar Relatório", command=gerar_relatorio).pack(pady=5)
    tk.Button(root, text="Cadastrar Novo Produto", command=cadastrar_produto).pack(pady=5)
    tk.Button(root, text="Remover Produto", command=remover_produto).pack(pady=5)
    tk.Button(root, text="Sair", command=root.quit).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
