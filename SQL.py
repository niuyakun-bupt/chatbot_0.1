__author__ = 'dell'
import sqlite3
conn=sqlite3.connect("QAtemplate.db")
curs=conn.cursor()#获得游标
conn.cursor()#完成查询后，要确保提交任务，每次修改数据库时都应该提交
conn.close()


