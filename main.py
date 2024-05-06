import sys

banned_brands = ["Amazon", "Colgate", "Starbucks", "Apple", "Johnson", "Coca Cola", "HP", "Adidas", "Calvin Klein", "Google", "Ikea", "McDonald's"]
brands_to_review = []

def banner():
  font = """
.______   .______          ___      .__   __.  _______       ______  __    __   _______   ______  __  ___ 
|   _  \  |   _  \        /   \     |  \ |  | |       \     /      ||  |  |  | |   ____| /      ||  |/  / 
|  |_)  | |  |_)  |      /  ^  \    |   \|  | |  .--.  |   |  ,----'|  |__|  | |  |__   |  ,----'|  '  /  
|   _  <  |      /      /  /_\  \   |  . `  | |  |  |  |   |  |     |   __   | |   __|  |  |     |    <   
|  |_)  | |  |\  \----./  _____  \  |  |\   | |  '--'  |   |  `----.|  |  |  | |  |____ |  `----.|  .  \  
|______/  | _| `._____/__/     \__\ |__| \__| |_______/     \______||__|  |__| |_______| \______||__|\__\
                                                                                    
"""
  print(font)

if __name__ == "__main__":
  banner()

def brand_check():
  print("\nCHECK A BRAND\n")
  prompt = input("To do a manual search by typing in the name of the brand, press 1 and ENTER. \n(Note: This is faster than scanning all the brands listed in alphabetical order, however please make sure you have the correct spelling \n as improper spelling could lead to an improper result!)\n \n If you would like to scan the list of boycotted brands in alphabetical order, enter 2. \n (Note: This is a safer option if you would like to eliminate spelling or potentially incorrect naming errors, \n however this list may take a little while longer to sift through).\n To be taken back to the main menu, type 3 and press ENTER. \n\n")

  if prompt == "1":
    manual_verification = input("Time to check a brand! Please be aware that our lists are only as comprehensive as the information that we have available in the public domain at this time. \n We cannot guarantee completely accuracy. \n Type the name of the brand that you would like to verify and press ENTER.\n\n")
    if manual_verification in banned_brands:
      print("\nThis brand DOES appear in our database of banned brands. \n Please seek alternative options. \n")
    elif manual_verification in brands_to_review:
      print("\nThis brand is under review. Please check back for an update. \n")
    else:
      print("\nThis brand DOES NOT appear in our list of banned brands! For the time being you may continue to shop from this company. \nPlease continue to check back for updates. \n")
  
  elif prompt == "2":
    print_brands()

  elif prompt == "3":
    main_menu()
  
  prompt2 = input("Think we’ve made a mistake? If so, type 3 and press ENTER. \n To return to the main menu type 1 and press ENTER. To exit the app type 2 and press ENTER.\n\n")
  if prompt2 == "3":
    edit_brand()
  elif prompt2 == "2":
    exit_bc()

def main_menu():
  # lists all of the options
  main_input = input("Thanks for logging in to Brand Check! Please choose from the options below: \n 1. Verify a Brand \n 2. Request a brand amendment. \n 3. Learn about this app. \n 4. Exit the app.\n\n")
  if main_input == "1":
    brand_check()
  elif main_input == "2":
    edit_brand()
  elif main_input == "3":
    about()
  elif main_input == "4":
    exit_bc()
  else:
    print("You have not selected a valid option, please select a valid menu item.")
    main_menu()
    
def print_brands():
  print("BANNED AND UNDER REVIEW BRANDS \n")
  input1 = input("To see the list of banned brands, press 1 and ENTER. \nTo see brands under review, press 2 and ENTER. \nTo go back to the main menu press 3 and ENTER. \n\n")
  if input1 == "1":
    print("\nHere is an up-to-date list of banned brands in alphabetical order. \n")
    if len(banned_brands) == 0:
      print("No brands are currently under review.")
      print_brands()
    sorted_brands = sorted(banned_brands)
    for item in sorted_brands:
      print(item + "\n")
  
  elif input1 == "2":
    print("Here is an up-to-date list of brands under review in alphabetical order. \n")
    sorted_review = sorted(brands_to_review)
    for item in sorted_review:
      print(item + "\n")

  elif input1 == "3":
    main_menu()

  else:
    print("Valid response not selected, you are being redirected to the main menu. \n")
    main_menu()


def edit_brand():
  print("\nOur database is in flux and is not fully comprehensive. If you think that there is an error and that a company should be on this list\n please follow these instructions.\n")
  input1 = input("To enter the amendment module, type “amend” (lower case) and press ENTER\n\n")
  if input1 == "amend":
    input2 = input("\nYou have selected 'amend'. If this is incorrect, please type 1 and ENTER to be taken back to the main menu. \n If you wish to continue, please type the name of the company to be added and then press ENTER.\n\n")
    if input2 == "1":
      main_menu()
    elif input2 in banned_brands:
      print("This brand is already in our list of banned brands! You will be redirected to the main menu.")
      main_menu()
    elif input2 in brands_to_review:
      print("This brand is already under review! You will be redirected to the main menu.")
      main_menu()
    else:
      input3 = input("\nWARNING: You have suggested an amendment to the database. After this step, an official request will be sent. \n If this is incorrect, press 1 and ENTER to exit this module and be taken back to the main menu. \n If this is correct, please provide us with any additional information on this brand that will help our research. If you have no further information, please type “N/A”.\n\n")
      if input3 == "1":
        main_menu()
      else:
        #add brand to review pile
        brands_to_review.insert(0,input3)
        print("\nThank you for proposing this addition to our database. \nOur team will look into your request and update the database if needed. You will be redirected to the main menu.\n")
        main_menu()
  else:
    print ("You have not typed 'amend', you will be redirected to the main menu\n")
    main_menu()

def about():
  input1 = input("This app was created to help users determine which brands are safe to purchase from. \n Boycotting is an effective strategy to fight injustice. \n This app can help you to make informed decisions on where you can safely purchase products.\n To return to the main menu press 1. To exit the app press 2.")
  if input1 == "1":
    main_menu()
  elif input1 == "2":
    exit_bc()
  
def exit_bc():
  print("Thanks for using Brand Check! Come back for future updates")
  sys.exit(0)


while True:
  # UI shows user list of actions that can be taken
  usr_data = input("Thanks for logging in to Brand Check!\n To verify a brand against the boycott list, press 1 and then ENTER.\n To see the full menu of options, press 2 and ENTER.\n\n")

  # If user enters 1, take them to the Brand check 
  if usr_data == "1":
    brand_check();

  # If user enters 2, take to main menu
  elif usr_data == "2":
    main_menu()

