class AuctionSubject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, bidder):
        for observer in self.observers:
            observer.update(bidder)

    def start_auction(self):
        print("Аукціон розпочато...")
        while True:
            bid = input("Введіть вашу ставку (або 'вийти', щоб завершити аукціон): ")
            if bid.lower() == 'вийти':
                print("Аукціон завершено.")
                break
            self.notify(bid)


class BidderObserver:
    def __init__(self, name):
        self.name = name

    def update(self, bid):
        print(f"{self.name} підвищив ставку до {bid}")


if __name__ == "__main__":
    auction = AuctionSubject()
    bidder1 = BidderObserver("Саша")
    bidder2 = BidderObserver("Петя")
    bidder3 = BidderObserver("Влад")

    auction.attach(bidder1)
    auction.attach(bidder2)
    auction.attach(bidder3)

    auction.start_auction()
