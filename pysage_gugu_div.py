#-*- coding: utf-8 -*-
from pysage_gugu_lib import *

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

def ask_q21( N):
    """
    ask_q21( N)
      - 두자리수와 한자리수를 곱했을 때 나오는 수를 나누는 계산이다.
    """
    print "두자리수 결과가 나오는 나눗셈을 다룬다."
    print
    
    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(2, 9)
        z = x * y
        # x를 찾는다.
        
        print cl("{}번째 문제입니다.").format( nn + 1)
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        #print "질문: {z:>3}".format(z=z) #두자리 수
        #print "     /{y:>3}".format(y=y) #한자리 수 
        #print
        
        #print "     {y:>3}".format(y=y) #한자리 수 
        #print " "
        print "질문은 다음과 같다."
        print                "      ab"
        print                "     ---"
        print dotstr2format( "  . |...").format(y, z)
        print "여기서 나눗셈의 몫인 XX는 얼마인가?"   
        print 

        xx_str = str(x)
        xx = [ int(xx_str[0]), int(xx_str[1])]

        print "1단계: 첫째자리 수를 맞춘다."
        print                "      a "
        print                "     ---"
        print dotstr2format( "  . |...").format(y, z)
        ans = xx[0] #ab --> a
        val_q1 = input("a = ? ")
        print

        b_y = val_q1 * y
        print dotstr2format( "      . ").format(val_q1)
        print                "     ---"
        print dotstr2format( "  . |...").format(y, z)
        if len(str( b_y)) == 1:
            print dotstr2format( "      .").format( val_q1 * y)
        else:
            print dotstr2format( "     ..").format( val_q1 * y)
        print
        if val_q1 != ans: 
            print "틀렸어요. 답은 {}입니다.".format( ans) 
        else:
            print "맞았어요."

        print "2단계: 둘쨰 자리 수를 맞춘다."
        print dotstr2format( "      .b").format(val_q1)
        print                "     ---"
        print dotstr2format( "  . |...").format(y, z)
        if len(str( b_y)) == 1:
            print dotstr2format( "      .").format( b_y)
        else:
            print dotstr2format( "     ..").format( b_y)
        rm = z - b_y*10
        print                "     ---"
        print dotstr2format( "     ...").format(rm)
        ans = xx[1] #ab --> a
        val_q2 = input("b = ?  ")
        #print "ans = {}, val_q2 = {}".format( ans, val_q2)
        print

        a_y = val_q2 * y
        print dotstr2format( "      ..").format(val_q1*10 + val_q2)
        print                "     ---"
        print dotstr2format( "  . |...").format(y, z)
        if len(str( b_y)) == 1:
            print dotstr2format( "      .").format( val_q1 * y)
        else:
            print dotstr2format( "     ..").format( val_q1 * y)
        print                "     ---"
        print dotstr2format( "     ...").format(rm)
        if len(str( a_y)) == 1:
            print dotstr2format( "       .").format( a_y)
        else:
            print dotstr2format( "      ..").format( a_y)
        print                "     ---"
        print dotstr2format( "     ...").format(rm - a_y)
        print

        if val_q2 != ans: 
            print "틀렸어요. 답은 {}입니다.".format( ans) 
        else:
            print "맞았어요."
            correct_N += 1
        print
    
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)
    
    return score