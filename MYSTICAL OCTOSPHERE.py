# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE!

# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

# Here is a sample of the kind of
# output this program should produce:
#
# Your question was... Will I get rich?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably yes.
# 
# Your question was... Are the Cubs going to win the World Series?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably not.

import random

def number_to_fortune(number):
   
    
    if number == 0:
        return "Yes, for sure!"
    elif number == 1:
        return "Probably yes."
    elif number == 2:
        return "Seems like yes..."
    elif number == 3:
        return "Definitely not!"
    elif number == 4:
        return "Probably not."
    elif number == 5:
        return "I really doubt it..."
    elif number == 6:
        return "Not sure, check back later!"
    elif number == 7:
        return "I really can't tell."
    else:
        return "Something was wrong with my input."
    
def mystical_octosphere(question):
   
    print "Your question was... " + question
    
    print "You shake the mystical octosphere."
    
    answer_number = random.randrange(0, 8)
 
    answer_fortune = number_to_fortune(answer_number)

    print "The cloudy liquid swirls, and a reply comes into view..."
  
    print "The mystical octosphere says... " + answer_fortune    

    print
 
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")