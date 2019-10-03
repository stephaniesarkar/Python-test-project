#exercise 9.2

fullfile = open('mbox.txt')
wds = 0

newlist = []
newlist2 = []
w=1
for linez in fullfile:
	if linez.startswith('From') :
		linez=linez.rstrip()
	#	print(linez)	
	
		if len(linez) > 40 :
			wds = linez.split()
			#print(wds[2:3])
			
			newlist.append(wds[2:3])
			
print(newlist)
  
# output list 
output = [] 
 # function used for removing nested  
# lists in python.  
def reemovNestings(newlist): 
    for i in newlist: 
        if type(i) == list: 
            reemovNestings(i) 
        else: 
            output.append(i) 
  
# Driver code 
print ('The original list: ', newlist) 
reemovNestings(newlist) 
print ('The list after removing nesting: ', output) 

di = dict()

for i in output:
	if i not in di:
		#print('Adding to dictionary')
		di[i] = 0
		di[i] = di[i] + 1
		
	else:
		di[i] = di[i] + 1
print(di)
		