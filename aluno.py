from entrada import *
import json

def cadastrar_aluno(id:int):
    """
    Cadastrar um dicionário de aluno e o retorna

    Parâmetro:
        - id: inteiro com o idenficador do aluno no sistema

    Retorno:
        - aln: dicionário com as informações do aluno lidas do teclado
    """
    aln = {}
    aln['id'] = id
    aln['nome'] = input("Nome do aluno: ")
    
    #ler sexo
    while True:
        sexo = input("sexo ('M' - Masculino 'F'- Feminino 'NB' - Não-binárie) : ")
        sexo = sexo.upper() #converter para maiúsculo
        if sexo in ["M","F","NB"]:
            aln["sexo"] = sexo
            break
        else:
            print("Opção inválida! digite novamente...")
    
    aln['peso'] = ler_real("Peso (Kg): ",pos=True)
    aln['altura'] = ler_real("Altura (m):",pos=True)
    aln['mensalidade'] = ler_real("Mensalidade: ",pos=True)

    print("Cadastro de usuário lido com sucesso:\n")
    print_aluno(aln)
    #return aln
    return aln

def print_aluno(aln:dict):
    """
    Imprime de forma inteligível os dadosa de um dicionário de aluno
    
    Parâmetro:
        - aln: Dicionário de aluno a ser impresso
    
    """

    for chave in aln:        
        print(f"{chave.capitalize()}: {aln[chave]}")

def print_alunos(alunos:list):
    """
    Imprime o conteúdo de uma lista de alunos de forma inteligível
    
    Parâmetro:
        - alunos: Lista de dicionários de aluno
    """
    print(f"Imprimindo {len(alunos)} cadastro(s) de alunos...\n")
    
    for aln in alunos:
        print_aluno(aln)
        print("-----------------------")

def salvar_dados(alunos:list,id:int):
    lista = [alunos,id]

    try:
        with open("Alunos.json","w") as esc:
            json.dump(lista,esc,indent=4,ensure_ascii=False)
            print("Dados salvos com sucesso!")
    except:
        print("Ocorreram erros na escrita do arquivo!")


def ler_dados():
    try:
        with open("Alunos.json","r") as ler:
            lista = json.load(ler)
            print("Dados lidos com sucesso!")
            return lista
    except:
        print("Ocorreram erros na leitura do arquivos!")