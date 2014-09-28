# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 18:31:26 2014

@author: james
"""

from pysage_gugu_lib import *

from pysage_gugu_mul import *
import pysage_gugu_div as gugu_div
import pysage_gugu_sym as gugu_sym

import time

#========================================================================
import operator
import os # for file checking for existing

class login_sys():
    def __init__(self):
        self.user_name = raw_input("사용자 이름은 무엇인가요: ")
        print "사용자 이름: ", self.user_name
        print 

    def append(self, problem, score, records):
        with open("score.txt", "a") as myfile:
            out_data = "{problem}, {name}, {score}".format( name = self.user_name, problem = problem, score = score)
            for record in records:
                out_data += ", {}".format(record)
            out_data += "\n"
            myfile.write( out_data)
    
    def show(self):
        """
        [File format]
        0번호, 1이름, 2점수, 3갯수, 4총시간, 5단위시간 
        """
        print "전체 아이템에 대해서 랭킹을 보여줍니다."
        words_all = []
        #print "최근순으로 보여준다."
        file_path_name = "score.txt"
        if os.path.isfile( file_path_name):
            with open(file_path_name, "r") as myfile:
                lines = myfile.readlines()
                for line in lines:
                    #print line,
                    words = line.split(',')
                    #print "{}의 시간 = {}".format( words[1], words[5])
                    # "랭킹: 0번호, 1이름, 2점수, 3갯수, 4총시간(초), 5단위시간(초)"
                    # sec must be changed to sec
                    words[5] = float( words[5])
                    words_all.append( words)
                #print
            
            print "단위시간이 최고 적은순으로 보여준다."
            print "TOP-15위까지만 보여줍니다."
            print "랭킹: 0번호, 1이름, 2점수, 3갯수, 4총시간(초), 5단위시간(초)"
            words_all.sort( key = operator.itemgetter(5))
            for idx, words in enumerate(words_all):
                if idx < 15:
                    # "랭킹: 0번호, 1이름, 2점수, 3갯수, 4총시간(초), 5단위시간(초)"
                    words[5] = str(words[5])
                    line = ",".join( words)
                    print idx+1, "순위: ", line
                else:
                    break
            print
        else:
            print "New high-score recoding is initiated."

    def show_sel_item(self, sel_item):
        """
        [File format]
        0번호, 1이름, 2점수, 3갯수, 4총시간, 5단위시간 
        지정한 번호에 대해서 랭킹을 보여준다.
        """
        print "%d번 아이템에 대해서 랭킹을 보여줍니다." % sel_item
        words_all = []
        #print "최근순으로 보여준다."
        file_path_name = "score.txt"
        if os.path.isfile( file_path_name):
            with open(file_path_name, "r") as myfile:
                lines = myfile.readlines()
                for line in lines:
                    #print line,
                    words = line.split(',')

                    #print "{}의 시간 = {}".format( words[1], words[5])
                    words[5] = float( words[5])

                    words_all.append( words)
                #print
            
            print "단위시간이 최고 적은순으로 보여준다."
            print "TOP-15위까지만 보여줍니다."
            print "랭킹: 0번호, 1이름, 2점수, 3갯수, 4총시간(초), 5단위시간(초)"
            words_all = [x for x in words_all if int(x[0]) == sel_item]
            words_all.sort( key = operator.itemgetter(5))
            for idx, words in enumerate(words_all):
                if idx < 15:
                    # "랭킹: 0번호, 1이름, 2점수, 3갯수, 4총시간(초), 5단위시간(초)"
                    words[5] = str(words[5])

                    line = ",".join( words)
                    print idx+1, "순위: ", line
                else:
                    break
            print
        else:
            print "New high-score recoding is initiated."


    def show_nosort(self):
        """
        [File format]
        0번호, 1이름, 2점수, 3갯수, 4총시간, 5단위시간 
        """
        words_all = []
        print "최근순으로 보여준다."
        with open("score.txt", "r") as myfile:
            lines = myfile.readlines()
            for line in lines:
                print line,
                words = line.split(',')
                print "{}의 시간 = {}".format( words[1], words[5])
                words_all.append( words)
            print
                
#========================================================================

def ask_q_login(ask_q, N, user_log, sel_item = 1):
    """
    추가할 기능
    - 10개중에 9개를 맞추었으면 단위 시간은 총시간/9개로 변경 예정
      (불리하게 하더라도 불합리하게 하면 안된다는 작은 딸의 생각 반영)
    """
    
    tstart = time.time()
    score = ask_q(N)
    time_all = time.time() - tstart
    # 시간은 맞고 틀리고에 상관없이 전체 횟수로 나눈다.     
    # time_each = time_all / (N * score)
    # 시간은 틀린 문제에 대해 panelty를 매기면서 측정한다. 맞는 부분만 나눠준다. 
    if score != 0:
        time_each = time_all / (N * score / 100.0)
        print "Total time is {t:.2f}sec for {N}, each time is {t1:.2f}sec.".format(t=time_all, N=N, t1=time_each)
    else:
        # time_each = time_all
        print "Total time is {t:.2f}sec for {N} (each time is not allowed.).".format(t=time_all, N=N)
    
    print "N>=2이고 score>0인 경우만 기록에 포함한다."
    print "N이 작은 경우는 평균치가 충분히 만들어지지 않는다."
    if N >= 2 and score != 0:   
        user_log.append( sel_item, score, [N, time_all, time_each])    
        
    raw_input("엔터키를 치시면 계속됩니다...")

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
    game_finish = False
    while game_finish != True:
        print "현재까지 랭킹 15위 리스트입니다."
        print "100점을 받아야 하고 5개 이상의 문제를 풀어야만 기록 됩니다."
        user_log.show()
        print

        print cl("메뉴: 어떤 에듀게임을 할까요")
        print "------------------------------------"
        print "0. 구구단 테이블을 보여줍니다." 

        print "------------------------------------"
        print cl("[곱셈]")
        print "1. 한자리 수 곱셈 게임입니다."
        print "2. 두자리수와 한자리수의 곱셉 게임입니다."
        print "3. 두자리 수 곱셈 게임입니다."
        print "9. 곱셈 종합 모드"

        print "------------------------------------"
        print cl("[나눗셈]")
        print "11. 한자리 수 나눗셈 게임입니다."
        print "12. (2x1) 결과에 대한 나눗셈 게임입니다."

        print "------------------------------------"
        print cl("[방정식]")
        print "21. 2차 방정식 근의 공식 게임입니다(a=1)."

        print "===================================="
        print cl("[심볼릭 Math: import sympy]")
        print "121. 2차 방정식 근의 공식 게임입니다(a=1)."  

        print "===================================="
        print cl("[제어 명령어]")
        print "991. 최고 순서대로 점수들을 정렬하여 보여준다."            
        print "992. 지정한 아이템에 대해서만 점수 리스트를 보여준다."
        print "999. 게임 완료"

        sel_item = raw_input( "번호를 입력해 주세요 --> ")
        print

        if len(sel_item) > 0:
            sel_item = int( sel_item)
        else:
            continue
        
        #기본 
        if sel_item == 0:
            print "0번: 구구단 테이블을 보여줍니다."
            show_table()
            print        

        # 곱셈 게임 
        elif sel_item == 1:
            print "1번:한자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            # with Timer( '1x1곱셈 {}개'.format( N_prob), N_prob):
            ask_q_login( ask_q1, N_prob, user_log, sel_item)
            print 
        
        elif sel_item == 2:
            print "2번:두자리수와 한자리수의 곱셉 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2x1곱셈 {}개'.format( N_prob), N_prob):
            #    ask_q21( N_prob)
            ask_q_login( ask_q21, N_prob, user_log, sel_item)
            print
            
        elif sel_item == 3:
            print "3번: 두자리 수 곱셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2x2곱셈 {}개'.format( N_prob), N_prob):
            #    ask_q2( N_prob)
            ask_q_login( ask_q2, N_prob, user_log, sel_item)
            print
            
        elif sel_item == 9:
            print "곱셈 종합 모드를 시작합니다."
            print "순서대로 하면서 실력을 높혀봅시다."            
            N_prob = int( raw_input("개별 문제들은 몇번씩 풀겠습니까? "))
            
            print "0번: 구구단 테이블을 보여줍니다."
            show_table()
            
            print "1번:한자리 수 곱셈 게임입니다."
            ask_q1( N_prob)
            print
            
            print "2번:두자리수와 한자리수의 곱셉 게임입니다."
            ask_q21( N_prob)
            print
            
            print "3번: 두자리 수 곱셈 게임입니다."
            ask_q2( N_prob)
            
        # [나눗셈 게임]
        elif sel_item == 11:
            print "11번:몫이 한자리 수인 나눗셈 게임입니다."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            # with Timer( '1x1곱셈 {}개'.format( N_prob), N_prob):
            ask_q_login( gugu_div.ask_q1, N_prob, user_log, sel_item)
            print 

        elif sel_item == 12:
            print "12번:몫이 두자리수 나눗셈 게임입니다 (나누는 수는 1자리)"
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            # with Timer( '1x1곱셈 {}개'.format( N_prob), N_prob):
            ask_q_login( gugu_div.ask_q21, N_prob, user_log, sel_item)
            print 


        # [이차 방정식에서 근 구하기]            
        elif sel_item == 21:
            print "4번: 2차 방정식 근의 공식 게임입니다 (a=1 경우)."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2차 방정식(a=1) {}개'.format( N_prob), N_prob):
            #    ask_root_2bc( N_prob)
            ask_q_login( ask_root_2bc, N_prob, user_log, sel_item)
            print
            
        # ------------------------------------
        # Sage에서 작동하는 게임
        # ------------------------------------

        elif sel_item == 121:
            print "121: 2차 방정식 근의 공식 게임입니다 (a=1 경우)."
            N_prob = int( raw_input("몇 개의 문제를 풀겠습니까? "))
            #with Timer( '2차 방정식(a=1) {}개'.format( N_prob), N_prob):
            #    SAGE_ask_root_2bc( N_prob)
            ask_q_login( gugu_sym.sympy_ask_root_2bc, N_prob, user_log)
            print


        # ------------------------------------
        # 운영과 관련된 모드
        # ------------------------------------

        elif sel_item == 991:
            print "최고순서대로 점수를 보여준다."
            print "- 일단은 전체를 보여준다."
            user_log.show()
            raw_input("엔터를 치면 계속합니다..")

        elif sel_item == 992:
            print "지정한 아이템에 대해서만 최고순서대로 점수를 보여준다."
            sel_item_show = input("보여줄 아이템 번호는? ")
            user_log.show_sel_item( sel_item_show)
            raw_input("엔터를 치면 계속합니다..")
        
        elif sel_item == 999:
            print "게임이 끝났습니다."
            game_finish = True
        
        print   


if __name__ == "__main__":
    print cl("교육과 게임이 진짜로 합쳐지는 리얼에듀게임이 시작됩니다.")
    print
    
    PythonSage_gugu_basic()