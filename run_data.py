# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:53:13 2018

@author: roy
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.CommandLineAuth() 
drive = GoogleDrive(gauth)

try:
    name = 'lottery_temp.xlsx'  
    file2 = drive.CreateFile({'id': file['id']})
    file2.SetContentFile(name)
    file2.Upload()
    print ("Uploading succeeded!")
except:
    print ("Uploading failed.")
