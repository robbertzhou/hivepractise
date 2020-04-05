# coding: utf-8
import random,datetime
def create_student_sc_dic(start):
    filename = str(start) + '.txt'
    print(start)
    with open('./' + filename , mode= 'w+') as fp:
        for i in range(start * 40000,(start + 1)*40000):
            course = random.sample([u'数学',u'数学',u'数学',u'数学',u'数学',
                                    u'语文',u'英语',u'化学',u'物理',u'生物'],1)[0]
            model = {"s_no":u"xuehao_no_" + str(i),
                     "course":u'{0}'.format(course),
                     "op_datetime":datetime.datetime.now().strftime("%y-%m-%d"),
                     "reason":u'我非常非常'u"非常非常非常非常非常非常{0}".format(course)}
            line = "{0}\t{1}\t{2}\t{3}"\
                .format(model['s_no'],model['course'],model['op_datetime'],model['reason'])
            fp.write(line)

for i in range(1,501):
    starttime = datetime.datetime.now()
    create_student_sc_dic(i)