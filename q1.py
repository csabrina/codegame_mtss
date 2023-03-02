text=input()
lista=[]
a = ""

for i in text:
  lista.append(i)
  
for x in range(len(lista)):
  if lista[x]=="o" and lista[x-1]=="O":
    a = "YES"

  elif lista[x]=="O" and lista[x-1]=="o":
    a = "YES"


if a != "YES":
  print("NO")  
else:
  print(a)


