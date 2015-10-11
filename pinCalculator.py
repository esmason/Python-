def pinCalculator():
    numGuesses = int(raw_input("Enter the number of guesses"))
    pinLength = int(raw_input("Enter the number of binary digits in your PIN"))
    combos = 2**pinLength
    for i in range(numGuesses):
        guess = 0       #guess is a counter, the particular "guess" you are on
        ans=0.0         # ans is the sum of the probabilities of all the "guess"s so far
        while guess<numGuesses:
            if guess == 0:
                ans = ans + 1.0/combos
                guess = guess + 1
            else: 
                counter = guess
                a = 1.0/(combos - guess)          #a is the probability of a particular guess being right          
                while counter > 0:
                    a= a * (combos - counter)/combos
                    counter -= counter
                ans = ans + a
                guess = guess +1    
                    
            
        
    print ans
        
        
pinCalculator()