
cal_to_hours=24
name_of_unit ="hours"

def days_to_unit(num_of_days, custom_message):
    print(f"Number of days unit {cal_to_hours * num_of_days} this is the result {custom_message}")
    
def days_to_unit2(num_of_days):
    if (num_of_days>50):
        return (50*num_of_days)
    elif (num_of_days)==0:
        return 0
    else:
        return (num_of_days)
    
user_input_number = int(input("Pleae enter the number \n"))
days_to_unit(user_input_number,"This is first call")
days_to_unit(50,"This is secnond call")

print(f"New Function {days_to_unit2(100)}")