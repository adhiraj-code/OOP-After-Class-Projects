class BMW:
    
    def fuel_type(self):
        print("BMW Fuel Type is Premium Gas")
    
    def max_speed(self):
        print("BMW Max Speed is 200")

class Ferrari:
    
    def fuel_type(self):
        print("Ferrari Fuel Type is Petrol")
    
    def max_speed(self):
        print("Ferrari Max Speed is 250")

obj_bmw = BMW()

obj_ferrari = Ferrari()

for car in (obj_bmw, obj_ferrari):
    car.fuel_type()
    car.max_speed()