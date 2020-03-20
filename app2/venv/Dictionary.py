# Converting into integer
# monthly_income=input("Entre your monthly income")
# income_As=int(monthly_income)
# income_As+=100
# print(income_As)

# a=input("Enter number: ")
# # b=float(a)
# # b+=1.51
# # print(b)

# Dictonary practice
# customer_12={"Fname":"Muhammd","Lname":"Siraj","Id":"61917"}
# print(customer_12["Id"])
# print(customer_12["Fname"])
# print(customer_12["Lname"])
#
# ranking={0:"a",9:"c",8:"d"}
# print(ranking[9])
# print(ranking["d"])

# things_to_remember = {
#     0: "the lowest number",
#  "a dozen": 12,
#  "snake eyes": "a pair of ones",
# 13: "a baker's dozen",
#  }
# print(things_to_remember["a dozen"])

# Adding item in dictionarycustomer_29876["city"] = "Toronto"
# # print(customer_29876["city"])
# # # del customer_29876["last name"]
# # # print(customer_29876["last name"])  #Error show that lnmae is not available
# # customer_29876["city"] = "Karachi"
# # print(customer_29876["city"])
customer_29876 = {
"first name": "David",
"last name": "Elliott",
"address": "4803 Wellesley St."
}

# for each_value in customer_29876.values():
#     print(each_value)
# for each_key in customer_29876.keys():
#      print(each_key)
#
# for each_key in customer_29876.keys():
#  print(each_key)

# for each_key,each_value in customer_29876.items():
#     print("The Customers "+ each_key+" is "+ each_value)

customers=[
{
"customer id": 0,
"first name":"John",
"last name": "Ogden",
"address": "301 Arbor Rd.",
},
{
 "customer id": 1,
 "first name":"Ann",
 "last name": "Sattermyer",
 "address": "PO Box 1145",
},
{
 "customer id": 2,
 "first name":"Jill",
 "last name": "Somers",
 "address": "3 Main St.",
}
]
dictionary_to_look=customers[0]
name=dictionary_to_look["first name"]
print(name)