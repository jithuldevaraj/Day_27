def make_pizza(size, crust_type, *toppings, **delivery_info): # topping = (tuple), delivery_infor = {dict}
    print(f"--- Order Summary ---")
    print(f"Size: {size}")
    print(f"Crust: {crust_type}")

    print("\nToppings:")
    for topping in toppings:
        print(f"- {topping}")

    print("\nDelivery Details:")
    for key, value in delivery_info.items():
        print(f"{key}: {value}")


# Calling the function
make_pizza(
    "Large",  # Standard pos argument (size)
    "Thin",  # Standard pos argument (crust_type)
    "Pepperoni",  # *args
    "Mushrooms",  # *args
    "Extra Cheese",  # *args
    name="John Doe",  # **kwargs
    address="123 Main St",  # **kwargs
    tip=5  # **kwargs
)