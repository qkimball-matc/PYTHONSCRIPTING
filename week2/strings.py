#!/usr/bin/env python3

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

print(f"Hello {varName}")
print(f"{varRed}-{varGreen}-{varBlue}")
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
print(f"My name is {varName.upper()}")
print(f"[++{varRed}++]")
print(f"[{varGreen.lower()}==]")
print(f"[*****{varBlue.lower()}]")
print(varBlue*10)
print(varLoot)
print(round(varLoot, 1))
print(f"I have ${round(varLoot,2)}")
print(f"[$$${varRed}$$$$][$${varGreen}$$$][$$${varBlue}$$$]")
print(f"[   {varRed[::-1]}   ][  {varGreen}   ][   {varBlue[::-1]}   ]")
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
