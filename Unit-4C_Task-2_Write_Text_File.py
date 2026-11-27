filename = "2_task.txt"
text = "welcome to python programming"  # e.g. "Learning file handling in Python."
with open(filename,"w" ) as file:  # "w"
    file.write(text)
print("Data written to",filename )