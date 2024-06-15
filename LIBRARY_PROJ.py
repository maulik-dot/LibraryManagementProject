import mysql.connector
import pyautogui
password=input("Enter the Mysql password..:-")

mydb=mysql.connector.connect(host="localhost",user="root",password=password)
cur=mydb.cursor()
def add_book():
   
    bid=int(input('Enter the Book Id-'))
    bname=input('Enter the Book Name-')
    bauth=input("Enter Author's name-")
    bprice=float(input("Enter Book's PRICE-₹"))
    btype=input("Enter its Genre-")

    qry=("insert into Bk(Book_ID,Book_Name,Author,Price,Book_Type)values(%s,%s,%s,%s,%s)")
    val=(bid,bname,bauth,bprice,btype)
    cur.execute(qry,val)
    mydb.commit()
    print("^^^^^^^^^^^^^^^^^^^^^^^")
    print("Successfully Added :):)")
    print("~~~~~~~~~~~~~~~~~~~~~~~")


    
    
def display_book():
    try:

        qry2=("select *from Bk")
        cur.execute(qry2)
        for (Book_ID,Book_Name,Author,Price,Book_Type,Book_Status) in cur:
        
            print('='*167)
            print("Book_ID      :",Book_ID)
            print("Book_Name    :",Book_Name)
            print("Author       :",Author)
            print("Price        :",Price)
            print("Book_Type    :",Book_Type)
            print("Book_Status  :",Book_Status)
            print('='*167)
        
        print("Here are your Books!!!!!!!")

    except Exception:
        print("Data doesn't Exist.")
        
    
def search_book():

    try:
        bd=input("Enter the Field name (Book_ID/Author) to SEARCH..>>")
        val=input("Enter the values to be Searched-")
        qry3="select *from Bk where {}='{}'".format(bd,val)
        cur.execute(qry3)
        result=cur.fetchall()
        for (Book_ID,Book_Name,Author,Price,Book_Type,Book_Status) in result:
            print('='*167)
            print("Book_ID      :",Book_ID)
            print("Book_Name    :",Book_Name)
            print("Author       :",Author)
            print("Price        :",Price)
            print("Book_Type    :",Book_Type)
            print("Book_Status  :",Book_Status)
            print('='*167)
        print("Wow!! That's a Successfull Search.")
        
    except Exception:
        print("Error, Record not found :(")


def update_book():
    try:
        
        bid1=int(input("Enter Book ID to Update-"))
        cur.execute("select *from Bk where Book_ID={}".format(bid1))
        for (Book_ID,Book_Name,Author,Price,Book_Type,Book_Status) in cur:
            print("Book_ID      :",Book_ID)
            print("Book_Name    :",Book_Name)
            print("Author       :",Author)
            print("Price        :",Price)
            print("Book_Type    :",Book_Type)
            print("Book_Status  :",Book_Status)
        while True:
            at=input("Enter the Field to be UPDATE-")
            values=input("Enter the Values-")
            query="update Bk set {}='{}' where Book_ID={}".format(at,values,bid1)
            cur.execute(query)
            c=input("Do you want to update more fields=")
            if c in 'nN':
                break
            
    
        print("^^^^^^^^^^^^^^^^^^^^")
        print("Records Updated :):)")
        print("~~~~~~~~~~~~~~~~~~~~")
        mydb.commit()
        
       

    except Exception:
        print("Error found Records Not Updated :(")
    mydb.close()        
    
def delete_book():
    try:
        bid2=int(input("Enter the Book ID to be Deleted-"))
        cur.execute("select *from Bk where Book_ID={}".format(bid2))
        for (bid,bname,bauth,bprice,btype,Book_Status) in cur:
            print("Book_ID      :",bid)
            print("Book_Name    :",bname)
            print("Author       :",bauth)
            print("Price        :",bprice)
            print("Book_Type    :",btype)
            print("Book_Status  :",Book_Status)
            

        qry1="delete from Bk where Book_ID={}".format(bid2)
        cur.execute(qry1)
        print("^^^^^^^^^^^^^^^^^^^^")
        print("Records Deleted :):)")
        print("~~~~~~~~~~~~~~~~~~~~")
        mydb.commit()
        
    except Exception:
        print("Error found Records Not Deleted..")


