# Import (Multi-file)

# how to import another file
import Import2      #import file name 'Import2.py'

print(Import2.data) #import variable from 'Import2.py'

Import2.checkingmodule() # import function from 'Import2.py'

print("\n" + 10*"=" + "Acces Module" + 10*"=")
import Import2 as CM # change name file with 'as'

CM.sum(2,2)

CM.minus(4,1)

print("\n" + 10*"=" + "Acces Module 2" + 10*"=")
from Import2 import sum, minus # import spesific

sum(5,5)
minus(10,3)

print("\n" + 10*"=" + "Acces Module 3" + 10*"=")
from Import2 import * # import All

sum(5,5)
minus(10,3)