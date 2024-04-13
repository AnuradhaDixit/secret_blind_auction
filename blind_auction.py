from replit import clear
from art import logo

print(logo)
auction_dict = {}
bid_list = []
auction_open = True
auction_bid = 0

def auction(name, bid):  
  auction_dict[name] = bid
  print(auction_dict)

while auction_open:
  name = str(input("What is your name?"))
  bid = int(input("What's your bid? $"))
  auction_dict[name] = bid
  bid_list.append(auction_dict[name])
  more_bids = str(input("Are there any other bidders?type 'yes' or 'no' ")).lower()
  if more_bids == "yes":
    auction_open = True
    clear()
  elif more_bids == "no":
    auction_open = False
    auction(name, bid)
    for winner in bid_list:
      if winner > auction_bid:
        auction_bid = winner
    position = bid_list.index(auction_bid)
    key_position = list(auction_dict.keys())[position]
    print (f'The winner is {key_position} with bid of $ {auction_bid}')
  else:
    print("Invalid input")