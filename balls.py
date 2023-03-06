import os
import sys
try:
    import holehe
except ImportError:
    print("Holehe not found. Exiting! (this means install it retard)")
    exit()

def giantcock():
   if sys.platform == "linux":
    os.system("clear")
   elif sys.platform == "win32":
    os.system("cls")
giantcock()

femboy = "Email Osint | Made by Lotus"
print(f'\33]0;{femboy}\a', end='', flush=True)

#too lazy to add google people api into this so do it yourself lmao

sus = input("Enter the target email: ")
giantcock()
print("Holehe:") #yes i was too lazy to actually use the module lol
os.system(f'holehe --only-used {sus}')
if "@gmail.com" in sus:
  #print(f"Google ID: {id}")
  #gayglemaps = f"https://www.google.com/maps/contrib/{id}"
  cock = f"https://calendar.google.com/calendar/u/7/embed?src={sus}"
  print(f"\nGoogle Calendar: {cock}")
else:
  pass
