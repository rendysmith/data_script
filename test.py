import os
import requests
import json

folder = []
for i in os.walk('event'):
    folder.append(i)

a = 0
for address, dirs, files in folder:
    for file in files:
        a += 1
        print ('-------------------------')
        print (a, file)

        with open('event/'+file, 'r', encoding='utf-8') as f: #открыли файл с данными

            text = json.load(f) #загнали все, что получилось в переменную
            #print (text)

            try:
                print ('***')
                for key in text:                   
                    print (key)
                print ('***')
                
                if 'id' not in text:
                    data = (f'-----------------\n{file}\n- Начало словаря с {list(text.keys())[0]}\n- Отсутствует ID, не верная схема, необходимо дополнить данные\n')
                    print (data)
                    f = open('README.txt', 'a')
                    f.write(data)
                    f.close()

                else:
                    data = (f'-----------------\n{file}\n- Данные в порядке\n')
                    print (data)
                    f = open('README.txt', 'a')
                    f.write(data)
                    f.close()
                    
            except:
  
                data = (f'-----------------\n{file}\n- Отсутствуют данные в файле!\n')
                print (data)
                f = open('README.txt', 'a')
                f.write(data)
                f.close()
                
                    
