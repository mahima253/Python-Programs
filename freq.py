str1 = input("Enter a string")
   
dic = {} 
  
for n in str1: 
    dic[n] = dic.get(n, 0) + 1
  
  
print ("Count of all characters in GeeksforGeeks is : \n"
                                             +  str(dic)) 
