filename = 'new.txt'
with open(filename,'w') as f:
    items= { "Mango", "Apple","Bread","Milk"}
    for item in items:
        f.write(item + "\n " )

    
 

