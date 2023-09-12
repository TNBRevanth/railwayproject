import random
class Account():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def checkpassword(self,password):
        return self.password==password
account=[Account("user","1234"),
         Account("user1","1234")]

class TrainDetails():
    def __init__(self,train_number,source,destination,seats):
        self.train_number=train_number
        self.source=source
        self.destination=destination
        self.seats=seats
    
    def TrainDetails_display_information(self):
        print(f"Enter the train number: {self.train_number}")
        print(f"Enter the source: {self.source}")
        print(f"Enter the destination: {self.destination}")
        print(f"Enter number of seats: {self.seats}")
    
    def book_tickets(self,number_tickets):
        if number_tickets>self.seats:
            return None
        else:
            PNR_list=[]
            for i in range(number_tickets):
                PNR_list.append(random.randint(10000-99999))
                self.seats -=number_tickets
                return PNR_list
class passenger_Details():
    def __init__(self,passenger_name,passenger_mobilenumber,passenger_gender,passenger_age):
        self.passenger_name=passenger_name
        self.passenger_mobilenumber=passenger_mobilenumber
        self.passenger_gender=passenger_gender
        self.passenger_age=passenger_age
    
    def passenger_Details_display_information(self):
        print(f"Enter passenger Name: {self.passenger_name}")
        print(f"Enter passenger Mobile number: {self.passenger_mobilenumber}")
        print(f"Enter passenger Gender: {self.passenger_gender}")
        print(f"Enterpassenger Age: {self.passenger_age}")
        for passengers in self.passenger:
            passengers.passenger_Details_display_information()
            print()
class ticket():
    def __init__(self,train,source,destination,passengers,pnr_no):
        self.train=train
        self.source=source
        self.destination=destination
        self.passengers=passengers
        self.pnr_no=pnr_no
    def display_info(self):
        print(f"train no:{self.train.train_number}")
        print(f"source:{self.source}")
        print(f"destination:{self.destination}")
        print(f"pnr_no:{self.pnr_no}")
        for passenger in self.passengers:
            passenger.display_info()
        print()

loginaccount=None
while True:
    print("\n1.Click 1 for creating an account. \n(Or)\n2.Click 2 for login ")
    option=int(input("Enter the number: "))
    if option==1:
        username=input("Enter Username: ")
        password=int(input("Enter password: "))
        account.append(Account(username,password))
        print("Account Created Succesfully")
    elif option==2:
        username=input("Username:")
        password=int(input("Password:"))
        for user in account:
            if user.username==username and user.checkpassword(password):
                loginaccount=user
                break
        if loginaccount is None:
            print("invalid username (or) Password")
        else:
            print("login successfull{loginaccount.username}")
            break
        if loginaccount is None:
            print("please provide correct username (or) password")
        else:
            print(f"\nLogged in as {loginaccount.username}\n")

        break
    else:
        print("Invalid choice.")
if loginaccount is not None:
    presenttrains=[TrainDetails("1234","Vijayawada","Hydrabad",10),
            TrainDetails("5678","Hyderabad","Vijayawada",20),
            TrainDetails("1011","Hyderabad","Bangalore",30),
            TrainDetails("1213","Banglore","Hyderabad",40)]
        
for train in presenttrains:
    train.passenger_Details_display_information()
        

while True:
    try:
        trainnumber=input("Enter the train Number: ")
        numberoftickets=int(input("Enter no of Tickets: "))
        if numberoftickets<=0:
            raise ValueError ("Number of tickets should be greater than 0: ")
        for train in presenttrains:
            if train.train_number == trainnumber:
                if numberoftickets > train.seats:
                    raise ValueError("Selected tickets are more than available")
                break
        else:
            raise ValueError("Please give the correct Train Number")
        break
    except ValueError as a:
        print(f"Provide validinput:{a}")
train=None
for t in presenttrains:
    if t.trains_number==trainnumber:
        train=t
        break
    if train is None:
        print("Invalid Train Number")
    else:
        passenger=[]
        for i in range(numberoftickets):
            print(f"enter the password details:{i+1}: ")
            while True:
                try:
                    Name=input("Name: ")
                    if not Name:
                        raise ValueError("Name cannot be empty")
                    Age=int(input("Age: "))
                    if not Age:
                        raise ValueError("Invalid age")
                    Gender=input("Gender: ")
                        # if not Gender:
                        #     raise ValueError("Invalid Gender")
                    Mobilenumber=int(input("Mobile number"))
                    if not Mobilenumber or len(Mobilenumber) !=10 or not Mobilenumber.isdigit():
                        raise ValueError("Invalid phone number")
                    passenger=passenger_Details(Name,Age,Gender,Mobilenumber)
                    passenger.append(passenger)
                    break
                except ValueError as e:
                    print(f"Invalid Input: {e}")

                pnrlist=train.book_tickets(numberoftickets)
                if pnrlist is None:
                    print("tickets not available")
                else:
                    for i in range(numberoftickets):
                        ticket=ticket(train,train.source,train.destination[passenger[i],pnrlist[i]])
                        ticket.passenger_Details_display_information()
                        print("booking Successfull")
                    
    

            













