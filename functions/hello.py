#a module is a file that contains python code
#many modules form a package


#Python Functions
#a function is a block of code that performs specific tasks
#By organizing coding functions we can reuse it as many times as you want

def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    year=2024-age
    print(f"Hello {name}, you were born in {year}")

#default value
def my_country(country="Uganda"):
    print(f'Hello Akirachix from {country}')

def greet(*namez):
    for name in namez:
        print(f"Hello {name}")
