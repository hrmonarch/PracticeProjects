import random
import sys

# Set correct number of lottery balls to choose from
# and run each lotto

def main():

    mega5 = [int(1 + 55*random.random()) for i in xrange(5)]
    mega1 = [int(1 + 45*random.random()) for i in xrange(1)]

    power5 = [int(1 + 58*random.random()) for i in xrange(5)]
    power1 = [int(1 + 34*random.random()) for i in xrange(1)]
    
    MegaMan(mega5, mega1)

    
    PowerMan(power1, power5)
    

# choose and print MegaMillions numbers
def MegaMan(mega5, mega1):
    
    print "Your MegaMillions numbers: " + str(mega5)
    
    print "\nMegaball: " + str(mega1)
    
    
# choose and print Powerball numbers
def PowerMan(power1, power5):
    
    print "Your Powerball numbers: " + str(power5)
    
    print "\nRed Powerball: " + str(power1)
    

if __name__ == '__main__':
    main()