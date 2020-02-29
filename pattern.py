print("pattern printing")
num =int(input("enter num how many rows u want :"))
print("enter 1 or 0")
bool_val = input("1 for true or 0 for false :")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*int(i))
if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*int(i))        