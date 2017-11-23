import simplegui
import random
import math


num_range = 100
secret_num = 0
guesses_left = 0



def new_game():  
    global num_range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, num_range)
    
    if num_range == 100 : 	
        guesses_left = 7
    elif num_range == 1000 :
        guesses_left = 10
      

    print "New game. The range is from 0 to", num_range, ". Good luck!"
    print "Number of remaining guesses is ", guesses_left, "\n"
    pass



def range100():
    global num_range
    num_range = 100 
    new_game() 
    pass

def range1000():
    global num_range
    num_range = 1000 
    new_game()
    pass

    
def input_guess(guess):    
   	
    global guesses_left
    global secret_num 
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print "That is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You didn't guess the number in time!"   
        new_game()
        return
    else:
        print result
        pass
            
    

f = simplegui.create_frame("Game: Guess the number!", 250, 250)
f.set_canvas_background('Green')


f.add_button("Range is [0, 100)", range100, 100)
f.add_button("Range is [0, 1000)", range1000, 100)	
f.add_input("Enter your guess", input_guess, 100)

new_game()
f.start()