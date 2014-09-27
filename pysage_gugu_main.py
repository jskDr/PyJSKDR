# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 18:31:26 2014

@author: james
"""

from pysage_gugu_mul import *

def SAGE_main():
    print "이 버젼은 sage를 기반한 것입니다."
    print "현재는 sage 기능을 파이썬에서 사용하는 형태로 진행하고,"
    print "나중에는 확장자도 sage로 바꾸어 full mode로 돌린다."
    print "Sage를 실행한 후에 load(fname)을 실행해야 한다."
    print "코멘트라인에서 sage fname.py는 순수한 python 모드이다."
    
    print "--------------------------------------------------------------"
    print "Sage Testing Commands"
    
    var('x b c')
    f = x**2 + b*x + c
    print "기존 모드로 보여준다."
    print f
    print "수식 모드(maxima)로 보여준다."
    print maxima(f)
    print "--------------------------------------------------------------"

    print "태스트의 편리를 위해 5번 2차방정식을 자동으로 실행한다."
    print "우선 한개의 문제를 다루도록 합니다. N -> 1"
    print
    SAGE_ask_root_2bc( 1)   
    

def _gugu_basic_r0():  

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
            ask_q1( N_prob, user_log)
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

def PythonSage_gugu_basic():  

    user_log = login_sys()
    level = 0
    while level != 99:
        print "현재까지 랭킹 15위 리스트입니다."
        print "100점을 받아야 하고 5개 이상의 문제를 풀어야만 기록 됩니다."
        user_log.show()
        print

        print "메뉴: 어떤 에듀게임을 할까요"
        print "------------------------------------"
        print "[Python & Sage에서 모두 가능한 게임]" 
        print "0. 레벨-업 모드"
        print "1. 구구단 테이블을 보여줍니다." 
        print "2. 한자리 수 곱셈 게임입니다."
        print "3. 두자리수와 한자리수의 곱셉 게임입니다."
        print "4. 두자리 수 곱셈 게임입니다."
        print "5. 2차 방정식 근의 공식 게임입니다(a=1)."
        print "------------------------------------"
        print "[Sage에서 가능한 게임 (심볼릭 Math)]"
        print "6. 2차 방정식 근의 공식 게임입니다(a=1)."  
        print "------------------------------------"
        print "[제어 명령어]"
        print "10. 최고 순서대로 점수를 보여준다."            
        print "99. 게임 완료"
        level = input( "번호를 입력해 주세요 --> ")
        print
        
        if level == 0:
            print "순서대로 하면서 레벨을 높혀봅시다."            
            print "레벨-1: 구구단 테이블을 보여줍니다."
            show_table()
            
            print "레벨-2:한자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            # ask_q1( N_prob)
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
            # with Timer( '1x1곱셈 {}개'.format( N_prob), N_prob):
            ask_q_login( ask_q1, N_prob, user_log)
            print 
        
        elif level == 3:
            print "레벨-3:두자리수와 한자리수의 곱셉 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2x1곱셈 {}개'.format( N_prob), N_prob):
            #    ask_q21( N_prob)
            ask_q_login( ask_q21, N_prob, user_log)
            print

            
        elif level == 4:
            print "레벨-4: 두자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2x2곱셈 {}개'.format( N_prob), N_prob):
            #    ask_q2( N_prob)
            ask_q_login( ask_q2, N_prob, user_log)
            print
            

        elif level == 5:
            print "레벨-5: 2차 방정식 근의 공식 게임입니다 (a=1 경우)."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2차 방정식(a=1) {}개'.format( N_prob), N_prob):
            #    ask_root_2bc( N_prob)
            ask_q_login( ask_root_2bc, N_prob, user_log)
            print
            
        # ------------------------------------
        # Sage에서 작동하는 게임
        # ------------------------------------

        elif level == 6:
            print "레벨-6: 2차 방정식 근의 공식 게임입니다 (a=1 경우)."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2차 방정식(a=1) {}개'.format( N_prob), N_prob):
            #    SAGE_ask_root_2bc( N_prob)
            ask_q_login( SAGE_ask_root_2bc, N_prob, user_log)
            print

        elif level == 10:
            print "최고순서대로 점수를 보여준다."
            print "- 일단은 전체를 보여준다."
            user_log.show()
        
        elif level == 99:
            print "게임이 끝났습니다."
        
        print   


if __name__ == "__main__":
    print cl("교육과 게임이 진짜로 합쳐지는 리얼에듀게임이 시작됩니다.")
    print
    
    PythonSage_gugu_basic()