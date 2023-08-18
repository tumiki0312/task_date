import datetime
text = '数学xx:xx~xx:xx\n物理xx:xx~xx:xx\n化学xx:xx~xx:xx\n英語(文法)xx:xx~xx:xx\n英語(単語)xx:xx~xx:xx'
datetime_now = datetime.datetime.now()
dt_string = datetime_now.strftime("%Y年%m月%d日")
file_path = "C:/Users/tumik/text_auto_generated/text_list/"
file_extension = ".txt"
text_path = file_path + dt_string + file_extension
f = open(text_path,'w')
writer = f.write(text)
closer = f.close()