def read_file():
    try:
        with open(r'C:\Users\DELL\Desktop\Venhan assignment\read.txt','r') as file:
            data = file.read()
            print(data)

    except FileNotFoundError:
        print("File not found")

read_file()


