import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="toor",database="stude")
mycursor=mydb.cursor()

def insert():
  try:
    roll_no=int(input("Enter the roll no of the student "))
    name=input("enter the Name of the student ")
    clas=int(input("enter the class of the student "))
    sec=input("enter the section of the student ")
    hobby=input(" enter student's hobby ")
    sql="insert into info values(%s,%s,%s,%s,%s)"
    f=(roll_no,name,clas,sec,hobby)
    mycursor.execute(sql,f)
    mydb.commit()
    print("____**Data Entered Successfully**____")
  except Exception:
    print("It feels like you have entered wrong value or using the rollno twice ")

def search():
  try:
    a=input("name of the student you want to search ")
    

    sql=" select * from info where name=%s"
    f=(a,)
    mycursor.execute(sql,f)
    print("******If No Value Displays It Means No Data Found*****")
    for i in mycursor:
      print("Rollno,Name,Class,Section,Hobby")
      print(i)
  except Exception:
    print("not found") 

def update():
  try:
    print("select the option you want to update"
    "\n1.Name "
    "\n2.class"
    "\n3.section"
    "\n4.Hobby"
    "\n5.return")
    b=int(input("Enter your option "))
    if b==1:
      roll_no=input("enter the rollno of the you want to update ")
      name=input("Enter the correct name ")
      sql="update info set name=%s where Roll_no=%s"
      d=(name,roll_no)
      mycursor.execute(sql,d)
      mydb.commit()
      sho="select * from info where Roll_no="+str(roll_no)
      mycursor.execute(sho)
      print("***If No values display it means wrong rollno***")
      for i in mycursor:
        print("*****Your update sucess full*****")
        print(i)
    elif b==2:
      roll_no=input("enter the rollno of the you want to update ")
      clas=input("Enter the correct class ")
      sql="update info set class=%s where Roll_no=%s"
      d=(clas,roll_no)
      mycursor.execute(sql,d)
      mydb.commit()
      sho="select * from info where Roll_no="+str(roll_no)
      mycursor.execute(sho)
      print("***If No values display it means wrong rollno***")
      for i in mycursor:
        print("*****Your update sucess full*****")
        print(i)
    elif b==3:
      roll_no=input("enter the rollno of the you want to update ")
      section=input("Enter the correct section ")
      sql="update info set section=%s where Roll_no=%s"
      d=(section,roll_no)
      mycursor.execute(sql,d)
      mydb.commit()
      sho="select * from info where Roll_no="+str(roll_no)
      mycursor.execute(sho)
      print("***If No values display it means wrong rollno***")
      for i in mycursor:
        print("*****Your update sucess full*****")
        print(i)
    elif b==4:
      roll_no=input("enter the rollno of the you want to update ")
      hobby=input("Enter the correct hobby ")
      sql="update info set hobby=%s where Roll_no=%s"
      d=(hobby,roll_no)
      mycursor.execute(sql,d)
      mydb.commit()
      sho="select * from info where Roll_no="+str(roll_no)
      mycursor.execute(sho)
      print("***If No values display it means wrong rollno***")
      for i in mycursor:
        print("*****Your update sucess full*****")
        print(i)
    else:
      return
  except Exception:
    print("***roll no not found***")

def delete():
  try:
    roll_no=int(input("enter the rollno of the student whose record you want to delete  "))
    sql="delete from info where Roll_no="+str(roll_no)
    mycursor.execute(sql)
    mydb.commit()
    print("___**deleted sucessfully**___")
  except Exception:
    print("please check the rollno u have entered")

def dicp():
  sql="select * from info"
  mycursor.execute(sql)
  for i in mycursor:
    print("\nrollno,namme,class,section,hobby")
    print(i)

while True:
  print("-"*70)
  print("\t\twellcome to school management system ")
  print("----------------*********************************---------------")
  print("\t\t*******WELCOME TO MAIN MENU**********"
    "\nselect your option ....")
  print("1.insert student details")
  print("2.search Student details")
  print("3.update student details")
  print("4.Delete srudent Details")
  print("5.to display all available details")
  print("5.Exit")
  print("\t\t---------------------------------------")
  try:
    opt=int(input("enter your choise  "))
    if opt==1:
      insert()
    elif opt==2:
      search()
    elif opt==3:
      update()
    elif opt==4:
      delete()
    elif opt==5:
      dicp()
    else:
        break
  except Exception:
     print("please enter correct option")
