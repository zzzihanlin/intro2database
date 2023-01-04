# 创建表格
# sql = "CREATE TABLE income(id int, item varchar(50), value int);"
# cursor.execute(sql)
# database.commit()
# cursor.close()

# 添加数据
# sql = "INSERT INTO income VALUES(1, 'get up at 9:30', 20)"
# cursor.execute(sql)
# database.commit()
# cursor.close()

# 用循环添加数据
# for i in range(10, 20):
#     sql = "INSERT INTO income(id, item, value) VALUES(%s, %s, %s)"
#     item = 'leg workout'
#     value = random.choice([10, 20, 50])
#     data = (i, item, value)
#     cursor.execute(sql, data)
#     database.commit()
# cursor.close()

# 将已经存在的列设置为primary key
# sql = "ALTER TABLE income ADD PRIMARY KEY(id)"
# cursor.execute(sql)
# database.commit()
# cursor.close()

# 更改列名
# sql = "ALTER TABLE income RENAME COLUMN value TO amount"
# cursor.execute(sql)
# database.commit()
# cursor.close()

# 删除一行数据
# sql = "DELETE FROM income WHERE id = 19"
# cursor.execute(sql)
# database.commit()
# cursor.close()

# 修改一行数据
# sql = "UPDATE income SET amount = %s WHERE amount = %s"
# val = (50, 1000)
# cursor.execute(sql, val)
# database.commit()
# cursor.close()

# 查询
# sql = "SELECT item FROM income WHERE amount = 10"
# sql = "SELECT * FROM income WHERE amount = 20"
# sql = "SELECT * FROM income"
# cursor.execute(sql)
# result = cursor.fetchall()
# for i in result:
#     print(i)
# database.commit()
# cursor.close()
