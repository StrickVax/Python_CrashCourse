x = float(input("Enter number: "))

if x == 0:
    print("NIL")
elif x <= 5:
    print("Smaller than 6")
elif x <= 100:
    print("Not quite C")
else:
    print("Big.")

listo = [1, 2, 3, 4, 999]
for w in listo:
    print(w, end=' ')
