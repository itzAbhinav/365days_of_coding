# Part 1 

def apply_priority_fee(money):
    return (money + 40)

print(apply_priority_fee(100))
print(apply_priority_fee(250))

# Part 2 

def check_technician(tech_dict,tech):
    res = ""
    for key,value in tech_dict.items():
        if tech == key:
            if value >= 5:
                return"Busy"
            else:
                return "Avaliable"
 
    return "Not in System" 

staff = {"Alice" : 2, "Bob" : 5}
print(check_technician(staff,"Alice"))
print(check_technician(staff,"Charlie"))

# Part 3 
service_dict = {"Screen_repair" : 150, "Battery_Swap" : 80, "Data_recovery": 100}
service_list = ["Screen_repair","Battery_Swap"]

def get_service_cost(service_dict,service_name):
    for key,value in service_dict.items():
        if service_name == key:
            return value
    return None

def calculate_bundle_total(service_dict,service_list):
    total_cost = 0
    for x in service_list:
        total_cost += get_service_cost(service_dict,x)
    return total_cost

print(calculate_bundle_total(service_dict,service_list))          
        