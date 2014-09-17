#-*- coding: utf-8 -*-
import random as rd
import time
import math

class Timer(object):
    def __init__(self, name=None, n = 1):
        self.name = name
        self.n = n

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print '[%s]' % self.name,
        t_e = time.time() - self.tstart
        print 'Elapsed: %.1f(sec) for %d, 1EA: %.1f(sec) for 1' % (t_e, self.n, t_e/self.n)
    """
    Time Estimation (시간을 측정할 예정이다. 가입도 시킬 예정이다.)
    import time
    t = time.time()
    # do stuff
    elapsed = time.time() - t

    클라스를 사용하면 다음과 같이 간단해 진다.
    with Timer('foo_stuff'):
    # do some foo
    # do some stuff
    """

class sizedInt():    
    """
    val은 정수이고, size는 정수의 허용 크기이다.
    """
    def __init__(self, val, size):
        self.val = val # int value such as 0, 12, etc.
        self.size = size # size corresponding int value such as 1, 2, etc.
        if len( str(val)) > size:
            print "Error: size is smaller than len( str(val))"
    
def dotstr2format( s_in):
    """
      - 만약 1자리수만 허락된다면 다음과 같이 표현할 수 있다.
    print ''.join( [ '{}' if a == '.' else a for a in aa])
      - 두자리수 이상도 허락이 된다면 다른 형태를 사용한다.
      - 자라수뿐아니라 color로 표시한다. ',' -> color가 있는 숫자         
    """
    s_out = ''
    dot_count = 0
    for i_s, s in enumerate( s_in):
        if s == '.':
            dot_count += 1
            if i_s == len( s_in) - 1:
                s_out += '{:>' + str( dot_count) + '}'
        else:
            if dot_count > 0:
                s_out += '{:>' + str( dot_count) + '}'
                dot_count = 0
            s_out += s
    return s_out 

# 컬러를 사용한다.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLO = '\033[93m'
    WARNING = '\033[93m' #yello
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# 컬러를 변환한다.
def cl( bw_str, color_mode = bcolors.YELLO):
    """
    흑백 문자열을 컬러 문자열로 변경한다.
    """
    return color_mode + bw_str + bcolors.ENDC


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
    
def _ask_q2_r0( N):
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

