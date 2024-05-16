def cls():
    print('\n'*50)
admin = input("Enter your username of mysql: ")
pswd = input("Enter password: ")
def main_menu():
    while True:
        print("                                                         WELCOME TO ABC POLICE STATION, NEW DELHI")
        print("                                                     *********************************************** ")
        print("                                                                     **MAIN MENU ** ") 
        print("                                                           1) STAFF INFORMATION ")
        print("                                                           2) FIR DETAILS ")
        print("                                                           3) CRIMINAL DETAILS ")
        print("                                                           4) EXIT")
        choice=int(input("Enter your choice [1/2/3/4] :"))
        cls()
        if choice==1:
            staff_info()
        elif choice==2:
            fir_info()
        elif choice==3:
            criminal_info()
        elif choice==4:
            print("THANKS FOR USING...  HAVE A GUD DAY AHEAD!! :)")
            import sys
            sys.exit()
        else:
            print("Invalid choice !!! ENTER AGAIN....")

def staff_info():
    def sub_menu1():
        print("                                                             ***STAFF MANAGEMENT***")
        print("                                                  ................................................")
        print()
        print()
        print("                                                                 ~~SUB-MENU~~")
        print()
        print("                                                          1. See all records")
        print("                                                          2. Add a record")
        print("                                                          3. Modify a record")
        print("                                                          4. Delete a record")
        print("                                                          5. Show a particular record")
        print("                                                          6. Back to main menu")
    
    while True:
        sub_menu1()
        print()
        choose=int(input("Enter your choice [1-6]:"))
        cls()
        import mysql.connector as mc
        t=mc.connect(host="localhost",user=admin,password=pswd,database="staff_details")
        mycur=t.cursor()

        if choose==1:
            mycur.execute("select * from staff_details")
            data=mycur.fetchall()
            from tabulate import tabulate
            print(tabulate(data,headers=["RegId","Name","Rank","Year of joining","Address","Phn no","salary"]))
            
        elif choose==2:
            RegId=int(input("Enter registration id:"))
            Name=input("Enter name:")
            _Rank=input("Enter rank:")
            Year_of_joining=int(input("Enter year:"))
            Address=input("Enter address:")
            Phn_no=int(input("Enter phone no.:"))
            Salary=int(input("Enter salary:"))
            insert_query="""insert into staff_details(RegId,Name,_Rank,Year_of_joining,Address,Phn_no,Salary)
                      values({},'{}','{}',{},'{}',{},{})""".format(RegId,Name,_Rank,Year_of_joining,Address,Phn_no,Salary)
            mycur.execute(insert_query)
            t.commit()
            print(mycur.rowcount,"Record has been saved!!")

        elif choose==3:
            _RegId=int(input("Enter registration id of te record to be updated:"))
            print("Input new data")
            _Name=input("Enter new name:")
            Rank=input("Enter new rank:")
            _Year_of_joining=int(input("Enter new year:"))
            _Address=input("Enter new address:")
            _Phn_no=int(input("Enter new phone no.:"))
            _Salary=int(input("Enter new salary:"))
            update_query="UPDATE staff_details SET Name='{}',_Rank='{}',Year_of_joining={},Address='{}',Phn_no={},Salary={} WHERE RegId={}".format(_Name,Rank,_Year_of_joining,_Address,_Phn_no,_Salary,_RegId)
            mycur.execute(update_query)
            t.commit()
            print("1 Record has been updated!!")
        
        elif choose==4:
            RegId=input("Enter registration id of te record to be deleted:")
            delete_query="DELETE FROM staff_details WHERE RegId=%s"
            data1=(RegId,)
            mycur.execute(delete_query,data1)
            t.commit()
            print(mycur.rowcount,"Rows affected!!")
        

        elif choose==5:
            RegId=int(input("Enter the id of the record you want to see:"))
            show_query="select * from staff_details WHERE RegId=%s"
            data2=(RegId,)
            mycur.execute(show_query,data2)
            data=mycur.fetchall()
            from tabulate import tabulate
            print(tabulate(data,headers=["RegId","Name","Rank","Year of joining","Address","Phn no","Salary"]))

        elif choose==6:
            cls()
            main_menu()
     

        elif choose==7:
            print("THANKS FOR USING... HAVE A GOOD DAY AHEAD!!!:")
       
        else:
            print("INVALID CHOISE!!! ENTER AGAIN...")
        mycur.close()


