part_name = ["servo","lidar","motor","sensor","gyroscope","gearbox","regulator","controller"]
part_stock = [42,28,63,29,54,51,95,77]
part_cost = [38.79,245.30,52.99,21.45,132.88,310.60,27.14,89.53]

models = {
    "R1" : [4,6,5,4,0,2,2,7],
    "R2" : [7,0,4,4,0,6,5,5],
    "R3" : [3,6,2,7,7,4,4,4],
    "R4" : [1,6,3,6,4,5,2,7]
}

queue = [("R4",2),("R1",2),("R3",1),("R2",4),("R1",1),("R4",2),("R2",3)]
queue_combined = {"R1" : 3, "R2" : 7, "R3" : 1, "R4" : 4}
constructed = {"R1" : 0,"R2" : 0, "R3" : 0, "R4" : 0}
backorder = {}
total_revenue = 0
counter = 0

for item in queue:
    model_no = item[0]
    quantity = item[1]
    parts_required = models[model_no]
    for x in range(quantity):
        counter = 0
        for j,k in zip(parts_required,part_stock):
            if(k>=j):
                counter += 1 
        if counter == len(parts_required):       
            for l in range(len(part_stock)): 
                part_stock[l] = part_stock[l] - parts_required[l]
                total_revenue += parts_required[l]*part_cost[l]
            constructed[model_no] += 1
for key in constructed:
    backorder[key] = queue_combined[key] - constructed[key]

print("Constructed units")
for i,j in constructed.items():
    print(f"{i}: {j}")
print("")
print(f"Total revenue: ${total_revenue:.2f}")
print("")
print("Backorder")
for i,j in backorder.items():
    print(f"{i}: {j}")
print("")
print("Inventory")
for i,j in zip(part_name,part_stock):
    print(f"{i}: {j}")





