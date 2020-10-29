import random

names = []

print('Please enter the names that you want to be in the drawing. When you are ready to select one, type \'run\': ')
entered_names = " "
while entered_names != 'run':
  entered_names = input()
  if entered_names != 'run':
    names.append(entered_names)
    print(f'Names entered in drawing: {names}')
  else:
    winner = random.choice(names)
    print(f'The winner is {winner}!!!! Congratulations!')

