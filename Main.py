import customtkinter as ctk
import tkinter as tk
from PIL import Image
import RPS

#Initializing the RPS class
game = RPS.RPS(rounds=3, players_choice="rock")

#Choosing a font for the game
small_font=("Comic Sans MS", 20)
font=("Comic Sans MS", 24)
biggest_font = ("Comic Sans MS", 48)
big_font = ("Comic Sans MS", 32)
bg_color = "#2af3d4" #Choosing a background color

#Changing the theme of the app/window
ctk.set_default_color_theme("Cyan.json")

#Creating the window(RPS) with it's attribtes and functionalities
class RPS(ctk.CTk):
        def __init__(self):
                super().__init__()
                self.title("RPS")

                #creating the size and centering the app on the screen
                screen_width = self.winfo_screenwidth()-600
                screen_height = self.winfo_screenheight()-400
                self.geometry(f"600x400+{screen_width//2}+{screen_height//2}")
                self.resizable(False, False)

                #changing the background color
                self.configure(fg_color=bg_color)

                # Running Page2 ----->>>>> This isn't suppose to be hear if there is Page1 because Page1 should implement Page2
                Page2(self) #self in this case is the window(class "RPS" at line 14)

                self.mainloop()

#Creating Page2 ->> This page is used to select the number of rounds a player will play
class Page2:
        def __init__(self, app):
                self.app = app #This connects the window(RPS) and Page2
                self.front_end()
                self.backend()

        def front_end(self):
                #label widget -->> This tells the player to input a certain number of rounds
                text = "How many rounds do you wish to play?"
                self.label1 = ctk.CTkLabel(self.app, text=text, font=big_font)
                self.label1.pack(expand=True, side="top")

                #Entry widget
                self.textvariable = tk.IntVar(value=1)
                self.entry = ctk.CTkEntry(self.app, textvariable=self.textvariable, width=175, height=100, font=big_font, justify="center")
                self.entry.pack(expand=True, side="top")

                #label widget --> This tells the user than he/she can only put 1-30 rounds in the game
                self.label2_present = False
                text = "You can only play at most 30 rounds"
                self.label2 = ctk.CTkLabel(self.app, text=text, text_color="red")
                #self.label2.pack(expand=True,side="top") #This isn't meant to be hear. Meant to be in the backend

                #To clear the page(Page2) to then run Page3(The Actual Game Page)
                def game_page():
                        #This will remove label2 based on if it is present or not to avoid errors
                        def label2_removal():
                                if self.label2_present == False:
                                        self.label1.pack_forget()
                                        self.entry.pack_forget()
                                        
                                elif self.label2_present == True:
                                        self.label1.pack_forget()
                                        self.entry.pack_forget()
                                        self.label2.pack_forget()
                                        
                        label2_removal()

                        #Runs the game page
                        Page3(self.app)

                self.game_page = game_page

        def backend(self):
                """This tells the app to display the "label2" label by changing the "self.label2_present" boolean attribute to (True or False).
                   This only changes the "self.label2_present" boolean attribute only and not actually display the label.
                """
                def label2_display(event):
                        rounds_value = self.textvariable.get()
                        if rounds_value > 0 and rounds_value <= 30: #If the input value is valid
                                game.rounds = rounds_value
                                self.game_page()
                                self.label2_present = False
                                game.scores = {"player":0, "computer":0} #Reseting the scores
                        else:
                                #This if statement below is to prevent repetition of the label2 as it will be packed multiple times if the statement wasn't present
                                if self.label2_present != True:
                                        self.label2.pack(expand=True, side="top")
                                        self.label2_present = True

                self.label2_display = label2_display
                
                self.entry.bind("<Return>", lambda event: self.label2_display(event))

