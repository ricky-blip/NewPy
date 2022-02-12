# Bitwise Operator
# Operator for binaries

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('==========OR==========')
print('nilai :',a,',', 'binary :', format(a,'08b')) # format (variabel,'08b')) adalah untuk mencetak variabel ke dalam bentuk biner
print('nilai :',b,',', 'binary :', format(b,'08b'))
print('---------------------------------------(|)')
print('hasil :',c,',binary :', format(c,'08b')) 

# bitwise AND (&)
c = a & b
print('==========AND==========')
print('nilai :',a,',', 'binary :', format(a,'08b'))
print('nilai :',b,',', 'binary :', format(b,'08b'))
print('---------------------------------------(&)')
print('hasil :',c,', binary :', format(c,'08b')) 

# bitwise XOR (^)
c = a ^ b
print('==========XOR==========')
print('nilai :',a,',', 'binary :', format(a,'08b'))
print('nilai :',b,',', 'binary :', format(b,'08b'))
print('---------------------------------------(^)')
print('hasil :',c,',binary :', format(c,'08b')) 

# bitwise NOT (~)
c = ~a 
print('==========NOT==========')
print('nilai :',a,',', 'binary :', format(a,'08b'))
print('---------------------------------------(~)')
print('hasil  :',c,',binary :', format(c,'08b'))# karena a = 9, maka not dari 9 adalah -10 (diMirror) di dalam operasi bitwise 
print('==========NOT(FLIP)==========')
d = 0b0000001001
e = 0b1111111111
print('---------------------------------------(^)')
print('hasil  :',e^d,',binary :', format(e^d,'08b'))

# bitwise shifting

# shift right (>>)
f = b >> 2
print('==========SHIFT>>==========')
print('nilai :',b,',', 'binary :', format(b,'08b'))
print('---------------------------------------(>>)')
print('hasil :',f,', binary :', format(f,'08b'))

# shift left (<<)
f = b << 2
print('==========<<SHIFT==========')
print('nilai :',b,',', 'binary :', format(b,'08b'))
print('---------------------------------------(<<)')
print('hasil :',f,',binary :', format(f,'08b'))
