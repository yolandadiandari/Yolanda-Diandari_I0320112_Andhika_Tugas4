x = 4       #4  = 0000 0100
y = 11      #11 = 0000 1011

#4 | 11     #15 = 0000 1111
a = x|y
print('nilai 4|11  :',a,'   binary :',format(a,'08b'))

#4 >> 11    #0 = 0000 0000
a = x >> y
print('nilai 4>>11 :',a,'    binary :',format(a,'08b'))

#4 ^ 11     #15 = 0000 1111
a = x ^ y
print('nilai 4^11  :',a,'   binary :',format(a,'08b'))

#~4         #-5 = 0000 0101
a = ~x
print('nilai ~4    :',a,'   binary :',format(a,'08b'))

#11 & 4     #0 = 0000 0000
a = y & x
print('nilai 4&11  :',a,'    binary :',format(a,'08b'))
