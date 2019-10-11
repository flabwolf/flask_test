# -*- coding: utf-8 -*-
# !/usr/bin/python3.6
import sys
import codecs
import locale
import datetime
import platform
import cgitb

cgitb.enable()

if __name__=='__main__':
    print("Content-Type: text/html;charset=shift-jis\n")
    print()
    print("===============================",end="<br/>")
    print("date:",datetime.datetime.today(),end="<br/>")
    print("python",platform.python_version(),end="<br/>")
    print(sys.getdefaultencoding(),end="<br/>")
    print(sys.stdout.encoding,end="<br/>")
    print("-------------------------------",end="<br/>")
    print("Hello World!")
    print("<b>こんにちは</b>")