def fir_info():
    def sub_menu2():
        print("                                                          ***CRIME MANAGEMENT***")
        print("                                                     ********************************")
        print()
        print("                                                             ---SUB-MENU---")
        print()
        print("                                                            1. See all records")
        print("                                                            2. Add a record")
        print("                                                            3. Modify a record")
        print("                                                            4. Delete a record")
        print("                                                            5. Show a particular record")
        print("                                                            6. Back to main menu")
        print()
    cls()
    sub_menu2()
    while True:
        choice1=int(input("Enter your choice(1-6):"))
        cls()
        import mysql.connector as mc
        t=mc.connect(host="localhost",user=admin,password=pswd,database="fir_details")
        mycur=t.cursor()

        if choice1==1:
            mycur.execute("select * from crime_register")
            data=mycur.fetchall()
            from tabulate import tabulate
            print(tabulate(data,headers=["Case no","Case type","VIctim","Witness","Complainer","Accused","Punishment"]))
            print()
            print("Press 1 to see victim details")
            print("Press 2 to see witness details")
            print("Press 3 to see complainer details")
            print("Press 4 to return to main menu")
            print()
            while True:
                print()
                choose1=int(input("Enter your choice(1-4):"))
                if choose1==1:
                    mycur.execute("select * from victim_details")
                    data1=mycur.fetchall()
                    from tabulate import tabulate
                    print(tabulate(data1,headers=["Case no","Victim's name","Age","Address","Phn no"]))
                elif choose1==2:
                    mycur.execute("select * from witness_details")
                    data2=mycur.fetchall()
                    from tabulate import tabulate
                    print(tabulate(data2,headers=["Case no","Witness's name","Age","Address","Phn no"]))
                elif choose1==3:
                    mycur.execute("select * from complainer_details")
                    data3=mycur.fetchall()
                    from tabulate import tabulate
                    print(tabulate(data3,headers=["Case no","Complainer's name","Age","Address","Phn no"]))
                elif choose1==4:
                    sub_menu2()
                    break
                else:
                    print("INVALID CHOICE!!!ENTER AGAIN...")

        elif choice1==2:
            Case_no=input("Enter case no:")
            Case_type=input("Enter case type:")
            Victim=input("Enter victim name:")
            Witness=input("Enter witness name:")
            Complainer=input("Enter complainer name:")
            Accused=input("Enter accused name:")
            Punishment=input("Enter punishment:")
            insert_query1="""insert into crime_register(Case_no,Case_type,Victim,Witness,Complainer,Accused,Punishment)
                        values('{}','{}','{}','{}','{}','{}',{})""".format(Case_no,Case_type,Victim,Witness,Complainer,Accused,Punishment)
            mycur.execute(insert_query1)
            t.commit()
            print(mycur.rowcount,"Record added")
            print()
            print("Press 1 to add record in victim details")
            print("Press 2 to add record in witness details")
            print("Press 3 to add record in complainer details")
            print("Press 4 to return to main menu")
            print()
            while True:
                choose2=int(input("Enter your choice(1-4):"))
                if choose2==1:
                    Case_no=input("Enter case no:")
                    Victim=input("Enter victim name:")
                    Age=int(input("Enter age:"))
                    Address=input("Enter address:")
                    Phone_no=int(input("Enter phone no:"))
                    insert_query="""insert into victim_details(Case_no,Victim,Age,Address,Phone_no)
                         values('{}','{}',{},'{}',{})""".format(Case_no,Victim,Age,Address,Phone_no)
                    mycur.execute(insert_query)
                    t.commit()
                    print(mycur.rowcount,"Record added")
                elif choose2==2:
                    Case_no=input("Enter case no:")
                    Witness=input("Enter witness name:")
                    Age=int(input("Enter age:"))
                    Address=input("Enter address:")
                    Phone_no=int(input("Enter phone no:"))
                    insert_query="""insert into witness_details(Case_no,Witness,Age,Address,Phone_no)
                        values('{}','{}',{},'{}',{})""".format(Case_no,Witness,Age,Address,Phone_no)
                    mycur.execute(insert_query)
                    t.commit()
                    print(mycur.rowcount,"Record added")
                elif choose2==3:
                    Case_no=input("Enter case no:")
                    Complainer=input("Enter complainer name:")
                    Age=input("Enter age:")
                    Address=input("Enter address:")
                    Phone_no=input("Enter phone no:")
                    insert_query="""insert into complainer_details(Case_no,Complainer,Age,Address,Phone_no)
                        values('{}','{}',{},'{}',{})""".format(Case_no,Complainer,Age,Address,Phone_no)
                    mycur.execute(insert_query)
                    t.commit()
                    print(mycur.rowcount,"Record added")
                elif choose2==4:
                    sub_menu2()
                    break
                else:
                    print("INVALID CHOICE!!!!ENTER AGAIN...")
               
        elif choice1==3:
            Case_no=input("Enter the case no of record to be updated:")
            print("Input new data")
            _Case_type=input("Enter new case type:")
            _Victim=input("Enter new victim:")
            _Witness=input("Enter new witness:")
            _Complainer=input("Enter new complainer:")
            _Accused=input("Enter new accused:")
            _Punishment=input("Enter new punishment:")
            update_query="UPDATE crime_register SET Case_type='{}',Victim='{}',Witness='{}',Complainer='{}',Accused='{}',Punishment={} WHERE Case_no='{}'".format(_Case_type,_Victim,_Witness,_Complainer,_Accused,_Punishment,Case_no)
            mycur.execute(update_query)
            t.commit()
            print(mycur.rowcount,"Record has been updated !")
            print()
            print("Press 1 to update victim record")
            print("Press 2 to update witness record")
            print("Press 3 to update complainer record")
            print("Press 4 to return to main menu")
            print()
            while True:
                choose3=int(input("Enter your choice(1-4):"))
                if choose3==1:
                    Case_no=input("Enter the case no of record to be updated:")
                    print("Input new data:")
                    _Victim=input("Enter new victim:")
                    _Age=int(input("Enter new age:"))
                    _Address=input("Enter new address:")
                    _Phone_no=int(input("Enter new phone no:"))
                    update_query="UPDATE victim_details SET Victim='{}',Age={},Address='{}',Phone_no={} WHERE Case_no='{}'".format(_Victim,_Age,_Address,_Phone_no,Case_no)
                    mycur.execute(update_query)
                    t.commit()
                    print(mycur.rowcount,"Record has been updated !")
                
                elif choose3==2:
                    Case_no=input("Enter the case no of record to be updated:")
                    print("Input new data")
                    _Witness=input("Enter new witness:")
                    _Age=int(input("Enter new age:"))
                    _Address=input("Enter new address:")
                    _Phone_no=int(input("Enter new phone no:"))
                    update_query="UPDATE witness_details SET Witness='{}',Age={},Address='{}',Phone_no={} WHERE Case_no='{}'".format (_Witness,_Age,_Address,_Phone_no,Case_no)
                    mycur.execute(update_query)
                    t.commit()
                    print(mycur.rowcount,"Record has been updated !")
                
                elif choose3==3:
                    Case_no=input("Enter the case no of the record to be updated:")
                    print("Input new data")
                    _Complainer=input("Enter new complainer:")
                    _Age=int(input("Enter new age:"))
                    _Address=input("Enter new address:")
                    _Phone_no=int(input("Enter new phone no:"))
                    update_query="UPDATE complainer_details SET Complainer='{}',Age={},Address='{}',Phone_no={} WHERE Case_no='{}'".format(_Complainer,_Age,_Address,_Phone_no,Case_no)
                    mycur.execute(update_query)
                    t.commit()
                    print(mycur.rowcount,"Record has been updated !")
                elif choose3==4:
                    sub_menu2()
                    break
                else:
                    print("INVALID CHOICE!!!ENTER AGAIN....")
                
        elif choice1==4:
            Case_no=input("Enter case no you want to delete:")
            delete_query="DELETE FROM crime_register WHERE Case_no=%s"
            delete1_query="DELETE FROM victim_details WHERE Case_no=%s"
            delete2_query="DELETE FROM witness_details WHERE Case_no=%s"
            delete3_query="DELETE FROM complainer_details WHERE Case_no=%s"
            data4=(Case_no,)
            mycur.execute(delete_query,data4)
            mycur.execute(delete1_query,data4)
            mycur.execute(delete2_query,data4)
            mycur.execute(delete3_query,data4)
            t.commit()
            print("1 Record has been deleted!")
       
        elif choice1==5:
            Case_no=input("Enter case no:")
            show_query="select * from crime_register where Case_no=%s"
            data8=(Case_no,)
            mycur.execute(show_query,data8)
            data=mycur.fetchall()
            from tabulate import tabulate
            print(tabulate(data,headers=["Case no","Case type","Victim","Witness","Complainer","Accused", "Punishment"]))
            print()
            print("Press 1 to see victim detail")
            print("Press 2 to see witness detail")
            print("Press 3 to see complainer detail")
            print("Press 4 to return to main menu")
            print()
            while True:
                choose5=int(input("Enter your choice(1-4):"))
                if choose5==1:
                    Case_no=input("Enter case no:")
                    show_query="select * from victim_details where Case_no=%s"
                    data9=(Case_no,)
                    mycur.execute(show_query,data9)
                    data9=mycur.fetchall()
                    from tabulate import tabulate
                    print(tabulate(data9,headers=["Case no","Victim's name","Age","Address","Phn no"]))

                elif choose5==2:
                    Case_no=input("Enter case no:")
                    show_query="select * from witness_details where Case_no=%s"
                    data10=(Case_no,)
                    mycur.execute(show_query,data10)
                    data11=mycur.fetchall()
                    from tabulate import tabulate
                    print(tabulate(data11,headers=["Case no","Witness's name","Age","Address","Phn no"]))
                    
                elif choose5==3:
                    Case_no=input("Enter case no:")
                    show_query="select * from complainer_details where Case_no=%s"
                    data11=(Case_no,)
                    mycur.execute(show_query,data11)
                    data12=mycur.fetchall()
                    from tabulate import tabulate
                    print(tabulate(data12,headers=["Case no","Complainer's name","Age","Address","Phn no"]))
                
                elif choose5==4:
                    sub_menu2()
                    break
                else:
                    print("INVALID CHOICE!!!ENTER AGAIN...")
                    
        elif choice1==6:
            cls()
            main_menu()

        else:
            print("INVALID CHOICE !!! ENTER AGAIN....")
        
        mycur.close()    
        
            
