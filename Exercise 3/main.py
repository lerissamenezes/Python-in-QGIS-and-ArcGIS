#importing the package easy_shopping
from easy_shopping import Calculator,Shopping
print()

c=Calculator()
print("Addition: ",c.add(4,5))
print("Subtraction: ",c.sub(34,21))
print("Multiplication: ",c.mul(54,2))
print("Division: ",c.div(144,2))
print("Division: ",c.div(45,0))

print()
s=Shopping()
s.add_item("Trouser",1)
s.add_item("Shirt",3)
s.add_item("Cap",10)
s.show_cart()
s.rem_item("Tee",1)
s.rem_item("Shirt",1)
s.rem_item("Cap",5)

print("Updated Cart")
s.show_cart()
print()