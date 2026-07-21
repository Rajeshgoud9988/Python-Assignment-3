try:
    with open("student.txt", "x") as file:
        file.write("Python is easy to learn.\n")
        file.write("File handling is important.\n")
        file.write("Practice makes perfect.\n")
    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

except Exception as e:
    print("Error:", e)