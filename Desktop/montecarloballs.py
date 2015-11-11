import random
def noReplacementSimulation(numTrials):
    yes=0
    for i in range(numTrials):
        
        results=[]
        
        bucket = [0,0,0,1,1,1]
        e=0
        while e <3:
            random.shuffle(bucket)
            results.append(bucket.pop())
            e+=1
            #print results
        if 1 not in results:
            yes+=1
        if 0 not in results:
            yes+=1
    return float(yes)/numTrials
    
print noReplacementSimulation(10000)