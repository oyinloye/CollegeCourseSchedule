"""
-------------------------CS 3364 Algorithms: Project2 -------------------------

Find the order of taking courses by applying Depth-First Search traversal and topological ordering algorithm.

By: Dapo Oyinloye - R11376119.
"""


a = []  #list to hold courseNames
b = []  #list to hold preReqs
newList = {} #dictionary structure to hold the courses as keys and subsequent courses(that depend on the keys) as values in a List
pre = 0  #declaring var for keeping preVisit and postVisit numbers
visited = {}    #dictionary to match cNames to True/False Boolean values
visitList = []  #a List to hold the cNames that have been traversed by DFS 
postList = {}   #dictionary to keep cNames and postVisit numbers


"""
Here we extract the courses and their pre-requisites from a text file.
"""
with open("courseschedule.txt", "r") as f:
  while True:
    lines = f.readline()  
    lines.strip()
    if not lines:
      break
    # Loop through all lines.
    
    # Add last element to list
    pos = lines.index('-')
    cName = lines[:pos-1]
    
    pos = lines.index('(')
    pos2 = lines.index(')')
    str2 = lines[pos + 1:pos2]
    
    list1 = str2.split(" and ")
   
    for i in list1:
      if ',' in i:
        value = i.split(', ')
        value.append(list1[-1])
        list1 = value.copy()
      else:
        continue

#since we are iterating line by line over the text file, we need to store the extracted values together.
#we save each extracted line to a list.

    a.append(cName) #storing all CourseNames in List:'a'
    b.append(list1) #storing all pReqs in List:'b'
      
        
#using the list:'a' that has all the extracted courseNames to 
#populate 'newList' dictionary in this manner; "courseName: [pReqs]"
for i in range(len(a)):
    newList[a[i]] = []
    
 

#A loop to create a list showing the classes that depend on each other
for x in range(len(a)):
    for y in b[x]:
        if y == 'N/A':
            pass
        else:
                       
            var = a[x]
            newList[y].insert(0, var)



print("a listing of classes showing the classes that depend on each other: ")
print()
print(newList)


"""
DFS Functions to traverse the courseNames and classes that depend on them.
"""
def explore(v, visited):
    global pre
    
    if v not in visitList:
        # Mark the current node as visited
        visited[v]= True
        visitList.append(v)
        pre = pre + 1   #count preVisit

    # Recursion for all the vertices adjacent to this vertex
    for value in newList[v]:
        for j in range(len(newList[v])):
            if visited[value] == False:
               
                explore(value, visited)
    
    pre = pre + 1       #count postVisit
    postList[v] = pre   #saving the postVisit value of each node to the postList


def DFS(graph):
    #first we mark all nodes(courseNames) as 'False' to indicate that the nodes have not been visited
    for i in newList:
        visited[i] = False
    
           
    #begin DFS traversal on all vertices
    for v in graph:
        if visited[v] == False:
            explore(v, visited)


#calling DFS function on newList
DFS(newList)
print()
print("Listing the nodes that the DFS algorithm visits and the post-visit number of that node:")
print()
print(postList)
print()

#sorting the postList in descending order of postVisit Numbers
sorted_by_post = sorted(postList.items(), key=lambda x:x[1], reverse=True)

#convert the sorted postList back to a dictionary structure.
converted_dict = dict(sorted_by_post)   

print()
#print(converted_dict)
print("Topological Order of Classes sorted in descending order of PostVisit numbers: ")
print()
for keys in converted_dict.keys():
    print(keys)
