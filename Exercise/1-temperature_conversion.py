#Exercise 1

print("\n====Conversion Temperature in Celcius====\n")
celcius = float(input("Type Temperature in Celcius :"))

print("Your Input",celcius,"Celsius","=","|", 
        (4/5)*celcius,"in Reamur","|", 
        (9/5)*celcius+32,"in Fahrenheit","|", 
        celcius+273.15,"in Kelvin","|")

print("\n====Conversion Temperature in Reamur====\n")
reamur = float(input("Type Temperature in Reamur:"))

print("Your Input",reamur,"Reamur","=","|", 
        (5/4)*reamur,"in Celcius","|", 
        (9/4)*reamur+32,"in Fahrenheit","|", 
        (5/4)*reamur+273.15,"in Kelvin","|")

print("\n====Conversion Temperature in Fahrenheit====\n")
fahrenheit = float(input("Type Temperature in Fahrenheit:"))

print("Your Input",fahrenheit,"Fahrenheit","=","|",
        round((fahrenheit-32)*5/9,3),"in Celsius","|",
        round((fahrenheit-32)*4/9,3),"in Reamur","|",
        round((fahrenheit-32)*5/9+273.15,3),"in Kelvin","|")

print("\n====Conversion Temperature in Kelvin====\n")
kelvin = float(input("Type Temperature in Kelvin:"))

print("Your Input",kelvin,"Kelvin","=","|",
        kelvin-273.15,"in Celsius","|",
        (kelvin-273.15)*0.8,"in Reamur","|",
        kelvin*1.8-459.67,"in Fahrenheit","|")