#Creating Page3 -->> This is where the game actually takes place
class Page3:
        def __init__(self, app):
                self.app = app
                self.frontend()
                self.backend()
            
        def frontend(self):
                #This canvas is the template for all "Page3" widgets
                self.canvas = ctk.CTkCanvas(self.app, bg="#2af3d4")

                #round label: this shows what round a play is in
                self.round_no = self.canvas.create_text((625,50), text=f"Round No:{game.rounds}", font=font)
                def change_rounds_no(): #This changs the round number everytime a "RPS" button is clicked
                        self.canvas.delete(self.round_no)
                        self.round_no =self.canvas.create_text((625,50), text=f"Round No:{game.rounds}", font=font)
                        
                self.change_rounds_no = change_rounds_no
                
                #scores: Computer
                self.Computer_Score = 0 #This is the actual score
                self.canvas.create_rectangle((245,140,315,200), fill="#3a7ebf", width=3) #This is just a canvas rectangle acting as the frame for the text
                self.Computer_Score_Text = self.canvas.create_text((285,170), text=f"{self.Computer_Score}", font=big_font) #This is the text displaying the scores

                #scores: Human
                self.Human_Score = 0 #This is the actual score
                self.canvas.create_rectangle((455,140,525,200), fill="#3a7ebf", width=3) #This is just a canvas rectangle acting as the frame for the text
                self.Human_Score_Text = self.canvas.create_text((490,170), text=f"{self.Human_Score}", font=big_font) #This is the text displaying the scores

                def change_scores(Computer_Score, Human_Score):
                        self.Computer_Score = Computer_Score
                        self.canvas.delete(self.Computer_Score_Text)
                        self.Computer_Score_Text = self.canvas.create_text((285,170), text=f"{self.Computer_Score}", font=big_font)

                        self.Human_Score = Human_Score
                        self.canvas.delete(self.Human_Score_Text)
                        self.Human_Score_Text = self.canvas.create_text((490,170), text=f"{self.Human_Score}", font=big_font)
                self.change_scores = change_scores
                
                #Left Cirle or Computer(C) Circle with text "C"
                self.canvas.create_oval((45,75,220,250), fill="#3a7ebf", width="3") #This is the circle that holds the letter "C". "C" means Computer
                self.canvas.create_text((135,165), text="C", font=biggest_font) #This is the letter "C"

                #Right Circle or Human(H) Circle with text "H"
                self.canvas.create_oval((555,75,730,250), fill="#3a7ebf", width="3") #This is the circle that holds the letter "H". "H" means Human
                self.canvas.create_text((645,165), text="H", font=biggest_font) #This is the letter "H"

                #Versus text(VS)
                self.canvas.create_text((385,170), text="VS", font=biggest_font)

                #Response--> This shows who won in a particular round and also the overall winner or possibly a draw. This is the label(actually an entry widget) in the middle
                self.Response = tk.StringVar(value="It's a draw")
                self.Response_Entry = ctk.CTkEntry(self.app, textvariable=self.Response, justify="center", font=small_font, fg_color="#3a7ebf", width=260, height=65)
                self.Response_Entry.configure(state="disabled") #To avoid user input
                self.canvas_response = self.canvas.create_window((385,255), window=self.Response_Entry) #Placing the widget

                def change_response(response):
                        self.canvas.delete(self.canvas_response)
                        self.Response.set(response)
                        self.canvas_response = self.canvas.create_window((385,255), window=self.Response_Entry)

                self.change_response = change_response

                #Left/Computer Option--> This shows what the computer has choosen as its option
                self.Computer_Option = tk.StringVar(value="Rock")
                self.Computer_Option_Entry = ctk.CTkEntry(self.app, textvariable=self.Computer_Option, justify="center", font=small_font, fg_color="#3a7ebf", width=140, height=60)
                self.Computer_Option_Entry.configure(state="disabled")
                self.Computer_Canvas_Option = self.canvas.create_window((130,300), window=self.Computer_Option_Entry) #Placing the widget

                #Right/Human Option--> This shows what the human has choosen as its option
                self.Human_Option = tk.StringVar(value="Rock")
                self.Human_Option_Entry = ctk.CTkEntry(self.app, textvariable=self.Human_Option, justify="center", font=small_font, fg_color="#3a7ebf", width=140, height=60)
                self.Human_Option_Entry.configure(state="disabled")
                self.Human_Canvas_Option = self.canvas.create_window((640,300), window=self.Human_Option_Entry) #Placing the widget

                def change_option(computer_option, human_option):
                        self.Computer_Option.set(computer_option)
                        self.Human_Option.set(human_option)
                        self.canvas.delete(self.Computer_Canvas_Option)
                        self.canvas.delete(self.Human_Canvas_Option)
                        self.Computer_Canvas_Option = self.canvas.create_window((130,300), window=self.Computer_Option_Entry)
                        self.Human_Canvas_Option = self.canvas.create_window((640,300), window=self.Human_Option_Entry)

                self.change_option = change_option

                #Rock, Paper, Scissors Frame. Contains the RPS Buttons
                frame = ctk.CTkFrame(self.app, border_width=3,fg_color="black")
                self.canvas.create_window((385,415), window=frame) #Placing the frame

                #Buttons for Rock, Paper, Scissors
                self.rock_button = ctk.CTkButton(frame, text="Rock", command=lambda: self.game_func("rock"), corner_radius=0, width=150, height=50)
                self.paper_button = ctk.CTkButton(frame, text="Paper", command=lambda: self.game_func("paper"), corner_radius=0, width=150, height=50)
                self.scissors_button = ctk.CTkButton(frame, text="Scissors", command=lambda: self.game_func("scissors"), corner_radius=0, width=150, height=50)
                
                #Placing the Buttons in the frame
                self.rock_button.pack(side="left", padx=2, pady=2)
                self.paper_button.pack(side="left")
                self.scissors_button.pack(side="left",padx=2)

                #Play Again Button-->This is actually an Entry. An entry is used because a ctkButton doesn't have a border
                self.play_again_text = tk.StringVar(value="Play Again")
                self.play_again_button = ctk.CTkEntry(self.app, textvariable=self.play_again_text, height=60, width=175)
                self.play_again_button.configure(state="disabled") #This disables the entry and makes it act/look like a button
                self.play_again_button.bind("<Button-1>", lambda event: play_again_button_clicked(event)) #Runs the button command

                #This binding function are when one hovers over the "Play Again" button. It only changes the color of the button "Play Again"
                self.play_again_button.bind("<Enter>", lambda event: self.play_again_button.configure(fg_color="#3a7ebf")) #Change the color when hovered on
                self.play_again_button.bind("<Leave>", lambda event: self.play_again_button.configure(fg_color="#325882")) #Change the color when hovered on

                #This function tell the button(Entry Widget) to run Page2(The Round Page) and the start the game all over again
                def play_again_button_clicked(event): #This changes the color of the button and takes the page to Page2 only
                        self.play_again_button.configure(fg_color="#325882") #Change color
                        self.canvas.pack_forget() #Clear the page
                        Page2(self.app) #Return to Page2

                self.play_again_button_clicked = play_again_button_clicked

                #Places the canvas(also the template) on the app
                self.canvas.pack(expand=True, fill="both")

        def backend(self):
                #This is the main game function. This function is run when the "RPS" buttons are clicked
                def game_func(button):
                        game.players_choice = button
                        game.game()

                        #This functions below are to change the value in the frontend Page3 such as round number, score, comments
                        self.change_rounds_no()
                        self.change_scores(game.scores["computer"], game.scores["player"])
                        self.change_response(game.comment)
                        self.change_option(game.computers_choice.capitalize(), game.players_choice.capitalize())

                        if game.rounds == 0: #Disable buttons when the game ends or when the rounds no ends
                                self.rock_button.configure(state="disabled")
                                self.rock_button.configure(fg_color="#325882")
                                self.paper_button.configure(state="disabled")
                                self.paper_button.configure(fg_color="#325882")
                                self.scissors_button.configure(state="disabled")
                                self.scissors_button.configure(fg_color="#325882")
                                self.play_again()
                                
                self.game_func = game_func
                
                #This funtion inserts a button(entry widget) to start the game all over again
                def play_again():
                        if game.rounds == 0:
                                self.canvas.create_window((375,75), window=self.play_again_button)

                self.play_again = play_again
                self.play_again()
if __name__ == "__main__":            
        RPS()
