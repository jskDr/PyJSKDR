# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 06:33:29 2014

@author: james
"""
from pysage_gugu_lib import *

import sympy
import random as rd
import math

def sympy_ask_root_2bc( N):
    print "=================================================================="
    print cl("2차 방정식의 근을 구하는 문제입니다.")
    print "sympy를 이용하여 동작합니다."
    
    sympy.init_printing()    
    
    x, B, C = sympy.symbols('x B C')
    b, c = sympy.symbols('b c', integer=True)
    f = sympy.symbols('f', cls=sympy.Function)
    f = x**2 + b*x + c

    print "풀고자하는 2차 방정식은 아래와 같습니다."
    sympy.pprint( sympy.Eq(f, 0))
    print "이론적으로 구한 근들은 다음과 같습니다."
    sol = sympy.solve( sympy.Eq( f, 0), x)
    sympy.pprint( sol)

    correct_N = 0
    for ii in range( N):
        print "--------------------------------------------------------------"
        print cl('{}번째 문제입니다.'.format( ii+1))
    
        alpha, beta = rd.randint(-9, 9), rd.randint(-9, 9)
        bb = -1 * (alpha + beta)
        cc = alpha * beta

        # print '문제:  x^2 + {b}x + {c} = 0, find x?'.format( b=bb, c=cc)
        print "풀고자하는 2차 방정식은 다음과 같다."
        f_bc = f.subs({b:bb, c:cc})
        sympy.pprint( sympy.Eq(f_bc, 0))
        print "즉, b = {b}, c = {c}".format(b=bb,c=cc)
        print "이론으로 구한 근들은 다음과 같다."
        sol = sympy.solve( sympy.Eq(f_bc, 0),x)
        sympy.pprint( sol)
            
        print 
        print cl("[단계1]")
        print "- 좌변을 2차 거듭제곱 형태로 만든다."
        print "- 2차 방정식의 근을 구하는 방법 중의 한가지는" 
        print "  좌변을 완전제곱 형태로 바꾸는 것입니다. 즉,"
        sympy.pprint( sympy.Eq((x+B)**2, C))
        print "이렇게 변환할 때, B는 어떤 값을 가지는지 알아봅시다."
        print
        
        #print('      x^2 + ' +  cl('{b}') + 'x + {c} = 0, find x?').format( b=bb, c=cc)
        print cl("문제:")
        sympy.pprint( sympy.Eq(f_bc, 0))

        print cl("완전제곱형태:")
        f_bc_B = (x+B)**2 + (b-2*B)*x + c-B**2
        sympy.pprint( sympy.Eq( f_bc_B.subs({b:bb,c:cc})))
        f_bc_B_x1 = 2 * x * (B - b/2)
        print "여기서, 완전제곱을 위해 x항은 없어져야 한다. 즉,"
        sympy.pprint( sympy.Eq( f_bc_B_x1.subs(b,bb), 0)) 
        
        print cl("위가 성립되려면,B를 얼마로 해야할까?")
        BB = input('B = b/2 = ? ')
        ans = bb/2.0
        if BB != ans: 
            print "틀렸어요. 답은 {}입니다.".format( ans)
            break
        else:
            print '맞았어요'
        print
        
        #--------------------------------------------------------------
        print cl("[단계2]")
        print "좌변의 완전제곱 형태 변화에 따른 우변의 대응되는 값을 구한다."

        print cl("문제:")
        sympy.pprint( sympy.Eq(f_bc, 0))

        print "완전제곱형태:"
        sympy.pprint( sympy.Eq( f_bc_B.subs({b:bb,c:cc}), 0))

        print cl("우변정리:")
        print "B={B}를 대입하면,".format(B=BB)
        sympy.pprint( sympy.Eq( f_bc_B.subs({b:bb,c:cc,B:BB}),0))

        print "완전제곱 외의 항을 우변으로 이전하면,"
        f_BC = sympy.Eq( (x+B)**2, C)
        sympy.pprint( f_BC.subs(B,BB))

        print cl("이제, C는 얼마일까요:")
        CC = input('C = B^2 - c = ? ')
        ans = BB**2 - cc
        if CC != ans: 
            print '틀렸어요. 답은 {}입니다.'.format( ans)
            break
        else: 
            print '맞았어요'
        print

        print "[단계3]"
        print "양의 근과 음의 근을 구하는 단계입니다."
        print cl("문제:")
        sympy.pprint( sympy.Eq(f_bc, 0))

        print "완전제곱형태:"
        sympy.pprint( sympy.Eq( f_bc_B.subs({b:bb,c:cc}), 0))

        print cl("우변정리:")
        print "B={B}를 대입하면,".format(B=BB)
        sympy.pprint( sympy.Eq( f_bc_B.subs({b:bb,c:cc,B:BB}),0))
        
        print cl("제곱근 풀기:")
        f_p = sympy.Eq( x+B, sympy.sqrt(C))
        f_n = sympy.Eq( x+B, -sympy.sqrt(C))
        sympy.pprint( f_p.subs({B:BB,C:CC}))
        sympy.pprint( f_n.subs({B:BB,C:CC}))
        
        print '정답은 지수형(+x.xe+XX)으로 표현 했거나'
        print '또는 내부 변환하여 소수점 첫째짜리까지 검증합니다.'
        sc = math.sqrt( CC)
        x_p = input( 'x_p = +{sc:.2e} - {B} = ? '.format(sc=sc, B=BB))       
        x_n = input( 'x_n = -{sc:.2e} - {B} = ? '.format(sc=sc, B=BB))        
        x_str = "{:.1e}, {:.1e}".format( x_p, x_n)
        ans_p, ans_n = sc - BB, -sc - BB
        ans_str = "{:.1e}, {:.1e}".format( ans_p, ans_n)         
        # if the answer is not int, this is not solvable for perfect precision
        if x_str != ans_str: 
            print '틀렸어요. 답은 {ans_str}이고 입력은 {x_str}을 했어요.'.format( ans_str = ans_str, x_str = x_str)
            print '(정답은 {:.3f},{:.3f}이고 입력은 {:.3f},{:.3f}을 했어요.)'.format( ans_p, ans_n, x_p, x_n)
        else:
            print '(두자리수 정밀도 기준으로) 맞았어요^^; '
            correct_N += 1        
        print
       
        a_p = x_p**2 + bb*x_p + cc
        print '검증(x_p): {x:.1e}^2 + {b}*{x:.1e} + {c} = {a_p:.1e}'.format(x=x_p, b=bb, c=cc, a_p=a_p)
        a_n = x_n**2 + bb*x_n + cc
        print '검증(x_n): {x:.1e}^2 + {b}*{x:.1e} + {c} = {a_n:.1e}'.format(x=x_n, b=bb, c=cc, a_n=a_n)
        print
        
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)
    
    return score


def SAGE_ask_root_2bc( N):
    print "=================================================================="
    print '2차 방정식의 근을 구하는 문제입니다.'
    print "Sage모드에서 동작합니다."
    var('x b c B C')
    f = x**2 + b*x + c == 0
    print "풀고자하는 2차 방정식은 아래와 같습니다."
    print maxima(f)
    print "이론적으로 구한 근들은 다음과 같습니다."
    sol = solve( f, x, solution_dict=True)
    for sol_i in sol:
        print maxima( sol_i[x])    
    
    correct_N = 0
    for ii in range( N):
        print "--------------------------------------------------------------"
        print cl('{}번째 문제입니다.'.format( ii+1))
    
        """
        cc = rd.randint(-10, 10)
        if cc < 0:
            bb = rd.randint(-10, 10) * 2
        else:                
            # b-4c >= 0 is necessary condition to be real roots.
            bb_min = 2 * math.sqrt( cc)
            bb_m = int( math.ceil( bb_min / 2.0))
            bb = rd.randint( bb_m, bb_m + 10) * 2
        """

        alpha, beta = rd.randint(-9, 9), rd.randint(-9, 9)
        bb = -1 * (alpha + beta)
        cc = alpha * beta

        # print '문제:  x^2 + {b}x + {c} = 0, find x?'.format( b=bb, c=cc)
        print "풀고자하는 2차 방정식은 다음과 같다."
        f_bc = f(b=bb, c=cc)
        print maxima( f_bc)
        print "즉, b = {b}, c = {c}".format(b=bb,c=cc)
        print "이론으로 구한 근들은 다음과 같다."
        sol = solve( f_bc, x, solution_dict=True)
        for sol_i in sol:
            print maxima( sol_i[x])
        
        print 
        print cl("[단계1]")
        print "- 좌변을 2차 거듭제곱 형태로 만든다."
        print "- 2차 방정식의 근을 구하는 방법 중의 한가지는" 
        print "  좌변을 완전제곱 형태로 바꾸는 것입니다. 즉,"
        print maxima( (x+B)**2 == C)
        print "이렇게 변환할 때, B는 어떤 값을 가지는지 알아봅시다."
        print
        
        #print('      x^2 + ' +  cl('{b}') + 'x + {c} = 0, find x?').format( b=bb, c=cc)
        print cl("문제:")
        print maxima( f_bc)

        print cl("완전제곱형태:")
        # print '      (x+B)^2 + ({b}-2B)x + {c}-B^2 = 0'.format( b=bb, c=cc)
        f_bc_B = (x+B)**2 + (b-2*B)*x + c-B**2 == 0
        # f_bc_B = x
        print maxima( f_bc_B(b=bb,c=cc))
        f_bc_B_x1 = 2 * x * (B - b/2) == 0
        print "여기서, 완전제곱을 위해 x항은 없어져야 한다. 즉,"
        print maxima( f_bc_B_x1(b=bb)) 
        
        print cl("위가 성립되려면,B를 얼마로 해야할까?")
        BB = input('B = b/2 = ? ')
        ans = bb/2
        if BB != ans: 
            print "틀렸어요. 답은 {}입니다.".format( ans)
            break
        else:
            print '맞았어요'
        print
        
        #--------------------------------------------------------------
        print cl("[단계2]")
        print "좌변의 완전제곱 형태 변화에 따른 우변의 대응되는 값을 구한다."

        print cl("문제:")
        print maxima( f_bc)

        print "완전제곱형태:"
        print maxima( f_bc_B(b=bb,c=cc))

        print cl("우변정리:")
        print "B={B}를 대입하면,".format(B=BB)
        print maxima( f_bc_B(b=bb,c=cc,B=BB))

        print "완전제곱 외의 항을 우변으로 이전하면,"
        #f_bc_B_right = (x+B)**2 == B**2 - c
        #print maxima( f_bc_B_right)
        #print " 즉,"
        #print maxima( f_bc_B_right(B=BB,c=cc))        

        f_BC = (x+B)**2 == C
        print maxima( f_BC(B=BB))

        print cl("이제, C는 얼마일까요:")
        CC = input('C = B^2 - c = ? ')
        ans = BB**2 - cc
        if CC != ans: 
            print '틀렸어요. 답은 {}입니다.'.format( ans)
            break
        else: 
            print '맞았어요'
        print

        print "[단계3]"
        print "양의 근과 음의 근을 구하는 단계입니다."
        print cl("문제:")
        print maxima( f_bc)

        print "완전제곱형태:"
        print maxima( f_bc_B(b=bb,c=cc))

        print cl("우변정리:")
        print "B={B}를 대입하면,".format(B=BB)
        print maxima( f_bc_B(b=bb,c=cc,B=BB))
        
        print cl("제곱근 풀기:")
        f_p = x+B == sqrt(C)
        f_n = x+B == -sqrt(C)
        print maxima( f_p(B=BB,C=CC))
        print maxima( f_n(B=BB,C=CC))        
        
        print '정답은 지수형(+x.xe+XX)으로 표현 했거나'
        print '또는 내부 변환하여 소수점 첫째짜리까지 검증합니다.'
        sc = math.sqrt( CC)
        x_p = input( 'x_p = +{sc:.2e} - {B} = ? '.format(sc=sc, B=BB))       
        x_n = input( 'x_n = -{sc:.2e} - {B} = ? '.format(sc=sc, B=BB))        
        x_str = "{:.1e}, {:.1e}".format( x_p, x_n)
        ans_p, ans_n = sc - BB, -sc - BB
        ans_str = "{:.1e}, {:.1e}".format( ans_p, ans_n)         
        # if the answer is not int, this is not solvable for perfect precision
        if x_str != ans_str: 
            print '틀렸어요. 답은 {ans_str}이고 입력은 {x_str}을 했어요.'.format( ans_str = ans_str, x_str = x_str)
            print '(정답은 {:.3f},{:.3f}이고 입력은 {:.3f},{:.3f}을 했어요.)'.format( ans_p, ans_n, x_p, x_n)
        else:
            print '(두자리수 정밀도 기준으로) 맞았어요^^; '
            correct_N += 1        
        print
       
        a_p = x_p**2 + bb*x_p + cc
        print '검증(x_p): {x:.1e}^2 + {b}*{x:.1e} + {c} = {a_p:.1e}'.format(x=x_p, b=bb, c=cc, a_p=a_p)
        a_n = x_n**2 + bb*x_n + cc
        print '검증(x_n): {x:.1e}^2 + {b}*{x:.1e} + {c} = {a_n:.1e}'.format(x=x_n, b=bb, c=cc, a_n=a_n)
        print
        
    score = 100.0 * correct_N / N
    print "Your score is {score}".format(score=score)
    
    return score