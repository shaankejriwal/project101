import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'VOCDVgM2GokAAAAAAAAAARZKsrw6NW_qEU2A5j7SW8HLFhdpfGzj4DmTORE2oS69'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload : - ") 

    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()