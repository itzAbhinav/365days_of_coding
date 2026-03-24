###############################
# Place your data model here. #
###############################
PRICE_CATALOG = {"servo": 38.79, "lidar": 245.30, "motor": 52.99, "sensor": 21.45, "gyroscope": 132.88, "gearbox": 310.60, "regulator": 27.14, "controller": 89.53}
MODELS = {
    "R1": [4, 6, 5, 4, 0, 2, 2, 7],
    "R2": [7, 0, 4, 4, 0, 6, 5, 5],
    "R3": [3, 6, 2, 7, 7, 4, 4, 4],
    "R4": [1, 6, 3, 6, 4, 5, 2, 7]
}
inventory = {"servo": 42, "lidar": 28, "motor": 63, "sensor": 29, "gyroscope": 54, "gearbox": 51, "regulator": 95, "controller": 77}

################################
# Place your API methods here. #
################################

def get_model_cost(model, catalog, models):
    arr = models[model]
    total = 0
    for i, j in zip(arr, catalog.values()):
        total += i * j
    return total


def can_build_one(model, inventory, models):
    arr = models[model]
    for i, j in zip(arr, inventory.values()):
        if j < i:
            return False
    return True


def build_one(model, inventory, catalog, models):
    # FIX: use can_build_one to check, return 0.0 if cannot build
    if not can_build_one(model, inventory, models):
        return 0.0

    arr = models[model]
    total = 0.0
    # FIX: iterate over inventory keys so we can modify inventory by key
    keys = list(inventory.keys())
    for i, key, cost in zip(arr, keys, catalog.values()):
        total += i * cost
        inventory[key] -= i
    return total


def process_order(model, count, inventory, catalog, models):
    subtotal = 0.0
    built = 0
    not_built = 0
    for _ in range(count):
        if can_build_one(model, inventory, models):
            built += 1
            subtotal += build_one(model, inventory, catalog, models)
        else:
            not_built += 1
    return (built, not_built, subtotal)


def apply_discount(total):
    # FIX: return the discount AMOUNT (not the discounted total) to match
    # the expected output: "Discount (dollars): $X", "Total: subtotal - X"
    if total > 1500.0:
        return total * 0.15
    elif total > 1000.0:
        return total * 0.10
    elif total > 300.0:
        return total * 0.05
    return 0.0


########################################
# Place your CLI code and methods here #
########################################

def show_models_and_costs():
    for model in MODELS:
        cost = get_model_cost(model, PRICE_CATALOG, MODELS)
        print(f"{model}: ${cost:.2f}")


def attempt_order():
    model_input = input("Please enter a model number: ")
    # Validate model
    if model_input not in MODELS:
        print("Invalid model.")
        return

    model_quantity = int(input(f"Please enter the number of {model_input} units you would like: "))
    # Validate quantity
    if model_quantity < 1:
        print("Quantity must be at least 1.")
        return

    print()
    print("Attempting to order models...")
    print()
    print(f"{model_input} order details.")

    # FIX: pass correct arguments (model_input, model_quantity, and global vars)
    result = process_order(model_input, model_quantity, inventory, PRICE_CATALOG, MODELS)
    built, on_backorder, subtotal = result

    print(f"Units built: {built}")
    print(f"Units on backorder: {on_backorder}")
    print()

    discount = apply_discount(subtotal)
    total = subtotal - discount
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount (dollars): ${discount:.2f}")
    print(f"Total: ${total:.2f}")


def show_inventory():
    print("Current inventory:")
    print()
    # FIX: iterate over inventory items, not range(inventory)
    for part, qty in inventory.items():
        print(f"{part}: {qty}")





while True:
    print("1) Show models and costs")
    print("2) Attempt order") 
    print("3) Show inventory")  
    print("0) Exit")
    print("")
    option = int(input("Please enter an integer between (0-3): "))

    # FIX: validate option range
    '''if option < 0 or option > 3:
        print("Please enter a number between 0 and 3.")
        continue
        '''

    print()

    match option:
        case 1:
            show_models_and_costs()
        case 2:
            attempt_order()
        case 3:
            show_inventory()
        case 0:
            break
        case _:
            print("Please enter a number between 0 and 3")
    print()