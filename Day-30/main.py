try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError:
    print("something is wrong")

