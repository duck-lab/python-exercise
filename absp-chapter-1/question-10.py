#-*-coding:utf-8-*-
# 为什么这个表达式会导致错误？如何修复？
# 'I have eaten' + 99 + 'burritos'


# 因为str型数据不能直接与整型数据连接，须将整型数据转换成str型数据
# 可改写成 
print ('I have eaten' +' ' +str(99)+ ' ' + 'burritos')