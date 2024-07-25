import os

carros = [ # tupla de todos os carros
          ("Chevrolet Tracker", 120),
          ("Chevrolet Onix", 90),
          ("Chevrolet Spin", 150),
          ("Hyundai HB20", 85),
          ("Hyundai Tucson", 120),
          ("Fiat Uno", 60),
          ("Fiat Mobi", 70),
          ("Fiat Pulse", 130)
          ]

alugados = []


def mostrar_lista_de_carros(lista_de_carros):
  for i, car in enumerate(lista_de_carros):
    print("[{}] {} - R$ {} /dia. ".format(i,car[0], car[1]))


while True:
  os.system("cls")
  print("===============================")
  print("Bem Vindo a Locadora de Carros")
  print("===============================\n")

  print("O que vc deseja fazer?")
  print("0 - Mostrar Carros | 1 - Alugar | 2 - Devolver")
  op = int(input())

  os.system("cls")

  if op == 0:
    mostrar_lista_de_carros(carros)

  elif op == 1:
    mostrar_lista_de_carros(carros)
    print("\n==================")
    print("Cod. do carro: ")
    cod_car = int(input())

    print("\n Por quantos dias deseja alugar o carro? ")
    days_car = int(input())
    os.system("cls")

    print("Voce escolheu o carro {}, por {} dias".format(carros[cod_car][0], days_car))
    print("O aluguel totalizaria R$ {}. Deseja alugar?".format(days_car *carros[cod_car][1]))
    
    print("0 - Sim | 1 - Nao")

    if int(input()) == 0:
      print("Parabens! Voce alugou o carro {}, por {} dias. ".format(carros[cod_car][0], days_car))

      alugados.append(carros.pop(cod_car))

  else:
    if len(alugados) == 0:
      print("Nao ha carro para devolver.")
    else:
      print("Segue Lista de carros alugagos.\n Qual deseja devolver?")
      mostrar_lista_de_carros(alugados)
      cod_car = int(input())

      carros.append(alugados.pop(cod_car))

  print("\n==================")
  print("Deseja Continuar?")
  print("0 - Continuar | 1 - Sair")

  if int(input()) == 1:
    break

