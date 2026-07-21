def find_max(a, b, c):
    return max(a, b, c)

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    print(find_max(x, y, z))

main()