#Create a program that accepts booking for time slots for Sri KL.
#make sure you record
# teachers name
# class booking time(when it is booked as well)
# no clashing timings
# 5 teachers, 5 timings

teachers = ['Mr Ryan', 'Puan Sharon', 'Ms Tey', 'Ms Daphne', 'Mdm Chandra']
time = ['10:00-11:00am', '11:00-12:00pm', '2:00-3:00pm', '3:00pm-4:00pm', '4:00-5:00pm']
data = str(1111111111111111111111111)
timecopy = time.copy()


print("Booking time slots for Sri KL")
print("-----------------------------------")
data_test = input("Please insert the data binary code below\nNote: leaving it empty indicates restarting the entire slot.\n")

if not isinstance(data_test, str) or len(data_test) != 25 or not data_test.isdigit() or not all(charac in '01' for charac in data_test): 
    print("Error in data collection. Proceeding to restarting slot.. ")
else: 
    print("Data successfully retrieved! Proceeding.. ")
    data = data_test
print("-----------------------------------")

for x in range(5):
    print(str(teachers[x]) + "'s available time slot(s): ")
    for a in range(5): 
        if (data[a+5*x]) == '0': 
            timecopy[a] = "--Booked--"
    print(timecopy)
    timecopy = time.copy()
    print('')

print("------------------------------------")
print("Please enter your booking details below:")

name = str(input("Enter teacher's name: "))
while name not in teachers: 
    print("Invalid teacher's name. Please try again.")
    name = str(input("Enter teacher's name: "))

timechosen = 0
while timechosen < 1 or timechosen > 5: 
    timecopy = ["1 for 10:00-11:00am", "2 for 11:00-12:00pm", "3 for 2:00-3:00pm", "4 for 3:00-4:00pm", "5 for 4:00-5:00pm"]
    for b in range(5): 
        if (data[b+5*(teachers.index(name))]) == '0': 
            timecopy[b] = ""
        else: 
            print(timecopy[b])
    
    if timecopy == ["","","","",""]: 
        print("Sorry, " + str(name) + "'s time slot has been fully booked!\n")
        print("------------------------------------")
        break;
    else: 
        req_time = int(input("Enter booking time: "))

        if req_time < 1 or req_time > 5: 
            print("Invalid time slot. Please re-enter the digits")
        elif (data[(req_time-1)+5*(teachers.index(name))]) == '0':
            print("Sorry, this slot has been booked! Retrying... \n")
            continue;
        else: 
            timechosen = req_time;

if timecopy != ["","","","",""]: 
    print("\nSuccessfully booked " + str(name) + "'s " + str(time[timechosen-1]) + " slot!")
    print("------------------------------------")
    slotnum = (timechosen-1)+(5*(teachers.index(name)))
    data = data[:int(slotnum)] + '0' + data[int(slotnum+1):]
    print("\nPlease copy the binary code as a save code.")

print(data)
print("For more bookings, please restart the program and paste the above binary code.")
