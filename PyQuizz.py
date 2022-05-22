import os
def nomeJogador():
  jogador = input("Qual é o seu nome? ")
  print("")
  return jogador


def anoNascimento():
  anoNascimento = int(input("Em que ano você nasceu? [Ex. AAAA] "))
  return anoNascimento


def boasvindas():
  print("Seja bem vindo ao quiz!")
  print("")
  print(f"Olá {nomeJogador()}, esperamos que você se divirta enquanto aprende algumas curiosidades sobre a copa do mundo...")
  print("")


def triagem():
  ano = anoNascimento()
  if ano >= 2000:
    print("")
    print("Você provavelmente presenciou 5 copas do mundo, e 'viu' o Brasil ser campeão uma vez...")
    print("")
    print("Talvez você não conheça tanto sobre Copa do Mundo, por isso recomendamos que você inicio o quizz no nível fácil...")
    resposta = input("Quer continuar? [s/n] ")
    if resposta == 's':
      nivelFacil();
    elif resposta == 'n':
      print("Então, de qual nível gostaria de começar?")
      print("Opção 1: Médio")
      print("Opção 2: Difícil")
      op = int(input("Digite a opção: "))
      if op == 1:
        nivelMedio();
      elif op == 2:
        nivelDificil();
      else:
        print("Erro")
    else:
      print("Desculpe, não entendi, reinicie a página, por favor!")
  elif ano >= 1987:
    print("")
    print("Talvez você conheça um pouco sobre Copa do Mundo, por isso recomendamos que você inicio o quizz no nível médio...")
    resposta = input("Quer continuar? [s/n] ")
    if resposta == 's':
      nivelMedio();
    elif resposta == 'n':
      print("Então, de qual nível gostaria de começar?")
      print("Opção 1: Fácil")
      print("Opção 2: Difícil")
      op = int(input("Digite a opção: "))
      if op == 1:
        nivelFacil();
      elif op == 2:
        nivelDificil();
      else:
        print("Erro")
    else:
      print("Desculpe, não entendi, reinicie a página, por favor!")
  elif ano < 1987:
    print("Você deve saber muito sobre a Copa do Mundo, por isso recomendamos que você inicio o quizz no nível Difícil...")
    resposta = input("Quer continuar? [s/n] ")
    if resposta == 's':
      nivelDificil();
    elif resposta == 'n':
      print("Então, de qual nível gostaria de começar?")
      print("Opção 1: Fácil")
      print("Opção 2: Médio")
      op = int(input("Digite a opção: "))
      if op == 1:
        nivelFacil();
      elif op == 2:
        nivelMedio();
      else:
        print("Erro")
    else:
      print("Desculpe, não entendi, reinicie a página, por favor!")
  else:
    print("Erro")

def nivelFacil():
  print("Você entrou no nível fácil")
  

def nivelMedio():
  print("Você entrou no nível médio")


def nivelDificil():
  print("Você entrou no nível difícil")

  
def main():
  boasvindas()
  triagem()


main()

