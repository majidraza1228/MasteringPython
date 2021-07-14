cal_to_hours=24
name_of_unit ="hours"

def days_to_unit(num_of_days, custom_message):
    print(f"Number of days unit {cal_to_hours * num_of_days} this is the result {custom_message}")
    

user_input_number = int(input("Pleae enter the number \n"))
days_to_unit(user_input_number,"This is first call")
days_to_unit(50,"This is secnond call")
