stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
import random
choosen_list=['camels','shopeesss','bullets']
choose = random.choice(choosen_list)
lives = 6
display =[]
for _ in choose:
    display +='_'
computer = len(choose)
print(logo)
end_game = False
while not end_game:
    user = input('enter a letter:\n')
    for position in range(computer):
        letter =choose[position]
        if letter == user:
            display[position] = letter
    print(display)
    if user not in choose:
            lives -=1
            if lives ==0:
                end_game = True
                print('you lose')
    if '_' not in display:
      end_game =True
      print('you Won!')
    print(stages[lives])