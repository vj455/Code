#!/usr/bin/env python
# coding: utf-8

# <H1> CARD CLASS

# In[90]:


import random
# Define Global Variables

# Create as tuples so its immutable(Cannot Change)
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') 
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Create Dictionary for getting integer values of card ranks 
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[91]:


class Card:
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self): # In case of print statements, returns what value does the object hold in the memory location
        
        return self.suit + " of " + self.rank


# Step 2: Now that the cards have been created, its time to create a deck of cards and have the functionality to deal the cards to the players. 
# 
# In this step we will create a Deck class, to create a new deck. This deck will contain methods to shuffle the deck for random card distribution and another method to deal cards to the players. 

# <H1> DECK CLASS

# In[92]:


#Create Deck Class

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                
                created_card = Card(suit, rank) #Instantiate an object of the Card class to create a Card object
                
                self.all_cards.append(created_card) #Append the card created to the list
                
    #Shuffle the new deck of cards    
    
    def shuffle_deck(self):
        
        return random.shuffle(self.all_cards)
    
    def deal_one(self):
        
        return self.all_cards.pop()
    
    


# In[93]:


new_deck = Deck()


# In[94]:


first_card = new_deck.all_cards[0]
print(first_card)


# As seen above the new deck is created. 
# 
# "new_deck" is an instance of the Deck class. 
# 
# first_card is an object of the all cards attribute
# 
# Below we will call the shuffle method and see the affect on the deck of card. 

# In[95]:


new_deck.shuffle_deck()


# In[96]:


first_card = new_deck.all_cards[0]
print(first_card)


# As seen above, after calling the shuffle method the first card in the deck has been shuffled and replaced by a Clubs of Five.
# 
# We will now assign a card to see if the length of the deck gets altered as we call the Deal One method. 

# In[97]:


card1 = new_deck.deal_one()


# In[98]:


print(card1)
print(len(new_deck.all_cards))


# As seen, when we call the deal one method to draw a card, the length of the deck of cards has been altered to 51 from the regular deck of cards of 52. 

# <H1> PLAYER CLASS

# In[99]:


class Player:
    
    def __init__(self, name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
            
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        
        return f' Player {self.name} has {len(self.all_cards)} card(s). '


# In[100]:


new_player = Player('Jose')


# In[101]:


new_player


# In[102]:


print(new_player)


# In[103]:


new_player.add_cards(card1)


# In[104]:


print(new_player)


# In[105]:


print(new_player.all_cards[0])


# In[106]:


new_player.add_cards([card1, card1, card1])


# In[107]:


print(new_player.all_cards[0], new_player.all_cards[1])


# In[108]:


print(new_player)


# In[109]:


new_player.remove_one()


# In[110]:


print(new_player)


# <H3> Test </H3>
# 
# 
# With the above different calls to different methods, we have been able to produce working methods what a player might be needing to do while playing the card game. 
# 
# From here onwards we will move towards working on the game logic

# <H2> Game Logic

# In[120]:


#Set up the game with initializing the two players and new decks

game_on = True

P1 = Player('P1')
P2 = Player('P2')

#Setup a new deck and shuffle the deck

new_deck = Deck()
new_deck.shuffle_deck()

#Split the deck into 2 parts between the 2 players

for _ in range(26):
    P1.add_cards(new_deck.deal_one())
    P2.add_cards(new_deck.deal_one())


# In[121]:


# WHILE GAME is ON

rounds = 0

game_on = True

while game_on:
    
    #Add cards to compare every time a new card is drawn
    rounds += 1
    
    print(f'Round {rounds}')
    Player_1_cards = []
    Player_1_cards.append(P1.remove_one())
    
    Player_2_cards = []
    Player_2_cards.append(P2.remove_one())
    #First time every time the round begins check if either player has less than 5 cards and end game if so
    
    if len(P1.all_cards) < 5:
        
        print("Player 1 Loses the game. PLAYER 2 WINS!!!")
        game_on = False
        break
    
    if len(P2.all_cards) < 5:
        
        print("Player 2 Loses the game. Player 1 WINS!!!")
        game_on = False
        break
        
    at_war = True
    
    while at_war:
        
        if Player_1_cards[-1].value < Player_2_cards[-1].value:
            P2.add_cards(Player_1_cards)
            P2.add_cards(Player_2_cards)
            at_war = False
            break
            
        elif Player_1_cards[-1].value > Player_2_cards[-1].value:
            P1.add_cards(Player_1_cards)
            P1.add_cards(Player_2_cards)
            at_war = False
            break
            
        else:
            
            print("WAR!!!")
            
            if len(P1.all_cards) < 5:
                print("Player 1 loses. Player 2 Wins")
                game_on = False
                break
            elif len(P2.all_cards) < 5:
                print("Player 2 loses. Player 1 wins")
                game_on = False
                break
            else: 
                for _ in range(5):
                    Player_1_cards.append(P1.remove_one())
                    Player_2_cards.append(P2.remove_one())
    


# In[ ]:




