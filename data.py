def backup(answer) :
    if answer == 'Yes' or answer == 'Y' or answer == 'y' :
        return True
    return False

def is_Data_Central_to_Business(response) :
    if response == "Yes" :
        print("Data is central to back up and...")
        if backup(response) :
            print("Data backed up")
        else :
            print("Data Not backed up")
        return True
    else :
        print("Data is not central to back up and...")
        return False

print(is_Data_Central_to_Business('Yes'))

# if is_Data_Central_to_Business('Yes') :
#     if backup("y") :
#         print("abc")
#     else :
#         print("def")
# else :
#     print("Im not okay")
