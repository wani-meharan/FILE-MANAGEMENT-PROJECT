# importing build in modules 
import os
import shutil

# take input for user
print("press 1 if you want to create file")
print("press 2 if you want to read file")
print("press 3 if you want to update file")
print("press 4 if you want to delete file")

# taking user input for operations
user_input = int(input("Enter your choice ?"))

# make function for creating folders
try: 
    def createFolder(path):
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"{path} is created successfully")
        else:
            print("Folder exists!")
except Exception as err:
    print(err)


# make function for creation of files
try:
    def createFile(path, text): 

        if not os.path.exists(path):
            with open(path,"w") as f:
                f.write(text)
            print(f"{path} is created successfully")
        else:
            print("file exists!")
except Exception as err:
    print(err)


# make function for reading files 
try:
    def readFile(path):
        if (os.path.isfile(path)):
            with open(path ,"r") as f:
                print(f.read())
        else:
            print("file doesn't exists! ")
except Exception as err:
    print(err)


# make function for update files 
try:
    def writeFile(path, text):
        if os.path.isfile(path):
            with open(path,"w") as f:
                f.write(text)
        else:
            print("file doesn't exist!")
except Exception as err:
    print(err)


# updating or appending data to a file
try:
    def updateFile(path, text):
        if os.path.isfile(path):
            with open(path,"a") as f:
                f.write(text)
        else:
            print("file doesn't exist!")
except Exception as err:
    print(err)


# function for deleting folder
try: 
    def deleteFolder(folder_path):
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print("folder deleted sucessfully")
        else:
            print("file not found or not exists")
except Exception as err:
    print(err)


# function for deleting files
try:
    def deleteFile(path):
        if os.path.isfile(path):
            os.remove(path)
            print("file deleted sucessfully!")
        else:
            print('file not found or not exists')
except Exception as err:
    print(err)


# do operation based on user input
if (user_input == 1):

    print('Do you want to create a folder or file')
    print('Enter 1 for folder and 2 for file')
    res = int(input("What is your choice ?"))

    if res == 1:
        path = input("Enter folder name ?")
        createFolder(path)

    elif res == 2 :
        path = input('Enter path or file name >')
        text = input('Enter text that you want to store in this file ?')
        createFile(path, text)
    else:
        print("Invalid choice!")

elif user_input == 2:
    path = input('Which file do you want to read. Enter file name or path ?')
    readFile(path)

elif user_input == 3:
    print('if you want to clear file and add data press 1')
    print('if you want to append data to the file without removing anything then press 2')
    res = int(input('Enter your choice ?'))
    if res == 1 :
        path = input('Enter your file path or name ?')
        text = input('Enter you data that you want to add into file ?')
        writeFile(path,text)
    elif res == 2:
        path = input('Enter your file path or name ?')
        text = input('Enter you data that you want to add into file ?')
        updateFile(path, text)
    else:
        print('Invalid choice')
elif user_input == 4 :
    print('what you want to remove folder or file ')
    print("press 1 for folder and 2 for file ?")
    res = int(input("Enter your choice ?"))
    if res == 1:
        folder_path = input("Enter you path or folder name ?")
        deleteFolder(folder_path)
    elif res == 2 :
        path = input('Enter your path or file name ?')
        deleteFile(path)
    else:
        print("invalid choice!")




