import EC_Joe_Classes as c 

name = "John Doe"
address = "123 Main St. Waco TX 76706"
phone = "214-555-1112"
customer = c.Customer(name,address,phone)

make = "Honda"
model = "Accord LX"
year = "2016"
car = c.Car(make,model,year)

part_cost = 1210.50
labor_cost = 765.00
costs = c.ServiceQuote(part_cost,labor_cost)

print("Customer:",customer.get_name(), "    ","Address:",customer.get_address(),
      "    ","Phone:",customer.get_phone())
print("Car Make:",car.get_make(),"    ","Car Model:",car.get_model(),"    ","Car Year:",car.get_year())
print("Service Quote")
print("Parts:$",costs.get_parts_charges())
print("Labor:$",costs.get_labor_charges())
print("Sales Tax:$",costs.get_sales_tax())
print("Total Charges:$",costs.get_total_charges())