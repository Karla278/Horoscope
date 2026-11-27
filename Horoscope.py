"""
Horoscope
Karla D
This program will simulate a horoscope consultation.
The user will enter personal information such as their name,
birth date and birth hour. The program will
automatically determine the user's zodiac sign and
generate personalized predictions, advice, and recommendations
related to personality and daily life.

"""

import random
import requests
from bs4 import BeautifulSoup


def age(current_year, birth_year):
    """
    Calculates the age of the user in years
    """
    if isinstance(current_year, int) or isinstance(birth_year, int):
        return current_year - birth_year
    else:
        return "Registered current year or birth year are not integers"


def data():
    """
    Inputs the personal data of the user
    """
    name = input("Enter your name: ")
    current_year = int(input("Enter the current year: "))
    birth_day = int(input("Enter your day of birth (dd): "))
    birth_month = int(input("Enter your month of birth (mm): "))
    birth_year = int(input("Enter the year of birth (aaaa): "))
    birth_hour = float(input("Enter your hour of birth (considerate hours as integers and minutes as decimals): "))
    Age = age(current_year, birth_year)
    return name, current_year, birth_day, birth_month, birth_year, birth_hour, Age


def num_destiny(birth_day,birth_month,birth_year):
    """
    Adds the numbers in the birth date of the user until it´s only one number or a master number (11,22,33) and returns a description 
    of the user´s personality based on that number

    Inputs: birth date (day, month and year)
    Outputs: Destiny number and description related
     
    """
    if isinstance(birth_day, int) or isinstance(birth_month, int) or isinstance(birth_year, int):
        bd = 0
        bm = 0
        by = 0
        while birth_day > 0:
            bd += birth_day % 10
            birth_day = birth_day // 10
        while birth_month > 0:
            bm += birth_month % 10
            birth_month = birth_month // 10
        while birth_year > 0:
            by += birth_year % 10
            birth_year = birth_year // 10
        suma = bd + bm + by
        n = 0
        while suma > 0:
            if suma != 11 and suma != 22 and suma != 33:
                digit1 = suma % 10
                digit2 = int(suma / 10)
                n=digit1 + digit2
                if n > 9 and n != 11 and n != 22 and n != 33:
                    n = (n % 10) + int(n / 10)
            else:
                n = suma
            suma = 0
        if n == 1:
            print("Your destiny number is ",n)
            print("""
The Leader - You are independent, ambitious, and original.
You were born to forge your own path, take the initiative,
and lead projects without depending on others.
Your greatest strength is determination, although you should be careful
not to fall into excessive individualism.
""")
        elif n == 2:
            print("Your destiny number is ",n)
            print("""
The Mediator - You are cooperative, empathetic, and sensitive.
You have a natural talent for connecting people,
resolving conflicts, and working as part of a team.
You create harmony around you, but you should be careful not to
put off your own needs in order to please others.
""")
        elif n == 3:
            print("Your destiny number is ",n)
            print("""
The Communicator - You are optimistic, charismatic, and creative.
Artistic expression and words are your greatest
tools. You inspire others with your enthusiasm
and vitality, although your constant challenge is to maintain
focus and not scatter your energy.
""")
        elif n == 4:
            print("Your destiny number is ",n)
            print("""
The Builder - You are organized, disciplined, and reliable.
You are someone who knows how to build solid foundations for
the future. Your pragmatic approach guarantees results,
but try to remain flexible when facing
unexpected changes.
""")
        elif n == 5:
            print("Your destiny number is ",n)
            print("""
The Explorer - You are free-spirited, curious, and adventurous.
You thrive in dynamic environments, dislike routine,
and adapt easily to change.
Your life is filled with constant learning,
although you should be careful that your search for novelty
does not lead to inconsistency.
""")
        elif n == 6:
            print("Your destiny number is ",n)
            print("""
The Protector - You are helpful, fair, and altruistic.
You are a safe haven for your family and community.
You enjoy creating environments of beauty and harmony, but
you should avoid taking on responsibilities that are not yours.
""")
        elif n == 7:
            print("Your destiny number is ",n)
            print("""
The Analyst - You are analytical, intuitive, and reflective.
You are drawn to deep knowledge, research, and
spirituality. You need moments of solitude to
recharge your energy and process what you have learned.
""")
        elif n == 8:
            print("Your destiny number is ",n)
            print("""
The Achiever - Your path is closely tied to material
accomplishment, authority, and strategic success.
You have a clear business vision, leadership
abilities, and a strong drive to achieve ambitious goals.
Your challenge is to maintain an ethical balance between
power and inner well-being.
""")
        elif n == 9:
            print("Your destiny number is ",n)
            print("""
The Humanitarian - Your vision of life is broad,
compassionate, and idealistic. You feel a deep empathy
for global well-being and possess the wisdom
needed to close cycles and move beyond different stages of life.
You inspire others through generosity and altruism.
""")
        elif n == 11:
            print("Your destiny number is ",n)
            print("""
The Messenger - You possess heightened intuition and an
almost mystical perception of your surroundings. Your mission is to act
as a channel of inspiration and awareness for others,
connecting higher ideas with earthly reality.
The challenge lies in channeling the intense emotional energy
that you carry.
""")
        elif n == 22:
            print("Your destiny number is ",n)
            print("""
The Master Builder - You have the potential to transform
great abstract ideals into real and tangible projects
that positively impact society. You combine the intuitive
vision of the 11 with the pragmatic discipline of the 4. It is an
energy of great scope that demands a high level of commitment.
""")
        else:
            print("Your destiny number is ",n)
            print("""
The Guide - Your energy represents unconditional love and the
highest expression of service. You have the calling to guide,
protect, and elevate the awareness of those around you
through example and deep empathy. Your challenge is to take care of
your own energy while supporting others.
""")
    else:
        print("Registered birth date is not an integer")


