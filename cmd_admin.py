import os
import datetime

                        # генерирование строчки для командной строки
now = datetime.datetime.now()
name_dir = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)

source = 'D:/project_Python/BackupISOGD/src/1 '
dest = 'D:/project_Python/BackupISOGD/Test_robocopy/' + str(name_dir)
codirovka = 'C:\Windows\System32\chcp 65001'
bcp = 'C:/Windows/System32/robocopy ' + \
      source + \
      dest + \
      ' /maxage:20221118 /E /COPYALL /Z /B /J /R:3 /W:1 /REG ' \
      '/LOG+:D:/project_Python/BackupISOGD/Test_robocopy/' + name_dir + '.log'

                        # Запуск командной строки

os.system(codirovka)
os.system(bcp)


