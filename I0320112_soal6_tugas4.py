x = 4       #4  = 0000 0100
y = 11      #11 = 0000 1011

#4 | 11
a = x|y
print('nilai 4|11  :',a,'   binary :',format(a,'08b'))

#4 >> 11
a = x >> y
print('nilai 4>>11 :',a,'    binary :',format(a,'08b'))

#4 ^ 11
a = x ^ y
print('nilai 4^11  :',a,'   binary :',format(a,'08b'))

#~4
a = ~x
print('nilai ~4    :',a,'   binary :',format(a,'08b'))

#11 & 4
a = y & x
print('nilai 4&11  :',a,'    binary :',format(a,'08b'))
