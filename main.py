import cx_Oracle

try:
    connection = cx_Oracle.connect('rxn6413', 'Rupini11', 'acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')
    cursor = connection.cursor()
    print("version : ", connection.version)
    print("Connection Established!, Ready to use..")

    #drop commands

    # drop_file = open("drop_commands_txtfile.txt", "r")
    # drop_commands = drop_file.read()
    # drop_commands = drop_commands.split(";")
    # # print(drop_commands)
    # for i in range(len(drop_commands)):
    #     table_name = drop_commands[i].split(" ")[-1]
    #     print(table_name)
    #     cursor.execute(drop_commands[i])
    #     print(table_name + " Table dropped succesfully")


    #create statements

    # person_table_create_query = """
    # create table Fall22_S004_5_person(
    # person_id Varchar(30) not null,
    # Name  Varchar(30) not null,
    # mail Varchar(30) not null,
    # gender Varchar(30) not null,
    # street Varchar(30) not null,
    # apt_number Varchar(30) not null,
    # zipcode int not null,
    # primary key(person_id)
    # )"""
    # cursor.execute(person_table_create_query)
    # print("person_table_create_query executed succesfully")

    # person_phone_table_create_query = """
    # create table Fall22_S004_5_person_phone(
    # person_id Varchar(30) not null,
    # phone_number Varchar(10) not null,
    # primary key(person_id,phone_number),
    # FOREIGN KEY (person_id)
    # REFERENCES Fall22_S004_5_person(person_id)
    # )"""
    # cursor.execute(person_phone_table_create_query)
    # print("person_phone_table_create_query executed succesfully")

    # audience_table_create_query = """
    # create table Fall22_S004_5_audience(
    # person_id Varchar(30) not null,
    # audience_category varchar(30) not null,
    # primary key(person_id),
    # FOREIGN KEY (person_id)
    #         REFERENCES Fall22_S004_5_person(person_id)
    # )"""
    # cursor.execute(audience_table_create_query)
    # print("audience_table_create_query executed succesfully")

    # audience_parking_table_create_query = """
    # create table Fall22_S004_5_parking_audience(
    # parking_id Varchar(30) not null,
    # audience_id Varchar(30) ,
    # license_plate_number Varchar(15) not null,
    # price int,
    # parking_type Varchar(30) not null,
    # date_of_parking date not null,
    # primary key(parking_id),
    # FOREIGN KEY (audience_id)
    # REFERENCES Fall22_S004_5_audience(person_id)
    # )"""
    # cursor.execute(audience_parking_table_create_query)
    # print("audience_parking_table_create_query executed succesfully")

    # employee_table_create_query = """
    # create table Fall22_S004_5_employee(
    # person_id Varchar(10) not null,
    # SSN int not null,
    # date_of_joining date not null,
    # employee_category varchar(30) not null,
    # salary int not null,
    # primary key(person_id ),
    # FOREIGN KEY (person_id)
    #         REFERENCES Fall22_S004_5_person(person_id )
    # )
    # """
    # cursor.execute(employee_table_create_query)
    # print("employee_table_create_query executed succesfully")

    # employee_supervisor_table_create_query = """
    # create table Fall22_S004_5_employee_supervisor(
    # employee_id Varchar(10) not null,
    # supervisor_id Varchar(10),
    # primary key(employee_id,supervisor_id ),
    # FOREIGN KEY (employee_id)
    #         REFERENCES Fall22_S004_5_employee(person_id),
    # FOREIGN KEY (supervisor_id )
    #         REFERENCES Fall22_S004_5_employee(person_id)
    # )"""
    # cursor.execute(employee_supervisor_table_create_query)
    # print("employee_supervisor_table_create_query executed succesfully")

    # audience_tickets_table_create_query = """
    # create table Fall22_S004_5_audience_tickets(
    # audience_id varchar(10) not null,
    # ticket_id varchar(10) not null,
    # ticket_category varchar(30) not null,
    # ticket_date date not null,
    # gate_number varchar(10) not null,
    # seat_number varchar(10) not null,
    # primary key(ticket_id) ,
    # FOREIGN KEY (audience_id )
    # REFERENCES Fall22_S004_5_audience(person_id)
    # )"""
    # cursor.execute(audience_tickets_table_create_query)
    # print("audience_tickets_table_create_query executed succesfully")

    # stores_table_create_query = """
    # create table Fall22_S004_5_stores(
    # store_id varchar(30) not null,
    # rent varchar(10) not null,
    # store_category varchar(30) not null,
    # vendor_name varchar(50) not null,
    # date_of_payment date not null,
    # primary key(store_id)
    # )"""
    # cursor.execute(stores_table_create_query)
    # print("stores_table_create_query executed succesfully")

    # event_table_create_query = """
    # create table Fall22_S004_5_event(
    # event_id Varchar(30) not null,
    # event_date date not null,
    # event_day varchar(15) not null,
    # start_time timestamp ,
    # end_time timestamp,
    # event_category varchar(30) not null,
    # primary key(event_id )
    # )"""
    # cursor.execute(event_table_create_query)
    # print("event_table_create_query executed succesfully")

    # teams_table_create_query = """
    # create table Fall22_S004_5_teams(
    # team_name varchar(100) not null,
    # team_category varchar(20) not null,
    # sport varchar(20) not null,
    # Is_UTA char(3) check(Is_UTA in ('Yes','No')),
    # primary key(team_name)
    # )"""
    # cursor.execute(teams_table_create_query)
    # print("teams_table_create_query executed succesfully")

    # event_stores_table_create_query = """
    # create table Fall22_S004_5_event_stores(
    # store_id varchar(30) not null,
    # event_id varchar(30) not null,
    # primary key(store_id, event_id),
    # foreign key(store_id ) references Fall22_S004_5_stores(store_id),
    # foreign key (event_id) references Fall22_S004_5_event(event_id)
    # )"""
    # cursor.execute(event_stores_table_create_query)
    # print("event_stores_table_create_query executed succesfully")

    # event_teams_table_create_query = """
    # create table Fall22_S004_5_event_teams(
    # event_id varchar(30) not null,
    # team varchar(100) not null,
    # primary key(event_id , team),
    # foreign key (event_id) references Fall22_S004_5_event(event_id),
    # foreign key(team) references Fall22_S004_5_teams(team_name)
    # )"""
    # cursor.execute(event_teams_table_create_query)
    # print("event_teams_table_create_query executed succesfully")

    # audience_event_table_create_query = """
    # create table Fall22_S004_5_audience_event(
    # event_id varchar(30) not null,
    # audience_id varchar(10) not null,
    # primary key (event_id, audience_id) ,
    # foreign key (event_id) references Fall22_S004_5_event(event_id),
    # foreign key (audience_id) references Fall22_S004_5_audience(person_id)
    # )"""
    # cursor.execute(audience_event_table_create_query)
    # print("audience_event_table_create_query executed succesfully")

    # event_employee_table_create_query = """
    # create table Fall22_S004_5_event_employee(
    # employee_id varchar(10) not null,
    # event_id varchar(30) not null,
    # clock_in timestamp not null,
    # clock_out timestamp not null,
    # event_date date not null,
    # primary key(employee_id, event_id),
    # foreign key (employee_id) references Fall22_S004_5_employee(person_id),
    # foreign key(event_id) references Fall22_S004_5_event(event_id)
    # )"""
    # cursor.execute(event_employee_table_create_query)
    # print("event_employee_table_create_query executed succesfully")


    #insert commands
    # insert_file = open("insert_commands_txt.txt", "r")
    # insert_commands = insert_file.read()
    # insert_commands = insert_commands.split(";")
    # print(len(insert_commands))
    # # print(drop_commands)
    # for i in range(len(insert_commands)):
    #     # table_name = insert_commands[i].split(" ")[-1]
    #     # print(table_name)
    #     cursor.execute(insert_commands[i])
    #     cursor.execute("commit")
    #     print(i)
    #     # print(table_name + " Table dropped succesfully")


    #query_execution




    # cursor.execute("INSERT INTO Fall22_S004_5_person values ('364980','Juliana Valentine McCourt','juliana.mccourt@hotmail.com','FEMALE','Garfield Avenue','2A',10005)")
    # cursor.execute("commit")
    # cursor.execute("SELECT * FROM Fall22_S004_5_person")
    # print("printing select command results here: ")
    # print(cursor.fetchall())
    cursor.execute("commit")

