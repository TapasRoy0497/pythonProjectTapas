# List - List of elements with any datatype
# List is mutable, we can change/update
l = [1, 2, 3, 4, 5]

# 1.Add item
# 2.Remove item
# 3.Update item
# 4.Fetch item

shopping_cart = ["Milk", "Bread", "Wine"]
print(shopping_cart)
shopping_cart.append("Meat")  # Add item to the list
shopping_cart.insert(0, "Sugar")  # Add item to the list at a specific index
shopping_cart.extend(["Fruits", "Vegetables"])  # Add multiple items to the list
print(shopping_cart)
print(len(shopping_cart))
print(shopping_cart[3])

print(type(shopping_cart))