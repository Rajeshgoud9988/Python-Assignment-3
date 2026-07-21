try:
    with open("student.txt", "r") as file:
        print("All Content:")
        print(file.read())

    print("\nLine by Line:")
    with open("student.txt", "r") as file:
        count = 1
        for line in file:
            print(f"Line {count}: {line.strip()}")
            count += 1

except Exception as e:
    print("Error:", e)