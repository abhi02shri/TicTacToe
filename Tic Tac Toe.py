#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random

l3=["","",""]
l2=["","",""]
l1=["","",""]


won =False
winner=""

def place_empty(num):
    if num == 1:
        if(l1[0] == "X" or l1[0] == "O"):
            return False
        else: return True
    elif num == 2:
        if(l1[1] == "X" or l1[1] == "O"):
            return False
        else: return True
    elif num == 3:
        if(l1[2] == "X" or l1[2] == "O"):
            return False
        else: return True
        
        
    elif num == 4:
        if(l2[0] == "X" or l2[0] == "O"):
            return False
        else: return True
    elif num == 5:
        if(l2[1] == "X" or l2[1] == "O"):
            return False
        else: return True
    elif num == 6:
        if(l2[2] == "X" or l2[2] == "O"):
            return False
        else: return True
        
        
    elif num == 7:
        if(l3[0] == "X" or l3[0] == "O"):
            return False
        else: return True
    elif num == 8:
        if(l3[1] == "X" or l3[1] == "O"):
            return False
        else: return True
    elif num == 9:
        if(l3[2] == "X" or l3[2] == "O"):
            return False
        else: return True
    pass


def place_marker(num,char):
    if num == 1:
        l1[0] = char        
    elif num == 2:
        l1[1] = char
    elif num == 3:
        l1[2] = char    
        
        
    elif num == 4:
        l2[0] = char
    elif num == 5:
        l2[1] = char
    elif num == 6:
        l2[2] = char
        
        
    elif num == 7:
        l3[0] = char
    elif num == 8:
        l3[1] = char
    elif num == 9:
        l3[2] = char
        
        
    print("current status:")
    print("".join(l3))
    print("".join(l2))
    print("".join(l1))
  #  clear_output()

        
def game_won():
    for i in range(0,3):
        if l1[i]==l2[i] and l2[i] ==l3[i]:
            winner=l1[i]
            won= True
            break
        else:
            won= False
            break
            
    if l1[0]==l1[1] and l1[1]==l1[2]:
        winner=l1[0]
        won= True
    elif l2[0]==l2[1] and l2[1]==l2[2]:
        winner=l2[2]
        won= True
    elif l3[0]==l3[1] and l3[1]==l3[2]:
        winner=l3[0]
        won= True
    elif l1[0]==l2[1] and l2[1]==l3[2]:
        winner=l1[0]
        won= True
    elif l3[0]==l2[1] and l2[1]==l1[2]:
        winner=l1[2]
        won= True
    else: 
        won= False
    
    pass

def board_full():
    for i in range(1,10):
        if(place_empty(i)):
            return False
            break
        else:
            return True
        
    
Player1= input("Enter the name of Player 1:")
Player2= input("Enter the name of Player 2:")

char1=input("select symbol for Player 1, X or O:")
#while (char1 !='X' or char1!= 'O'):
 #   char1=input("select symbol for Player 1, X or O:")

char2=input("select symbol for Player 2, X or O:")
#while (char2 !='X' or char2!= 'O'):
 #   char2=input("select symbol for Player 2, X or O:")

d = random.randint(1,100)
if d %2==0:
    print("player 1 will play first")
    present_char = char1
else: 
    print("player 2 will start the game")
    present_char = char2
    
    
    
while(not won) :
    
    present_marker= int(input("Enter the number[1-9] where you want to place your {}: ".format(present_char)))

    while(not place_empty(present_marker)):
        present_marker= int(input("Please Enter the number[1-9] which is empty and where you want to place your marker: "))

    if(board_full()):
        print("Match Tie")
        break
        
    place_marker(present_marker,present_char)
    
        
    
    won = game_won()
    
    if present_char==char1:
        present_char=char2
    else:
        present_char=char1

if winner == char1:
    print("Congratulations, {} won the game".format(Player1))
else:
    print("Congratulations, {} won the game".format(Player2))