except cx_Oracle.DatabaseError as e:
	print("There is a problem with Oracle", e)


#
#
# def check_integer(input_data):
#     try:
#         if input_data == "" or input_data == '0' or input_data == -1 or int(input_data) < 1:
#             return 0
#         input_data = int(input_data)
#         print(input_data)
#         return  1
#     except ValueError:
#         return 0
#         # print('The provided value is not an integer')
#
#
# def bg_15():
#     print("Update Fall22_S004_5_audience_tickets")
#
#     print("Parameters in Fall22_S004_5_audience_tickets are :")
#     col_names = ["audience_id", "ticket_id", "ticket_category", "ticket_date","gate_number" ,"seat_number"]
#     print(col_names)
#     n= int(input("How many parameters you want to change :"))
#     # print("1.audience_id")
#     # print("2.ticket_id")
#     print("2.ticket_category")
#     print("3.ticket_date")
#     print("4.gate_number")
#     print("5.seat_number")
#     print("please select parameters 1 after other using above column numbers: ")
#     col=[]
#     for i in range(1,n+1):
#         # c_num = "c"+str(i)
#         col_num = input("Please enter the column number :")
#         col_value = input("enter new value : ")
#         col.append([col_num, col_value])
#
#     ticket_id = input("Please select ticket id 'WHERE' above changes need to happen :, ticket_id = ")
#
#     print("update details = ", col)
#
#     update_query = "UPDATE Fall22_S004_5_audience_tickets SET "
#     up2 = " WHERE ticket_id = " + "'" + str(ticket_id) + "'"
#
#     for j in range(len(col)):
#         col_index = int(col[j][0])
#         print("col_index : ",col_index)
#         col_name = col_names[col_index]
#         print("col_name : ",col_name)
#         update_value = col[j][1]
#         print("update_value : ", update_value)
#         if j==0:
#             update_query = update_query + col_name + "=" + "'"+update_value + "'"
#         if j>0:
#             update_query = update_query + " , " +col_name +"=" + "'"+update_value + "'"
#
#     # update_query =  '"' + update_query + up2 + '"'
#     update_query = update_query + up2
#
#     print("UPDATE QUERY : ", update_query)
#
#     try:
#         cursor.execute(str(update_query))
#         cursor.execute("commit")
#
#         select_updated_row = "SELECT * FROM Fall22_S004_5_audience_tickets WHERE ticket_id = "+ str(ticket_id)
#         cursor.execute(select_updated_row)
#         print("Fetching updated row from database ..")
#         # print("printing bg1_query command results here: ")
#         bg15_output = cursor.fetchall()
#         print("There are total ", len(bg15_output), " rows :")
#         print("UPDATED row from database : ",bg15_output[0])
#         # print("STORE NAME                       RENT")
#         # for i in range(len(bg15_output)):
#         #     result = "   ".join(str(x) for x in bg15_output[i])
#         #     print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
#
#
#
#
#
#
# def bg_14():
#     print("Fetch all rows from the data set")
#
#     bg14_query = """SELECT * FROM """
#
#
#     try:
#         print("Please select the table name to fetch the data from that table:")
#         print("1.Fall22_S004_5_person")
#         print("2.Fall22_S004_5_event_employee")
#         print("3.Fall22_S004_5_event_teams")
#         print("4.Fall22_S004_5_event_stores")
#         print("5.Fall22_S004_5_teams")
#         print("6.Fall22_S004_5_event")
#         print("7.Fall22_S004_5_stores")
#         print("8.Fall22_S004_5_audience_tickets")
#         print("9.Fall22_S004_5_employee_supervisor")
#         print("10.Fall22_S004_5_employee")
#         print("11.Fall22_S004_5_parking_audience")
#         print("12.Fall22_S004_5_audience")
#         print("13.Fall22_S004_5_person_phone")
#         print("14.Fall22_S004_5_audience_event")
#         table_num = input("Please select the table name to fetch the data from above list :")
#         match table_num:
#             case "1":
#                 table_name = "Fall22_S004_5_person"
#                 column_names = "person_id , Name, mail, gender, street, apt_number , zipcode"
#             case "2":
#                 table_name = "Fall22_S004_5_event_employee"
#                 column_names = "employee_id , event_id , clock_in, clock_out , event_date"
#             case "3":
#                 table_name = "Fall22_S004_5_event_teams"
#                 column_names = "event_id , team"
#             case "4":
#                 table_name = "Fall22_S004_5_event_stores"
#                 column_names = "store_id , event_id "
#             case "5":
#                 table_name = "Fall22_S004_5_teams"
#                 column_names = "team_name , team_category , sport, Is_UTA "
#             case "6":
#                 table_name = "Fall22_S004_5_event"
#                 column_names = "event_id , event_date , event_day , start_time , end_time ,event_category "
#             case "7":
#                 table_name = "Fall22_S004_5_stores"
#                 column_names = "store_id ,rent, store_category ,vendor_name ,date_of_payment "
#             case "8":
#                 table_name = "Fall22_S004_5_audience_tickets"
#                 column_names = "audience_id , ticket_id , ticket_category ,ticket_date ,  gate_number , seat_number "
#             case "9":
#                 table_name = "Fall22_S004_5_employee_supervisor"
#                 column_names = "employee_id , supervisor_id "
#             case "10":
#                 table_name = "Fall22_S004_5_employee"
#                 column_names = "person_id , SSN, date_of_joining , employee_category , salary"
#             case "11":
#                 table_name = "Fall22_S004_5_parking_audience"
#                 column_names = "parking_id , audience_id ,license_plate_number , price, parking_type ,date_of_parking  "
#             case "12":
#                 table_name = "Fall22_S004_5_audience"
#                 column_names = "person_id , audience_category"
#             case "13":
#                 table_name = "Fall22_S004_5_person_phone"
#                 column_names = "person_id , phone_number "
#             case "14":
#                 table_name = "Fall22_S004_5_audience_event"
#                 column_names = "event_id , audience_id "
#             case _:
#                 print("please select valid name from above table names")
#
#         bg14_query = bg14_query + table_name
#         cursor.execute(bg14_query)
#         # print("printing bg1_query command results here: ")
#         bg14_output = cursor.fetchall()
#         # print("There are total ", len(bg14_output), " rows :")
#         print(column_names)
#         for i in range(len(bg14_output)):
#             result = "  ".join(str(x) for x in bg14_output[i])
#             print(result)
#         print("There are total ", len(bg14_output), " rows :")
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
#
# def bg_13():
#     print("Listing the temporary stores available for every event")
#
#     bg13_query = """SELECT store_id, event_id from Fall22_S004_5_event_stores WHERE store_id IN (SELECT store_id FROM Fall22_S004_5_stores WHERE store_category = 'Temporary')"""
#
#     try:
#         cursor.execute(bg13_query)
#         # print("printing bg1_query command results here: ")
#         bg13_output = cursor.fetchall()
#         print("There are total ", len(bg13_output), " rows :")
#         print("STORE NAME                       RENT")
#         for i in range(len(bg13_output)):
#             result = "                  ".join(str(x) for x in bg13_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
# def bg_12():
#     print("Generating list of all parking IDs to find number of parking spots booked under each category")
#
#     bg12_query = """
#     SELECT license_plate_number ,parking_id,COUNT(*)
#     OVER (PARTITION BY license_plate_number ) AS total_PARKING_SLOTS_BOOKED
#     FROM   Fall22_S004_5_parking_audience """
#
#     try:
#         cursor.execute(bg12_query)
#         # print("printing bg1_query command results here: ")
#         bg12_output = cursor.fetchall()
#         print("There are total ", len(bg12_output), " rows :")
#         print("STORE NAME                       RENT")
#         for i in range(len(bg12_output)):
#             result = "                  ".join(str(x) for x in bg12_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
#
# def bg_11():
#     print("Q11) CUBE : Generate report for all stores along with rent,total rent for each category and sum of total rent till date.")
#
#     bg11_query = """
#     SELECT store_id,store_category,sum(rent) AS Total_Rent  FROM Fall22_S004_5_stores GROUP BY CUBE  (store_id,store_category) ORDER BY 2"""
#     try:
#         cursor.execute(bg11_query)
#         # print("printing bg1_query command results here: ")
#         bg11_output = cursor.fetchall()
#         print("There are total ", len(bg11_output), " rows :")
#         print("STORE NAME                       RENT")
#         for i in range(len(bg11_output)):
#             result = "                  ".join(str(x) for x in bg11_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
# def bg_10():
#     print("ROLL-UP : Generate report for total amount of rent received till date including all years and display rent of each store yearly :")
#
#     bg10_query = """SELECT store_id ,sum(rent) AS Total_Rent FROM Fall22_S004_5_stores GROUP BY ROLLUP(store_id)"""
#     try:
#         cursor.execute(bg10_query)
#         # print("printing bg1_query command results here: ")
#         bg10_output = cursor.fetchall()
#         print("There are total ", len(bg10_output), " rows :")
#         print("STORE NAME                       RENT")
#         for i in range(len(bg10_output)):
#             result = "                  ".join(str(x) for x in bg10_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
# def bg_9():
#     valid1 = 0
#     print("generating the category of tickets which has highest sales :")
#
#     bg9_query = """
#     SELECT Fall22_S004_5_audience_tickets.ticket_category, (COUNT(Fall22_S004_5_audience_tickets.ticket_id)) FROM Fall22_S004_5_audience_tickets
#     GROUP BY Fall22_S004_5_audience_tickets.ticket_category order by ticket_category desc fetch first 1 row only"""
#     try:
#         cursor.execute(bg9_query)
#         # print("printing bg1_query command results here: ")
#         bg9_output = cursor.fetchall()
#         print("There are total ", len(bg9_output), " rows :")
#         print("Ticket CATEGORY      #NO OF TICKETS SOLD")
#         for i in range(len(bg9_output)):
#             result = "                  ".join(str(x) for x in bg9_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
#
#
# def bg_8():
#     valid1 = 0
#     print("fetch top n teams that has more number of people attending their games :")
#
#     while valid1 != 1:
#         n = input("please enter the n value :")
#         if n == '-1':
#             return 0
#
#         valid1 = check_integer(n)
#         if valid1 == 0:
#             print("please enter a valid input")
#     if valid1 == 1:
#         bg8_query = """
#         select Fall22_S004_5_event_teams.team,COUNT(Fall22_S004_5_audience_event.audience_id) AS NO_OF_ATTENDEES
#         from Fall22_S004_5_audience_event INNER JOIN
#         Fall22_S004_5_event_teams ON Fall22_S004_5_audience_event.event_id = Fall22_S004_5_event_teams.event_id
#         GROUP BY (Fall22_S004_5_event_teams.team) ORDER BY NO_OF_ATTENDEES DESC
#             fetch  first """
#
#         bg8_query = bg8_query + " " + n + " rows only"
#         print("bg3_query : ", bg8_query)
#         try:
#             cursor.execute(bg8_query)
#             print("printing bg1_query command results here: ")
#             bg8_output = cursor.fetchall()
#             print("There are total ", len(bg8_output), " rows :")
#             print("TEAM NAME                        #NO of Audience")
#             for i in range(len(bg8_output)):
#                 result = "      ".join(str(x) for x in bg8_output[i])
#                 print(result)
#         except cx_Oracle.DatabaseError as e:
#             print("There is a problem with Oracle", e)
#
#
# def bg_7():
#     valid1 = 0
#     print("Generate report of TOP n employees based on number of working shifts :")
#
#     while valid1 != 1:
#         n = input("please enter the n value :")
#         if n == '-1':
#             return 0
#
#         valid1 = check_integer(n)
#         if valid1 == 0:
#             print("please enter a valid input")
#     if valid1 == 1:
#         bg7_query = """
#         select employee_id , count(clock_out-clock_in) AS NO_OF_SHIFTS from Fall22_S004_5_event_employee
#         GROUP BY Fall22_S004_5_event_employee.employee_id ORDER BY NO_OF_SHIFTS DESC
#         fetch  first """
#
#         bg7_query = bg7_query + " " + n + " rows only"
#         print("bg3_query : ", bg7_query)
#         try:
#             cursor.execute(bg7_query)
#             print("printing bg1_query command results here: ")
#             bg7_output = cursor.fetchall()
#             print("There are total ", len(bg7_output), " rows :")
#             print("EMPLOYEE-ID  Total Number of shifts")
#             for i in range(len(bg7_output)):
#                 result = "      ".join(str(x) for x in bg7_output[i])
#                 print(result)
#         except cx_Oracle.DatabaseError as e:
#             print("There is a problem with Oracle", e)
#
#
# def bg_6():
#     print("Generating a  report of Number of Audiences for every category :")
#
#     bg6_query = """
#     SELECT Fall22_S004_5_audience.audience_category, COUNT(Fall22_S004_5_audience.person_id) AS COUNT
#     FROM Fall22_S004_5_audience
#     INNER JOIN Fall22_S004_5_audience_event
#     ON Fall22_S004_5_audience.person_id  = Fall22_S004_5_audience_event.audience_id
#     GROUP BY (Fall22_S004_5_audience.audience_category)"""
#     try:
#         cursor.execute(bg6_query)
#         # print("printing bg1_query command results here: ")
#         bg6_output = cursor.fetchall()
#         print("There are total ", len(bg6_output), " rows :")
#         print("AUDIENCE CATEGORY  No# OF Audience")
#         for i in range(len(bg6_output)):
#             result = "              ".join(str(x) for x in bg6_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
# def bg_5():
#     valid1 = 0
#     print("calculate annual revenue based on ticket sales :")
#
#     bg5_query = """
#     select to_char(ticket_date, 'yyyy') ,SUM(
#     CASE ticket_category WHEN 'BRONZE' THEN '25'
#        WHEN 'SILVER' THEN '40'
#        WHEN 'GOLD ' THEN '60'
#        WHEN 'PLATINUM' THEN '80'END ) REVENUE
#        FROM Fall22_S004_5_audience_tickets group by
#     to_char(ticket_date, 'yyyy') order BY REVENUE DESC"""
#     try:
#         cursor.execute(bg5_query)
#         # print("printing bg1_query command results here: ")
#         bg5_output = cursor.fetchall()
#         print("There are total ", len(bg5_output), " rows :")
#         print("YEAR  REVENUE IN DOLLARS")
#         for i in range(len(bg5_output)):
#             result = "      ".join(str(x) for x in bg5_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
#
# def bg_4():
#     valid1 = 0
#     print("Fetch bottom n event ids based on revenue generated :")
#
#     while valid1 != 1:
#         n = input("please enter the n value :")
#         if n == '-1':
#             return 0
#
#         valid1 = check_integer(n)
#         if valid1 == 0:
#             print("please enter a valid input")
#     if valid1 == 1:
#         bg4_query = """
#         SELECT Fall22_S004_5_audience_event.event_id AS EVENT_ID ,
#         SUM(
#         CASE ticket_category WHEN 'BRONZE' THEN '25'
#            WHEN 'SILVER' THEN '40'
#            WHEN 'GOLD ' THEN '60'
#            WHEN 'GOLD' THEN '60'
#            WHEN 'PLATINUM' THEN '80'END ) REVENUE
#         FROM Fall22_S004_5_audience_event
#         INNER JOIN Fall22_S004_5_audience_tickets
#         ON Fall22_S004_5_audience_event.audience_id  = Fall22_S004_5_audience_tickets.audience_id
#         GROUP BY (Fall22_S004_5_audience_event.event_id) ORDER BY REVENUE ASC
#         fetch  first """
#
#         bg4_query = bg4_query + " " + n + " rows only"
#         print("bg3_query : ", bg4_query)
#         try:
#             cursor.execute(bg4_query)
#             print("printing bg1_query command results here: ")
#             bg4_output = cursor.fetchall()
#             print("There are total ", len(bg4_output), " rows :")
#             print("EVENT-ID  REVENUE IN DOLLARS")
#             for i in range(len(bg4_output)):
#                 result = "      ".join(str(x) for x in bg4_output[i])
#                 print(result)
#         except cx_Oracle.DatabaseError as e:
#             print("There is a problem with Oracle", e)
#
#
# def bg_3():
#     valid1=0
#     print("Fetch top n event ids based on revenue generated :")
#
#     while valid1!=1 :
#         n = input("please enter the n value :")
#         if n == '-1':
#             return 0
#
#         valid1 = check_integer(n)
#         if valid1 ==0:
#             print("please enter a valid input")
#     if valid1 ==1:
#         bg3_query = """
#         SELECT Fall22_S004_5_audience_event.event_id AS EVENT_ID ,
#         SUM(
#         CASE ticket_category WHEN 'BRONZE' THEN '25'
#         WHEN 'SILVER' THEN '40'
#         WHEN 'GOLD ' THEN '60'
#         WHEN 'GOLD' THEN '60'
#         WHEN 'PLATINUM' THEN '80'END ) REVENUE
#         FROM Fall22_S004_5_audience_event
#         INNER JOIN Fall22_S004_5_audience_tickets
#         ON Fall22_S004_5_audience_event.audience_id  = Fall22_S004_5_audience_tickets.audience_id
#         GROUP BY (Fall22_S004_5_audience_event.event_id) ORDER BY REVENUE DESC
#         fetch  first """
#
#         bg3_query =  bg3_query +" "+  n +  " rows only"
#         print("bg3_query : ", bg3_query)
#         try:
#             cursor.execute(bg3_query)
#             print("printing bg1_query command results here: ")
#             bg3_output = cursor.fetchall()
#             print("There are total ", len(bg3_output), " rows :")
#             print("EVENT-ID  REVENUE IN DOLLARS")
#             for i in range(len(bg3_output)):
#                 result = "      ".join(str(x) for x in bg3_output[i])
#                 print(result)
#         except cx_Oracle.DatabaseError as e:
#             print("There is a problem with Oracle", e)
#
# def bg_2():
#     bg2_query = """
#     select to_char(ticket_date, 'yyyy-mm') ,SUM(
#     CASE ticket_category WHEN 'BRONZE' THEN '25'
#     WHEN 'SILVER' THEN '40'
#     WHEN 'GOLD ' THEN '60'
#     WHEN 'PLATINUM' THEN '80'END ) REVENUE
#     FROM Fall22_S004_5_audience_tickets group by
#     to_char(ticket_date, 'yyyy-mm') order BY REVENUE DESC"""
#
#     try:
#         cursor.execute(bg2_query)
#         print("printing bg1_query command results here: ")
#         bg2_output = cursor.fetchall()
#         print("There are total ", len(bg2_output), " rows :")
#         print("YEAR-MONTH  REVENUE IN DOLLARS")
#         for i in range(len(bg2_output)):
#             result = "      ".join(str(x) for x in bg2_output[i])
#             print(result)
#     except cx_Oracle.DatabaseError as e:
#         print("There is a problem with Oracle", e)
#
#
# def bg_1():
#     valid1 =0
#     valid2=0
#     print("INSIDE BG1 :")
#     print("comparing revenue of 2 event id's based on revenue: ")
#
#     while valid1!=1 :
#         event1 = input("please enter 1st event id :")
#         if event1 == '-1':
#             return 0
#
#         valid1 = check_integer(event1)
#         if valid1 ==0:
#             print("please enter a valid input")
#
#
#     while valid2!=1 :
#         event2 = input("please enter 2nd event id :")
#         if event1 == '-1':
#             return 0
#         valid2 = check_integer(event1)
#         if valid2 ==0:
#             print("please enter a valid input")
#
#     if valid1 == 1 and valid2 == 1 :
#         bg1_query = """
#         SELECT Fall22_S004_5_audience_event.event_id AS EVENT_ID ,
#         SUM(
#         CASE ticket_category WHEN 'BRONZE' THEN '25'
#         WHEN 'SILVER' THEN '40'
#         WHEN 'GOLD ' THEN '60'
#         WHEN 'PLATINUM' THEN '80'END ) REVENUE
#         FROM Fall22_S004_5_audience_event
#         INNER JOIN Fall22_S004_5_audience_tickets
#         ON Fall22_S004_5_audience_event.audience_id  = Fall22_S004_5_audience_tickets.audience_id
#         GROUP BY (Fall22_S004_5_audience_event.event_id) HAVING (Fall22_S004_5_audience_event.event_id IN
#         """
#         bg1_query = bg1_query + "('" + str(event1) +  "', '" + str(event2) + "'))"
#         try:
#             cursor.execute(bg1_query)
#             print("printing bg1_query command results here: ")
#             bg1_outputb = cursor.fetchall()
#             print("There are total ", len(bg1_outputb), " rows :")
#             print(bg1_outputb)
#         except cx_Oracle.DatabaseError as e:
#             print("There is a problem with Oracle", e)
#
# # execute_bg1_query(85650,14438)
#
# print("\n*** WELCOME TO SPORTS EVENT MANAGEMENT ***\n")
#
# print("List of all Business goals:  \n")
# print("Q1) Compare revenue of 2 events based on event id ?")
# print("Q2) Generate report of month vs revenue ?")
# print("Q3) Generate report of TOP n event ids based on revenue, ex: top 5 events")
# print("Q4) Generate report of BOTTOM n event ids based on revenue, ex: bottom 5 events")
# print("Q5) Generate report of Revenue by Tickets for every year")
# print("Q6) Generate report of Number of Audiences for every category")
# print("Q7) Generate report of TOP n employees based on number of  working shifts")
# print("Q8) Generate report of Top n Teams vs number of audience attended for the team")
# print("Q9) Which category tickets are sold most along with number of tickets sold for this category")
# print("Q10) ROLL-UP : Generate report for total amount of rent received till date including all years and display rent of each store yearly")
# print("Q11) CUBE : Generate report for all stores along with rent,total rent for each category and sum of total rent till date.")
# print("Q12) Generate list of all parking IDs to find number of parking spots booked under each category")
# print("Q13) List the temporary stores available for every event")
# print("Q14) Get all rows fromm the table ")
# print("Q15) Update table : Fall22_S004_5_audience_tickets")
# print("Please enter 'EXIT' to exit")
#
# bg=0
#
# while bg != 'exit':
#     bg = input("Select any business goal using business goal number : (example : 10) : ")
#     print("bg requested = ", bg)
#     match bg:
#         case "1":
#             bg_1()
#         case "2":
#             bg_2()
#         case "3":
#             bg_3()
#         case "4":
#             bg_4()
#         case "5":
#             bg_5()
#         case "6":
#             bg_6()
#         case "7":
#             bg_7()
#         case "8":
#             bg_8()
#         case "9":
#             bg_9()
#         case "10":
#             bg_10()
#         case "11":
#             bg_11()
#         case "12":
#             bg_12()
#         case "13":
#             bg_13()
#         case "14":
#             bg_14()
#         case "15":
#             bg_15()
#
#
#         case _:
#             print("please enter valid query number")