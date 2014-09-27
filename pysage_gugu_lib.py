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
