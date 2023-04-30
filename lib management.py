import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="Shreya",database="lm2")
def pswd():
    ps=input("Enter Password:")
    if ps=="py143":
        main()
    else:
        print("Wrong Password")
    pswd()

def main():
    print("""
    1.ADD BOOK
    
    LIBRARY MANAGER

    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOKS
    """)
    choice=input("Enter Task No:")
    print("> <")
    if(choice=='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice=='4'):

        dbook()
    elif(choice=='5'):
        dispbook()
    else:
        print("Wrong choice....... ")

def addbook():
    bn=input("Enter BOOK Name:")
    c=input("Enter BOOK Code:")
    t=input("Total Books:")
    s=input("Enter Subject:")
    data=(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("> <")
    print("Data entered Successfully")
    main()
def issueb():
    n=input("Enter Name:")
    r=input("Enter Reg No:")
    co=input("Enter Book Code:")
    d=input("enter date")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("> <")
    print("Book issued to:",n)
    bookup(co,-1)

def bookup(co,u):
    a='Select TOTAL from books where BCODE=%s';
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    d=(t,co)
    sql="update books set TOTAL =%s where BCODE=%s";



    c.execute(sql,d)
    con.commit()
def submitb():
    n=input("Enter Name:")
    r=input("Enter Reg No:")
    co=input("Enter Book Code:")
    d=input("enter date")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("> <")
    print("Book Submitted from:",n)
    bookup(co,1)

def dbook():
    ac=input("Enter Book Code:")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()
def dispbook():
    a="select * from books"
    c= con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name:",i[0])
        print("Book Code:",i[1])
        print("Total:",i[2])
        print("> <")
    main()
pswd()
main()
addbook()
issueb()
submitb()
dbook()
dispbook()
