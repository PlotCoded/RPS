import random

#Starting of creating the back-end of the game
class RPS:
        def __init__(self, rounds=5, players_choice="rock", scores={"player":0, "computer":0}): 
                self.rounds = rounds
                self.players_choice = players_choice
                self.computers_choice = None
                self.scores = scores
                self.comment = None

        def game(self):
                #Creating a response/choice for the computer
                def computer_choice():
                        choices = ["rock", "paper", "scissors"]
                        self.computers_choice = random.choice(choices)

                computer_choice()

                #Processing information and creating a response when the player's response is 'rock'
                if self.players_choice == "rock":
                        if self.computers_choice == "rock":
                                self.comment = "It's a draw"
                        elif self.computers_choice == "paper":
                                self.scores["computer"]+=1
                                self.comment = "1 point for Computer"
                        elif self.computers_choice == "scissors":
                                self.scores["player"]+=1
                                self.comment = "1 point for Human"
                        else:
                                raise Exception("An error has been made my the computer's input value")

                #Processing information and creating a response when the player's response is 'paper'
                elif self.players_choice == "paper":
                        if self.computers_choice == "rock":
                                self.scores["player"]+=1
                                self.comment = "1 point for Human"
                        elif self.computers_choice == "paper":
                                self.comment = "It's a draw"
                        elif self.computers_choice == "scissors":
                                self.scores["computer"]+=1
                                self.comment = "1 point for Computer"
                        else:
                                raise Exception("An error has been made my the computer's input value")

                #Processing information and creating a response when the player's response is 'scissors'
                elif self.players_choice == "scissors":
                        if self.computers_choice == "rock":
                                self.scores["computer"]+=1
                                self.comment = "1 point for Computer"
                        elif self.computers_choice == "paper":
                                self.scores["player"]+=1
                                self.comment = "1 point for Human"
                        elif self.computers_choice == "scissors":
                                self.comment = "It's a draw"
                        else:
                                raise Exception("An error has been made my the computer's input value")
                else:
                        raise Exception("An error has been made my the player's input value")

                #updating the number of rounds played
                self.rounds-=1

#Testing
if __name__ == "__main__":
        game = RPS(players_choice="rock")                
        def test():
                if game.rounds > 0: 
                        game.game()
                        print(game.rounds, ",", game.players_choice,',', game.computers_choice, ',', game.comment, game.scores)

        for x in range(game.rounds):
                if game.rounds > 0:
                        test()

