# Loops in pyruits = ["Bananthon
fruits = ["Banana", "Apple", "Orange", "Mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print(f"{fruits[0]}, this is using print")
print(f"{fruits[1]}, this is using print")
print(f"{fruits[2]}, this is using print")
print(f"{fruits[3]}, this is using print")

fruits = ["Banana", "Apple", "Orange", "Mango", "Kiwi"]

# for fruits in fruits:
#   print(f"{fruit}, this is using loop")

for x in range(0, 11, 2):
    print(x)


for fruit in fruits:
    print(f"{fruit}), this is using loop")

fruits



    # Break statement
for x in range(11):
        if x == 5:
            break
        print(x)

for x in range(1,11):
    print(x)
    if x == 5:
            break
    
for x in range(1,11):
    if x == 5:
        continue
    print(x)

for i in range (1, 11):
     print(i)
     if i ==5:
          break
     
     num = [0,1,2,3,4,5,6,7,8,9,10]
     for x in range(1,11):
        print(x)
     else:
        print("Finished the looping successfully!!!")
