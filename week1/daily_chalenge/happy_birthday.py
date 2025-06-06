from datetime import datetime
import calendar

def comparaisonDate(date):
    today = datetime.today().date()
    if date < today:
        diff_days = (today - date).days
        diff_years = diff_days // 365
    return int(diff_years)

def nombreDeBougies(nbr):
    lastDigit = nbr % 10
    if lastDigit == 0:
        return " "
    else:
        return "i" * lastDigit
    
def cake(bougie):
    print(f'''
       __{bougie:^7}__
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~''')


date_str = input("Entez une date de naissance (JJ-MM-AAAA): ")

try:
    user_date = datetime.strptime(date_str, "%d-%m-%Y").date()
    print(f"La date est : {user_date.strftime('%d-%m-%Y')}")

    bougie = nombreDeBougies(comparaisonDate(user_date))
    cake(bougie)
    if calendar.isleap(user_date.year):
        cake(bougie)
    
except ValueError:
    print("Format DD-MM-YYYY. SVP")
