try:
    with open("student.txt", "a") as file:
        file.write("Python file handling becomes simple with practice.\n")

    print("Line added successfully.")

except Exception as e:
    print("Error:", e)