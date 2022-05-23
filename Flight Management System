import sys
import cx_Oracle
db = cx_Oracle.connect('system/prince@localhost:1521/xe')
conn = db.cursor()
table=input("Do you want the table to be created at your database (yes/no): ")
table=table.lower()
if(table=='yes'):
 conn.execute('CREATE TABLE FLIGHT(REG_NO number PRIMARY KEY NOT NULL, NAME 
VARCHAR2(10) NOT NULL, FATHER_NAME VARCHAR2(15) NOT NULL, MOBILE_NO 
VARCHAR2(13) NOT NULL, STATUS VARCHAR2(10) NOT NULL)') 
 conn.execute('CREATE TABLE FLIGHT1(REG_NO number PRIMARY KEY NOT NULL,FLIGHT_NO 
number NOT NULL, BOARDING VARCHAR2(10) NOT NULL, DESTINATION VARCHAR2(10) NOT 
NULL, FOREIGN KEY (REG_NO) REFERENCES FLIGHT(REG_NO))')
 print("Table created at Database version:",db.version)
elif(table=='no'):
 exit
else:
 print("Invalid Input")
def Input():
 reg_no=int(input("ENTER THE REGISTRATION NO : "))
 name=input("ENTER THE NAME : ")
 f_name=input("ENTER THE FATHER NAME : ")
 a=input("ENTER THE MOBILE NO :")
 if len(a)==10:
 exit
 else:
 print("renter")
 a = input("ENTER THE MOBILE NO :")
 flight_no=int(input("ENTER THE FLIGHT NO :"))
 boarding=input("ENTER THE BOARDING :")
 destination=input("ENTER THE DESTINATION :")
 status=input("ENTER THE STATUS :")
 data1=[reg_no, name,f_name ,a, status]
 data2=[reg_no, flight_no, boarding, destination]
 conn.execute("insert into FLIGHT (reg_no,name,father_name,mobile_no,status) 
values(:1,:2,:3,:4,:5)", data1)
 conn.execute("insert into FLIGHT1 (reg_no,FLIGHT_no,boarding,destination) values 
(:1,:2,:3,:4)", data2)
 db.commit()
 print("data entered succrssfully")
 
def update():
 up_data = int(input("enter the reg_no which you want to update : "))
 print("01. To update name : ")
 print("02. To update father name : ")
 print("03. To update mobile_no : ")
 print("04. To update flight_no : ")
 print("05. To update boarding : ")
 print("06. To update destination :")
 print("07. To update status : ")
 choice = int(input("enter your choice : "))
 if (choice == 1):
 up_name = input("enter the new name :")
 reqd=[up_name,up_data]
 statement2 = "UPDATE FLIGHT SET name=(:1) where REG_NO=(:2)"
 conn.execute(statement2, reqd)
 db.commit()
 print("update successfuly")
 elif(choice==2):
 up_f_name = input("enter the new father name :")
 reqd=[up_f_name,up_data]
 statement2 = "UPDATE FLIGHT SET father_name=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 elif (choice == 3):
 a = input("Enter the new mobile no : ")
 reqd=[a,up_data]
 if len(a) == 10:
 statement2 = "UPDATE FLIGHT SET mobile_no=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 else:
 print("renter")
 a = input("ENTER THE MOBILE NO : ")
 statement2 = "UPDATE FLIGHT SET mobile_no=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 elif (choice == 4):
 up_fno = input("enter the new flight_no : ")
 reqd=[up_fno,up_data]
 statement2 = "UPDATE FLIGHT1 SET flight_no=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 elif (choice == 5):
 up_boarding = input("enter the new BOARDING : ")
 reqd=[up_boarding,up_data]
 statement2 = "UPDATE FLIGHT1 SET boarding=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 elif (choice == 6):
 up_ds = input("enter the new destination : ")
 reqd=[up_ds,up_data]
 statement2 = "UPDATE FLIGHT1 SET destination=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 elif (choice == 7):
 up_status = input("enter the new status : ")
 reqd=[up_status,up_data]
 statement2 = "UPDATE FLIGHT SET status=:1 where REG_NO=:2"
 conn.execute(statement2,reqd)
 db.commit()
 print("update successfuly")
 else:
 print("please enter valid choice")
 db.commit()
def delete():
 del_id = int(input("enter the reg_no which you want to delete :"))
 reqd=[del_id]
 sql="select * from FLIGHT"
 conn.execute(sql)
 check=conn.fetchall()
 print(check)
 sql1 = "delete from FLIGHT1 where REG_NO=:1"
 conn.execute(sql1,reqd)
 sql2 = "delete from FLIGHT where REG_NO=:1"
 conn.execute(sql2
 ,reqd)
 print("delete successfully")
 print("data doesnot exist")
 db.commit()
 
def show():
 text=int(input("ENTER THE REGISTRATION NO : "))
 reqd=[text]
 statement3 = "SELECT * FROM FLIGHT where REG_NO=:1"
 conn.execute(statement3,reqd)
 a=conn.fetchall()
 for row in a:
 print("reg no is :",row[0])
 print("Name is :", row[1])
 print("Father name is :", row[2])
 print("Phone number is :", row[3])
 print("status is:",row[4])
 statement6 = "SELECT * FROM FLIGHT1 where REG_NO=:1"
 conn.execute(statement6,reqd)
 b = conn.fetchall()
 for row1 in b:
 print("flight no is : ", row1[1])
 print("boarding at : ", row1[2])
 print("destination is : ", row1[3])
 db.commit()
def login():
 a=input("ENTER THE USERNAME :")
 if(a=="ACET"):
 print()
 b=input("ENTER THE PASSWORD :")
 if(b=="RDBMS"):
 print("LOGIN SUCCESSFUL")
 ad()
 else:
 print("*ENTER THE VALID PASSWORD*")
 else:
 print("*ENTER THE VALID USERNAME*")
def ad():
 ch='y'
 while(ch=='y'):
 print("\t01. TO INPUT NEW DATA")
 print("\t02. TO UPDATE DATA")
 print("\t03. TO DELETE DATA")
 print("\t04. FOR MAIN MENU")
 print("\t05. TO EXIT")
 choice = int(input("\t\tENTER YOUR CHOICE :"))
 if (choice == 1):
 Input()
 elif (choice == 2):
 update()
 elif (choice == 3):
 delete()
 elif(choice==4):
 main()
 elif(choice==5):
 sys.exit("thank you")
 else:
 print("\t\tPLEASE ENTER THE VALID CHOICE")
 ch=input("if want to continue press (y/n)")
def user():
 show()
def queries():
 import Queries.py
 main()
def joins():
 import Joins.py
 main()
def procedure():
 import Cursr_prcdrExcptn.py
 main()
 
def main():
 ch='y'
 while(ch=='y'):
 print('\n'"\t01. FOR ADMIN MODE")
 print("\t02. FOR USER MODE")
 print("\t03. FOR SQL QUERIES")
 print("\t04. FOR JOINS")
 print("\t05. FOR PROCEDURE")
 print("\t06. EXIT")
 ind=int(input("\t\tENTER YOUR CHOICE :"))
 if(ind == 1):
 login()
 elif(ind == 2):
 user()
 elif(ind == 3):
 queries()
 elif(ind==4):
 joins()
 elif(ind==5):
 procedure()
 elif(ind==6):
 sys.exit("thank you")
 ch=input("if you want to continue PRESS (y/n)")
main()
