# ## Problem Statement
# ### Food ordering system 

print('\n' * 1)

import sys
import pandas as pd 
import time
from datetime import datetime

def selectRastaurent():
    while True:
        print("*" * 31 + "Welcome to Swiggy" + "*" * 28 + '\n'
            "\t(O) ONE COOK RESTAURENT \n"
            "\t(T) TWO COOK RESTAURENT \n"
            "\t(F) FAST COOK RESTAURENT \n"
            "\t(A) Admin Login \n"+
            "-"* 72
        )

        input_1 = str(input('Please select Restaurent: ').upper())
        if (len(input_1) == 1):
            if(input_1 == 'O'):
                print("\n" * 2)
                Retro = "FoodMenu.txt" 
                menu(Retro)
                break

            elif(input_1 == 'T'):
                print("\n" * 2)
                Retro = "FoodMenuTwo.txt" 
                menu(Retro)
                break

            elif(input_1 == 'F'):
                print("\n" * 2)
                Retro = "FoodMenuThree.txt" 
                menu(Retro)
                break

            elif(input_1 == 'A'):
                print("\n" * 2)
                print('This is admin Panel')
                admin()
                break
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")         #Invalid input



def menu(Retro):
    
    menu_card = pd.read_csv(f"{Retro}",sep = ';',index_col=False)

    
    print(menu_card)
    print('\n' * 3)
    code = input("Enter the Item code to order the Food: ")
    counter = 3
    order_receive_estimation_time = []
    total_bill = []
    flag = 0
    while counter != 0:
        
        try:
            order_receive = menu_card.loc[menu_card['Item'] == code.upper()]
            print(order_receive)

            if order_receive.empty:
                print("Please enter correct value")
                counter = counter - 1
                flag = 1

            order_receive_estimation_time.append((order_receive['time'].values[0]))
            total_bill.append(order_receive['price'].values[0])

            print('\n' * 2)
            query = input("Do you Wish to order more  yes/No:- ")
            if query.lower() == "yes":
                code = input("Enter the Item code to order the Food:")
                counter = counter - 1
            else:
                break
                
        except:
            print("Please enter the correct code ")
            counter = counter - 1
    

    # print(order_receive_estimation_time)
    if flag == 0:           
        print("Thanx for ordering")
        est_time_in_min = max(order_receive_estimation_time) 
        print("Estimated time for food preparing and dispatch {} mins.".format(est_time_in_min))
        # print(order_receive_estimation_time)
        print("Bill amount Rs {}".format(sum(total_bill)))
        sleep_time = est_time_in_min 
        print('\n' * 2)
        print("Please wait for {} mins to order".format(est_time_in_min))
        time.sleep(sleep_time)
        query = input("Do you want to order more ?")
        if query.lower() == "yes":
            menu(Retro)
        else:
            print("Thank you for choosing us")

selectRastaurent()