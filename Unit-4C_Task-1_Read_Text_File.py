filename = "sample.txt"
with open(filename,"r" ) as file:  # "r"
    content = file.read()
print(content)