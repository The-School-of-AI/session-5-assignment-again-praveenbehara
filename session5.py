"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
from datetime import datetime
import math

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    # Repetition should be positive number
    total_time = 0
    for _ in range(repetitions):
        start = datetime.now()
        fn(args, kwargs)
        total_time += datetime.now() - start
    return total_time


def squared_power_list(number, *args, start=0, end=5, **kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if (type(number) is not int):
        raise TypeError("Only integer type arguments are allowed")
    elif (number >= 10):
        raise ValueError("Value of number should be less than 10")
    
    if (start < 0 or end < 0):
        raise ValueError("Value of start or end can't be negative")
    elif (start >= end):
        raise ValueError("Value of start should be less than end")
    
    if (len(args) > 0):
        raise TypeError("takes maximum 1 positional arguments")
    elif (len(kwargs) > 0):
        raise TypeError("maximum 2 keyword/named arguments")

    # Return the list of number to the power of numbers from start to end
    lst = [pow(base=number, exp=cnt)  for cnt in range(start, end)]
    return lst

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 both inclusive"""

    # Validations
    if (type(length) not in [int, float]):
        raise TypeError("Only int or float values are allowed for length")
    elif (type(sides) is not int):
        raise TypeError("Only int values are allowed for sides")

    if (length <= 0):
        raise ValueError("Length value should be greater than 0")
    
    if (sides < 3 or sides > 6):
        raise ValueError("Sides need to between 3 and 6, both inclusive")

    if (len(args) > 0):
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    elif (len(kwargs) > 0):
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    
    # Return area
    if sides == 3:
        return math.sqrt(3)*pow(length, 2)/4.0
    elif sides == 4:
        return length * length
    elif sides == 5:
        return pow(length, 2) * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) / 4.0
    else:
        return pow(length, 2) * 3 * math.sqrt(3) / 2.0
 
def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if (type(temp) not in [int, float]):
        raise TypeError("Only int or float values are allowed for temperature")

    if (temp_given_in.lower() == 'c' and temp < -273.15):
        raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
    elif (temp_given_in.lower() == 'f' and temp < -459.67):
        raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")

    if (not type(temp_given_in) is str):
        raise TypeError("Character string expected")
    elif (temp_given_in.lower() not in ['f', 'c']):
        raise ValueError("Only f or c is allowed")

    if (len(args) > 0):
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    elif (len(kwargs) > 0):
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature
    if temp_given_in.lower() == 'f':
        return (temp- 32) * 5 / 9.0
    else:
        return (temp * 9 / 5.0) + 32

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    dist, time = dist.lower(), time.lower()

    # Validations
    if (not any(type(speed) is t for t in [int, float])):
        raise TypeError("Speed can be int or float type only")

    if (not type(dist) is str):
        raise TypeError(f"Character string expected for distance unit. Provided {time}")
    
    if (not type(time) is str):
        raise TypeError(f"Character string expected for time. Provided {time}")
    
    if (speed < 0):
        raise ValueError("Speed can't be negative")
    elif (speed > 300000):
        raise ValueError("Speed can't be greater than speed of light")

    if (not any(time == x for x in ['ms', 's', 'min', 'hr', 'day'])):
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    
    if (not any(dist == x for x in ['km', 'm', 'ft', 'yrd'])):
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    
    if (len(args) > 0):
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    elif (len(kwargs) > 0):
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

    # Return the converted speed
    if (dist == 'km'):
        mul_fac = dict(zip(['ms', 's', 'min', 'hr', 'day'], [1/3600000.0, 1/3600, 1/60.0, 1, 24]))
        return int(speed * mul_fac[time])
    elif (dist == 'm'):
        mul_fac = dict(zip(['ms', 's', 'min', 'hr', 'day'], [1/3600.0, 1/3.6, 1/0.06, 1000, 24000]))
        return int(speed * mul_fac[time])
    elif (dist == 'ft'):
        pass
    elif (dist == 'yrd'):
        pass
