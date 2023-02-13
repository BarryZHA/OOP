import FliesClass as FC 

mosquito = FC.Flies()
housefly = FC.Flies()


housefly = FC.flight_length()
mosquito = FC.flight_length()
print(f"the {mosquito.getname()} can fly: ", housefly.getmiles(), " miles")
print(f"the {housefly.getname()} can fly: ", mosquito.getmiles(), " miles")




