import random
import smtplib
import smtplib
import json


a_file=open('data.json',"r")
output=json.load(a_file)
#print(output.keys())
a_file.close()


cd=open('login_data.json',"r")
customer_data=json.load(cd)
cd.close()


price=0
confirmed_ticket=output
admin_data={'Ram':'123'}
#customer_data={'raja':'123'}
#movie_list={'0':30,'1':40}
#print(confirmed_ticket.items())



cd=open('movie_count.json',"r")
movie_count=json.load(cd)
cd.close()




class ticket_booking():
    movie_A=movie_count['movie_A']
    movie_B=movie_count['movie_B']

    def __init__(self,uname,password):
        self.uname=uname
        self.password=password

    
    def create_ticket(self):
        print("\tHola Customers ")
    
    
        #print(movie_list)

        print("Hello "+self.uname+" "+ "Which Movie do you want to watch")
        print("\n\t 1.movie_1")
        print("\t 2.movie_2")
        print("\n press one or two to proceed?")
        print()

        n=int(input())
        print("please specify the number of tickets you need?")
        no_of_tickets=int(input())
        if(ticket_booking.movie_A<no_of_tickets):
            print("Sorry Customer we dont have tickets better luck next time")
            exit()
        else:
            global price
            #print('n of t',no_of_tickets)
            price+=self.displayprices(n,no_of_tickets)
            price+=self.food_display()
            self.confirmation(price,n,no_of_tickets)

    def ticket_print(self,user_data):
        print()
    
        print()
        confirmed_ticket[user_data[0]]={'no_of_tickets':user_data[2],'movie':user_data[3],'price':user_data[1]}
        print("Thank You")
        print()

    def food_display(self):
        print("\n The food items present are 1.pizza: 100 2.burger:200 3.juice:300")
        p=0
        check=int(input())
        if(check==1):
            p+=100
        elif(check==2):
            p+=200
        elif(check==3):
            p+=300
        return p

    def displayprices(self,n,no_of_tickets):
        print("no of tickets",no_of_tickets)
        print("Ticket price for the movie:")
        if(n==1):
            print("\n\tmovie 1 starring hero1")
            print("\n\tmovie_1=200")
            p=200*no_of_tickets
            print("\n Your ticket price will be",p)
            print("\n Are You ok with this tickets? if so press one or else press 2")
            check=int(input())

            if(check==1):
                return p

            else:
                print("Thank You ,BI")
                exit()   
            
        else:
            print("movie 2 starring heroine 2")
            p=100*no_of_tickets
            print("movie_2=100")
            print("Your ticket price will be",p)
            print()
            print("Are You ok with this tickets? if so press one or else press 2")
            print()
            check=int(input())

            if(check==1):
                return p

            else:
                print("Thank You ,BI")
                exit()
                

    def confirmation(self,price,n,no_of_tickets):
        if(n==1):
            print("R u sure to proceed with payment of rupees",price)
            user_data=(self.uname,price,no_of_tickets,"movie1")
            print("Final Confirmation y or n")
            check=input().strip()
            if(check=='y'):
                ticket_booking.movie_A-=no_of_tickets
                self.ticket_print(user_data)
        else:
            print("R u sure to proceed with payment of rupees",price)
            user_data=(self.uname,price,no_of_tickets,"movie1")
            print("Final Confirmation y or n")
            check=input().strip()
            if(check=='y'):
                ticket_booking.movie_B-=no_of_tickets
                self.ticket_print(user_data)

    def generateotp(self):
        otp = random.randint(1111,9999)
        return otp


    def cancel_ticket(self):
        a_file=open('data.json',"r")
        output=json.load(a_file)
        #print(output.keys())
    
    
        if self.uname in output:
        
            otp=self.generateotp()
            sender = 'assignment681@gmail.com'
            rec = 'assignmentuser597@gmail.com'
            password = 'assignment681!_'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, rec, str(otp))
            print("please type the otp to confirm your request")
            check=int(input())
        
        
            #print(confirmed_ticket[uname].get('no_of_tickets'))
            if(otp==check):
                #print(movie_list.get('0'))
                #print(confirmed_ticket[uname].get('no_of_tickets'))
                if(output[self.uname]['movie']=="movie1"):
                    ticket_booking.movie_A+=confirmed_ticket[self.uname].get('no_of_tickets')
                else:
                    ticket_booking.movie_B+=confirmed_ticket[self.uname].get('no_of_tickets')
                #print(movie_list.get('0'))
                confirmed_ticket.pop(self.uname)
                print("Ticket Cancelled Sucessfully")
                print(confirmed_ticket)
                pass
        a_file.close()





def admin_privileges():
    pass

def admin_login():
    print("Please typer Your Username")
    admin_username=input().strip()
    password=input().strip()
    if(admin_username in admin_data and admin_data[admin_username]==password):
        admin_privileges()
    else:
        print("Sorry Wrong password or Username")
        
def login_page():
    print("If Admin press 1 or Customer press 2")
    check=int(input())
    if(check==1):
        admin_login()
    else:
        customer_login()


def customer_login():
    print("new user(1) or existing user(2)")
    
    check=int(input())

    if(check==1):
        print("give urself a username")
        uname=input().strip()
        print("give urself a password")
        password=input().strip()
        customer_data[uname]=password
        customer=ticket_booking(uname,password)
        customer.create_ticket()
    else:
        
        print("Please enter Your Username")
        uname=input().strip()
        print("password")
        password=input().strip()
        
        if uname in customer_data and customer_data[uname]==password:
            print("*********************************************************************")
            print("\t1.Create Ticket ")
            print("\t2.Cancel Ticket ")
            print("\t3.Check Availability")
            print("\t4.View Ticket")
            print("\t5.Exit")
            print("\npls enter a key")
            print("\n ********************************************************************")
            check=int(input())

            if(check==1):
                customer=ticket_booking(uname,password)
                customer.createticket()
            else:
                customer=ticket_booking(uname,password)
                customer.cancel_ticket()
        else:
            print("Wrong Username or Password")
            



while True:
    print("\t Theatre Ticket Booking")
    print()
    login_page()
   
    print(confirmed_ticket.items())
    print( "movie count A" ,ticket_booking.movie_A)
    
    a_file=open("data.json","w")
    json.dump(confirmed_ticket,a_file)
    a_file.close()

    cd=open("login_data.json","w")
    json.dump(customer_data,cd)
    cd.close()

    movie_count['movie_A']=ticket_booking.movie_A
    movie_count['movie_B']=ticket_booking.movie_B

    mc=open("movie_count.json","w")
    json.dump(movie_count,mc)
    mc.close()
    
    print("\n\tdo you want to continue 1.yes 2.No")
    check=int(input())
    if(check==2):
        break

