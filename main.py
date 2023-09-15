# Importo librerias necesarias
import random

# Defino opciones
options = ('piedra', 'papel', 'tijera')
name = input('Nombre: ')
max_wins = int(input('elija un numero de victorias para elegir un ganador: '))

rounds = 1
score_user = 0
score_computer = 0

while True:

  print('*'*30)
  print('ROUND ', rounds)
  print('*'*30)
  print(f"score => {name}:{score_user}, computer:{score_computer}")
  
  # Creo las variables
  user_option = input('Piedra, papel o tijera => ').lower()
  
  if user_option not in options:
    print('opcion no valida')
    continue
  
  computer_option = random.choice(options)
  
  print('='*30)
  print(f'{name} => ', user_option)
  print('Computer => ', computer_option)
  
  if user_option == computer_option:
    print('='*30)
    print('Empate!')
    print('='*30)
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('='*30)
      print('piedra gana a tijera')
      print(f'{name} gana!')
      print('='*30)
      score_user += 1
    else:
      print('='*30)
      print('papel gana a piedra')
      print('computer gana!')
      print('='*30)
      score_computer += 1
  
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('='*30)
      print('papel gana a piedra')
      print(f'{name} gana!')
      print('='*30)
      score_user += 1
    else:
      print('='*30)
      print('tijera gana a papel')
      print('computer gana!')
      print('='*30)
      score_computer += 1
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('='*30)
      print('tijera gana a papel')
      print(f'{name} gana!')
      print('='*30)
      score_user += 1
    else:
      print('='*30)
      print('piedra gana a tijera')
      print('computer gana!')
      print('='*30)
      score_computer += 1

  if score_computer == max_wins:
    print('🏆'*10)
    print('computer wins!!!')
    print('🏆'*10)
    break

  if score_user == max_wins:
    print('🏆'*10)
    print(f'{name} wins!!!')
    print('🏆'*10)
    break
    
  rounds += 1