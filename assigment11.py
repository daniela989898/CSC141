# 11-1
def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
# 11-2
from city_functions import city_country
def test_city_country():
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'
def test_city_country_population():
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – population 5000000'
# 11-3
from employee import Employee
def test_give_default_raise():
    emp = Employee('juan', 'perez', 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000
def test_give_custom_raise():
    emp = Employee('juan', 'perez', 50000)
    emp.give_raise(10000)
    assert emp.annual_salary == 60000