## We check the type of the data
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
print(type(temperatures_C))

## Minimum temperature
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
min_temp=[min(temperatures_C)]
print("The minimun temperature during the days was", min_temp,"degrees celsius")

## Maximum temperature
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
max_temp=[max(temperatures_C)]
print("The maximun temperature during the days was", max_temp,"degrees celsius")

## Temperatures equal to or greater than 70ºC
x = 70
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
greater_equal = [temps for temps in temperatures_C if temps >= x]
print("This are the temperatures equal or greater than 70 Celsius:",greater_equal)

## another way

temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
greater_equal=[]
for temp in temperatures_C:
    if temp >= 70:
        greater_equal.append(temp)
print("This are the temperatures equal or greater than 70 Celsius:",greater_equal)

## Average temperatures throughout the day.
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
import statistics
average = statistics.mean(temperatures_C)
print("The average temperature during the day was",average,"degrees celsius")

## If there was a sensor failure at 03:00 and we did not capture the data, how would you estimate the missing value? Correct that value in the list of temperatures.
# Estimating the missing value could be an approach to deal with the missing value.

## We search if there is a wrong vale like 0
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
for temps in temperatures_C:
    if temps == 0:
        print("We found and unexpected value. The value is:",temps)
    else:
        pass

#We modify that value
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
temperatures_C[3] = 62
print("The modified list with the corrected value:",temperatures_C)

## We find it and modify automatically. The condition used in here is if the temperature is equal to 0.
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
for temp in range(len(temperatures_C)):
    if temperatures_C[temp] == 0:
        temperatures_C[temp] = 32
print("The modified list with the corrected value:",temperatures_C)


## Bonus: Our maintenance staff is from the United States and does not understand the international metric system. Convert temperatures to Degrees Fahrenheit.
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,69,80,83,68,79,61,53,50,49,53,48,45,39]
fahrenheit = []
for temps in temperatures_C:
    f = (temps * 1.8) + 32
    fahrenheit.append(f)

print(fahrenheit)
