entries = int(input())
characters = {}
for i in range(entries):
    hold = input()
    hold = hold.split(" ")
    characters[hold[0]] = hold[1]

decode = input()

def search(coded):
    for i in range(len(coded)):
        for key, value in characters.items():
            if coded[:i+1] == value:
                return str(coded[i+1:] + " " + key)
    return False
finished = ''
while decode != 0:
    control = search(decode)
    if control != False:
        control = control.split(" ")
        decode = control[0]
        finished = finished + control[1]
    else:
        break
print(finished)

