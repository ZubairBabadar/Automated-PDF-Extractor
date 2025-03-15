from TextExtractorZ import nice 
from tableextractor import table 
from OCRz import eximg


while True:
    ask_user = int(input(f"\n1.Create Text File \n2.Create Table file \n3.Create Image file \n4.Create All \n5.Exit \nInput: "))
    
    if ask_user == 5:
        break
    else:
        user_path = input("\nEnter File Name:")
        user_path += ".pdf"
    
    if ask_user == 1:
            if nice(user_path):
                print(f"Text file of {user_path} Created")
            else:
                print(f"Failed to Create File")
    elif ask_user == 2:
            if table(user_path):
                print(f"CSV file of {user_path} Created")
            else:
                print(f"Failed to Create File")
    elif ask_user == 3:
            if eximg(user_path):
                print(f"Image file of {user_path} Created")
            else:
                print(f"Failed to Create File")

    elif ask_user ==4:
            if table(user_path):
                print(f"CSV file of {user_path} Created")
            else:
                print(f"Failed to Create File")
            if nice(user_path):
                print(f"Text file of {user_path} Created")
            else:
                print(f"Failed to Create File")
            if eximg(user_path):
                print(f"Image file of {user_path} Created")
            else:
                print(f"Failed to Create File")

    elif ask_user == 5:
            break

    else:
            print("Incorrect Input")


        

