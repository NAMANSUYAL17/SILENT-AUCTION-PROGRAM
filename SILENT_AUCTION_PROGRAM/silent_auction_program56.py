import os
print("**WELCOME TO SILENT AUCTION PROGRAM**")
def find_winner(bidder_details):
   highest_bid=0
   winner=""
   for bidder in bidder_details:
      bidding_price=bidder_details[bidder]
      if bidding_price>highest_bid:
          highest_bid=bidding_price
          winner=bidder
   print(f"here is the list of all bidders:{bidder_details}")       
   print(f"highest bid is made by {winner} of {highest_bid} ")
   


bidder_data={}
end_of_bidding=False
while not end_of_bidding:    
   name=input('enter the name of bidder:')
   bid_price=int(input('enter the bid price:'))
   bidder_data[name]=bid_price
   more_bidders=input('are there more bidders:type yes or no:').lower()
   if more_bidders=="no":
      end_of_bidding=True
      find_winner(bidder_data)
   elif more_bidders=='yes':
      os.system('cls')
      
