#Fernanda Andrade e Italo Guasti

# Frase de César, 15 deslocamentos: IT HAS BEEN SAID THAT ASTRONOMY IS A HUMBLING AND CHARACTER BUILDING EXPERIENCE THERE IS PERHAPS NO BETTER DEMONSTRATION OF THE FOLLY OF HUMAN CONCEITS THAN THIS DISTANT IMAGE OF OUR TINY WORLD TO ME IT UNDERSCORES OUR RESPONSIBILITY TO DEAL MORE KINDLY WITH ONE ANOTHER AND TO PRESERVE AND CHERISH THE PALE BLUE DOT THE ONLY HOME WE HAVE EVER KNOWN

from math import log10
from ngram_score import ngram_score

ngram_scorer = ngram_score('quadgrams.txt')

#função que vai criar o menu
def menu():
    escolha = int(input("BEM VINDO USUARIO\n"
                       "1 - Cifra de César\n2 - Cifra de substituição\n"
                       "Qual cifra deseja descriptografar: "))

    if escolha == 1:
        print("CIFRA DE CESAR")
        arquivo = input("Digite o caminho do arquivo txt: ")
        deslocamento = int(input("Digite o deslocamento desejado: "))
        print("\n")
        conteudo_arquivo = percorrer_arquivo(arquivo)
        txt = binario_para_texto(conteudo_arquivo)
        descriptografado = cifra_de_cesar(txt, deslocamento)
 
    elif escolha == 2:
        print("CIFRA DE SUBSTITUIÇÃO")
        arquivo = input("Digite o caminho do arquivo txt: ")
        conteudo_arquivo = percorrer_arquivo(arquivo)
        txt = binario_para_texto(conteudo_arquivo)
        
        pontuacao = ngram_scorer.score(descriptografado)
        print("Pontuação do texto descriptografado:", pontuacao)


    else:
        print("Opção inválida")

#função que percorre e armazena arquivo
def percorrer_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
        return conteudo  # Retorna o conteúdo lido do arquivo

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    except Exception as e:
        print("Ocorreu um erro:", str(e))
        return None
    
#funcao que converte binario para texto

def binario_para_texto(binario):
    texto = ''.join(chr(int(char, 2)) for char in binario.split())
    print("Texto criptografado:", texto)
    print("\n")
    return texto

# Função para descriptografar com a cifra de César
def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            if letra.isupper():
                nova_letra = chr(((ord(letra) - deslocamento - 65) % 26) + 65)
            else:
                nova_letra = chr(((ord(letra) - deslocamento - 97) % 26) + 97)
            resultado += nova_letra
        else:
            resultado += letra
    print("Texto descriptografado: ", resultado)
    print("\n")
    return resultado


# main principal
def main():
    menu()

if __name__ == "__main__":
    main()