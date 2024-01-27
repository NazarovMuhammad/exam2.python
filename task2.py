my_list = [] 
while True:
     a = input()
     my_list.append(a)
     if int(a) == 0:
         break
print(max(my_list))