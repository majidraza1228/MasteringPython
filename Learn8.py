def days_to_unit2(num_of_days):
    if (num_of_days>50):
        return (50*num_of_days)
    elif (num_of_days)==0:
        return 0
    else:
        return (num_of_days)
    
def validate_and_Exectue():
    try :
        user_input_number =int(user_input)
        if user_input_number>0:
           calculated_vaue =days_to_unit2(user_input_number)
           print(calculated_vaue)
        elif user_input_number == 0:
            print("Hello")
            
        else:
            print("End")
    except ValueError:
           print("End of try")

user_input=input("Please input the number \n")

while user_input != "exit":
      user_input= input("input end to exit")
      validate_and_Exectue()