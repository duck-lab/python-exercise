#-*-coding:utf-8-*-
# 识别这段代码中的3个语句块

spam = 0
if spam == 10:
	print('eggs')
	if spam > 5:
		print('bacon')
	else:
		print('ham')
	print('spam')
print('spam')

# 第1个语句块：开始，第6行print('eggs')；结束，第11行print('spam')
# 第2个语句块：只有，第8行print('bacon')；
# 第3个语句块：只有，第10行print('ham')；