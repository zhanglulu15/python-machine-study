
#利用枚举类型的字段的期望信息和连续型的字段的期望信息的计算方法
#学历分类中大专，本科，硕士所占比例
education = (2.0/12,5.0/12,5.0/12)
import math

#大专分类中相亲占比
junior_college = (1.0/2,1.0/2)

#本科分类中相亲占比
undegraduate_college = (3.0/5,2.0/5)

#硕士分类占比
master_college = (4.0/5,1.0/5)

#学历个分类相亲占比
date_per = (junior_college,undegraduate_college,master_college)

#相亲字段划分下的熵
def info_date(p):
    info = 0
    for v in p:
        info += v * math.log(v,2)
    return info
#使用学历字段划分规则下的熵
def infoA():
    info = 0
    for i in range(len(education)):
        info += -education[i] * info_date(date_per[i])
    return info
print(infoA())



#年龄字段分割
age = [25,25,28,29,30,33,34,35,36,40,46]

#是否相亲 1：是  0：否
date = [0,1,1,0,1,1,1,1,1,0,0,0]

#这里年龄从28和29中间切开
#左右分类中数量占总数的百分比
split_per = (4.0/12,8.0/12)


#左边分类中相亲占比
date_left = (1.0/2,1.0/2)

#右边分类相亲占比
date_right = (5.0/8,3.0/8)

#左右分类中相亲占比
date_per = (date_left,date_right)

#相亲字段划分下的熵
def info_date(p):
    info = 0
    for v in p:
        info += v*math.log(v,2)
    return info

#左右划分下的信息熵
def infoA():
    info = 0
    for i in range(len(split_per)):
        info += -split_per[i] * info_date(date_per[i])
    return info
print(infoA())
