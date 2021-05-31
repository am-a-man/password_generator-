import pyperclip
import json
from random import randint
import os
def new_entry(num ,LETTERS, var = [], c_num=1):
    c_num = int(c_num)
    try:
        with open("store.json" , 'r+') as jsonFile:
            jsonData = json.load(jsonFile)
    except:
        jsonData = {}
    

    
    
    
    length = len(LETTERS)
    
    if c_num==0:
        for i in jsonData.keys():
            print(i)
        
    if c_num==0:
        while True:
            site = input("enter site: ")
            site = site.strip()
            if site in jsonData.keys():
                break
            else:
                print("enter a valid site: ")

    else:
        site = input("enter site: ")


    code=r""


    
    for i in range(int(num)):
        char = str(LETTERS[randint(0, length-1)])
        code+=char
    
    code=code.strip()
    if c_num==0:
        for i in jsonData[site].keys():
            print(i)

    if c_num==0:
        while True:
            id = input("enter account/nickname: ")
            id = id.strip()
            if id in jsonData[site].keys():
                break
            else:
                print("enter a valid account/ nickname: ")
    
    else:
        id = input("enter an account/nickname: ")
    id = id.strip()
    change=0

    if site in jsonData.keys():
        if id in jsonData[site].keys() and c_num == 1:
            change = int(input("are you sure you want to change the password, this entry already exists ? continue(1/0): "))
        

    if site in jsonData.keys():
        if id in jsonData[site].keys():
            if change == 0 and c_num == 1:
                pyperclip.copy(jsonData[site][id])
                print("current password copied")
                return

    
    code = code.strip()
    jsonData[site] = { id : code}
    
    print(f'''
        {site} : {id} : {jsonData[site][id]}
    ''')
    pyperclip.copy(jsonData[site][id])

    json.dump(jsonData,open("store.json", 'w'))


def instruction():
    print(
        '''
    enter s : see all the websites
    enter q : quit
    enter n : new entry
    enter c : chage entry
         '''
    )





def search():
    with open("store.json", 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    for i in jsonData.keys():
        print(i) 
    while True:
        var = input("enter the name of site you want the password of: ")
        var.strip()
        if var in jsonData:
            break
        else:
            print("enter a valid site name: ")
        
    for i in jsonData[var].keys():
        print(i)
    
    while True:
        id = input("enter the name of id you want the password of: ")
        id = id.strip()
        if id in jsonData[var]:
            break
        else: 
            print("enter a valid id: ")
        
    print("successfully coppied password ")
    
    pyperclip.copy(jsonData[var][id])

    

    
         


def setup():
    while(True):
        instruction()
        var = input("enter your choice: ")
        if(var=='q'):
            return
        
        elif(var== 'n'):
            characters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''

            special_characters = '''!"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}'''

            
            num = int(input("enter number of characters: "))
            var = int(input("include special characters?(1/0) : "))
            if(var):
                characters+=special_characters
           
            new_entry(num, characters, var)

        elif(var == 's'):
            search()
        
        elif var=='c':
            characters = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''

            special_characters = '''!"#$%&\'()*+, -./:;<=>?@[\\]^_`{|}'''
            num = int(input('enter num of charaters in new password: '))
            var = int(input("include special characters?(1/0) : "))
            if(var):
                characters+=special_characters
            new_entry(num,characters, var, 0)

        else:
            print("enter valid response")   
        




def start():
    try:
        setup()
    except: 
        os.system('cls')
        start()


#setup()
start()