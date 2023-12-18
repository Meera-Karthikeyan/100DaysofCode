logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
from replit import clear
#As used replit console importing the clear() from replit module
from art import logo
print(logo)
to_continue = True
bidder = {}
while to_continue:
  name = input("What is your name?")
  bid = int(input("What is your bid?"))
  bidder[name] = bid
  value = input("Are there any other bidders, Yes or No?")
  if value == "yes":
    clear()
  else:
    to_continue = False
    result = 0
    for name in bidder:
      bid_final = bidder[name]
      if bid_final > result:
        result = bid_final
        final_name = name

    
print(f"The winner is {final_name} is the highest bidder of ${result}")
