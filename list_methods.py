# List methods
numbers = [2, 67, 19, 2, 23, 4, 5, 7, 6, 5, 19, 5, 20]


print(f"\nOriginal List: {numbers}", end='')
print(f"\t and is of length: {len(numbers)}\n")


# Remove duplicates from a list
def unique(numb):
    uniques = []
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
    print(f"Return unique values from the list above: {uniques}")
unique(numbers)


#Return the maximum in a list
def find_maximum(numb): 
    maximum = numb[0]
    for number in numb:
        if number > maximum:
            maximum = number
    return maximum

maxi = find_maximum(numbers)
print(f"Return maximum value from the list above: {maxi}\n")




