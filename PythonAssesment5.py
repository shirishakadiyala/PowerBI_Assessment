import csv
# initializing headers and data 
Headers=['Name','Age','Salary']
data=[
    {'Name':'Shiri','Age':'21','Salary':'45000'},
      {'Name':'Laxmi','Age':'45','Salary':'56000'},
      {'Name':'padma','Age':'48','Salary':'25000'}
]
# #creating and writing to a new csv file
with open('data.csv','w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=Headers)
    writer.writeheader()
    writer.writerows(data)

# #reading and printing the initial content  
print("initial content of data.csv:")
with open(r'data.csv','r') as f:
    print(f.read())

#appending content
new_data=[
    {'Name':'Hari','Age':'42','Salary':'80000'},
    {'Name':'Kiara','Age':'31','Salary':'90000'}
]
with open('data.csv','a',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=Headers)
    writer.writerows(new_data)
#reading  the entire content after appending 
print("content of data.csv after appending:")
with open('data.csv', 'r') as f:
    print(f.read())
