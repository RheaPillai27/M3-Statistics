import csv
with open ('Height-Weight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]   
for i in range (len(file_data)):
     n_num = file_data[i][1]
     new_data.append(float(n_num))  

#writing the formula for median 
n=len(new_data) 
new_data.sort()

#using float division to get the nearest whole no
if n % 2 == 0:
     # getting the first num
     median1=float(new_data [n//2])

     # getting the second  num
     median2=float(new_data [n//2-1])

     #getting meadian of two num
     median=(median1+median2)/2
else : 
    median=new_data[n/2] 

print("Median is:"+str(median))        

