import datetime
import fmath
from colorama import Fore, Style, init
init(convert=True)

print(Fore.RED + "Hola mundo")

print(datetime.date.today())

print(datetime.timedelta(minutes=50000))

fmath.add(40, 50)
fmath.restar(50, 40)