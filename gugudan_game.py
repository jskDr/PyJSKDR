#-*- coding: utf-8 -*-

def show_table():
    for x in range(2, 10):
        print "{0} Level".format( x)
        for y in range( 2, 10):
            z = x*y
            print "{0} x {1} = {2}".format( x, y, z)
        print

# 지금은 한자리수에 대해서 물어본다. 
def ask_q1( N):
    import random as rd
    
    correct_N = 0
    for iter in range( N):
        x, y = rd.randint(2, 9), rd.randint(2, 9)
        z = x * y
        val_str = raw_input( "{x} x {y} =? ".format(x=x, y=y))
        val = int( val_str)
        if val == z:
            print "You are right."
            correct_N += 1
        else:
            print "It is incorrect!"
    
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)                

show_table()
N_prob = int( raw_input("How many problems do you want to solve?"))
ask_q1( N_prob)