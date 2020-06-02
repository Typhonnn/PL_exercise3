"""Tal Balelty - 312270291"""


class Twitter:
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.msg = ""
        self.received_tweet = ""

    def follow(self, who):
        who.followers.append(self)
        return self

    def tweet(self, msg):
        self.msg = msg
        print(msg)
        for follower in self.followers:
            follower.received_tweet = msg
            print("{} Tweet received: {}".format(follower.name, follower.received_tweet))


if __name__ == '__main__':
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    h = Twitter('Mad Hatter')
    c = Twitter('Cheshire Cat')
    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)

    print(f'==== {q.name} tweets ====')
    q.tweet('Off with their heads!')
    print(f'\n==== {a.name} tweets ====')
    a.tweet('What a strange world we live in.')
    print(f'\n==== {k.name} tweets ====')
    k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {c.name} tweets ====')
    c.tweet("We're all mad here.")
    print(f'\n==== {h.name} tweets ====')
    h.tweet('Why is a raven like a writing-desk?')
