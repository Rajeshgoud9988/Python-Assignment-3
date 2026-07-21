try:
    with open("student.txt", "r") as file:
        text = file.read()
        words = text.split()
        print("Total words:", len(words))

except Exception as e:
    print("Error:", e)