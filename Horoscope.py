"""
Horoscope
Karla D
This program will simulate a horoscope consultation.
The user will enter personal information such as their name,
birth date, birthplace, and current mood. The program will
automatically determine the user's zodiac sign based and
generate personalized predictions, advice, and recommendations
related to love, friendships, studies, work, and personal well-being.

"""

def age(current_year, birth_year):
    return current_year-birth_year

def data():
    name=input("Enter your name: ")
    current_year=int(input("Enter the current year: "))
    birth_day=int(input("Enter your day of birth (dd): "))
    birth_month=int(input("Enter your month of birth (mm): "))
    birth_year=int(input("Enter the year of birth (aaaa): "))
    birth_hour=float(input("Enter your hour of birth (considerate hours as integers and minutes as decimals): "))
    Age=age(current_year, birth_year)
    
def num_destiny(birth_day,birth_month,birth_year):
    suma= birth_day+birth_month,birth_year
    n=0
    while suma>0:
        if suma=!11 and suma=!22 and suma=!33:
            digito1=suma%10
            n=n+digito
            digito2=int(suma/10)
            n=n+digito
        else:
            n=suma
    if n==1:
        print("Your destiny number is ",n)
        print("""
The Leader - You are independent, ambitious, and original.
You were born to forge your own path, take the initiative,
and lead projects without depending on others.
Your greatest strength is determination, although you should be careful
not to fall into excessive individualism.
""")
    elif n==2:
        print("Your destiny number is ",n)
        print("""
The Mediator - You are cooperative, empathetic, and sensitive.
You have a natural talent for connecting people,
resolving conflicts, and working as part of a team.
You create harmony around you, but you should be careful not to
put off your own needs in order to please others.
""")
    elif n==3:
        print("Your destiny number is ",n)
        print("""
The Communicator - You are optimistic, charismatic, and creative.
Artistic expression and words are your greatest
tools. You inspire others with your enthusiasm
and vitality, although your constant challenge is to maintain
focus and not scatter your energy.
""")
    elif n==4:
        print("Your destiny number is ",n)
        print("""
The Builder - You are organized, disciplined, and reliable.
You are someone who knows how to build solid foundations for
the future. Your pragmatic approach guarantees results,
but try to remain flexible when facing
unexpected changes.
""")
    elif n==5:
        print("Your destiny number is ",n)
        print("""
The Explorer - You are free-spirited, curious, and adventurous.
You thrive in dynamic environments, dislike routine,
and adapt easily to change.
Your life is filled with constant learning,
although you should be careful that your search for novelty
does not lead to inconsistency.
""")
    elif n==6:
        print("Your destiny number is ",n)
        print("""
The Protector - You are helpful, fair, and altruistic.
You are a safe haven for your family and community.
You enjoy creating environments of beauty and harmony, but
you should avoid taking on responsibilities that are not yours.
""")
    elif n==7:
        print("Your destiny number is ",n)
        print("""
The Analyst - You are analytical, intuitive, and reflective.
You are drawn to deep knowledge, research, and
spirituality. You need moments of solitude to
recharge your energy and process what you have learned.
""")
    elif n==8:
        print("Your destiny number is ",n)
        print("""
The Achiever - Your path is closely tied to material
accomplishment, authority, and strategic success.
You have a clear business vision, leadership
abilities, and a strong drive to achieve ambitious goals.
Your challenge is to maintain an ethical balance between
power and inner well-being.
""")
    elif n==9:
        print("Your destiny number is ",n)
        print("""
The Humanitarian - Your vision of life is broad,
compassionate, and idealistic. You feel a deep empathy
for global well-being and possess the wisdom
needed to close cycles and move beyond different stages of life.
You inspire others through generosity and altruism.
""")
    elif n==11:
        print("Your destiny number is ",n)
        print("""
The Messenger - You possess heightened intuition and an
almost mystical perception of your surroundings. Your mission is to act
as a channel of inspiration and awareness for others,
connecting higher ideas with earthly reality.
The challenge lies in channeling the intense emotional energy
that you carry.
""")
    elif n==22:
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


def zodiac(birth_day, birth_month):
    sign=""
    if birth_month==1:
        if birth_day<=19:
            sign="CAPRICORN"
        else:
            sign="AQUARIUS"
    elif birth_month==2:
        if birth_day<=18:
            sign="AQUARIUS"
        else:
            sign="PISCES"
    elif birth_month==3:
        if birth_day<=20:
            sign="PISCES"
        else:
            sign="ARIES"
    elif birth_month==4:
        if birth_day<=19:
            sign="ARIES"
        else:
            sign="TAURUS"
    elif birth_month==5:
        if birth_day<=20:
            sign="TAURUS"
        else:
            sign="GEMINI"
    elif birth_month==6:
        if birth_day<=20:
            sign="GEMINI"
        else:
            sign="CANCER"
    elif birth_month==7:
        if birth_day<=22:
            sign="CANCER"
        else:
            sign="LEO"
    elif birth_month==8:
        if birth_day<=22:
            sign="LEO"
        else:
            sign="VIRGO"
    elif birth_month==9:
        if birth_day<=22:
            sign="VIRGO"
        else:
            sign="LIBRA"
    elif birth_month==10:
        if birth_day<=22:
            sign="LIBRA"
        else:
            sign="SCORPIO"
    elif birth_month==11:
        if birth_day<=21:
            sign="SCORPIO"
        else:
            sign="SAGITTARIUS"
    elif birth_month==12:
        if birth_day<=21:
            sign="SAGITTARIUS"
        else:
            sign="CAPRICORN"
    else:
        sign="Invalid value"
    return sign

def tests():
    current_year=2026
    birth_day=7
    birth_month=2
    birth_year=2008
    print("Age: ",age(current_year, birth_year))
    print("Zodiac sign: ", zodiac(birth_day, birth_month))
    print("Expected result: 18, AQUARIUS")
    birth_day=6
    birth_month=8
    birth_year=2006
    print("Age: ",age(current_year, birth_year))
    print("Zodiac sign: ", zodiac(birth_day, birth_month))
    print("Expected result: 20, LEO")
    
            
def menu():
    print("HOROSCOPE")
    print("1. My data")
    print("2. I want to know my zodiac sign")
    print("3. Divine number and it´s meaning")
    print("4. Run tests")
    print("5. Exit")


def main():
    menu()
    option=int(input("Select option: "))
    while True:
        if option==1:
            if name=="" or birth_month="" or current_year="":
                data()
            else:
                print("Name: ",name)
                print("Birth date: ",birth_day,"/",birth_month,"/",birth_year)
                print("Hour of birth: ",birth_hour,"am" if birth_hour<12 else "pm")
                print("Age: ",Age)
                change=input("Do you want to change them? yes/no: ")
                if change=="yes":
                    data()
        elif option==2:
            print("Your zodiac sign is ", zodiac(birth_day, birth_month))
        elif option ==3:
            num_destiny(birth_day,birth_month,birth_year)
        elif option==5:
            print("End of consult")
            break
        elif option==4:
            tests()
        else:
            print("That option does not exist")
        option=int(input("Select another option: "))
            
    
main()
            



