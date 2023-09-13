import random

class GameLogic:
    
    def GenerateRandomNumber(self):
        RandomNumber = random.randint(0, 10)
        return RandomNumber
    
    def GetGameState(self, Guess, SecretValue):

        if Guess == SecretValue:
            return True
         
        if Guess < SecretValue:
            return "False"
        
        if Guess > SecretValue:
            return False

class Points:
    
    def CalculateScore(self, FailedAttempts):
        Score = 10 - FailedAttempts
        return Score

    def Count(self, Number, add, AddNumberTo=0):
        if add == True:
            AddedbyOneNumber = Number+1
            return AddedbyOneNumber
        if AddNumberTo != 0:
            return Number + AddNumberTo
        
class Main:

    def Main(self):
        
        print("Guess the number by Enulix!")
        logic = GameLogic()
        points = Points()
        SecretValue = logic.GenerateRandomNumber()
        FailedAttempts = 0
        TotalAttempts = 0
        CompletePoints = 0

        while True:
            
            Guess = int(input("Guess(0 to 10): "))
            GameState = logic.GetGameState(Guess, SecretValue)
            
            if GameState == False:
                print("Your guess is too high")
                FailedAttempts = points.Count(FailedAttempts, True)
            
            if GameState == "False":
                print("Your guess is too low")
                FailedAttempts = points.Count(FailedAttempts, True)
            
            if GameState == True:
                print("Correct!")
                Totalpoints = points.CalculateScore(FailedAttempts)
                print(f"You won {Totalpoints} Points!")
                CompletePoints = points.Count(CompletePoints, False, Totalpoints)
                ContinueGame = input("Would you like to play again(Y/N)? ")
                
                if ContinueGame == "Y" or ContinueGame == "y" or ContinueGame == "E" or ContinueGame == "e":
                    SecretValue = logic.GenerateRandomNumber()
                    FailedAttempts = 0
                    TotalAttempts = points.Count(TotalAttempts, True)

                else:
                    input(f"Congrats!, You won (in total) {CompletePoints} Points!")
                    break

if __name__ == "__main__":
    main = Main()
    main.Main()
