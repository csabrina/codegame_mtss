n=input().split(".")
count=0

for i in range(4):
  count+=int(n[i])

if count%8==0:
  print("BLOCK")
else:
  print("PASS")
