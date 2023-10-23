from aluno import *
from entrada import *
from navegabilidade import *

id = 0
alunos = []

#carregar_arquivo()

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro()

    #navegabilidade
    if (opc == 1):
        #cadastrar
        pass
    elif (opc == 2):
        #imprimir
        pass
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
