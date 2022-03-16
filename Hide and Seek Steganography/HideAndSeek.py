                    #### HIDES FILES INSIDE OF A PICTURE USING WINRAR ZIPS ####

import os, sys

winrar = r'"TypeThePathToYourWinRAR.exeHere"'           # CHANGE THIS TO THE PATH OF YOUR WinRAR.exe 
steganography = False                                   # DETERMINES IF IT KNOWS YOUR STEGANOGRAPHY FILE PATH

# DEFINES STEGANOGRAPHY FILE PATHS #
def file_path():
    global file_location
    global file_name
    global full_path
    file_location = input('Where would you like to save the zip? ')
    file_name = input('What would you like to name the zip? ')
    file_name = '\\' + file_name + '.zip'
    full_path = file_location + file_name

# FUNCTION TO HIDE FILES INSIDE OF A PICTURE #
def hide(file_location, file_name,):
    global picture
    global hidden_image
    file_location = r'' + file_location + ''
    text = input('Type full path for the text you want to hide: ')
    text = r'' + text
    picture = input('Type full path for the picture you want to use: ')
    picture = r'' + picture
    os.system(winrar + ' a ' + full_path + ' ' + text + ' ' + picture)  
    print(f'File Saving to {full_path}')
    hidden_image = input('Type a name for your picture (holding hidden file): ')
    hidden_image = full_path + '\\' + hidden_image
    os.system(f'copy /b {picture} + {full_path} {hidden_image}')

# DELETES THE EXISITING FILES AFTER PLACING THEM INSIDE THE ZIP- EXITS IF PICTURES, TEXT, or ZIP WASNT CREATED PROPERLY #
    if os.path.exists(hidden_image) and os.path.exists(full_path) and os.path.exists(picture) and os.path.exists(text):
        os.remove(full_path)
        os.remove(text)
        os.remove(picture)
    else:
        print('file error...exiting')
        sys.exit()
    print(f'Hiding {text} inside of {picture}')
    steganography = True

# FUNCTION TO REVEAL HIDDEN FILES INSIDE OF A PICTURE #
def seek():
    if steganography == True:
        os.system(f'cd {file_location}')
        os.system(f'ren {hidden_image} RevealedZipFile.rar')
    else:
        file_location = input("Type the directory of hidden file: ")
        file_location = r'' + file_location
        hidden_image = input('Type name of hidden file: ')
        hidden_image = file_location + '\\' + hidden_image
        os.system(f'cd {file_location}')
        os.system(f'ren {hidden_image} RevealedZipFile.rar')
    print('File Revealed: {file_location}' + '\\' + 'RevealedFile.rar')

# LOOP FOR HIDING OR SEEKING FILES #
user = ''
while user != 'hide' or user != 'seek':        
    user = input('hide or seek? (or exit): ')
    if user == 'hide':
        file_path()
        hide(file_location, file_name)
    elif user == 'seek':
        seek()
    elif user == 'exit':
        sys.exit()
    else:
        print('type hide or seek: ')


