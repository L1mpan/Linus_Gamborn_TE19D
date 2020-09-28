    # Uppgift 1 
#x = int(input("Skriv in ett tal"))
#if x > 0:
#    print(f"{x} är ett positivt tal")

#elif x < 0:
#    print(f"{x} är ett negativt tal")

#elif -1 < x < 1:
#    print(f"{x} är 0")

#x = 0
#print(f"x blev återställd till {x}")

#--------------------------------------------------------------

# Uppgift 2
#y = int(input("Skriv in ett tal"))
#if y % 2 == 0:
#    print("talet är jämnt")
#elif y % 3 == 0:
#    print("talet är udda")
#elif y % 5 == 0:
#    print("talet är delbart med 5")

#--------------------------------------------------------------

# Uppgift 3
#x = float(input("Skriv in ett tal"))
#y = float(input("Skriv in ett till tal"))
#if x > y:
#    print(f"{x} är större än {y}")
#elif x < y:
#    print(f"{x} är mindre än {y}")

#--------------------------------------------------------------

# Uppgift 4
r = float(input("Skriv längden för radien"))
if r < 0:
    print("Error! Radien kan inte ha en negativ längd")

else: 
    A = 3.14*r**2/2 
    print(f"Circelns area är {A} a.e.")