def _ask_q21_r0( N):
    """
    ask_q21( N)
      - 두자리와 한자리 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
      - 덧셈을 가로가 아닌 세로로 칸을 맞추어 할 수 있도록 만들어본다.
      - 기본 아이디어만 제시하고 태크니션의 도움을 받아 더 멋지게 만든다.
      - 이전 코드이므로 앞에 _을 붙이고 뒤에는 리비젼 번호를 붙인다.
      추가할 모드
      - 곱셉도 세로로 하게 한다. (2014.9.9 --> 완료 시점)
      - 스스로 곱셈의 단계를 입력하도록 한다. (2014.9.9 --> 완료 시점)
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

def _ask_q21_r1( N):
    """
    ask_q21( N)
      - 두자리와 한자리 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
      - 덧셈을 가로가 아닌 세로로 칸을 맞추어 할 수 있도록 만들어본다.
      - 기본 아이디어만 제시하고 태크니션의 도움을 받아 더 멋지게 만든다.
      추가한 모드 & 추가할 모드 
      - 곱셉도 세로로 하게 한다. (2014.9.9 --> 2014.9.9)
      - 스스로 곱셈의 단계를 입력하도록 한다. (2014.9.9 --> 완료 시점)
      - 각 단계의 답 입력을 자리 수에 맞춘다. (2014.9.9 --> 완료 시점)
      - 덧셈을 뒷자리부터 하게 한다. (2014.9.9 --> 완료시점, advanced)
    """
    print "두자리수와 한자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(2, 9)
        z = x * y
        
        print "{}번째 문제입니다.".format( nn + 1)
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        print "질문: {x:>2}".format(x=x) #두자리 수
        print "    x{y:>2}".format(y=y) #한자리 수 
          
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        
        print "1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
        print "Sub-Q1: {xx0:>2}".format( xx0=xx[0])
        print "       x{y:>2}".format( y=y)
        print "       ------"
        val_q1 = input("Answer:  ")
        ans = xx[0] * y 
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print "Sub-Q2: {xx1:>2}".format( xx1=xx[1])
        print "       x{y:>2}".format( y=y)
        print "       ------"
        val_q2 = input("Answer:  ")
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

def _ask_q21_r2( N):
    """
    ask_q21( N)
      - 두자리와 한자리 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
      - 덧셈을 가로가 아닌 세로로 칸을 맞추어 할 수 있도록 만들어본다.
      - 기본 아이디어만 제시하고 태크니션의 도움을 받아 더 멋지게 만든다.
      추가한 모드 & 추가할 모드 
      - 곱셉도 세로로 하게 한다. (2014.9.9 --> 2014.9.9)
      - 스스로 곱셈의 단계를 입력하도록 한다. (2014.9.9 --> 완료 시점)
      - 각 단계의 답 입력을 자리 수에 맞춘다. (2014.9.9 --> 완료 시점)
      - 덧셈을 뒷자리부터 하게 한다. (2014.9.9 --> 완료시점, advanced)
    """
    print "두자리수와 한자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(2, 9)
        z = x * y
        
        print bcolors.OKBLUE + "{}".format( nn + 1) + bcolors.ENDC + "번째 문제입니다."
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        print "질문: {x:>2}".format(x=x) #두자리 수
        print "    x{y:>2}".format(y=y) #한자리 수 
          
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        
        print "1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
		#앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print   "Sub-Q1:   " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print   "         x" + " " + bcolors.YELLO + "{y}".format( y=y) + bcolors.ENDC
        print   "         ---"
        str = "{}x{}=?    ".format(xx[0], y)  
        val_q1 = input( bcolors.YELLO + str + bcolors.ENDC)

        ans = xx[0] * y 
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print     "Sub-Q2:    " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print     "          x" + " " + bcolors.YELLO + "{y}".format( y=y) + bcolors.ENDC
        print     "          ---"
        print     "          {:>3}".format(val_q1)  
        str = "{:>2}x{}=?    ".format(xx[1], y)  
        val = input( bcolors.YELLO + str + bcolors.ENDC)
        ans = xx[1] * y
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print      "Sub-Sum:    " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "           x" + " " + "{y}".format( y=y) 
        print      "           ---"
        print      "           " + bcolors.YELLO + "{:>3}".format(val_q1) + bcolors.ENDC 
        print      "          +" + bcolors.YELLO + "{:>3}".format(val_q2) + bcolors.ENDC  
        print      "           ---"
        str = "{:>2}+{:>3}=?   ".format(val_q1, val_q2)  
        val = input( bcolors.YELLO + str + bcolors.ENDC)
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
   
def _ask_q21_r3( N):
    """
    ask_q21( N)
      - 두자리와 한자리 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
      - 덧셈을 가로가 아닌 세로로 칸을 맞추어 할 수 있도록 만들어본다.
      - 기본 아이디어만 제시하고 태크니션의 도움을 받아 더 멋지게 만든다.
      추가한 모드 & 추가할 모드 
      - 곱셉도 세로로 하게 한다. (2014.9.9 --> 2014.9.9)
      - 스스로 곱셈의 단계를 입력하도록 한다. (2014.9.9 --> 완료 시점)
      - 각 단계의 답 입력을 자리 수에 맞춘다. (2014.9.9 --> 2014.9.9)
      - 덧셈을 뒷자리부터 하게 한다. (2014.9.9 --> 완료시점, advanced)
      - 부분 답을 입력하는 위치를 맞춘다. (2014.9.9 --> 완료시점)
    """
    print "두자리수와 한자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(2, 9)
        z = x * y
        
        print bcolors.OKBLUE + "{}".format( nn + 1) + bcolors.ENDC + "번째 문제입니다."
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        print "질문: {x:>2}".format(x=x) #두자리 수
        print "    x{y:>2}".format(y=y) #한자리 수 
          
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        
        print "1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
		#앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print      "Sub-Q1:   " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print      "         x" + " " + bcolors.YELLO + "{y}".format( y=y) + bcolors.ENDC
        print      "         ---"
        str =    "{}x{}=?    ".format(xx[0], y)  
        val_q1 = input( bcolors.YELLO + str + bcolors.ENDC)
        ans = xx[0] * y 
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print      "Sub-Q2:   " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print      "         x" + " " + bcolors.YELLO + "{y}".format( y=y) + bcolors.ENDC
        print      "         ---"
        print      "         {:>3}".format(val_q1)  
        str =  "{:>2}x{}=?   ".format(xx[1], y)  
        val_q2 = input( bcolors.YELLO + str + bcolors.ENDC)
        ans = xx[1] * y
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print      "Sub-Sum:  " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "         x" + " " + "{y}".format( y=y) 
        print      "         ---"
        print      "         " + bcolors.YELLO + "{:>3}".format(val_q1) + bcolors.ENDC 
        print      "        +" + bcolors.YELLO + "{:>3}".format(val_q2) + bcolors.ENDC  
        print      "         ---"
        str = "{:>2}+{:>3}=? ".format(val_q1, val_q2)  
        val = input( bcolors.YELLO + str + bcolors.ENDC)
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
    
def ask_q21( N):
    """
    ask_q21( N)
      - 두자리와 한자리 수의 곱셈에 대해서 배운다.
      - 덧셈을 뒤에서부터 하는 것도 추가하는 것을 고려해 본다.
      - 덧셈을 가로가 아닌 세로로 칸을 맞추어 할 수 있도록 만들어본다.
      - 기본 아이디어만 제시하고 태크니션의 도움을 받아 더 멋지게 만든다.
      추가한 모드 & 추가할 모드 
      - 곱셉도 세로로 하게 한다. (2014.9.9 --> 2014.9.9)
      - 스스로 곱셈의 단계를 입력하도록 한다. (2014.9.9 --> 완료 시점)
      - 각 단계의 답 입력을 자리 수에 맞춘다. (2014.9.9 --> 2014.9.9)
      - 덧셈을 뒷자리부터 하게 한다. (2014.9.9 --> 완료시점, advanced)
      - 부분 답을 입력하는 위치를 맞춘다. (2014.9.9 --> 완료시점)
    """
    print "두자리수와 한자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(2, 9)
        z = x * y
        
        print bcolors.OKBLUE + "{}".format( nn + 1) + bcolors.ENDC + "번째 문제입니다."
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        print "질문: {x:>2}".format(x=x) #두자리 수
        print "     x{y:>2}".format(y=y) #한자리 수 
        print
 
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        
        print "1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
		#앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print      "Sub-Q1:   " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print      "         x" + " " + bcolors.YELLO + "{y}".format( y=y) + bcolors.ENDC
        print      "         ---"
        ans = xx[0] * y 
        cmd =    "{}x{}=?    ".format(xx[0], y) + (" "*(3 - len(str( ans)))) 
        val_q1 = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print      "Sub-Q2:   " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print      "         x" + " " + bcolors.YELLO + "{y}".format( y=y) + bcolors.ENDC
        print      "         ---"
        print      "         {:>3}".format(val_q1)  
        ans = xx[1] * y
        cmd =  "{:>2}x{}=?   ".format(xx[1]/10, y) + (" "*(3 - len(str( ans)))) 
        val_q2 = input( bcolors.YELLO + cmd + bcolors.ENDC) * 10
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print      "Sub-Sum:  " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "         x" + " " + "{y}".format( y=y) 
        print      "         ---"
        print      "         " + bcolors.YELLO + "{:>3}".format(val_q1) + bcolors.ENDC 
        print      "        +" + bcolors.YELLO + "{:>2}".format(val_q2/10) + bcolors.ENDC  
        print      "         ---"
        ans = val_q1 + val_q2 
        cmd = "{:>2}+{:>3}=? ".format(val_q1, val_q2) + (" "*(3 - len(str( ans)))) 
        val = input( bcolors.YELLO + cmd + bcolors.ENDC)
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

def _ask_q2_r1( N):
    """
    ask_q22( N)
    - 두자리 수와 두자리 수를 곱한다.
    """
    print "두자리수와 두자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(10, 99)
        z = x * y
        
        print bcolors.OKBLUE + "{}".format( nn + 1) + bcolors.ENDC + "번째 문제입니다."
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        print "Q: {x:>2}".format(x=x) #두자리 수
        print "  x{y:>2}".format(y=y) #두자리 수 
        print
 
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        yy = [ y % 10, (y/10)*10]

        """
        [2014-9-13] 편집 사항
        - 전체적으로 한칸씩 미룬다. 최종합산 부분에서 1칸이 모자라기 때문이다.
        """
        #---------------------------------------------
        print "1단계: 곱하는 수의 첫 자리에 대한 계산을 한다."        
        print "1-1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
        #앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print      "Sub1-1:    " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print      "          x" + "{y1}".format( y1=yy[1]/10) + bcolors.YELLO + "{y0}".format( y0=yy[0]) + bcolors.ENDC
        print      "          ---"
        ans = xx[0] * yy[0] 
        cmd =    "{}x{}=?     ".format(xx[0], yy[0]) + (" "*(3 - len(str( ans)))) 
        val_q1 = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "1-2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print      "Sub1-2:    " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print      "          x" + "{y1}".format( y1=yy[1]/10) + bcolors.YELLO + "{y0}".format( y0=yy[0]) + bcolors.ENDC
        print      "          ---"
        print      "           {:>2}".format(val_q1)  
        ans = xx[1] * yy[0]
        cmd =  "{}x{}=?     ".format(xx[1]/10, yy[0]) + (" "*(2 - len(str( ans)))) 
        val_q2 = input( bcolors.YELLO + cmd + bcolors.ENDC) * 10
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "1단계 합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print      "Sub-Sum:   " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "          x" + "{y}".format( y=y) 
        print      "          ---"
        print      "           " + bcolors.YELLO + "{:>2}".format(val_q1) + bcolors.ENDC 
        print      "         +" + bcolors.YELLO + "{:>2}".format(val_q2/10) + bcolors.ENDC  
        print      "          ---"
        ans = val_q1 + val_q2 
        cmd = "{:>2}+{:>3}=?  ".format(val_q1, val_q2) + (" "*(3 - len(str( ans)))) 
        val_01 = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val_01 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print
        
        #------------------------------------------
        print "2단계: 곱하는 수의 둘째 자리에 대한 계산을 한다."        
        print "2-1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))      
        #앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print      "Sub2-1:    " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print      "          x" + bcolors.YELLO + "{y1}".format( y1=yy[1]/10) + bcolors.ENDC + "{y0}".format(y0=yy[0])
        print      "          ---"
        ans = xx[0] * yy[1] 
        cmd =    "{}x{}=?     ".format(xx[0], yy[1]/10) + (" "*(2 - len(str( ans/10)))) 
        val_q1 = input( bcolors.YELLO + cmd + bcolors.ENDC) *10
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2-2단계: 더해지는 수의 앞자리에 대해 계산한다. 계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print      "Sub2-2:    " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print      "          x" + bcolors.YELLO + "{y1}".format( y1=yy[1]/10) + bcolors.ENDC + "{y0}".format(y0=yy[0])
        print      "          ---"
        print      "          {:>2}".format(val_q1/10)  
        ans = xx[1] * yy[1] 
        cmd =  "{}x{}=?    ".format(xx[1]/10, yy[1]/10) + (" "*(2 - len(str( ans/100)))) 
        val_q2 = input( bcolors.YELLO + cmd + bcolors.ENDC) * 10 * 10
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계 합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print      "Sub-Sum:   " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "          x" + "{y}".format( y=y) 
        print      "          ---"
        print      "         " + bcolors.YELLO + "{:>3}".format(val_q1/10) + bcolors.ENDC 
        print      "       +" + bcolors.YELLO + "{:>3}".format(val_q2/10/10) + bcolors.ENDC  
        print      "          ---"
        ans = val_q1 + val_q2 
        cmd = "{:>3}+{:>4}=".format(val_q1, val_q2) + (" "*(4 - len(str( ans)))) 
        val_02 = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val_02 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print

        print "최종합산단계: 두 결과를 합친다."
        print      "Tot-Sum:   " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "          x" + "{y}".format( y=y) 
        print      "          ---"
        print      "          " + bcolors.YELLO + "{:>3}".format(val_01) + bcolors.ENDC 
        print      "        +" + bcolors.YELLO + "{:>3}".format(val_02/10) + bcolors.ENDC  
        print      "          ---"
        ans = val_01 + val_02 
        cmd = "{:>3}+{:>4}=".format(val_01, val_02) + (" "*(4 - len(str( ans)))) 
        val = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print        
        
        #------------------------------------------
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
	
def ask_q2( N):
    """
    ask_q22( N)
    - 두자리 수와 두자리 수를 곱한다.
    """
    print "두자리수와 두자리수의 곱셈 계산을 배우면서 테스트한다."
    print "- 각 자리를 단계적으로 나눠서 계산하는 방법을 익히게 한다."
    print "  (2자리 숫자의 계산을 아래에서 위로 단계적으로 계산한다.)"

    correct_N = 0
    for nn in range( N):
        x, y = rd.randint(10, 99), rd.randint(10, 99)
        z = x * y
        
        print bcolors.OKBLUE + "{}".format( nn + 1) + bcolors.ENDC + "번째 문제입니다."
        # print "Q: {x} x {y} =?".format(x=x, y=y)
        print "Q: {x:>2}".format(x=x) #두자리 수
        print "  x{y:>2}".format(y=y) #두자리 수 
        print
 
        # 자리수별로 x를 나타내어 xx 어레이에 저장한다.
        # yy = [ y % 10, (y/10)*10] 
        xx = [ x % 10, (x/10)*10]
        yy = [ y % 10, (y/10)*10]

        """
        [2014-9-13] 편집 사항
        - 전체적으로 한칸씩 미룬다. 최종합산 부분에서 1칸이 모자라기 때문이다.
        """
        #---------------------------------------------
        print "1단계: 곱하는 수의 첫 자리에 대한 계산을 한다."        
        print "1-1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))
        #앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print      "Sub1-1:    " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print      "          x" + "{y1}".format( y1=yy[1]/10) + bcolors.YELLO + "{y0}".format( y0=yy[0]) + bcolors.ENDC
        print      "          ---"
        ans = xx[0] * yy[0] 
        cmd =    "{}x{}=?      ".format(xx[0], yy[0]) + (" "*(2 - len(str( ans)))) 
        val_q1 = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "1-2단계: 더해지는 수의 앞자리에 대해 계산한다."
        print "계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print      "Sub1-2:    " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print      "          x" + "{y1}".format( y1=yy[1]/10) + bcolors.YELLO + "{y0}".format( y0=yy[0]) + bcolors.ENDC
        print      "          ---"
        print      "           {:>2}".format(val_q1)  
        ans = xx[1] * yy[0]
        cmd =  "{}x{}=?     ".format(xx[1]/10, yy[0]) + (" "*(2 - len(str( ans/10)))) 
        val_q2 = input( bcolors.YELLO + cmd + bcolors.ENDC) * 10
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "1단계 합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        print      "Sub-Sum:   " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "          x" + "{y}".format( y=y) 
        print      "          ---"
        print      "           " + bcolors.YELLO + "{:>2}".format(val_q1) + bcolors.ENDC 
        print      "         +" + bcolors.YELLO + "{:>2}".format(val_q2/10) + bcolors.ENDC  
        print      "          ---"
        ans = val_q1 + val_q2 
        cmd = "{:>2}+{:>3}=?  ".format(val_q1, val_q2) + (" "*(3 - len(str( ans)))) 
        val_01 = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val_01 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print
        
        #------------------------------------------
        print "2단계: 곱하는 수의 둘째 자리에 대한 계산을 한다."        
        print "2-1단계: 더해지는 수의 뒷자리부터 계산한다."
        #val_q1 = input( "Sub-Q1: {xx0} x {y} = y_q1? ".format( xx0=xx[0], y=y))      
        #앞에서 뒤에 풀어야 할 수식을 적어준다. 가로 방식과 세로 방식의 융합이다. 2*9 = 을 앞에 적어준다.
        print      "Sub2-1:    " + "{xx1}".format( xx1=xx[1]/10) + bcolors.YELLO + "{xx0}".format( xx0=xx[0]) + bcolors.ENDC
        print      "          x" + bcolors.YELLO + "{y1}".format( y1=yy[1]/10) + bcolors.ENDC + "{y0}".format(y0=yy[0])
        print      "          ---"
        ans = xx[0] * yy[1] 
        cmd =    "{}x{}=?     ".format(xx[0], yy[1]/10) + (" "*(2 - len(str( ans/10)))) 
        val_q1 = input( bcolors.YELLO + cmd + bcolors.ENDC) *10
        if val_q1 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2-2단계: 더해지는 수의 앞자리에 대해 계산한다."
        print "계산후 자리수를 맞추기 위해 0을 덧붙인다."
        #val_q2 = input( "Sub-Q2: ({xx1} x {y}) x 10 = y_q2? ".format( xx1=xx[1]/10, y=y))
        print      "Sub2-2:    " + bcolors.YELLO + "{xx1}".format( xx1=xx[1]/10) + bcolors.ENDC +"{xx0}".format( xx0=xx[0])
        print      "          x" + bcolors.YELLO + "{y1}".format( y1=yy[1]/10) + bcolors.ENDC + "{y0}".format(y0=yy[0])
        print      "          ---"
        print      "          {:>2}".format(val_q1/10)  
        ans = xx[1] * yy[1] 
        cmd =  "{}x{}=?    ".format(xx[1]/10, yy[1]/10) + (" "*(2 - len(str( ans/100)))) 
        val_q2 = input( bcolors.YELLO + cmd + bcolors.ENDC) * 10 * 10
        if val_q2 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        
        print "2단계 합산단계: 두 결과를 합친다."
        # 합산이 용이하도록 자리 수를 맞춘다.
        # 숫자들의 위치가 갖도록 오른쪽 정렬한다. 
        # :>3이면 3자리로 오른쪽 정렬하라는 의미이다. 
        # 2단계에서는 10의 자리는 단순함을 위해 무시하고 계산하고 다음 단계에서 제대로 반영한다.
        print      "Sub-Sum:   " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "          x" + "{y}".format( y=y) 
        print      "          ---"
        print      "         " + bcolors.YELLO + "{:>3}".format(val_q1/10) + bcolors.ENDC 
        print      "       +" + bcolors.YELLO + "{:>3}".format(val_q2/10/10) + bcolors.ENDC  
        print      "          ---"
        ans = val_q1 + val_q2 
        cmd = "{:>2}+{:>3}=? ".format(val_q1/10, val_q2/10) + (" "*(3 - len(str( ans/10)))) 
        val_02 = input( bcolors.YELLO + cmd + bcolors.ENDC) * 10
        if val_02 != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print

        print "최종합산단계: 두 결과를 합친다."
        print      "Tot-Sum:   " + "{xx1}".format( xx1=xx[1]/10) + "{xx0}".format( xx0=xx[0])
        print      "          x" + "{y}".format( y=y) 
        print      "          ---"
        print      "          " + bcolors.YELLO + "{:>3}".format(val_01) + bcolors.ENDC 
        print      "        +" + bcolors.YELLO + "{:>3}".format(val_02/10) + bcolors.ENDC  
        print      "          ---"
        ans = val_01 + val_02 
        cmd = "{:>3}+{:>4}=".format(val_01, val_02) + (" "*(4 - len(str( ans)))) 
        val = input( bcolors.YELLO + cmd + bcolors.ENDC)
        if val != ans: print "틀렸어요. 답은 {}입니다.".format( ans) 
        print        
        
        #------------------------------------------
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
    
def ask_root_2bc( N):
    print '2차 방정식의 근의 공식을 구하는 문제입니다.'
    correct_N = 0
    for ii in range( N):
        print '{}번째 문제입니다.'.format( ii+1)
        
        # b는 계산의 편이를 위해 짝수만 사용한다.
        c = rd.randint(-10, 10)
        if c < 0:
            b = rd.randint(-10, 10) * 2
        else:                
            # b-4c >= 0 is necessary condition to be real roots.
            b_min = 2 * math.sqrt( c)
            b_m = int( math.ceil( b_min / 2.0))
            b = rd.randint( b_m, b_m + 10) * 2
            
        print '문제:  x^2 + {b}x + {c} = 0, find x?'.format( b=b, c=c)
        print 
        print '단계1: 좌변을 2차 거듭제곱 형태로 만든다.'
        print('      x^2 + ' +  cl('{b}') + 'x + {c} = 0, find x?').format( b=b, c=c)
        print '      (x+B)^2 + ({b}-2B)x + {c}-B^2 = 0'.format( b=b, c=c)
        print '      여기서, (x+B)^2 = x^2 + 2Bx + B^2' 
        B = input('B = {b}/2 = ? '.format( b=b))
        ans = b/2
        if B != ans: print "틀렸어요. 답은 {}입니다.".format( ans)
        else: print '맞았어요'
        print

        print '단계2: 좌변을 2차 거듭제곱 형태로 만든다.' 
        print('      x^2 + ' +  cl('{b}') + 'x + {c} = 0, find x?').format( b=b, c=c)
        print('      (x+' + cl('{B}') + ')^2 + ({b}-' + cl('{B_2}') + ')x + {c}-' + cl('{B2}') + ' = 0').format( b=b, c=c, B=B, B_2 = 2*B, B2=B**2)
        print '      (x+{B})^2 = C'.format( B=B)
        C = input('C = ({B})^2 - {c} = ? '.format( B=B, c=c))
        ans = B**2 - c
        if C != ans: print '틀렸어요. 답은 {}입니다.'.format( ans)
        else: print '맞았어요'
        print

        print '단계3: 양의 근과 음의 근을 구하는 단계입니다.'
        print('      x^2 + ' +  cl('{b}x') + ' + {c} = 0, find x?').format( b=b, c=c)
        print('      (x+' + cl('B') + ')^2 + ({b}-2' + cl('B') + 'x + {c}-' + cl('B^2') + ' = 0').format( b=b, c=c)
        print('      (x+{B})^2 = ' + cl('C')).format( B=B)
        print '      (x_p, x_n) = (+sqrt({C}) - {B}, -sqrt({C}) - {B})'.format(C=C,B=B)
        print '정답은 지수형(+x.xe+XX)으로 표현 했거나'
        print '      또는 내부 변환하여 소수점 첫째짜리까지 검증합니다.'
        sc = math.sqrt( C)
        x_p = input( 'x_p = +{sc:.2e} - {B} = ? '.format(sc=sc, B=B))       
        x_n = input( 'x_n = -{sc:.2e} - {B} = ? '.format(sc=sc, B=B))        
        x_str = "{:.1e}, {:.1e}".format( x_p, x_n)
        ans_p, ans_n = sc - B, -sc - B
        ans_str = "{:.1e}, {:.1e}".format( ans_p, ans_n)         
        # if the answer is not int, this is not solvable for perfect precision
        if x_str != ans_str: 
            print '틀렸어요. 답은 {ans_str}입니다.'.format( ans_str = ans_str)
        else:
            print '(두자리수 정밀도 기준으로) 맞았어요^^; '
            correct_N += 1        
        print
        
        a_p = x_p**2 + b*x_p + c
        print '검증(x_p): {x:.1e}^2 + {b}*{x:.1e} + {c} = {a_p:.1e}'.format(x=x_p, b=b, c=c, a_p=a_p)
        a_n = x_n**2 + b*x_n + c
        print '검증(x_n): {x:.1e}^2 + {b}*{x:.1e} + {c} = {a_n:.1e}'.format(x=x_n, b=b, c=c, a_n=a_n)
        print
        
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)
	
def gugu_basic():  
    
    level = 0
    while level != 9:
        print "메뉴: 어떤 에듀게임을 할까요"
        print "0. 레벨-업 모드"
        print "1. 구구단 테이블을 보여줍니다." 
        print "2. 한자리 수 곱셈 게임입니다."
        print "3. 두자리수와 한자리수의 곱셉 게임입니다."
        print "4. 두자리 수 곱셈 게임입니다."
        print "5. 2차 방정식 근의 공식 게임입니다(a=1)."
        print "9. 게임 완료"
        level = input( "번호를 입력해 주세요 (0-5, 9=quit) --> ")
        print
        
        if level == 0:
            print "순서대로 하면서 레벨을 높혀봅시다."            
            print "레벨-1: 구구단 테이블을 보여줍니다."
            show_table()
            
            print "레벨-2:한자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            ask_q1( N_prob)
            print
            
            print "레벨-3:두자리수와 한자리수의 곱셉 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            ask_q21( N_prob)
            print
            
            print "레벨-4: 두자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            ask_q2( N_prob)
            
        elif level == 1:
            print "레벨-1: 구구단 테이블을 보여줍니다."
            show_table()
            print
            
        elif level == 2:
            print "레벨-2:한자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            with Timer( '1x1곱셈 {}개'.format( N_prob), N_prob):
                ask_q1( N_prob)
            print 
        
        elif level == 3:
            print "레벨-3:두자리수와 한자리수의 곱셉 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            with Timer( '2x1곱셈 {}개'.format( N_prob), N_prob):
                ask_q21( N_prob)
            print
            
        elif level == 4:
            print "레벨-4: 두자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            with Timer( '2x2곱셈 {}개'.format( N_prob), N_prob):
                ask_q2( N_prob)

        elif level == 5:
            print "레벨-5: 2차 방정식 근의 공식 게임입니다 (a=1 경우)."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            with Timer( '2차 방정식(a=1) {}개'.format( N_prob), N_prob):
                ask_root_2bc( N_prob)

        elif level == 9:
            print "게임이 끝났습니다."
        
        print         

print bcolors.WARNING + "교육과 게임이 진짜로 합쳐지는 리얼에듀게임이 시작됩니다." + bcolors.ENDC
gugu_basic()
