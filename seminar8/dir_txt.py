def LoadDirectory():
    directory = []
    with open("seminar8\directory.txt", "r", encoding='utf-8') as file:
        dirStr = file.read()
        nodesStr = dirStr.split("\n\n")
        for nodeStr in nodesStr:
            node = nodeStr.split("\n")
            directory.append((node[0], node[1], node[2], node[3]))
    return directory

def SaveDirectory(directory):
    with open("seminar8\directory.txt", "w", encoding='utf-8') as file:
        for node in directory:
            file.write(directory[0] + "\n")
            file.write(directory[1] + "\n")
            file.write(directory[2] + "\n")
            file.write(directory[3] + "\n")
            file.write("\n")

  
