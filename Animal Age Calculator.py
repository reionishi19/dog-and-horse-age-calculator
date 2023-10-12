"""
Rei Onishi
August 31, 2023

This is a program that will convert human ages to dog and horse years.
"""

""" Simple human to dog age conversion"""
human_age = float(input('Enter age'))
dog_age = human_age * 7 #dog age is human age multiplied by 7

print(f'{human_age} human years is {dog_age} dog years')

""" Specific year/month/day human to dog age conversion """
# This is the human age
human_age = float(input('Enter age: '))

#This will calculate dog ages by multiplying human age by 7
dog_age_years = float(human_age * 7)
dog_years = dog_age_years // 1

#This will calculate dog ages into months
dog_age_months = ((dog_age_years - dog_years) * 12)
dog_months = dog_age_months // 1

#This will calculate dog ages into days
dog_age_days = ((dog_age_months - dog_months) * 30)
dog_days = dog_age_days // 1


print(f'{human_age} human years is {dog_years} years, {dog_months} months, and {dog_days} days in dog age.')

""" Simple human to horse age conversion"""

import math
human_age = float(input('Enter age'))
horse_age = 3 * ((((human_age ** 2) - 47) / 7) + 12)

print(horse_age)

""" Specific year/month/day human to horse age conversion """

# This is the human age
human_age = float(input('Enter age: '))

#This will calculate horse ages by using the formula
horse_age_years = float(3 * ((((human_age ** 2) - 47) / 7) + 12))
horse_years = horse_age_years // 1

#This will calculate dog ages into months
horse_age_months = ((horse_age_years - horse_years) * 12)
horse_months = horse_age_months // 1

#This will calculate dog ages into days
horse_age_days = ((horse_age_months - horse_months) * 30)
horse_days = horse_age_days // 1


print(f'{human_age} human years is {horse_years} years, {horse_months} months, and {horse_days} days in horse age.')
