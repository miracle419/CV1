def get_name():
  while True:
    try:
      user_name = input("Inpute your user name: ")
      if (user_name.isalpha() and user_name.isdigit() or len(user_name) >=6):
        print("Your user name is: ", user_name)
        break
      else:
        print("please inpute a valid user name")
    except ValueError:
        print("invalid inpute")
      
get_name()

def get_number():
    while True:
        try:
            number = int(input("Input a number up to 11: "))
            if len(str(number)) == 11:
                print("Valid number entered:", number)
                break
            else:
                print("Invalid input: Number should be up to 11 digits. Please try again.")
        except ValueError:
            print("Invalid input: Please enter a valid number.")

get_number()