import pymysql;
import re;

db = pymysql.connect('123456', '123456', '123456@123456', '123456');

cursor = db.cursor(pymysql.cursors.DictCursor);

cursor.execute("select * from ielts_experience_topic where questions REGEXP '^[0-9]{1,}'");

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall();

print(len(data));

print(data);

i = 0;
length = len(data);
rep = re.compile('[\d|\.|\ ]');
while i < length:
    rowQuestions = data[i]['questions'];
    id = data[i]['id'];
    print(type(id));
    print(rowQuestions);
    rowQuestions = rep.sub('', rowQuestions);
    rowQuestions = rowQuestions.replace('\'', '\\\'');
    print(rowQuestions);
    sql = "update ielts_experience_topic set questions = '%s' where id = %d" % (rowQuestions, id);
    print(sql);
    cursor.execute(sql);
    db.commit();
    i += 1;

# 关闭数据库连接
db.close();