def criminal_info():
    def sub_menu3():
        print("                                                          ***CRIMINAL RECORD MANAGEMENT***")
        print("                                                     ..........................................")
        print()
        print()
        print("                                                                 ----SUB-MENU----")
        print()
        print("                                                            1. See all records")
        print("                                                            2. Add a record")
        print("                                                            3. Modify a record")
        print("                                                            4. Delete a record")
        print("                                                            5. Show a particular record")
        print("                                                            6. Back to main menu")
    
    while True:
        sub_menu3()
        choice2 =int(input("Enter your choice [1-6]:"))
        cls()
        import mysql.connector as mc
        t=mc.connect(host="localhost",user=admin,password=pswd,database="criminal")
        mycur=t.cursor()

        if choice2==1:
            mycur.execute("select * from criminal_record")
            data=mycur.fetchall()
            from tabulate import tabulate
            print(tabulate(data,headers=["Reg Id","Name","Age","Phone no","Address","Case no","Arrested for","Punishment"]))
        elif choice2==2:
            Reg_id=int(input("Enter registration id:"))
            Name=input("Enter name:")
            Age=int(input("Enter age:"))
            Address=input("Enter address:")
            Phoneno=int(input("Enter phone number:"))
            Case_no=input("Enter case no:")
            Arrestedfor=input("Enter the reason for arrest:")
            Punishmentgiven=input("Enter the punishment given:")
            insert_query2="""insert into criminal_record(Reg_id,Name,Age,Address,Phoneno,Case_no,Arrestedfor,Punishmentgiven)
                      values({},'{}',{},'{}',{},'{}','{}','{}')""".format(Reg_id,Name,Age,Address,Phoneno,Case_no,Arrestedfor,Punishmentgiven)
            mycur.execute(insert_query2)
            t.commit()
            print(mycur.rowcount,"Record has been saved!!")

        elif choice2==3:
            Reg_id=int(input("Enter the id of the record to be updated:"))     
            print("Input new data")
            _Name=input("Enter new name:")
            _Age=int(input("Enter new age:"))
            _Address=input("Enter new address:")
            _Phoneno=int(input("Enter new phone no:"))
            _Case_no=input("Enter case no:")
            _Arrestedfor=input("Enter reason why arrested for:")
            _Punishmentgiven=input("Enter punishment given:")
            update_query="UPDATE criminal_record SET Name='{}',Age={},Address='{}',Phoneno={},Case_no='{}',Arrestedfor='{}',Punishmentgiven='{}' WHERE Reg_id={}".format(_Name,_Age,_Address,_Phoneno,_Case_no,_Arrestedfor,_Punishmentgiven,Reg_id)
            mycur.execute(update_query)
            t.commit()
            print(mycur.rowcount,"Record has been updated!!")

        elif choice2==4:
            Reg_id=input("Enter id of the record to be deleted:")
            delete_query="DELETE FROM criminal_record WHERE Reg_id =%s"
            data1=(Reg_id,)
            mycur.execute(delete_query,data1)
            t.commit()
            print(mycur.rowcount,"Rows affected!!")

        elif choice2==5:
            Reg_id=input("Enter the id of the record you want to see:")
            show_query="select * from criminal_record where Reg_id=%s"
            data2=(Reg_id,)
            mycur.execute(show_query,data2)
            data=mycur.fetchall()
            from tabulate import tabulate
            print(tabulate(data,headers=["Reg Id","Name","Age","Phone no","Address","Case no","Arrested for","Punishment"]))

        elif choice2==6:
            main_menu()

        else:
            print("INVALID CHOICE !!! ENTER AGAIN....")
        mycur.close()
            
#calling
main_menu()


