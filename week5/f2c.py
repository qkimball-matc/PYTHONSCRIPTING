#!/usr/bin/env python3

def f_to_c(number):
   return ((number - 32) * 5/9 )

def main():
    number = int(input("What is the temperature in Fahrenheit you would like to convert to Celsius? "))
    print(f_to_c(number))

if __name__ == "__main__":
    main()