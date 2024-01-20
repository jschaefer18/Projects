list = []
val = -1
biggest_positive_val = 0
biggest_negative_val = 0
num_of_inputs = 0
total = 0
print("Enter a list of numbers, type 0 when finished.")
while val != 0:
    val = int(input("Enter a number: "))
    if val != 0:
        list.append(val)
        total = total + val
        num_of_inputs = num_of_inputs + 1
        if val > 0:
            if val > biggest_positive_val:
                biggest_positive_val = val
        if val < 0:
            if val < biggest_negative_val:
                biggest_negative_val = val
list.sort()        
print(list)
print(f"The sum of the nums is {total}")
print(f"The average of the nums is {total/num_of_inputs}")
print(f"The biggest positive value is {biggest_positive_val}")
print(f"The biggest negative value is {biggest_negative_val}")
print("Sorted list is: ")
for i in list:
    print(f"{i}")
