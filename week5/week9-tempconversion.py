#!/usr/bin/env python3

import f2c
import c2f

def main():
    number = int(input("What is the temperature you would like to convert? "))
    measure = input("Is this temperature in Fahrenheit(f) or Celcius(c)? ")

# Convert the input to lowercase for both the letter and the word to work successfully for different variations of input
    if measure.lower() == "f" or measure.lower() == "fahrenheit":
        print(f2c.f_to_c(number))
    elif measure.lower() == "c" or measure.lower() == "celcius":
        print(c2f.c_to_F(number))

main()