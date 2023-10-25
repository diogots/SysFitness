from aluno import *
from entrada import *
from navegabilidade import *

id = 1
alunos = []

#carregar_arquivo()

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    #navegabilidade
    if (opc == 1):
        aln = cadastrar_aluno(id)
        alunos.append(aln)
        id += 1
    elif (opc == 2):
        print_alunos(alunos)
    elif (opc == 3):
        #buscar id
        pass
    elif (opc == 4):
        #filtrar por imc
        pass
    elif (opc == 5):
        #salvar
        break
    else:
        print("Opção inválida!")

    limpar_tela()
