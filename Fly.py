import InsectClass as i

wings = int(input("How many wings does the insect have? "))
legs = int(input("How many legs does the insect have? "))
mosquito = i.Insect(2,4)
housefly = i.Insect(3,6)

mosquito.length_of_flight()
housefly.length_of_flight()
print('The mosquito can fly', mosquito.get_flight_length(), 'miles.')
print('The housefly can fly', housefly.get_flight_length(), 'miles.')