def zodiac(birth_day, birth_month):
    """
    Uses the month and day of birth to determine the zodiac sign of the user
    """
    if isinstance(birth_day, int) or isinstance(birth_month, int):
        sign = ""
        if birth_month == 1:
            if birth_day <= 19:
                sign = "CAPRICORN"
            else:
                sign = "AQUARIUS"
        elif birth_month == 2:
            if birth_day <= 18:
                sign = "AQUARIUS"
            else:
                sign = "PISCES"
        elif birth_month == 3:
            if birth_day <= 20:
                sign = "PISCES"
            else:
                sign = "ARIES"
        elif birth_month == 4:
            if birth_day <= 19:
                sign = "ARIES"
            else:
                sign = "TAURUS"
        elif birth_month == 5:
            if birth_day <= 20:
                sign = "TAURUS"
            else:
                sign = "GEMINI"
        elif birth_month == 6:
            if birth_day <= 20:
                sign = "GEMINI"
            else:
                sign = "CANCER"
        elif birth_month == 7:
            if birth_day <= 22:
                sign = "CANCER"
            else:
                sign = "LEO"
        elif birth_month == 8:
            if birth_day <= 22:
                sign = "LEO"
            else:
                sign = "VIRGO"
        elif birth_month == 9:
            if birth_day <= 22:
                sign = "VIRGO"
            else:
                sign = "LIBRA"
        elif birth_month == 10:
            if birth_day <= 22:
                sign = "LIBRA"
            else:
                sign = "SCORPIO"
        elif birth_month == 11:
            if birth_day <= 21:
                sign = "SCORPIO"
            else:
                sign = "SAGITTARIUS"
        elif birth_month == 12:
            if birth_day <= 21:
                sign = "SAGITTARIUS"
            else:
                sign = "CAPRICORN"
        else:
            sign = "Invalid value"
        return sign
    else:
        return "Registered brith date is not an integer"

def compatibility(sign1, sign2):
    """
    Creates a matrix 12*12 with the zodiac signs and their compatibility, it compares 2 given signs to find the row and 
    coulumn where they intersect, returning the compatibility rate between them

    Inputs: sign 1 and sign 2
    Outputs: compatibility rate between the input signs

    """
    if isinstance(sign1, str) or isinstance(sign2, str):
        Rate = ["High", "Low", "Medium"]
        matrix = [["capricorn", "aquarius", "pisces", "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius"]]
        if sign1 in matrix[0] and sign2 in matrix[0]:
            for element in matrix[0]:
                row = []
                for i in range(12):
                   row.append(Rate[random.randint(0,2)])
                row.insert(0, element)
                matrix.append(row)
            matrix[0].insert(0, "vacio")        
            columna = matrix[0].index(sign1)
            fila = matrix[0].index(sign2)
            compatible_rate = matrix[fila][columna]
            return compatible_rate
        else:
            print("One or both signs aren´t in the list")
    else:
        return "One or both signs aren´t strings"


def astral_name(name, sign):
    """
    Combines the users name and sign to create an alias

    Inputs: name, sign
    Outputs: name composition

    """
    if isinstance(name, str) or isinstance(sign, str):
        NAME = name[:3] + sign[-3:]
        print("Your astral name is: ", NAME.upper())
    else: 
        print("Registered name or sign aren´t str")


