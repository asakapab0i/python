#create a standard bubble sort algorithm

def bubble(mylist):
  print mylist
  length = len(mylist) - 1
  issorted = False
  while not issorted:
    issorted = True
    for x in range(0, length): 
      if mylist[x] > mylist[x + 1]:
        issorted = False
        #perform hold and replace method
        hold = mylist[x]
        mylist[x] = mylist[x + 1]
        mylist[x + 1] = hold
  
  print mylist


mylist = [9,8,7,4,3,2,1,1,6,8,9]



bubble(mylist)
