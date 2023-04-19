with open("file1.txt") as file1, open("file2.txt") as file2:
    same = True
    for i, (line1, line2) in enumerate(zip(file1, file2)):
        if line1 != line2:
            same = False
            print(f"Line {i+1}:")
            print(f"File 1: {line1.strip()}")
            print(f"File 2: {line2.strip()}")
            
    if same:
        print("The files are the same.")
    else:
        print("The files are different.")
