from PC_Function import *
def store():
    with open("pc_list.txt", "w") as file:
        file.write("PC Number\tOS\tStatus\n")
        for pc in pc_list:
            file.write(f"{pc.number}\t\t{pc.os}\t{pc.status}\n")