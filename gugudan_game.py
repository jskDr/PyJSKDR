#-*- coding: utf-8 -*-
import random as rd

def show_table():
    for x in range(2, 10):
        print "{0} Level".format( x)
        for y in range( 2, 10):
            z = x*y
            print "{0} x {1} = {2}".format( x, y, z)
        print

# 지금은 한자리수에 대해서 물어본다. 
def ask_q1( N):
    """
      한자리수에 대해서 물어본다.
    """
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
    
def ask_q2( N):
    """
    ask_q2( N)
      - 두자리 이상 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
    """
    print "두자리수 이상에 대한 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for iter in range( N):
        x, y = rd.randint(10, 99), rd.randint(10, 99)
        z = x * y
        
        print "{}번째 문제입니다.".format( iter + 1)
        print "Q: {x} x {y} =?".format(x=x, y=y)
          
        # 자리수별로 y를 나타내어 yy 어레이에 저장한다.
        yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
          
        print "1단계: 더하는 수의 뒷자리수부터 계산을 시작한다."           
        print "Sub-Q1: {x} x {yy0} =? ".format(x=x, yy0=yy[0])
        # 이 질문들에 대한 답도 틀렸는지 맞는지 알려준다. 이후 구현 필요함.        
        print "1-1단계: 더해지는 수의 뒷자리부터 계산한다."
        val_q11 = input( "Sub-Q1-1: {xx0} x {yy0} = y_q11? ".format( xx0=xx[0], yy0=yy[0]))
        ans = xx[0] * yy[0] 
        if val_q11 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "1-2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        val_q12 = input( "Sub-Q1-2: ({xx1} x {yy0}) x 10 = y_q12? ".format( xx1=xx[1]/10, yy0=yy[0]))
        ans = xx[1] * yy[0] 
        if val_q12 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "1-합산단계: 두 결과를 합친다."
        # val_q1 = input("Sub-Q1-Sum: {q11} + {q12} = y_q1? ".format( q11=val_q11, q12=val_q12))
        print "Sub-Q1-Sum: {q1:>4}".format( q1=val_q11)
        print "           +{q2:>4}".format( q2=val_q12)
        print "           -------"            
        val_q1 = input("Answer:      ")        
        ans = val_q11 + val_q12 
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print
        
        print "2단계: 더하는 수의 이제 앞자리 수를 계산한다."   
        print "- 십단위 수를 곱하니 계산 후에 0을 더 포함해 자리수를 올려야 함을 숙지한다."        
        print "Sub-Q2: ({x} x {yy1}) x 10 =? ".format(x=x, yy1=yy[1]/10)
        # 이 질문들에 대한 답도 틀렸는지 맞는지 알려준다. 이후 구현 필요함.        
        print "2-1단계: 더해지는 수의 뒷자리부터 계산한다."
        val_q21 = input( "Sub-Q2-1: {xx0} x {yy1} = y_q21? ".format( xx0=xx[0], yy1=yy[1]/10))
        ans = xx[0] * yy[1]/10 
        if val_q21 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 

        print "2-2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        val_q22 = input( "Sub-Q2-2: ({xx1} x {yy1}) x 10 = y_q22? ".format( xx1=xx[1]/10, yy1=yy[1]/10))
        ans = xx[1] * yy[1]/10 
        if val_q22 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2-합산단계: 두 결과를 합치고 자리수를 하나 올려준다."
        # val_q2 = input("Sub-Q2-Sum: ({q21} + {q22})*10 = y_q2? ".format( q21=val_q21, q22=val_q22))
        print "Sub-Q2-Sum: {q1:>4}".format( q1=val_q21*10)
        print "           +{q2:>4}".format( q2=val_q22*10)
        print "           -------"            
        val_q2 = input("Answer:      ") 
        ans = (val_q21 + val_q22) * 10 
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print

        print "3단계: 앞자리 계산 결과와 뒷자리 계산 결과를 합친다."
        # val = input("Sub-Q-Sum: {q1} + {q2} =? ".format( q1=val_q1, q2=val_q2))
        print "Sub-Q-Sum: {q1:>4}".format( q1=val_q1)
        print "          +{q2:>4}".format( q2=val_q2)
        print "          -------"            
        val = input("Answer:    ")
        ans = (val_q1 + val_q2) 
        if val != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print
        
        print "최종 결과를 검증한다."
        if val == z:
            print "You are right."
            correct_N += 1
        else:
            print "It is incorrect!"
            print "답은 {}이고, 당신은 {}라고 답했습니다.".format( z, val)
        print
    
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)

def ask_q21( N):
    """
    ask_q21( N)
      - 두자리와 한자리 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
      - 덧셈을 가로가 아닌 세로로 칸을 맞추어 할 수 있도록 만들어본다.
      - 기본 아이디어만 제시하고 태크니션의 도움을 받아 더 멋지게 만든다.
    """
    print "두자리수와 한자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for iter in range( N):
        x, y = rd.randint(10, 99), rd.randint(2, 9)
        z = x * y
        
        print "{}번째 문제입니다.".format( iter + 1)
        print "Q: {x} x {y} =?".format(x=x, y=y)
          
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        
        print "1단계: 더해지는 수의 뒷자리부터 계산한다."
        val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
        ans = xx[0] * y 
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        ans = xx[1] * y
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print "Sub-Sum: {q1:>3}".format( q1=val_q1)
        print "        +{q2:>3}".format( q2=val_q2)
        print "        -------"            
        val = input("Answer:  ")
        ans = val_q1 + val_q2 
        if val != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print
        
        print "최종 결과를 검증한다."
        if val == z:
            print "You are right."
            correct_N += 1
        else:
            print "It is incorrect!"
            print "답은 {}이고, 당신은 {}라고 답했습니다.".format( z, val)
        print
    
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)

def gugu_basic():                    
    print "구구단 테이블을 보여줍니다."
    show_table()
    
    print "레벨-1:한자리 수 곱셈 게임입니다."
    N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
    ask_q1( N_prob)
    print
    
    print "레벨-2:두자리수와 한자리수의 곱셉 게임입니다."
    N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
    ask_q21( N_prob)
    print
    
    print "레벨-3: 두자리 수 곱셈 게임입니다."
    N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
    ask_q2( N_prob)
    
gugu_basic()
