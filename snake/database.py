
'''
File Paths
Relative Path
Absolute Path
'''
with open('database.txt','w+',encoding='utf-8') as file:
    file.write('mohamed')
    file.seek(0)
    content=file.read()
    print(content)