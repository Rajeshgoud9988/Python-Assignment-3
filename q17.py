numbers = [7, 4, 0, -2, 3]

print("List:", numbers)

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])

except IndexError:
    print("IndexError: Invalid index.")

except Exception as e:
    print("Error:", e)