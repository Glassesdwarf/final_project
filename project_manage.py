# import database module

# define a funcion called initializing
from database import Database, Table
import random

def initializing():
    # Create a Database object to read all CSV files
    
    db = Database('login.csv')


    login_table = db.create_table('login_data')  
    person = Table('persons.csv','person_table')
   
    db.add_table(login_table) 
    db.add_table(person)

    return db

# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database


    
    
# define a funcion called login

def login():
   
    username = input("Enter your username: ")
    password = input("Enter your password: ")

   
    login_table = db.search('login_data')  
    login_data = login_table.data

    for entry in login_data:
        if entry['username'] == username and entry['password'] == password:
            return [entry['ID'], entry['role'],entry['username'],entry['password']]

    print("Invalid username or password.")
    return None

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None


# define a function called exit

def exit():

    pass

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:
   
   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
projectlist = []
db = initializing()
print 
val = login()

if val[1] == 'admin':
    print('Managing Project')
    print('')
 
elif val[1] == 'student':
    while True:
        print('Managing Project')
        print('1:Creating new project')
        print('2:Accept request')
        print('3:Endprogram')
        choice = int(input('What you do'))
        if not isinstance(choice,int):
            raise TypeError('You must enter 1 or 2 or 3')
        if choice == 1:
            b = {}
            namep = input("naming your project: ")
            b["Projectname"] = namep
            b["Project lead"] = val[2]
            login_table = db.search('login_data')  
            login_data = login_table.data
            for entry in login_data:
                if entry['username'] == val[2] and entry['password'] == val[3]:
                    entry['role'] == "Lead"
                    login_data._save_data
                    projectlist.append(b)
        if choice == 2:
            pname = input('Your Team project name:')
            for i in projectlist:
                if i["Projectname"] == pname:
                    num = random.randint(1,99999)
                    i[f'Member{num}'] == val[2]
        if choice == 3:
            exit()

elif val[1] == 'lead':
    
elif val[1] == 'faculty':
    
elif val[1] == 'advisor':
    

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()