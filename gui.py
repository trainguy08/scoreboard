import tkinter
from tkinter import *
from tkinter import messagebox
import score_classes
import csv

class Gui:
    def __init__(self,window):
        self.button_clicks = 0
        self.radio_values = IntVar()
        self.window = window
        self.starting_frame = Frame(self.window).grid(row=0, column=0, rowspan=3, columnspan=4)
        self.label =  Label(self.starting_frame, text='Please Select Sport').grid(row=0, columnspan=4)
        self.option1 = Radiobutton(self.starting_frame, text = 'Football',variable=self.radio_values, value=1).grid(row=1,column=0)
        self.option2 = Radiobutton(self.starting_frame, text = 'Basketball',variable=self.radio_values, value=2).grid(row=1,column=1)
        self.option3 = Radiobutton(self.starting_frame, text = 'Baseball',variable=self.radio_values, value=3).grid(row=1,column=2)
        self.option4 = Radiobutton(self.starting_frame, text = 'Hockey',variable=self.radio_values, value=4).grid(row=1,column=3)
        self.__teamAname = Entry(self.starting_frame)
        self.__teamAname.grid(row=2, column=1)
        self.teamAlabel = Label(self.starting_frame, text='Name of Team A:').grid(row=2,column=0)
        self.__teamBname = Entry(self.starting_frame)
        self.__teamBname.grid(row=2, column=3)
        self.teamBlabel = Label(self.starting_frame, text='Name of Team B:').grid(row=2, column=2)
        self.button5 = Button(self.starting_frame,text='Submit', command=self.sport_choice).grid(row=2,columnspan=4)
        self.scoring_board = Frame(self.window)
        self.scoring_board.grid(rowspan=6,columnspan=4,row=3,column=0)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_columnconfigure(3, weight=1)
    def sport_choice(self):
        if self.radio_values.get()==1:
            self.button_clicks += 1
            self.scoring_board.destroy()
            self.scoring_board = Frame(self.window)
            self.scoring_board.grid(rowspan=6, columnspan=4, row=3, column=0,sticky='ew')
            self.football()
        elif self.radio_values.get()==2:
            self.button_clicks += 1
            self.scoring_board.destroy()
            self.scoring_board = Frame(self.window)
            self.scoring_board.grid(rowspan=6, columnspan=4, row=3, column=0,sticky='ew')
            self.basketball()
        elif self.radio_values.get()==3:
            self.button_clicks += 1
            self.scoring_board.destroy()
            self.scoring_board = Frame(self.window)
            self.scoring_board.grid(rowspan=6, columnspan=4, row=3, column=0,sticky='ew')
            self.baseball()
        elif self.radio_values.get()==4:
            self.button_clicks += 1
            self.scoring_board.destroy()
            self.scoring_board = Frame(self.window)
            self.scoring_board.grid(rowspan=6, columnspan=4, row=3, column=0,sticky='ew')
            self.hockey()
        else:
            messagebox.showerror("Selection Error","Please Select a Sport")

    def football(self):
        self.__teamAclass = score_classes.Football(self.__teamAname.get())
        self.__teamAscore = self.__teamAclass.score
        self.__teamBclass = score_classes.Football(self.__teamBname.get())
        self.__teamBscore = self.__teamBclass.score
        self.__scoreboardA = Label(self.scoring_board,text="%03d" % (self.__teamAscore),font=('Arial',214)).grid(row=4,column=1,rowspan=2)
        self.__scoreboardB = Label(self.scoring_board, text="%03d" % (self.__teamBscore), font=('Arial', 214)).grid(row=4, column=2,rowspan=2)

        if self.__teamAname.get() != '':
            self.__teamA = Label(self.scoring_board,text = self.__teamAclass.team_name,font=('Arial',58)).grid(row=6,column=1)
        else:
            self.__teamA = Label(self.scoring_board,text = "Team A",font=('Arial',58)).grid(row=6,column=1)
        if self.__teamBname.get() != '':
             self.__teamB = Label(self.scoring_board, text=self.__teamBclass.team_name, font=('Arial', 58)).grid(row=6,column=2)
        else:
            self.__teamB = Label(self.scoring_board, text="Team B", font=('Arial', 58)).grid(row=6, column=2)
        self.safteyA = Button(self.scoring_board, text='Safety +2', command=lambda:[self.__teamAclass.safety(),self.update_score()]).grid(row=4,column=0,sticky='w')
        self.safteyB = Button(self.scoring_board, text='Safety +2', command=lambda:[self.__teamBclass.safety(),self.update_score()]).grid(row=4, column=3, sticky='e')
        self.field_goalA = Button(self.scoring_board, text='Field Goal +3',command=lambda:[self.__teamAclass.field_goal(),self.update_score()]).grid(row=5, column=0,sticky='w')
        self.field_goalB = Button(self.scoring_board, text='Field Goal +3', command=lambda:[self.__teamBclass.field_goal(),self.update_score()]).grid(row=5, column=3,sticky='e')
        self.touchdownA = Button(self.scoring_board, text='Touchdown +6', command=lambda:[self.__teamAclass.touchdown(),self.update_score()]).grid(row=6, column=0,sticky='w')
        self.touchdownB = Button(self.scoring_board, text='Touchdown +6', command=lambda: [self.__teamBclass.touchdown(), self.update_score()]).grid(row=6, column=3,sticky='e')
        self.extapointA = Button(self.scoring_board, text='Extra Point +1', command=lambda: [self.__teamAclass.extra_point(),self.update_score()]).grid(row=7,column=0,sticky='w')
        self.extapointB = Button(self.scoring_board, text='Extra Point +1', command=lambda: [self.__teamBclass.extra_point(), self.update_score()]).grid(row=7, column=3,sticky='e')
        self.twopointA = Button(self.scoring_board, text='Two Point Conversion +1', command=lambda: [self.__teamAclass.two_point_conversion(),self.update_score()]).grid(row=8,column=0,sticky='w')
        self.twopointB = Button(self.scoring_board, text='Two Point Conversion +1', command=lambda: [self.__teamBclass.two_point_conversion(), self.update_score()]).grid(row=8, column=3,sticky='e')
        self.configure()
    def basketball(self):
        self.__teamAclass = score_classes.Basketball(self.__teamAname.get())
        self.__teamAscore = self.__teamAclass.score
        self.__teamBclass = score_classes.Basketball(self.__teamBname.get())
        self.__teamBscore = self.__teamBclass.score
        self.__scoreboardA = Label(self.scoring_board, text="%03d" % (self.__teamAscore), font=('Arial', 214)).grid(row=4, column=1, rowspan=2)
        self.__scoreboardB = Label(self.scoring_board, text="%03d" % (self.__teamBscore), font=('Arial', 214)).grid(row=4, column=2, rowspan=2)


        if self.__teamAname.get() != '':
            self.__teamA = Label(self.scoring_board, text=self.__teamAclass.team_name, font=('Arial', 72)).grid(row=6,column=1)
        else:
            self.__teamA = Label(self.scoring_board, text="Team A", font=('Arial', 58)).grid(row=6, column=1)
        if self.__teamBname.get() != '':
            self.__teamB = Label(self.scoring_board, text=self.__teamBclass.team_name, font=('Arial', 58)).grid(row=6,column=2)
        else:
            self.__teamB = Label(self.scoring_board, text="Team B", font=('Arial', 72)).grid(row=6, column=2)
        self.twopointerA = Button(self.scoring_board,text='Two Pointer',command=lambda:[self.__teamAclass.two_point(),self.update_score()]).grid(row=4,column=0,sticky='w')
        self.twopointerB = Button(self.scoring_board, text='Two Pointer', command=lambda: [self.__teamBclass.two_point(), self.update_score()]).grid(row=4, column=3,sticky='e')
        self.threepointerA = Button(self.scoring_board, text='Three Pointer',command=lambda: [self.__teamAclass.three_point(),self.update_score()]).grid(row=5,column=0,sticky='w')
        self.threepointerB = Button(self.scoring_board, text='Three Pointer',command=lambda: [self.__teamBclass.three_point(), self.update_score()]).grid(row=5,column=3,sticky='e')
        self.freethrowA = Button(self.scoring_board, text='Free Throw',command=lambda: [self.__teamAclass.free_throw(), self.update_score()]).grid(row=6,column=0,sticky='w')
        self.freethrowB = Button(self.scoring_board, text='Free Throw',command=lambda: [self.__teamBclass.free_throw(), self.update_score()]).grid(row=6,column=3,sticky='e')
        self.configure()
    def baseball(self):
        self.__teamAclass = score_classes.Baseball(self.__teamAname.get())
        self.__teamAscore = self.__teamAclass.score
        self.__teamBclass = score_classes.Baseball(self.__teamBname.get())
        self.__teamBscore = self.__teamBclass.score
        self.__scoreboardA = Label(self.scoring_board, text="%03d" % (self.__teamAscore), font=('Arial', 214)).grid(row=4, column=1, rowspan=2)
        self.__scoreboardB = Label(self.scoring_board, text="%03d" % (self.__teamBscore), font=('Arial', 214)).grid(row=4, column=2, rowspan=2)


        if self.__teamAname.get() != '':
            self.__teamA = Label(self.scoring_board, text=self.__teamAclass.team_name, font=('Arial', 58)).grid(row=6, column=1)
        else:
            self.__teamA = Label(self.scoring_board, text="Team A", font=('Arial', 58)).grid(row=6, column=1)
        if self.__teamBname.get() != '':
            self.__teamB = Label(self.scoring_board, text=self.__teamBclass.team_name, font=('Arial', 58)).grid(row=6, column=2)
        else:
            self.__teamB = Label(self.scoring_board, text="Team B", font=('Arial', 58)).grid(row=6, column=2)
        self.home_runA = Button(self.scoring_board, text="Run +1", command=lambda:[self.__teamAclass.run(),self.update_score()]).grid(row=4,column=0,sticky='w')
        self.home_runB = Button(self.scoring_board, text="Run +1", command=lambda:[self.__teamBclass.run(),self.update_score()]).grid(row=4,column=3,sticky='e')
        self.grand_slamA = Button(self.scoring_board, text="Grand Slam +4", command=lambda:[self.__teamAclass.grand_slam(),self.update_score()]).grid(row=5,column=0,sticky='w')
        self.grand_slamB = Button(self.scoring_board, text="Grand Slam +4", command=lambda: [self.__teamBclass.grand_slam(), self.update_score()]).grid(row=5, column=3,sticky='e')
        self.configure()
    def hockey(self):
        self.__teamAclass = score_classes.Hockey(self.__teamAname.get())
        self.__teamAscore = self.__teamAclass.score
        self.__teamBclass = score_classes.Hockey(self.__teamBname.get())
        self.__teamBscore = self.__teamBclass.score
        self.__scoreboardA = Label(self.scoring_board, text="%03d" % (self.__teamAscore), font=('Arial', 214)).grid(row=4, column=1, rowspan=2)
        self.__scoreboardB = Label(self.scoring_board, text="%03d" % (self.__teamBscore), font=('Arial', 214)).grid(row=4, column=2, rowspan=2)


        if self.__teamAname.get() != '':
            self.__teamA = Label(self.scoring_board, text=self.__teamAclass.team_name, font=('Arial', 58)).grid(row=6,column=1)
        else:
            self.__teamA = Label(self.scoring_board, text="Team A", font=('Arial', 58)).grid(row=6, column=1)
        if self.__teamBname.get() != '':
            self.__teamB = Label(self.scoring_board, text=self.__teamBclass.team_name, font=('Arial', 58)).grid(row=6, column=2)
        else:
            self.__teamB = Label(self.scoring_board, text="Team B", font=('Arial', 58)).grid(row=6, column=2)
        self.goalA = Button(self.scoring_board, text="Goal +1",command=lambda: [self.__teamAclass.goal(), self.update_score()]).grid(row=4, column=0,rowspan=2,sticky='nswe')
        self.goalB = Button(self.scoring_board, text="Goal +1", command=lambda: [self.__teamBclass.goal(), self.update_score()]).grid(row=4, column=3,rowspan=2,sticky='nswe')
        self.configure()
    def configure(self):
        self.reset_score = Button(self.scoring_board, text="Reset Score",command=lambda: [self.__teamAclass.reset(), self.__teamBclass.reset(),self.update_score()]).grid(row=9, column=0, columnspan=2,sticky='ew')
        self.restart_button = Button(self.scoring_board, text="Restart Program",command=lambda: [self.__teamAclass.reset(), self.__teamBclass.reset(),self.restart()]).grid(row=9, column=2, columnspan=2, sticky='ew')
        self.determine_winner = Button(self.scoring_board, text="End Game", command=self.winner).grid(row=10, columnspan=4,sticky='ew')
        self.scoring_board.grid_columnconfigure(0, weight=1)
        self.scoring_board.grid_columnconfigure(1, weight=1)
        self.scoring_board.grid_columnconfigure(2, weight=1)
        self.scoring_board.grid_columnconfigure(3, weight=1)

    def store_results(self,teamA,teamB):
        with open("Game Results","a") as sportsbook:
            field = ['Team Name','Score']
            writer = csv.writer(sportsbook)

            writer.writerow([teamA, self.__teamAscore,'vs',teamB,self.__teamBscore])


    def update_score(self):
        self.__teamAscore = self.__teamAclass.score
        self.__teamBscore = self.__teamBclass.score
        self.__scoreboardA = Label(self.scoring_board, text="%03d" % (self.__teamAscore), font=('Arial', 214)).grid(row=4, column=1, rowspan=2)
        self.__scoreboardB = Label(self.scoring_board, text="%03d" % (self.__teamBscore), font=('Arial', 214)).grid(row=4, column=2, rowspan=2)


    def restart(self):
        self.scoring_board.destroy()
    def winner(self):
        if self.__teamAname.get() != '':
            teamA = self.__teamAname.get()
        else:
            teamA = "Team A "
        if self.__teamBname.get() != '':
            teamB = self.__teamBname.get()
        else:
            teamB = "Team B "
        if self.__teamAscore > self.__teamBscore:
            self.message = "Final:" + teamA +"defeats " + teamB + str(self.__teamAscore) + "-" + str(self.__teamBscore)
            messagebox.showinfo("GAME OVER",self.message)
        elif self.__teamAscore < self.__teamBscore:
            self.message = "Final:" + teamB + "defeats " + teamA + str(self.__teamBscore) + "-" + str(self.__teamAscore)
            messagebox.showinfo("GAME OVER", self.message)
        else:
            messagebox.showinfo("GAME OVER", "Tie Game")
        self.store_answers = Button(self.scoring_board, text="Store Data in CSV", command=lambda: [self.store_results(teamA,teamB)]).grid(row=11, columnspan=4, sticky='ew')
