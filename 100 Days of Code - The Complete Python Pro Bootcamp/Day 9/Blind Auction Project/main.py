# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
def find_highest_bidder(bidding_dictionary):
    winner =""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the highest bid is ${highest_bid}")
bids = {}
continue_bid = True
while continue_bid:
    name = input("what is your name? ")
    bid = int(input("what is your bid? $"))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    bids[name]=bid
    if other_bidders == "no":
        continue_bid = False
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        print("\n" * 50)





















