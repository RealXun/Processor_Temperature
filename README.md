# Processor_Temperature
We have a temperature sensor in our company's server processor and we want to analyze the data.
<p align="center">
    <img src="https://github.com/RealXun/Processor_Tmperature/blob/main/Resources/Cover.png">
    
We have a temperature sensor in the processor of our company's server. We want to analyze the data provided to analyze if we should change the cooling system for a better one. It is expensive and as a data analyst we cannot make decisions without basis.

We provide the measured temperatures throughout the 24 hours of a day in a list-like data structure made up of 24 integers:
```
temperaturas_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
```

## Problem

If the sensor detects more than 4 hours with temperatures greater than or equal to 70ºC or any temperature greater than 80ºC or the average is greater than 65ºC throughout the day, we must give the order to change the cooling system to avoid damaging the processor.

We are going to guide you step by step so that you can make the decision calculating some intermediate steps:

1. Minimum temperature
2. Maximum temperature
3. Temperatures equal to or greater than 70ºC
4. Average temperatures throughout the day.
5. If there was a sensor failure at 03:00 and we did not capture the data, how would you estimate the missing value? Correct that value in the list of temperatures.
6. Bonus: Our maintenance staff is from the United States and does not understand the international metric system. Convert temperatures to Degrees Fahrenheit.

Formula: F = 1.8 * C + 32

web: https://es.wikipedia.org/wiki/Grado_Fahrenheit

## Taking the decission
Remember that if the sensor detects more than 4 hours with temperatures greater than or equal to 70ºC or any temperature greater than 80ºC or the average is greater than 65ºC throughout the day, we must give the order to change the cooling system to avoid the danger of damaging the equipment:
* more than 4 hours with temperatures greater than or equal to 70ºC
* some temperature higher than 80ºC
* average outside above 65ºC throughout the day
If any of these three are met, the cooling system will have to be changed.

## Objectives
1. List processing
2. Use of loop or list comprehension
3. Calculation of the average, minimum and maximum.
4. List filtering.
5. Interpolate an outlier.
6. Logical operators.
7. Print by console
