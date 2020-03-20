# class MyRouter(object):
#     def _init_(self,routername,model,serialno,ios):
#         self.routername=routername
#         self.model=model
#         self.serialno=serialno
#         self.ios=ios
#
#         def printRouter(self,manuf_date):
#             print("The router name is : "+self.routername)
#             print("The router model is : "+self.model)
#             print("The router serialno is : "+serialno)
#             print("The router ios is : "+ self.ios)
#             print("The model and date combimed is: "+self.model+self.manuf_date)
#
# router1=MyRouter('R1', '2600', '123456', '12.4')
class Point:
     def move(self):
         print("move")

point1=Point()
# point1.move()
point1.x=10
print(point1.x)