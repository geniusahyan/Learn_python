import pymysql
def CreateConn():
    return pymysql.connect(
        host='localhost', 
        database='ahyandb',
        user='root', 
        password='Life@Ahyan7',
        port=3306
    )
    
# def CreateTable():
#     conn = CreateConn()
#     cursor = conn.cursor()
#     query = 'create table student(sid int primary key auto_increment, name VARCHAR(50), email VARCHAR(50), city VARCHAR(50))'
#     cursor.execute(query)
#     conn.commit()
#     print('table creater')
#     conn.close()
    
# CreateTable()

# def InsertData(name,email,city):
#     conn = CreateConn()
#     cursor = conn.cursor()
#     args = (name,email,city)
#     query = 'insert into student(name,email,city)value(%s,%s,%s)'
#     cursor.execute(query,args)
#     conn.commit()
#     print('data inserted')
#     conn.close()
    
# InsertData('Ahyan','something@gmail.com','Motihari')

def showalldata(sid):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (sid)
    # query = 'select * from student'
    query = 'select * from student where sid=%s'
    cursor.execute(query,args)
    # result = cursor.fetchall()
    result = cursor.fetchall()
    for i in result:
        print(i)
        

# def updateData(name,email,city,sid):
#     conn = CreateConn()
#     cursor = conn.cursor()
#     args = (name,email,city,sid)
#     query = 'update student set name=%s,email=%s,city=%s where sid=%s'
#     cursor.execute(query,args)
#     conn.commit()
#     print('updated')
#     conn.close()
    
# updateData('another','aslam@gmail.com','mirpur',2)
# showalldata(2)

def DeleteDate(sid):
    conn = CreateConn()
    cursor = conn.cursor()
    args = (sid)
    query = 'delete from student where sid=%s'
    cursor.execute(query,args)
    conn.commit()
    print('data deleted')
    conn.close()
    
showalldata(2)
DeleteDate(2)
showalldata(2)
