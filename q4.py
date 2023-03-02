n=int(input())
lista=[]
a = ""

for i in range(n):
  text=input()
  lista.append(text)

for x in lista:
  for j in range(len(x)):
    if x[j] == "B":
      a="YES"

if a != "YES":
  print("NO")  
else:
  print(a)