def issue_book():

    print('='*167)
    print("1. Issue Book to Students")
    print("2. Display the Student's Details")
    print("3. Search Student's Details")
    print("4. Update Student's Details")
    print("5. Return Book")
    print("6. Back to Main Menu")
    print('='*167)
    global ch
    ch=int(input("Enter your Choices...:"))
    print('='*167)


def add_stud():
    print("You can Issue only 1 book at a time.")
    print('='*167)
    adm_no=int(input('Enter Your Adm.No.(only 4-Characters)-'))
    cls=input('Enter Your Class -')
    Sec=input("Enter the Section(A/B/C/D)-")
    name=input("Enter your Name-₹")
    doi=input("Date of Issue(yyyy/mm/dd)-")

    qry3=("select *from Bk")
    cur.execute(qry3)
    for (Book_ID,Book_Name,Author,Price,Book_Type,Book_Status) in cur:
        
        print('='*167)
        print("Book_ID      :",Book_ID)
        print("Book_Name    :",Book_Name)
        print("Author       :",Author)
        print("Price        :",Price)
        print("Book_Type    :",Book_Type)
        print("Book_Status  :",Book_Status)
        print('='*167)

    bnam=input("Enter the Book's Name that you want to Issue-")

    
    qry4=("insert into Bk_issue(Adm_No,Class,Section,Student_Name,Date_of_Issue,BName)values(%s,%s,%s,%s,%s,%s)")
    val2=(adm_no,cls,Sec,name,doi,bnam)
    cur.execute(qry4,val2)
    cur.execute("update Bk_issue set Date_of_Return=date_add(Date_of_Issue, interval 15 day)")
    cur.execute("update Bk set Book_Status='ISSUED' where Book_Name='{}'".format(bnam))
    mydb.commit()
    print("^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("Successfully Issued  :):)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")


   

def disp_detail():
    try:

        qry2=("select *from Bk_issue")
        cur.execute(qry2)
        for (Adm_No,Class,Section,Student_Name,Date_of_Issue,Date_of_Return,BName) in cur:
        
            print('='*167)
            print("Admission No      :",Adm_No)
            print("Class             :",Class)
            print("Section           :",Section)
            print("Student_Name      :",Student_Name)
            print("Date of Issue     :",Date_of_Issue)
            print("Date_of_Return    :",Date_of_Return)
            print("Issued Book       :",BName)
            print('='*167)
        

    except Exception:
        print("Data doesn't Exist.")

def search_detail():

    try:
        bd1=input("Enter your Admission No. to SEARCH..>>")
        qry3="select *from Bk_issue where Adm_No={}".format(bd1)
        cur.execute(qry3)
        result=cur.fetchall()
        for (Adm_No,Class,Section,Student_Name,Date_of_Issue,Date_of_Return,BName) in cur:
            print('='*167)
            print("Admission No      :",Adm_No)
            print("Class             :",Class)
            print("Section           :",Section)
            print("Student_Name      :",Student_Name)
            print("Date of Issue     :",Date_of_Issue)
            print("Date_of_Return    :",Date_of_Return)
            print("Issued Book       :",BName)
            print('='*167)
        print("Wow!! That's a Successfull Search.")
        
    except Exception:
        print("Error, Record not found :(")

def update_detail():
    try:
        
        adm2=int(input("Enter your Admission No. to Update -"))
        cur.execute("select Adm_No,Class,Section,Student_Name,Date_of_Issue from Bk_issue where Adm_No={}".format(adm2))
        for (Adm_No,Class,Section,Student_Name,Date_of_Issue) in cur:
            print('='*167)
            print("Admission No      :",Adm_No)
            print("Class             :",Class)
            print("Section           :",Section)
            print("Student_Name      :",Student_Name)
            print("Date_of_Issue     :",Date_of_Issue)
            print('='*167)
        while True:
            at1=input("Enter the Field to be UPDATED-")
            values1=input("Enter the New Value-")
            query4="update Bk_issue set {}='{}' where Adm_No={}".format(at1,values1,adm2)
            cur.execute(query4)
            c=input("Do you want to update more fields(Y/y)=")
            if c in 'nN':
                break
        
    
        print("^^^^^^^^^^^^^^^^^^^^")
        print("Records Updated :):)")
        print("~~~~~~~~~~~~~~~~~~~~")
        mydb.commit()

    except Exception:
        print("Error Found!! Records Not Updated :(")
    mydb.close()        
    
    

