# Method 1

# def cleanFiles(currentMem, exMem):
#     with open(currentMem, 'r+') as f_current:
#         whole_list = []
#         for line in f_current:
#             whole_list.append(line)
#         # print(whole_list)
    
#     list_no_active = []
#     list_active = []
    
#     for row in whole_list:
#         if 'Membership No' in row:
#             header = row
    
#         elif 'no' in row:
#             list_no_active.append(row)
        
#         elif 'yes' in row:
#             list_active.append(row)
    
#     # print(header)
#     # print('list_no_active is:', list_no_active)
#     # print('list_active is:', list_active)

#     with open(exMem, 'a+') as f_noactive:
#         for row in list_no_active:
#             f_noactive.write(row)
    
#     with open(currentMem, 'w') as f_active:
#         f_active.write(header)
#         for row in list_active:
#             f_active.write(row)

# cleanFiles('members.txt', 'inactive.txt')

# memReg = 'members.txt'
# exReg = 'inactive.txt'

# headers = "Membership No  Date Joined  Active  \n"
# with open(memReg,'r') as readFile:
#     print("Active Members: \n\n")
#     print(readFile.read())
    
# with open(exReg,'r') as readFile:
#     print("Inactive Members: \n\n")
#     print(readFile.read())

# Method 2

def cleanFiles(currentMem, exMem):
    with open(currentMem, 'r+') as f_active:
        with open(exMem, 'a+') as f_noactive:
            whole_list = []
            for line in f_active:
                whole_list.append(line)
            # print(whole_list)
        
            list_no_active = []
            list_active = []
            
            for row in whole_list:
                if 'Membership No' in row:
                    header = row
            
                elif 'no' in row:
                    list_no_active.append(row)
                
                elif 'yes' in row:
                    list_active.append(row)
        
            print(header)
            print('list_no_active is:', list_no_active)
            print('list_active is:', list_active)

            for row in list_no_active:
                f_noactive.write(row)

            f_active.seek(0)
            f_active.write(header)
            for row in list_active:
                f_active.write(row)
            f_active.truncate()

cleanFiles('members.txt', 'inactive.txt')

memReg = 'members.txt'
exReg = 'inactive.txt'

headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())