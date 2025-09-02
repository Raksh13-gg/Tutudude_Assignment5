# taking inputs
stue_name_marks = {'Alice': 85,'Mein': 56,'Sheil':72 }
name = input("Enter student name: ")
marks = (stue_name_marks.get(name))
if marks is not None:
    print("{}'s marks : {}".format(name,marks))
else:
    print("student not found")





    


