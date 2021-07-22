#!/usr/bin/env python3

def c_to_F(number):   
   return ((number * 9/5) + 32 )

def main():
    number = int(input("What is the temperature in Celcius you would like to convert to Fahrenheit? "))
    print(c_to_F(number))

if __name__ == "__main__":
    main()