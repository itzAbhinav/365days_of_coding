PRICE_CATALOG = {
    "servo": 38.79,
    "lidar": 245.30,
    "motor": 52.99,
    "sensor": 21.45,
    "gyroscope": 132.88,
    "gearbox": 310.60,
    "regulator": 27.14,
    "controller": 89.53
}

MODELS = {
    "R1": [4,6,5,4,0,2,2,7],
    "R2": [7,0,4,4,0,6,5,5],
    "R3": [3,6,2,7,7,4,4,4],
    "R4": [1,6,3,6,4,5,2,7]
}

inventory = {
    "servo": 42,
    "lidar": 28,
    "motor": 63,
    "sensor": 29,
    "gyroscope": 54,
    "gearbox": 51,
    "regulator": 95,
    "controller": 77
}

cost = {}

for model_name, model_req in MODELS.items():

    counter = 0

    # check if enough inventory
    for req, inv in zip(model_req, inventory.values()):
        if inv >= req:
            counter += 1

    # if inventory is enough
    if counter == len(model_req):

        total_cost = 0

        for req, (part, price), (inv_part, inv_val) in zip(model_req,PRICE_CATALOG.items(),inventory.items()):
            total_cost += req * price
            inventory[inv_part] -= req

        cost[model_name] = total_cost


for key, value in cost.items():
    print(f"{key}: ${value:.2f}")