print("\n\t\tWELCOME TO GAME COMPENDIUM!!")
print("This game compendium has three games which are tic-tac-toe, War game and a Blackjack game!")
print(" Press 1 for Tic-tac-toe 2 for War or 3 for Blackjack or 4 to exit\n")
x = input("Which game do you want to play: ")
while x not in ["1", "2", "3", "4"]:
    print("Incorrect input! Pls enter a correct choice!")
    x = input("Which game do you want to play: ")
if int(x) == 1:
    # PLAYER CHOOSES X OR O
    def player_choice():
        y = 'wrong'
        while y not in ['X', 'O']:
            y = input("Enter ur choice(X or O): ").upper()
            if y not in ['X', 'O']:
                print("Sorry! Invalid Input..")
        print("Player 1 is assigned '{}'".format(y))
        if y == 'X':
            return 1
        else:
            return 2

    # PRINT THE BOARD
    def print_board(arr):
        # arr=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']
        # print('\n'*100)
        print('{}|{}|{}'.format(arr[7], arr[8], arr[9]))
        print('-----')
        print('{}|{}|{}'.format(arr[4], arr[5], arr[6]))
        print('-----')
        print('{}|{}|{}'.format(arr[1], arr[2], arr[3]))

    # Defines whether the user wants to play further or not
    def play_game():
        choice = 'Wrong'
        while choice not in ['Y', 'N']:
            choice = input("To start game press Y else N: ").upper()
            if choice not in ['Y', 'N']:
                print('Invalid Choice! ENter again...')
        return choice == 'Y'


    # game()
    def main_game(arr):
        if [arr[4], arr[5], arr[6]] == ['X', 'X', 'X'] or [arr[1], arr[2], arr[3]] == ['X', 'X', 'X'] or [arr[7],arr[8],arr[9]] == ['X', 'X', 'X'] or [arr[1], arr[4], arr[7]] == ['X', 'X', 'X'] or [arr[2], arr[5], arr[8]] == ['X', 'X','X'] or [arr[3], arr[6], arr[9]] == ['X', 'X', 'X'] or [arr[7], arr[5], arr[3]] == ['X', 'X', 'X'] or [arr[1],arr[5],arr[9]] == ['X', 'X', 'X']:
            x = 1
            print("X Wins")
            return False
        elif [arr[4], arr[5], arr[6]] == ['O', 'O', 'O'] or [arr[1], arr[2], arr[3]] == ['O', 'O', 'O'] or [arr[7],arr[8],arr[9]] == ['O', 'O', 'O'] or [arr[1], arr[4], arr[7]] == ['O', 'O', 'O'] or [arr[2], arr[5], arr[8]] == ['O', 'O','O'] or [arr[3], arr[6], arr[9]] == ['O', 'O', 'O'] or [arr[7], arr[5], arr[3]] == ['O', 'O', 'O'] or [arr[1],arr[5],arr[9]] == ['O', 'O', 'O']:
            x = 2
            print("O Wins")
            return False
        elif ' ' in arr:
            x = 0
            return True
        else:
            x = 3
            print('Its a Draw')
            return False


    x = 0

    # arr=[0,' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Start of the main part
    print("Welcome to TIC TAC TOE Game!!")
    while play_game() == True:
        arr = [0, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print_board(arr)
        n = 1
        if (player_choice() == 1):

            while main_game(arr):
                loc = int(input("Enter the location:(1-9):"))
                if arr[loc] == ' ':
                    if not (1 <= loc <= 9):
                        print("Invalid Choice! Enter again...")
                    elif n % 2 == 1:
                        arr[loc] = 'X'
                        n += 1
                    else:
                        arr[loc] = 'O'
                        n += 1
                else:
                    print("This location was already taken! Enter another location!!")
                    continue
                (print_board(arr))
        else:
            while main_game(arr):
                loc = int(input("Enter the location:(1-9): "))
                if not (1 <= loc <= 9):
                    print("Invalid Choice! Enter again...")
                elif n % 2 == 1:
                    arr[loc] = 'O'
                    n += 1
                else:
                    arr[loc] = 'X'
                    n += 1
                (print_board(arr))
    else:
        print("Thanks for Playing!! ")

if int(x)==2:
    # CARD CLASS
    # Suite, rank, value
    import random

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

        def __str__(self):
            return self.rank + " of " + self.suit


    # two_hearts=Card("Heart","Two")
    # print(two_hearts.values)
    # three_club=Card("Clubs","Three")
    # print(two_hearts.values<three_club.values)

    class Deck:
        def __init__(self):

            self.all_cards = []
            for suit in suits:
                for rank in ranks:
                    # Create the card object
                    created_card = Card(suit, rank)
                    self.all_cards.append(created_card)

        def shuffle(self):
            random.shuffle(self.all_cards)

        def deal_one(self):
            return self.all_cards.pop()


    new_deck = Deck()
    new_deck.shuffle()
    # print(new_deck.all_cards[3])
    # n1=new_deck.deal_one()
    # print(n1)
    # n2=new_deck.deal_one()
    # print(n2)
    # print(n1.value>n2.value)
    # print(len(new_deck.all_cards))
    # m=new_deck.all_cards[1]
    # print(m)
    mycard = Card('Heart', 'Two')
    print(mycard)


    # for card in new_deck.all_cards:                     #This line is used to print all the elements of the deck
    #     print(card)

    class Player:
        def __init__(self, name):
            self.name = name
            self.all_cards = []

        def remove_one(self):
            return self.all_cards.pop(0)

        def add_cards(self, new_cards):
            if type(new_cards) == type([]):
                # For multiple card objects
                self.all_cards.extend(new_cards)
            else:
                # For single card object
                self.all_cards.append(new_cards)

        def __str__(self):
            return f'Player {self.name} has {len(self.all_cards)} cards.'


    # new_player=Player('Sukant')
    # new_player.add_cards(mycard)
    # print(new_player)
    # new_player.add_cards([mycard,mycard,mycard])
    # print(new_player)
    # new_player.remove_one()
    # print(new_player)
    player_one = Player('Sukant')
    player_two = Player('Eshan')
    new_deck = Deck()
    new_deck.shuffle()
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    # print(player_one.all_cards[0])
    game_on = True
    round_num = 0
    while game_on:

        round_num += 1
        print(f"Round {round_num}")

        # Check to see if a player is out of cards:
        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            game_on = False
            break

        # Otherwise, the game is still on!

        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                # Player One gets the cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                # No Longer at "war" , time for next round
                at_war = False

            # Player Two Has higher Card
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # Player Two gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            else:
                print('WAR!')
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.

                # First check to see if player has enough cards

                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins! Player One Loses!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins! Player One Loses!")
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

if int(x)==3:
    import random

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}

    playing = True


    class Card:

        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + ' of ' + self.suit


    class Deck:

        def __init__(self):
            self.deck = []  # start with an empty list
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))  # build Card objects and add them to the list

        def __str__(self):
            deck_comp = ''  # start with an empty string
            for card in self.deck:
                deck_comp += '\n ' + card.__str__()  # add each Card object's print string
            return 'The deck has:' + deck_comp

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            single_card = self.deck.pop()
            return single_card


    # class Hand:
    #     def __init__(self):
    #         self.cards = []  # start with an empty list as we did in the Deck class
    #         self.value = 0  # start with zero value
    #         self.aces = 0  # add an attribute to keep track of aces
    #
    #     def add_card(self, card):
    #         self.cards.append(card)
    #         self.value += values[card.rank]
    #
    #     def adjust_for_ace(self):
    #         pass

    class Hand:

        def __init__(self):
            self.cards = []  # start with an empty list as we did in the Deck class
            self.value = 0  # start with zero value
            self.aces = 0  # add an attribute to keep track of aces

        def add_card(self, card):
            self.cards.append(card)
            self.value += values[card.rank]
            if card.rank == 'Ace':
                self.aces += 1  # add to self.aces

        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1


    class Chips:

        def __init__(self):
            self.total = 100  # This can be set to a default value or supplied by a user input
            self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet


    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if chips.bet > chips.total:
                    print("Sorry, your bet can't exceed", chips.total)
                else:
                    break


    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()


    def hit_or_stand(deck, hand):
        global playing  # to control an upcoming while loop

        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                hit(deck, hand)  # hit() function defined above

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                playing = False

            else:
                print("Sorry, please try again.")
                continue
            break


    def show_some(player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')


    def show_all(player, dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)


    def player_busts(player, dealer, chips):
        print("Player busts!")
        chips.lose_bet()


    def player_wins(player, dealer, chips):
        print("Player wins!")
        chips.win_bet()


    def dealer_busts(player, dealer, chips):
        print("Dealer busts!")
        chips.win_bet()


    def dealer_wins(player, dealer, chips):
        print("Dealer wins!")
        chips.lose_bet()


    def push(player, dealer):
        print("Dealer and Player tie! It's a push.")


    while True:
        # Print an opening statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

                # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

                # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

                # Inform Player of their chips total
        print("\nPlayer's winnings stand at", player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break

else:
    print("Thanks for Visiting! Visit again!! ")