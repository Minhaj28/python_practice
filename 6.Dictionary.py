d1 = {"minhaj":"3","robi":"5","minhaj":"4","sakib":{"cn":"98","hci":"87"}}
# print(d1["sakib"])
# print(d1["sakib"]["cn"])
# del d1["robi"]
# print(d1)

name = input("Enter the name: ")
if name in d1:
    print(d1[name])
else:
    print("Not found")
