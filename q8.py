def introduce(name, age=None):
    if age is None:
        print("My name is", name + ". My age is secret.")
    else:
        print("My name is", name + ". I am", age, "years old.")

introduce("John", 20)
introduce("John")