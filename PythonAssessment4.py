class departments:
    dept_count=0
    def __init__(self,id,name,location,head_of_dept):
        self.id=id
        self.name=name
        self.location=location
        self.head_of_dept=head_of_dept
        departments.dept_count+=1
    
    
    def display_department_details(self):
        print(f"Details of the {i+1} department") 
        print("----------------")
        print("Department details:")
        print("-----------------")
        print(f"DEPT ID:{self.id}")
        print(f"DEPT NAME:{self.name}")
        print(f"DEPT LOCATION:{self.location}")
        print(f"DEPT HEAD:{self.head_of_dept}")
        
    @classmethod
    def get_noof_dept(cls):
        return cls.dept_count
    
#inputs from user
dept_c=int(input("Enter no of departments") )
departments_list=[]
for i in range(dept_c): 
    dept_id=input('Enter department ID ')
    dept_name=input('Enter departemnt Name')
    dept_location=input('Enter department Location')
    dept_head=input('Enter head of the department') 
    dept=departments(dept_id,dept_name,dept_location,dept_head)
    departments_list.append(dept)
    
for dept in departments_list:
    dept.display_department_details()
print(f"Total departments:{departments.get_noof_dept()}")


#search department by depatment no if it present print details of department  
search_id = input("\nEnter department ID to search: ")
found = False

for dept in departments_list:
    if dept.id == search_id:
        print("\nDepartment name found!")
        dept.display_department_details()
        found = True
        break

if not found:
    print("Department name not found.")
  
#search department by depatment name if it present print details of department  
search_name=input("\nEnter department name to search: ")
found = False
for dept in departments_list:
    if dept.name.lower() == search_name:
        print("\nDepartment name found!")
        dept.display_department_details()
        found = True
        break

if not found:
    print("Department name not found.")

    
  
  
      