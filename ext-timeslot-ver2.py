import sys

def extline():
    print("--------------------------------")

def viewtimeslot(data, time):
    for x in range(5):
        if data[x] == '0':
            time[x] = "--Booked--"
    print(time)
    return time

def error(x):
    print(x + " error, rebooting...")
    extline()


def saveslot():
    try:
        data = str(input("Please enter your savecode (leave it empty if none): "))
        if data == '':
            data = '11111'
       
        data2 = str(data[5:])
        data = str(data[:5])
        maxsplit = 0
        for c in range(5):
            if data[c] == '0':
                maxsplit += 1

        tchrs = data2.split("#", maxsplit)
        #print(str(tchrs) + "\n" + str(data) + "\n" + str(data2))
       
        if len(data) != 5 or data.isdigit() == False:
            raise ValueError()
        else:
            for char in range(len(data)):
                if data[char] == '0' or data[char] == '1':
                    pass;
                else:
                    raise ValueError()
           
            extline()
            if data != '00000':
                print("Savecode successfully applied")
            else:
                print("Sorry, there are no timeslots left to book!\n")
                for a in range(5):
                    print("Timeslot " + str(a+1) + " is booked by user " + tchrs[a])

                sys.exit()

       
    except ValueError:
        error("Savecode")
        data = str(11111)
    return data, tchrs;


def name(teachers):
    username = str(input("Please enter your name (for teachers): "))
    if username.isdigit() == True:
        error("Type")
        return name()
    else:
        for i in teachers:
            if i == username.upper():
                print("Username already taken, sorry!")
                extline()
                sys.exit()
        return username;

def timeslotno(time, data):
    try:
        for c in range(len(time)):
            if time[c] != '--Booked--':
                print(str(c+1) + "  " + str(time[c]))
           
        timeno = int(input("Please type in the timeslot number of your choice according to the list: "))
        timeno -= 1

        if data[timeno] != '1':
            raise ValueError;
        else:
            print("Timeslot number successfully recorded")
            extline()
            return timeno;
       
    except ValueError:
        error("Value")
    except:
        error("Syntax")
        sys.exit()
    return -1;
   

def timeslot():
    print("Sri KL's Timeslot for Explorer Lab: Monday ver.")
    extline()

    data, teachers = saveslot()
    time = ['10:00-11:00am', '11:00-12:00pm', '2:00-3:00pm', '3:00pm-4:00pm', '4:00-5:00pm']
   
    print("Timeslots available: ")
    print("10:00-11:00am | 11:00-12:00pm | 2:00-3:00pm | 3:00-4:00pm | 4:00-5:00pm")
    updt = viewtimeslot(data,time)

    #enter name of user
    username = name(teachers)
    extline()
    print("Welcome, " + username.upper() + ". ")
   
    timeno = -1
    while timeno == -1:
        timeno = int(timeslotno(time, data))
        if timeno != -1:
            data = data[:int(timeno)] + '0' + data[int(timeno+1):]
            teachers.insert(timeno, username.upper())

            if teachers.count("") == True:
                teachers.remove("")
            print(teachers)
            for d in range(len(teachers)):
                if d != 0:
                    data = data + '#'
                data = data + str(teachers[d])

           
            print("Version no.: 1.2\nYour savecode: " + str(data) + "\nPlease copy and paste this code for future use.")
            extline()
           
       
timeslot()
