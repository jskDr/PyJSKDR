#-*- coding: utf-8 -*-
import random as rd

def ask_q1( N):
    """
      한자리수에 대해서 물어본다.
    """
    correct_N = 0
    for iter in range( N):
        x, y = rd.randint(2, 9), rd.randint(2, 9)
        z = x * y
        val_str = raw_input( "{z} / {x} =? ".format(z=z, x=x))
        val = int( val_str)
        if val == y:
            print "맞았어요."
            correct_N += 1
        else:
            print "틀렸어요. 답은 {}이예요.".format(y)
    
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)

    return score
