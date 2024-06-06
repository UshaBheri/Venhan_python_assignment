def writeFile():
    try:
        with open(r'C:\Users\DELL\Desktop\Venhan assignment\readFile.txt','w') as file:
            data = file.write('python')
            print(data)
    except IOError:
        print("Error occured while writing a file")
    
writeFile()

