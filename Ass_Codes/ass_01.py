from msilib.schema import MsiAssembly
mass = float(input("Enter the mass of object(Kg):"))
velocity = float(input("Enter the velocity of object(m/s):"))

momentum = mass*velocity
print("----->Momentum is",momentum,"kgm/s")

energy = 0.5*mass*(velocity**2)
print("----->Energy is",energy,"Joule")