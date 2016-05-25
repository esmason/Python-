import numpy as np

''' for testing  a solution to the following problem 

  you are given 10 resistors, 9 of them are 1 ohms and 1 of them is 2 ohms. Find an arrangement of resistors in a circuit that
  
  allows you to determine which resistor is 2 ohms using 1 voltmeter measurement (also determine the position of this reading) '''

n = 10
resistor_combinations = np.ones((n, n)) + np.eye(n)

#resistor_combinations = np.array([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0]])
results = []

for combo in resistor_combinations:
    total_resistance = 0
    combo = list(combo)
    #handle case where odd num resistors
    if len(combo)%2 == 1:
        first, second = [combo.pop() for x in range(2)]
        rest_so_far = 1/ ( 1/first + 1/second)
        combo.append(rest_so_far)
        
    while len(combo) > 2:
        first, second, third = [combo.pop() for x in range(3)]
        rest_so_far = 1/ (1/(first+second)  + 1/third)
        combo.append(rest_so_far)
    result = combo[0] + combo[1]
    results.append(result)

print(results)

for i in reversed(range(len(results))):
    res = results.pop()
    if res in results:
        print("match found! ", end = '')
        print("2 ohm resistor in positions " + str(i+1) + " and " + str(results.index(res) + 1) + " are equivalent circuits!!!") 
