def main():
    celerity = 300000000
    mass = int(input("Please enter a mass in kg to convert to Joules: "))
    energy = mass * pow(celerity, 2)
    print(energy)

main ()