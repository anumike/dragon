import copy
class machine:
    pass

machine_1=machine
machine_1.wheels=4
machine_2=machine_1
machine_2.wheels=3
print(machine_1.wheels)
machine_3= copy.copy(machine_1)
machine_3.wheels=6
print(machine_1.wheels)