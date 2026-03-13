product_name = ["motor","sensor","frame","cpu"]
product_price = [49.99,15.75,120.00,85.50]
print("-----------------------")
print("Product Name | Price")
print("-----------------------")
for i,j in zip(product_name,product_price):
    print(f"{i:<12}| ${j:.2f}")
print("")
print("Welcome to the RoboWorks Quote Calculator.")
print("")
print("For each product below, please specify your required quantity.")
print("")
motor = int(input("motor: "))
sensor = int(input("sensor: "))
frame = int(input("frame: "))
cpu = int(input("cpu: "))
print("")
print("Please see your quote below.")
print("")
motor_val=motor*product_price[0]
sensor_val=sensor*product_price[1]
frame_val=frame*product_price[2]
cpu_val=cpu*product_price[3]
print(f"motor: {motor} x ${product_price[0]} = ${motor_val:.2f}")
print(f"sensor: {sensor} x ${product_price[1]} = ${sensor_val:.2f}")
print(f"frame: {frame} x ${product_price[2]} = ${frame_val:.2f}")
print(f"cpu: {cpu} x ${product_price[3]} = ${cpu_val:.2f}")
print("")
subtotal = motor_val + sensor_val + frame_val + cpu_val
Discount = 0
if(subtotal > 1500.00):
    Discount = (15/100)*subtotal
        
elif(subtotal > 1000.00):
    Discount = (10/100)*subtotal
        
elif(subtotal > 300.00):
    Discount = (5/100)*subtotal
else:
    pass
Total = subtotal - Discount
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${Discount:.2f}")
print(f"Total: ${Total:.2f}")    


