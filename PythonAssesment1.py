inventory=[ ["Strawberry","Fruit",3.50,40,10],
            ["Broccoli","Vegetable",2.20,25,8],
            ["Cheddar","Dairy",5.00,18,4],
            ["Baguette","Bakery",2.80,18,4],
            ["Blueberry","Fruit",4.00,22,6],
            ["Spinach","Vegetable",1.80,30,12],
            ["Yogurt","Diary",1.20,50,15],
            ["Crosisaant","Bakery",3.00,28,3],
            ]

#calculate the TotalRevenue
total_revenue=0
for item in inventory:
    total_revenue+=item[2]*item[3]
    
print(total_revenue)

#List Low stock item if stock is less than 5
low_stock=[]
for item in inventory:
    if item[4]<5:
        low_stock.append(item[0])

print(low_stock)

#calculte the categorywise Revenue
category_reve={}
for item in inventory:
    category=item[0]
    revenue=item[2]*item[3]
    if category not in category_reve:
        category_reve[category]=0
        category_reve[category]+=revenue
        
for category in category_reve:
    print(f'{category}:{round(category_reve[category])},{2}')
    
