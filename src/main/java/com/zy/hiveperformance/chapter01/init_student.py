# coding: utf-8
import random
import datetime
import importlib,sys
importlib.reload(sys)
#sys.set('utf-8')

#lastname和firstname随机构造名称
lastname = '阿斯顿发顺丰案发生法法师阿斯顿发生发送到发送到发送到发沙发的说法是的发送到发生的过去额我如果企鹅额地方国企而过去而二哥'
firstname = '阿斯顿发斯蒂芬高峰期诶啊哦改回去饿哦很奇怪去撒大V爱国前卫和覅偶千万别过期肉更方便去饿哦不能去群殴IE改回去我过不去欧股份不起而融'

def create_student_dict(start):
   firstlen = len(firstname)
   lastlen = len(lastname)
   scoreList = [int(random.normalvariate(100,50)) for _ in range(1,5000)]
   filename = str(start) + '.txt'
   print(filename)
   with open('./' + filename,mode='w+') as fp:
     for i in range(start * 40000, (start+1)*40000):
         firstind = random.randint(1,firstlen - 4)
         model = {"s_no" : u"xuehao_no_" + str(i),
                  "s_name":u"{0}{1}".format(lastname[random.randint(1,lastlen - 1)],firstname[firstind:firstind + 1]),
                  "s_birth":u"{0}-{1}-{2}".format(random.randint(1991,2000),'0' + str(random.randint(1,9)),random.randint(10,28)),
                  "s_age":random.sample([20,20,20,20,21,22,23,24,25,25],1)[0],
                  "s_sex":str(random.sample(['男','女'],1)[0]),
                  "s_score":abs(33),
                  "s_dec":u"大恶趣味二分区二分"u"服务器二分法" * random.randint(1,20)}
         fp.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(
             model['s_no'],model["s_name"],model["s_birth"],model["s_age"],
             model["s_sex"],model["s_score"],model["s_dec"]
         ))

for i in range(1,501):
    starttime = datetime.datetime.now()
    create_student_dict(i)
