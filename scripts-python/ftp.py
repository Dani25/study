# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:24:46 2017

@author: saia12
"""

# ftplib FTP transfers Python
from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username',passwd='password')

#change working directory
ftp.cwd('/specificdomain-or-location/')


def grabFile():
    filaName = 'fileName.txt'
    localFile = open(filename, 'wb')
    ftp.retrbinary('RETR' + filename, localfile.write, 10)
    
    ftp.quit()
    localfile.close()
    
def placeFile():
    filename='fileName.txt'
    ftp.storbinary('STOR'+filename, open(filename, 'rb'))
    ftp.quit()