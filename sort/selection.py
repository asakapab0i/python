#standard selection sort algorithm
def selection(list):
  length = len(list) - 1
  
  #perform the main loop
  #first num to start looping
  #second loop limit anything lesser than 0 will exit
  #the stride or the manner of looping in this case descending
  for x in range(length, 0, -1):
    #set maxNumber
    maxNumber = 0;
    #since we are comparing indices
    #we need another loop for compare it to the main loop
    #this time its ascending order
    #it will loop to the entire list just to find
    #the position of the maxNumber for 1 interation in the
    #main loop
    for y in range(0, x+1):
      #print y                                  #this for loop will iterate
      if list[y] > list[maxNumber]:     #len(list) number of times
        maxNumber = y             #before it will loop again to main loop

    #if iteration is done and the above loop determined the
    #position of the max number, then perform the hold and transfer
    #variable
    hold = list[x]
    list[x] = list[maxNumber]
    list[maxNumber] = hold
  print list

list = [2,5,2,6,7,8,9,3,2,35,65,6,6,7,1,4,7,8,9,2,4,65,76]

selection(list)
