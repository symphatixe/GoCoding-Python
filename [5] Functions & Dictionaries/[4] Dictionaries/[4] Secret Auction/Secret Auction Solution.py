# Starter Code
import os

auction_bids = {}
bidding_finished = False

# Write your code below

from art import logo
print(logo)


def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = auction_bids[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winning bid is from {winner} with an amount of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?\n")
    amount = float(input("What is the bid amount, in $USD?\n"))

    auction_bids[name] = amount
    continue_bid = input("Bid has been added. Are there other bidders?\n").lower()

    match continue_bid:
        case "yes":
            os.system("cls")
        case "no":
            bidding_finished = True

            print("Auction has finished!")
            find_highest_bidder(auction_bids)
        case _:
            bidding_finished = True
            print("Unknown entry. Exiting...")