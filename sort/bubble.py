#standard bubble sort algorithm

def bubble(list):
  print list #print the list before the whole operation
  issorted = False #set the issort to false to we can use it in our while loop
  length = len(list) - 1 #get the total array content
  while not issorted: #evaluate the issort
    issorted = True #assume issorted to true before the whole eval
    for x in range(0, length): #actual checking of each array
      if list[x] > list[x + 1]: #if list with index x is greater than list with index x+1
        issorted = False #sort will be false because if
        #list x is greater that list with x+1 it means it is unsorted
        hold = list[x] #typical hold and replace method
        list[x] = list[x + 1]
        list[x + 1] = hold
  #after the whole loop check if the list is properly sorted
  print list

  #test cases
list = [9,5,6,7,8,2,3,5,7,10,29,99,100,32,23,2,8,2,1,3];



bubble(list)
