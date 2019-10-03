#exercise 9.2

fullfile = open('mbox.txt')
wds = 0

newlist = []
newlist2 = []
w=1
k = ('@')
j = ('.')
for linez in fullfile:
	if k and j in linez :
		linez=linez.rstrip()
		#print(linez)	
	
		wds = linez.split()
		#print(wds)
		
			
		newlist.append(wds)
			
#print(newlist)
  
# output list 
output = [] 
 # function used for removing nested lists in python. 
 
def reemovNestings(newlist): 
    for i in newlist: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
			
  
# Driver code 
#print ('The original list: ', newlist) 

reemovNestings(newlist) 

finallist = []

for i in output:
	if k not in i:
		continue
	if k in i:
		# print(i)
		finallist.append(i)
		
# print(finallist)


# print ('The list after removing nesting: ', output) 

di = dict()

for i in finallist:
	if i not in di:
		# print('Adding to dictionary')
		di[i] = 0
		di[i] = di[i] + 1
		
	else:
		di[i] = di[i] + 1
		
# print(di)

maximum = max(di, key=di.get)  # Just use 'min' instead of 'max' for minimum.
print(maximum, di[maximum])
# D 87

# KEY | VALUE
		