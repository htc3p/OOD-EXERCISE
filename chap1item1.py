print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = map(float, input("Enter Input : ").split())

fly_time = d / (Vt - Vr)
fly_distance = fly_time*Vf

print("{:.2f}".format(fly_distance))