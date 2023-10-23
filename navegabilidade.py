import os
import sys


def imprimir_cabecalho():
    """
    Imprime o cabeçalho do programa
    """
    cabecalho = """
****************************************************************
*                                                              *
*                         SysFitness                           *
*                                                              *
*                                       powered by: CC-UNIP 23 *
****************************************************************    
"""
    print(cabecalho)

def exibir_menu():
    menu = """
 1 - Cadastrar aluno
 2 - Imprimir cadastros
 3 - Buscar aluno por id
 4 - Filtrar alunos por IMC
 5 - Salvar e sair
 -------------------------------
"""
    print(menu)

def limpar_tela():
    input("Digite 'ENTER' para continuar...")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
     