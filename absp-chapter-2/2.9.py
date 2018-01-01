#-*-coding:utf-8-*-
# 编写代码，如果变量spam中存放1，就打印Hello，如果变量中存放2，
# 就打印Howdy，如果变量中存放其他值，就打印Greetings！


spam = int(input())

if spam == 1:
	print('Hello')
elif spam == 2:
	print('Howdy')
else:
	print('Greetings!')