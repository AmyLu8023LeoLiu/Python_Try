# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:03:43 2017
@author: Amy_Lu
"""
import random
import codecs

file = codecs.open("F:/1.txt", "w","utf-8")
for i in range(0,40):
          city = random.sample('冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤川青藏琼宁渝京津沪',1)
          Letter1 = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',1)
          Numbers5 = random.sample('0123456789',5)
          Car_Num = city + Letter1 + Numbers5
          Change = random.randint(0,1)
          if Change == 0 :
                    Car_Num_string = ''.join(Car_Num)
          elif Change == 1 :
                    Change_bit = random.randint(2,6)
                    Car_Num[Change_bit] = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',1) 
                    Car_Num[Change_bit] = ''.join(Car_Num[Change_bit])
                    Car_Num_string = ''.join(Car_Num)
          print(Car_Num_string)
          file.write(Car_Num_string + "\n")
file.close()
          



