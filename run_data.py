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
    name = 'lottery_temp.xlsx'  # It's the file which you'll upload
#    file = drive.CreateFile()  # Create GoogleDriveFile instance
#    file.SetContentFile(name)
#    file.Upload()
#    permission = file.InsertPermission({
#                        'type': 'anyone',
#                        'value': 'anyone',
#                        'role': 'reader'})
    file2 = drive.CreateFile({'id': '1V_zff4iTDwJjV2F5ETRDvDYVwgHBtO4j'})
    # id=1w5HetL2R4brLnCyb1JVrTDABUtJv-cBP
    file2.SetContentFile(name)
    file2.Upload()
    print ("Uploading succeeded!")
except:
    print ("Uploading failed.")