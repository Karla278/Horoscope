
## Horoscope
A horoscope is a prediction or interpretation of different aspects of life for each of the 12 zodiac signs (Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, and Pisces), which is determined by the sun's position on a person's birth date. Although astrology is not an exact science and is primarily used for entertainment and leisure, it plays a meaningful role in daily self-reflection.

Even without scientific accuracy, reading a horoscope can encourage people to reflect on their life choices, provide motivation to accomplish postponed projects, or offer a sense of calm and perspective when feeling lost or overwhelmed. However, users usually have to visit multiple websites or apps to access different astrological tools.

This program solves that problem by simulating a complete, centralized horoscope consultation in Python. The user enters personal information (such as their name, birth date, and birth hour) and the system automatically calculates their age, determines their zodiac sign, and unlocks personalized astrological and numerological features.   In addition to basic zodiac identification, the program includes several interactive features. The user will be able to: 

  - Manage and update their personal profile data (name, birth date, birth hour, and age).
  - Calculate their numerological Destiny Number (including master numbers 11, 22, and 33) along with a detailed personality analysis.
  - Check compatibility between any two zodiac signs using a dynamically generated 12x12 matrix.
  - Generate a personalized Astral Name by combining letters from their name and zodiac sign.
  - Consult and record important astrological events in a local text file (astrological_events.txt).
  - Fetch real-time daily horoscope predictions directly from Vogue via web scraping.

## Algorithm
  1. Display the main interactive menu with 8 available options.
  2. Prompt the user to select an option and enter their personal data (name, current year, birth day, birth month, birth year, and birth hour).
  3. Calculate the user's current age and determine their zodiac sign based on their birth month and day.
  4. Process the user's selected feature:
       - Destiny Number: Sum and reduce the digits of the birth date to display the corresponding personality profile.
       - Compatibility: Build a 12x12 zodiac matrix with randomized compatibility rates (High, Medium, Low) and locate the intersection of two input signs.
       - Astral Name: Slice and concatenate characters from the user's name and zodiac sign.
       - Astrological Events: Read or append date-event records in astrological_events.txt.
       - Daily Horoscope: Send an HTTP request to Vogue India for the specified date and parse the HTML to display the prediction for the user's sign.
   5. Display the results clearly in the console.
   6. Repeat the menu loop until the user selects Option 8 to exit the consultation.   
