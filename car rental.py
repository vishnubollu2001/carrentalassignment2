def main():
    print('Welcome to Formula Selfdrive Cars')
    print('Available cars are as follows:')
    print('1. Alto')
    print('2. Creta')
    print('3. Swift')
    print('4. Innova')
    print('5. WagonR')
    num = int(input('Enter your chosen car:'))
    if num == 1:
        alto()
    elif num == 2:
        creta()
    elif num == 3:
        swift()
    elif num == 4:
        innova()
    elif num == 5:
        wagonR()
    else:
        print('Selected car not available')
def alto ():
    print('This car rent for one day is RS.1200')
    conformation=input('Do you want to proceed:')
    if conformation=='yes':
     rent_per_day=1200
    no_of_days=int(input('enter how many days:' ))
    name=input('enter your name:')
    age=int(input('enter your age:'))
    if age>=21:
        print('your age is eligible to book the car')
        amount=rent_per_day*no_of_days
        gst=0.05*amount
        total_amount=amount+gst
        if no_of_days>=3:
            discount=total_amount-400
            print(f'Hi {name},thank you for bokking formula selfdrive cars.since you have booked for {no_of_days}days you will get a discount of 400.\n So the final amount you have to pay (incuding gst)=Rs.{discount}')
        else:
           print(f'Hi {name},thank you for booking formula selfdrive cars.since you have booked for {no_of_days}days.\nSo the total amount you have to pay (incuding gst)=RS.{total_amount}')
        print('Drive safer! Slow driving saves lives. Thank you for booking!')
    else:
        print('sorry you cannot book as your age is not above 21 or above')
def creta():
    print('This car rent for one day is RS.2000')
    rent_per_day=2000
    conformation=input('Do you want to proceed:')
    if conformation=='yes':
      no_of_days=int(input('enter how many days:' ))
    name=input('enter your name:')
    age=int(input('enter your age:'))
    if age>=21:
        print('you are eligible to book the car')
        amount=rent_per_day*no_of_days
        gst=0.05*amount
        total_amount=amount+gst
        if no_of_days>=3:
            discount=total_amount-550
            print(f'Hi {name},thank you for bokking formula selfdrive cars.since you have booked for {no_of_days}days you will get a discount of 400.\n So the final amount you have to pay (incuding gst)=Rs.{discount}')
        else:
           print(f'Hi {name},thank you for booking formula selfdrive cars.since you have booked for {no_of_days}days.\nSo the total amount you have to pay (incuding gst)=RS.{total_amount}')
        print('Drive safer! Slow driving saves lives. Thank you for booking!')
    else:
        print('sorry you cannot book as your age is not above 21 or above')
def swift():
    print('This car rent for one day is RS.1700')
    conformation=input('Do you want to proceed:')
    if conformation=='yes':
      rent_per_day=1700
    no_of_days=int(input('enter how many days:' ))
    name=input('enter your name:')
    age=int(input('enter your age:'))
    if age>=21:
        print('you are eligible to book the car')
        amount=rent_per_day*no_of_days
        gst=0.05*amount
        total_amount=amount+gst
        if no_of_days>=3:
            discount=total_amount-470
            print(f'Hi {name},thank you for bokking formula selfdrive cars.since you have booked for {no_of_days}days you will get a discount of 470.\n So the final amount you have to pay (incuding gst)=Rs.{discount}')
        else:
           print(f'Hi {name},thank you for booking formula selfdrive cars.since you have booked for {no_of_days}days.\nSo the total amount you have to pay (incuding gst)=RS.{total_amount}')
        print('Drive safer! Slow driving saves lives. Thank you for booking!')
    else:
        print('sorry you cannot book as your age is not above 21 or above')
def innova():
    print('This car rent for one day is RS.2300')
    rent_per_day=2300
    conformation=input('Do you want to proceed:')
    if conformation=='yes':
     no_of_days=int(input('enter how many days:' ))
    name=input('enter your name:')
    age=int(input('enter your age:'))
    if age>=21:
        print('you are eligible to book the car')
        amount=rent_per_day*no_of_days
        gst=0.05*amount
        total_amount=amount+gst
        if no_of_days>=3:
            discount=total_amount-600
            print(f'Hi {name},thank you for bokking formula selfdrive cars.since you have booked for {no_of_days}days you will get a discount of 600.\n So the final amount you have to pay (incuding gst)=Rs.{discount}')
        else:
           print(f'Hi {name},thank you for booking formula selfdrive cars.since you have booked for {no_of_days}days.\nSo the total amount you have to pay (incuding gst)=RS.{total_amount}')
        print('Drive safer! Slow driving saves lives. Thank you for booking!')
    else:
        print('sorry you cannot book as your age is not above 21 or above')
def wagonR():
    print('This car rent for one day is RS.1400')
    rent_per_day=1400
    conformation=input('Do you want to proceed:')
    if conformation=='yes':
     no_of_days=int(input('enter how many days:' ))
    name=input('enter your name:')
    age=int(input('enter your age:'))
    if age>=21:
        print('you are eligible to book the car')
        amount=rent_per_day*no_of_days
        gst=0.05*amount
        total_amount=amount+gst
        if no_of_days>=3:
            discount=total_amount-430
            print(f'Hi {name},thank you for bokking formula selfdrive cars.since you have booked for {no_of_days}days you will get a discount of 430.\n So the final amount you have to pay (incuding gst)=Rs.{discount}')
        else:
           print(f'Hi {name},thank you for booking formula selfdrive cars.since you have booked for {no_of_days}days.\nSo the total amount you have to pay (incuding gst)=RS.{total_amount}')
        print('Drive safer! Slow driving saves lives. Thank you for booking!')
    else:
        print('sorry you cannot book as your age is not above 21 or above')
main()