'''rock paper scissors with the computer in cmd'''

from os import system
from time import sleep
from random import choice

class Game(object):
    def __init__(self):
        print('Welcome in a rock, paper, scissors game!')
    
    def rules(self):
        system('cls')
        print('FREE, FAST TUTORIAL!\n\n')
        print('rock smash scissors\npaper smash rock\nscissors smash paper\nAll you have to do is choose one of them', end='')
        print('and the other side do the same thing.\n')
     
    def nickname(self, name):
        self.name = name
        self.name = input(('Give me your nickname: '))
        while self.name == '':
            print('You cannot leave it empty')
            self.name = input('Your nickname: ')
        system('cls')
        
        return self.name
         
         
tools = ['rock', 'paper', 'scissors']
player = Game()

'''player nickname'''
start = input(f'Hi {player.nickname("")}, I hope you know the rules\nIf you do not know~!\n Just type one..\n or click enter')
if start == '1' or start == 'one':
    player.rules()
''''''  
 
print("Let's begin!")
sleep(1)
system('cls')

print('ROCK/PAPER/SCISSORS')
selection = (input('Choose one of the following options: '))


'''resulr checking system'''
if selection == choice(tools):
    print(f'I took {tools[0]} soo: Draw..')
    
elif selection == 'paper':
    if choice(tools) == 'rock':
        print(f'I took {tools[0]} soo: You won!')
    else:
        print('I won! Scissors smashing paper!')

elif selection == 'scissors':
    if choice(tools) == 'paper':
        print(f'I took {tools[1]} soo: You won!')
    else:
        print('I won! Rock smashing scissors!')

elif selection == 'rock':
    if choice(tools) == 'scissors':
        print(f'I took {tools[2]} soo: You won!')
    else:
        print('I won! Paper smashing rock!')
''''''