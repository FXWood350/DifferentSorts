list = [5, 4, 3, 2, 11,2,3,123,98,553466,6,-1,-2,-3,-5,69,70,-100,999,289394,-90]

SwapsDone = True
while SwapsDone == True:
  SwapsDone = False
  for x in range(0,len(list)-1):
    print(list)
    if list[x]>list[x+1]:
      Temp = list[x+1]
      list[x+1]=list[x]
      list[x]=Temp
      SwapsDone = True
  

print(list)


list = [5, 4, 3, 2, 11,2,3,98,553466,6,-1,-2,-3,-5,69,70,-100,999,289394,-90]

for x in range(0,len(list)-1):
  CurrentVal = list[x]
  Pos = x
  while (Pos > 0) and (list[Pos-1]>CurrentVal):
    print(list)
    list[Pos] = list[Pos-1]
    Pos = Pos-1
  list[Pos] = CurrentVal