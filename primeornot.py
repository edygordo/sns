x = int(input('Enter a number'))
Prime_List = [True for i in range(x+1)]

for i in range(2,x+1):
    for k in range(2*i,x+1,i):
        Prime_List[k] = False

print(f'Number {x} is Prime:- {Prime_List[x]}')