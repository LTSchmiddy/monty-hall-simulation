import random, time

UseRandomSeed = True
RandomSeed = 1
TotalIterations = 100000000
# TotalIterations = 100

# Execution Start: **************************************

# Execution Variables:
switchCount = 0
stayCount = 0

# Method Start
if UseRandomSeed:
    random.seed(RandomSeed)

def DoMontyHall():
    global switchCount, stayCount
    correctDoor = 0
    chosenDoor = 0
    revealedDoor = 0
    
    # Set the Answer
    correctDoor = random.randint(1, 3)
    
    # Pick a Door
    chosenDoor = random.randint(1, 3)
    
    # The Reveal
    revealedDoor = random.randint(1, 3)
    while revealedDoor == correctDoor:
        # print "Retrying Revealed Door\n"
        revealedDoor = random.randint(1, 3)
    
    # print "correctDoor =", correctDoor
    # print "chosenDoor =", chosenDoor
    # print "revealedDoor =", revealedDoor
    
    finalOption1 = 0
    finalOption2 = 0
    
    if revealedDoor == 1:
        finalOption1 = 2
        finalOption2 = 3
    elif revealedDoor == 2:
        finalOption1 = 1
        finalOption2 = 3
    elif revealedDoor == 3:
        finalOption1 = 1
        finalOption2 = 2
    
        
    # print "\n"
    # print "finalOption1 =", finalOption1
    # print "finalOption2 =", finalOption2
    
    # Finally, should I switch or stay?:
    
    if correctDoor == chosenDoor:
        stayCount += 1
        # print "\nShoulda stayed..."
    else:
        switchCount += 1
        # print "\nShoulda switched..."

        
    
# DoMontyHall()


for i in range(0, TotalIterations):
    DoMontyHall()
    
    if i % (TotalIterations / 10) == 0:
        print i, "Out of", TotalIterations, "Iterations Completed..."
    # print "\n\n************************************\n\n"
    

print "Out of", TotalIterations, "Iterations, here are the results:"
print "Number of times I should have stayed:", stayCount
print "Number of times I should have switched:", switchCount
print "******"
print "Percent of times I should have stayed: " + str(stayCount * 100.0 / TotalIterations) + "%"
print "Percent of times I should have switched:" + str(switchCount * 100.0 / TotalIterations) + "%"
time.sleep(5)