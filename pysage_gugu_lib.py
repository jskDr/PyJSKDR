# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 07:26:01 2014

@author: james
"""

#========================================================================
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
#========================================================================

#========================================================================
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
#========================================================================