def delete_detail():
    try:
        adm=int(input("Enter Your Admssion No.-"))
        cur.execute("select *from Bk_issue where Adm_No={}".format(adm))
        for (Adm_No,Class,Section,Student_Name,Date_of_Issue,Date_of_Return,BName) in cur:
            print('='*167)
            print("Admission No      :",Adm_No)
            print("Class             :",Class)
            print("Section           :",Section)
            print("Student_Name      :",Student_Name)
            print("Date of Issue     :",Date_of_Issue)
            print("Date_of_Return    :",Date_of_Return)
            print("Issued Book       :",BName)
            print('='*167)

        bn=input("Enter the Book's Name to Return it:")
            

        qry5="delete from Bk_issue where Adm_No={}".format(adm)
        cur.execute(qry5)
        cur.execute("update Bk set Book_Status='Available' where Book_Name='{}'".format(bn))
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("The Book is Returned.Thank You :):)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        mydb.commit()
        
    except Exception:
        print("Error found Records Not Deleted..")

   
    
  

def bookdetails():
    print('='*167)
    print("1. Add Book details")
    print("2. Display the Book Details")
    print("3. Search the Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Back to Main Menu")
    print('='*167)
    global ch
    ch=int(input("Enter your choice...:"))
    print('='*167)
def main_menu():
    print('='*167)
    print("MAIN MENU")
    print("1. Book's Portal")
    print("2. Student's Portal")
    print("3. EXIT")
    print('='*167)
    global ch
    ch=int(input("Enter your choice...:"))
def main_run():
    while True:
        main_menu()
        if ch==1:
            bookdetails()
            if ch==1:
                add_book()
            elif ch==2:
                display_book()
            elif ch==3:
                search_book()
            elif ch==4:
                update_book()
            elif ch==5:
                delete_book()
            elif ch==6:
                main_menu()
        elif ch==2:
            issue_book()
            if ch==1:
                add_stud()
            elif ch==2:
                disp_detail()
            elif ch==3:
                search_detail()
            elif ch==4:
                update_detail()
            elif ch==5:
                delete_detail()
            elif ch==6:
                main_menu()
                
            
        elif ch==3:
            break
    mydb.close()
        
def pssd():
        uid=input("Input User-id  :")
        pwd=pyautogui.password(text='Input Your Password:',title='PASSWORD',default='',mask='*')
        if uid=="abc" and pwd=="1234":
            print("Login successful...")
        else:
            print("Wrong Userid and Password..")
            print("Enter Userid and password again...")
        


if mydb.is_connected(): 
    print("CONNECTION IS SUCCESSFUL!!!!")
    
    cur.execute("create database if not exists LIB_Proj")
    cur.execute("use LIB_Proj")
    #creating required tables 
    cur.execute("create table if not exists Bk(Book_ID int primary key, Book_Name varchar(40), Author varchar(30), Price float(7,2), Book_Type varchar(30), Book_Status char(10) DEFAULT 'Available')")
    cur.execute("create table if not exists Bk_issue(Adm_No int, Class char(3), Section char(2), Student_Name varchar(30), Date_of_Issue date, Date_of_Return date, BName char(15))")
    mydb.commit()
    print('*'*71,'WELCOME TO WEB LIBRARY ','*'*71)
    print('-'*167)

    pssd()

    
    try:
        main_run()
    except Exception as e:
        print('='*167)
        print("PROGRAM RUNNING AGAIN")
        print('='*167)
        print("\t"+str(e))
        main_run()
else:
    print("CONNECTION IS NOT SUCCESSFUL")








