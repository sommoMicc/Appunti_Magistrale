data = [0,1,2,3,4,5,6,7,8,9]
length = len(data)

for i in range(1,4) :
    for j in range(0,length):
        data.append(j+10*i)

print(data)        
print(data[-20:]);