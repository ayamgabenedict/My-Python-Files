#File Handling

with open("sample.txt", "w") as f:
    f.write("Sample text\n" * 7)

    #Draw "F" using List and Iteration
    li = [5, 2, 5, 2, 2]
    f.write("\n")
    for each_item in li:
        f.write("#" * each_item)
        f.write("\n")


#To read the contents of the "sample.txt"
with open("sample.txt", "r") as f:
    for each_line in f.readlines():
        print(each_line, end="")

    


    