def astro_events(file):
    """
    1. Searches the date given in the file and returns the astrological event corresponding to it.
    2. Allows the user to add new events to the file
    
    inputs: date, file
    Outputs: Astrological event or " Event added successfuly "

    """
    op=input("Do you want to add or consult an event? add/consult: ")
    if op == "consult":
        date = input("In wich date do you wanna consult? Enter dd/mm/2026: ")
        with open (file, "r") as file:
            res = ""
            for line in file:
                if line[:10] == date:
                    res = line[13:]
            if res == "":
                print("There is no important astrological event in this date")
            else: 
                print(res)
    elif op == "add":
        Date = input("Write the date of the event dd/mm/aaaa: ")
        event = input("Write the event you want to add: ")
        with open(file,"a") as file:
            file.write(f"{Date} - {event.capitalize()}\n")
            print("Event added successfuly")


def consult_horoscope(sign, day, month, year):
    """
    Consult the daily horoscope from Vogue given a date and a name.
    
    Inputs: sign, day, month and year
    Output: Horoscope form Vogue
    """
    months = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
    ]
    clean_month = months[int(month) - 1] 
    clean_day = str(int(day)) 
    clean_sign = sign.strip().capitalize() 
    
    url = f"https://www.vogue.in/content/horoscope-today-{clean_month}-{clean_day}-{year}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        answer = requests.get(url, headers=headers)
        
        if answer.status_code != 200:
            return f"The horoscope for this date is not found (Error {answer.status_code}). Verify the URL: {url}"
            
        soup = BeautifulSoup(answer.text, "html.parser")
        
        encabezados = soup.find_all(["h2", "h3"])
        
        for encabezado in encabezados:
            if clean_sign in encabezado.get_text():
                paragraph = encabezado.find_next("p")
                if paragraph:
                    return paragraph.get_text(strip=True)
                    
        return f"The page has loaded, but there isn´t a section for '{clean_sign}'"
        
    except Exception as e:
        return f"An error has ocured when loading the page: {e}"
    85


def menu():
    print("\n")
    print("...................................................................................")
    print("HOROSCOPE")
    print("1. My data")
    print("2. I want to know my zodiac sign")
    print("3. Destiny number and it´s meaning")
    print("4. Compatibility")
    print("5. Astral name")
    print("6. Astrological events")
    print("7. Consult daily horoscope prediction in Vogue")
    print("8. Exit")
    print("...................................................................................")
    print("\n")


def main():
    menu()
    option = int(input("Select option: "))
    name = ""
    birth_month = ""
    birth_year = ""
    birth_day = ""
    current_year = ""
    while True:
        if option == 1:
            print("\n")
            if name == "" or birth_month == "" or current_year == "":
                datos = data()
                name = datos[0]
                current_year = datos[1]
                birth_day = int(datos[2])
                birth_month = int(datos[3])
                birth_year = int(datos[4])
                birth_hour = datos[5]
                Age = datos[6]
            else:
                print("Name: ", name)
                print("Birth date: ", birth_day, "/", birth_month, "/", birth_year)
                print("Hour of birth: ", birth_hour, ("am" if birth_hour < 12 else "pm"))
                print("Age: ", Age)
                change = input("Do you want to change them? yes/no: ")
                if change == "yes":
                    name, current_year, birth_day, birth_month, birth_year, birth_hour, Age = data()
        elif option == 2:
            print("\n")
            if birth_month == "" or birth_day == "":
                print("You need to fill the data first")
            else:
                print("Your zodiac sign is ", zodiac(birth_day, birth_month).upper())
        elif option == 3:
            print("\n")
            if birth_month == "" or birth_day == "":
                print("You need to fill the data first")
            else:
                num_destiny(birth_day, birth_month, birth_year)
        elif option == 4:
            print("\n")
            sign1 = input("Enter sign 1: ").lower()
            sign2 = input("Enter sign 2: ").lower()
            print("The compatibility between these signs is ", compatibility(sign1, sign2))
        elif option == 5:
            print("\n")
            if birth_month == "" or birth_day == "":
                print("You need to fill the data first")
            else:
                astral_name(name, zodiac(birth_day, birth_month))
        elif option == 6:
            print("\n")
            archivo = "astrological_events.txt"
            astro_events(archivo)
        elif option == 7:
            print("\n")
            if birth_month == "" or birth_day == "":
                print("You need to fill the data first")
            else:
                date = input("Introduce the date for consultation dd/mm/aaaa: ")
                day, month, year = date.split("/")
                print("\n")
                print(consult_horoscope(zodiac(birth_day, birth_month), day, month, year))
        elif option == 8:
            print("\n")
            print("End of consult")
            break
        else:
            print("\n")
            print("That option does not exist")
        menu()
        option = int(input("Select another option: "))
            
    
main()
        