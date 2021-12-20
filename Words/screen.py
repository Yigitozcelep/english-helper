from tkinter import *
from data import *
import random
from tkinter.messagebox import *

class Interface:
    def __init__(self):
        self.word_list = Words.today_words
        self.limit = len(self.word_list)
        self.current = 0
        self.root = Tk()
        self.root.configure(bg="#532A21")
        self.root.geometry("1200x950+300+65")
        self.root.title("Yiğit özcelep tarafından yazılmıştır :D")
        self.in_train = False
        self.fnish = False

        #Bindler
        self.root.bind("<Right>", self.change_auto)
        self.root.bind("<Left>", self.change_auto)
        self.root.bind("<Return>", self.add_new_word_auto)
        self.root.bind("<Key>", self.next_word_auoto)

        #Frameler
        self.eng_frame = Frame(self.root, bg="#532A21", pady=20)
        self.eng_frame.grid(row=0, column=0)

        self.true_false_frame = Frame(self.root, bg="#532A21")
        self.true_false_frame.grid(row=2, column=0)

        self.orta_frame = Frame(self.root, bg="#532A21")
        self.orta_frame.grid(row=3, column=0)


        self.alt_frame = Frame(self.root, bg="#532A21")
        self.alt_frame.grid(row=4, column=0, pady=(50, 0))

        #Orta kısım label ve entyler

        self.noun_label = Label(self.eng_frame, text="Noun", font=("helvetica",50,"bold"), bg="#532A21", width=15)
        self.noun_label.grid(row=0, column=0)
        self.alt_noun_label = Label(self.eng_frame, text="Kelime yok", font=("helvetica",25, "bold"), bg="#532A21", width=15)
        self.alt_noun_label.grid(row=1,column=0)

        self.adjective_label = Label(self.eng_frame, text="Adjective", font=("helvetica", 50, "bold"), bg="#532A21", width=15)
        self.adjective_label.grid(row=0, column=1)
        self.alt_adjective_label = Label(self.eng_frame, text="Kelime yok", font=("helvetica", 25, "bold"), bg="#532A21", width=30)
        self.alt_adjective_label.grid(row=1, column=1)

        self.verb_label = Label(self.eng_frame, text="Verb", font=("helvetica", 50, "bold"), bg="#532A21", width=15)
        self.verb_label.grid(row=0, column=2)
        self.alt_verb_label = Label(self.eng_frame, text="Kelime yok", font=("helvetica", 25, "bold"), bg="#532A21", width=15)
        self.alt_verb_label.grid(row=1, column=2)



        self.explanation_label = Label(self.eng_frame, text="Explanation", font=("helvetica", 50, "bold"),bg="#532A21")
        self.explanation_label.grid(row=2, column=0, columnspan=3)
        self.alt_explanation_label = Label(self.eng_frame, text="Kelime yok"
                                           ,font=("helvetica",18,"bold"), bg="#532A21", width=100)
        self.alt_explanation_label.grid(row=3,column=0,columnspan=3)

        self.true_button = Button(self.true_false_frame, text="True", font=("helvetica", 20, "bold"), highlightbackground='#645959', command=self.next_true)
        self.true_button.grid(row=0, column=1, ipadx=50, ipady=20, padx=40, pady=20)

        self.false_button = Button(self.true_false_frame, text="False", font=("helvetica", 20, "bold"), highlightbackground='#645959', command=self.next_false)
        self.false_button.grid(row=0, column=0, ipadx=50, ipady=20, padx=40, pady=20)


        self.eng_noun_label = Label(self.orta_frame, text="Noun", font=("helvetica", 18, "bold"), bg="#532A21")
        self.eng_noun_label.grid(row=0,column=0, pady=(15,0))
        self.eng_noun_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"), bg="#532A21", highlightbackground="black")
        self.eng_noun_entry.grid(row=0, column=1, pady=(15,0))

        self.eng_adjective_label = Label(self.orta_frame, text="Adjective", font=("helvetica", 18, "bold"), bg="#532A21")
        self.eng_adjective_label.grid(row=1, column=0,pady=10)
        self.eng_adjective_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"),  bg="#532A21", highlightbackground="black")
        self.eng_adjective_entry.grid(row=1, column=1,pady=10)

        self.eng_verb_label = Label(self.orta_frame, text="Verb", font=("helvetica", 18, "bold"), bg="#532A21")
        self.eng_verb_label.grid(row=2, column=0,pady=(10,0))
        self.eng_verb_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"), bg="#532A21", highlightbackground="black")
        self.eng_verb_entry.grid(row=2, column=1,pady=(10,0))

        self.tr_label = Label(self.orta_frame, text="Turkish", font=("helvetica", 18, "bold"), bg="#532A21")
        self.tr_label.grid(row=3, column=0, pady=(10, 0))
        self.tr_label_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"), bg="#532A21",
                                    highlightbackground="black")
        self.tr_label_entry.grid(row=3, column=1, pady=(10, 0))

        self.exp_label = Label(self.orta_frame, text="Explanation", font=("helvetica", 18, "bold"), bg="#532A21")
        self.exp_label.grid(row=4, column=0, pady=(10, 0))
        self.exp_label_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"), bg="#532A21",
                                    highlightbackground="black")
        self.exp_label_entry.grid(row=4, column=1, pady=(10, 0))

        self.phrase_label = Label(self.orta_frame, text="Phrase", font=("helvetica", 18, "bold"), bg="#532A21")
        self.phrase_label.grid(row=5, column=0, pady=(10, 0))
        self.phrase_label_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"), bg="#532A21",
                                     highlightbackground="black")
        self.phrase_label_entry.grid(row=5, column=1, pady=(10, 0))

        self.frequency_label = Label(self.orta_frame, text="Frequency", font=("helvetica", 18, "bold"), bg="#532A21")
        self.frequency_label.grid(row=6, column=0, pady=(10, 0))
        self.frequency_label_entry = Entry(self.orta_frame, font=("helvetica", 18, "bold"), bg="#532A21",
                                        highlightbackground="black")
        self.frequency_label_entry.grid(row=6, column=1, pady=(10, 0))
        self.frequency_label_entry.insert(0,"0/1/7/14/30/90")


        #Aşağı butonlar ve shown label
        self.add_button = Button(self.alt_frame, text="Add", font=("helvetica", 18, "bold"),
                                  highlightbackground='#645959', command=self.add_word)
        self.add_button.grid(row=0, column=4, ipadx=35, ipady=15, padx=(20,0))

        self.shown_label = Label(self.alt_frame, text="0", font=("helvetica", 18, "bold"), bg="#485D5B", fg="black")
        self.shown_label.grid(row=0, column=6, ipadx=35, ipady=15, padx=(20,0))

        self.delete_button = Button(self.alt_frame, text="Delete", font=("helvetica", 18 ,"bold"), highlightbackground='#645959', command=self.del_word)
        self.delete_button.grid(row=0,column=2, ipadx=35, ipady=15, padx=(20,0))


        self.edit_button = Button(self.alt_frame, text="Edit", font=("helvetica", 18 ,"bold"), highlightbackground='#645959', command=self.edit_word)
        self.edit_button.grid(row=0,column=3, ipadx=35, ipady=15, padx=(20,0))



        self.back_button = Button(self.alt_frame, text="Back", font=("helvetica", 18 ,"bold"), highlightbackground='#645959', command=self.back_word)
        self.back_button.grid(row=0,column=0, ipadx=35, ipady=15, padx=(20,0))

        self.all_word_button = Button(self.alt_frame, text="Train", font=("helvetica", 18, "bold"),
                                  highlightbackground='#645959', command=self.train_word)
        self.all_word_button.grid(row=0, column=1, ipadx=35, ipady=15, padx=(20,0))

        self.random_button = Button(self.alt_frame, text="Random 10", font=("helvetica", 18, "bold"),
                                  highlightbackground='#645959', command=self.random_word)
        self.random_button.grid(row=0, column=5, ipadx=35, ipady=15, padx=(20, 0))

        if self.word_list:
            self.change("True")
        else:
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

        self.root.mainloop()


    def add_word(self):
        noun = self.eng_noun_entry.get()
        adjective = self.eng_adjective_entry.get()
        verb = self.eng_verb_entry.get()
        turkish = self.tr_label_entry.get().replace("\n", " ")
        explanation = self.exp_label_entry.get().replace("\n", "")
        phrase = self.phrase_label_entry.get()
        frequency = self.frequency_label_entry.get()
        if (len(noun) > 2 or len(adjective) > 2 or len(verb) or len(phrase) > 2) and len(turkish) > 2:pass
        else:return
        if (len(noun) + len(adjective) + len(verb) > 1 and len(phrase) == 0) or (len(phrase) > 0 and len(noun) + len(verb) + len(adjective) == 0):
            self.eng_noun_entry.delete(0, END)
            self.eng_verb_entry.delete(0, END)
            self.eng_adjective_entry.delete(0, END)
            self.eng_verb_entry.delete(0, END)
            self.tr_label_entry.delete(0, END)
            self.exp_label_entry.delete(0, END)
            self.phrase_label_entry.delete(0, END)
            self.frequency_label_entry.delete(0, END)
            self.frequency_label_entry.insert(0, "0/1/7/14/30/90")
            add_word(noun, adjective, verb, turkish, explanation, phrase, frequency)
        else:
            return


    def phrase_word(self,info="x"):
        x = self.adjective_label.cget("text")
        if self.fnish == True:info = "x"

        if x == "Phrase" or info == "True":
            self.noun_label.config(fg="#532A21")
            self.verb_label.config(fg="#532A21")
            self.alt_noun_label.config(fg="#532A21")
            self.alt_verb_label.config(fg="#532A21")
            self.explanation_label.config(fg="#532A21")
            self.alt_explanation_label.config(fg="#532A21")
            self.alt_adjective_label.config(fg="#532A21")
            self.adjective_label.config(fg="green", text=self.word_list[self.current].turkish)
            self.shown_label.config(text=self.word_list[self.current].shown)
            self.grid_changer()

        else:
            self.noun_label.config(fg="#532A21")
            self.verb_label.config(fg="#532A21")
            self.alt_noun_label.config(fg="#532A21", text=self.word_list[self.current].noun)
            self.alt_verb_label.config(fg="#532A21", text=self.word_list[self.current].verb)
            self.explanation_label.config(fg="black")
            self.alt_explanation_label.config(fg="black", text=self.word_list[self.current].explanation)
            self.alt_adjective_label.config(fg="black", text=self.word_list[self.current].phrase)
            self.adjective_label.config(fg="black", text="Phrase")
            self.shown_label.config(text=self.word_list[self.current].shown)
            self.grid_changer()

    def change(self, info="x"):
        if self.word_list:pass
        else:return
        if self.fnish == False:
            if self.word_list[self.current].phrase:
                self.phrase_word(info)
                return

            self.adjective_label.config(fg="black", text="Adjective")
            x = self.noun_label.cget("fg")
            if info == "True" or x == "black":
                self.noun_label.config(fg="#532A21")
                self.verb_label.config(fg="#532A21")
                self.alt_noun_label.config(fg="#532A21")
                self.alt_verb_label.config(fg="#532A21")
                self.explanation_label.config(fg="#532A21")
                self.alt_explanation_label.config(fg="#532A21")
                self.alt_adjective_label.config(fg="#532A21")
                self.adjective_label.config(fg="green", text=self.word_list[self.current].turkish)
                self.shown_label.config(text=self.word_list[self.current].shown)
                self.grid_changer()
            else:
                self.noun_label.config(fg="black")
                self.verb_label.config(fg="black")
                self.alt_noun_label.config(fg="black", text=self.word_list[self.current].noun)
                self.alt_verb_label.config(fg="black", text=self.word_list[self.current].verb)
                self.explanation_label.config(fg="black")
                self.alt_explanation_label.config(fg="black", text=self.word_list[self.current].explanation)
                self.alt_adjective_label.config(fg="black", text=self.word_list[self.current].adjective)
                self.adjective_label.config(fg="black", text="Adjective")
                self.shown_label.config(text=self.word_list[self.current].shown)
                self.grid_changer()

        else:
            if self.word_list[self.current].phrase:
                self.phrase_word(info)
                return
            x = self.noun_label.cget("fg")
            if info == "True" or x == "#532A21":
                self.noun_label.config(fg="black")
                self.verb_label.config(fg="black")
                self.alt_noun_label.config(fg="black", text=self.word_list[self.current].noun)
                self.alt_verb_label.config(fg="black", text=self.word_list[self.current].verb)
                self.explanation_label.config(fg="black")
                self.alt_explanation_label.config(fg="black", text=self.word_list[self.current].explanation)
                self.alt_adjective_label.config(fg="black", text=self.word_list[self.current].adjective)
                self.adjective_label.config(fg="black", text="Adjective")
                self.shown_label.config(text=self.word_list[self.current].shown)
                self.grid_changer()

            else:
                self.noun_label.config(fg="#532A21")
                self.verb_label.config(fg="#532A21")
                self.alt_noun_label.config(fg="#532A21")
                self.alt_verb_label.config(fg="#532A21")
                self.explanation_label.config(fg="#532A21")
                self.alt_explanation_label.config(fg="#532A21")
                self.alt_adjective_label.config(fg="#532A21")
                self.adjective_label.config(fg="green", text=self.word_list[self.current].turkish)
                self.shown_label.config(text=self.word_list[self.current].shown)
                self.grid_changer()

    def change_auto(self, event):
        x = self.root.focus_get()
        if x == self.frequency_label_entry or x == self.exp_label_entry or x == self.tr_label_entry or x == self.exp_label_entry or x == self.eng_verb_entry or x == self.eng_adjective_entry or x == self.phrase_label_entry or x == self.eng_noun_entry:
            return
        self.change()

    def next_true(self, a="x"):
        if not self.fnish:
            self.update_same()
            if not self.in_train:
                sql_command = """UPDATE word SET shown = %s WHERE user_id = %s"""
                values = (self.word_list[self.current].shown + 1, self.word_list[self.current].user_id)
                my_cursor.execute(sql_command, values)
                data_b.commit()
            if self.current + 1 == self.limit:
                self.stantart()
                return
            self.current += 1
            self.change("True")
        else:
            if self.current + 1 == self.limit:
                self.stantart()
                return
            self.current += 1
            self.change("True")

    def del_word(self):
        a = askyesno(message="do you want to delete")
        if not a: return
        sql_command = """UPDATE word SET frequency = %s WHERE user_id = %s"""
        values = ("9000/12500", self.word_list[self.current].user_id)
        my_cursor.execute(sql_command, values)
        data_b.commit()
        if len(self.word_list) == 1:
            self.alt_noun_label.config(text="Kelimeler bitti")
            self.alt_verb_label.config(text="Kelimeler bitti")
            self.alt_noun_label.config(text="Kelimeler bitti")
            self.alt_explanation_label.config(text="Kelimeler bitti")
            self.alt_adjective_label.config(text="Kelimeler bitti")
            self.shown_label.config(text="0")
            self.adjective_label.config(text="Kelimeler bitti")
            self.back_button.config(state=DISABLED)
            self.delete_button.config(state=DISABLED)
            self.edit_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)
        del self.word_list[self.current]
        self.limit = len(self.word_list)
        if self.current == self.limit:
            self.stantart()
            return
        self.change("True")

    def stantart(self):
        if self.fnish == True:
            self.make_new_list()
            if self.word_list and not self.in_train:
                self.current = 0
                self.fnish = False
                self.change("True")

            else:
                self.alt_noun_label.config(text="Kelimeler bitti")
                self.alt_verb_label.config(text="Kelimeler bitti")
                self.alt_noun_label.config(text="Kelimeler bitti")
                self.alt_explanation_label.config(text="Kelimeler bitti")
                self.alt_adjective_label.config(text="Kelimeler bitti")
                self.shown_label.config(text="0")
                self.adjective_label.config(text="Kelimeler bitti")
                self.back_button.config(state=DISABLED)
                self.delete_button.config(state=DISABLED)
                self.edit_button.config(state=DISABLED)
                self.false_button.config(state=DISABLED)
                self.true_button.config(state=DISABLED)
        else:
            self.fnish_word()

    def edit_word(self):
        if len(self.word_list) == 0:return
        if self.edit_button.cget("text") == "Edit":
            self.false_button.config(state=DISABLED)
            self.true_button.config(state=DISABLED)
            self.back_button.config(state=DISABLED)
            self.all_word_button.config(state=DISABLED)
            self.delete_button.config(state=DISABLED)
            self.add_button.config(state=DISABLED)
            self.edit_button.config(text="Save")
            self.eng_noun_entry.insert(0,self.word_list[self.current].noun)
            self.eng_adjective_entry.insert(0, self.word_list[self.current].adjective)
            self.eng_verb_entry.insert(0, self.word_list[self.current].verb)
            self.tr_label_entry.insert(0, self.word_list[self.current].turkish)
            self.exp_label_entry.insert(0, self.word_list[self.current].explanation)
            self.phrase_label_entry.insert(0, self.word_list[self.current].phrase)
            self.frequency_label_entry.delete(0, END)
            self.frequency_label_entry.insert(0, self.word_list[self.current].frequancy_str)
        else:
            noun = self.eng_noun_entry.get()
            adjective = self.eng_adjective_entry.get()
            verb = self.eng_verb_entry.get()
            turkish = self.tr_label_entry.get()
            explanation = self.exp_label_entry.get()
            phrase = self.phrase_label_entry.get()
            frequency = self.frequency_label_entry.get()
            info = frequency == self.word_list[self.current].frequancy_str

            self.word_list[self.current].noun = noun
            self.word_list[self.current].adjective = adjective
            self.word_list[self.current].phrase = phrase
            self.word_list[self.current].turkish = turkish
            self.word_list[self.current].turkish = turkish.replace("\n", " ")
            self.word_list[self.current].verb = verb
            self.word_list[self.current].explanation = explanation.replace("\n", " ")
            self.word_list[self.current].frequancy_str = frequency
            self.word_list[self.current].split_explanation()
            self.word_list[self.current].data = []
            self.word_list[self.current].split_turkish()

            word = self.word_list[self.current]
            noun = word.noun
            adjective = word.adjective
            verb = word.verb
            phrase = word.phrase
            turkish = word.turkish
            explanation = word.explanation

            if (len(noun) > 2 or len(adjective) > 2 or len(verb) or len(phrase) > 2) and len(turkish) > 2:
                pass
            else:
                return
            if (len(noun) + len(adjective) + len(verb) > 1 and len(phrase) == 0) or (
                    len(phrase) > 0 and len(noun) + len(verb) + len(adjective) == 0):
                self.false_button.config(state=NORMAL)
                self.true_button.config(state=NORMAL)
                self.back_button.config(state=NORMAL)
                self.all_word_button.config(state=NORMAL)
                self.delete_button.config(state=NORMAL)
                self.add_button.config(state=NORMAL)
                self.edit_button.config(text="Edit")

                shown = self.word_list[self.current].shown if frequency == self.word_list[self.current].frequancy_str else 0
                self.eng_noun_entry.delete(0, END)
                self.eng_verb_entry.delete(0, END)
                self.eng_adjective_entry.delete(0, END)
                self.eng_verb_entry.delete(0, END)
                self.tr_label_entry.delete(0, END)
                self.exp_label_entry.delete(0, END)
                self.phrase_label_entry.delete(0, END)
                self.frequency_label_entry.delete(0, END)
                self.frequency_label_entry.insert(0, "0/1/7/14/30/90")
                sql_command = """UPDATE word SET noun = %s, adjective = %s, verb = %s, turkish = %s, explanation = %s, phrase = %s, frequency = %s, shown = %s WHERE user_id = %s"""
                values = (noun,adjective,verb,turkish,explanation,phrase,frequency,shown,self.word_list[self.current].user_id)
                my_cursor.execute(sql_command, values)
                data_b.commit()

                if info:
                    self.change("True")
                else:
                    if self.current + 1 == self.limit:
                        self.stantart()
                        return
                    self.current += 1
                    self.change("True")

    def back_word(self):
        if self.current < 1:return
        self.current += -1
        self.change("True")


    def train_word(self):
        self.fnish = False
        self.in_train = True
        self.word_list = Words.all_words
        self.edit_button.config(state=NORMAL)
        self.false_button.config(state=NORMAL)
        self.true_button.config(state=NORMAL)
        self.back_button.config(state=NORMAL)
        self.all_word_button.config(state=NORMAL)
        self.delete_button.config(state=NORMAL)
        self.add_button.config(state=NORMAL)
        self.current = 0
        self.limit = len(self.word_list)
        random.shuffle(self.word_list)
        self.change("True")

    def fnish_word(self):
        self.current = 0
        self.fnish = True
        self.change("True")

    def update_same(self):
        sql_command = """UPDATE word SET noun = %s, adjective = %s, verb = %s, turkish = %s, explanation = %s, phrase = %s, frequency = %s, shown = %s WHERE user_id = %s"""
        values = (self.word_list[self.current].noun, self.word_list[self.current].adjective, self.word_list[self.current].verb, self.word_list[self.current].turkish, self.word_list[self.current].explanation, self.word_list[self.current].phrase, self.word_list[self.current].frequancy_str, self.word_list[self.current].shown, self.word_list[self.current].user_id)
        my_cursor.execute(sql_command, values)
        data_b.commit()

    def next_false(self):
        if not self.in_train:
            sql_command = """UPDATE word SET shown = %s,day = %s WHERE user_id = %s"""
            values = (0,datetime.date.today(), self.word_list[self.current].user_id)
            my_cursor.execute(sql_command,values)
            data_b.commit()
            if self.current + 1 == self.limit:
                self.stantart()
                return
            self.current += 1
            self.change("True")
        else:
            if self.current + 1 == self.limit:
                self.stantart()
                return
            self.current += 1
            self.change("True")

    def make_new_list(self):
        my_cursor.execute("SELECT * FROM word")
        result = my_cursor.fetchall()
        del Words.today_words
        Words.today_words = []
        Words.all_words = []
        for x in result:
            Words(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9])
        self.word_list = Words.today_words
        self.limit = len(self.word_list)

    def next_word_auoto(self,event) :
        x = self.root.focus_get()
        y = self.true_button.cget("state")
        if y == "disabled":return
        if x == self.frequency_label_entry or x == self.eng_noun_entry or x == self.eng_adjective_entry or x == self.eng_verb_entry or x == self.exp_label_entry or x == self.tr_label_entry or x == self.phrase_label_entry:return
        if event.keysym == "2":
            self.next_true("True")
        elif event.keysym == "1":
            self.next_false()

    def add_new_word_auto(self, event):
        x = self.edit_button.cget("text")
        if x == "Edit":
            self.add_word()
        else:
            self.edit_word()

    def grid_changer(self):
        x = self.noun_label.cget("fg")
        if x != "black":
            self.noun_label.grid_remove()
            self.verb_label.grid_remove()
            self.adjective_label.config(width=30)
        else:
            self.adjective_label.config(width=15)
            self.noun_label.grid()
            self.verb_label.grid()

    def random_word(self):
        my_cursor.execute("SELECT * FROM word")
        result = my_cursor.fetchall()
        new_window = Toplevel()
        new_window.geometry("1200x950+300+65")
        new_window.configure(bg="orange")
        new_window.title("Pink: Noun -------- Green: Adj -------- Blue: Verb -------- Purple: Phrase")
        result = [x for x in result if "?" not in x[3]]

        class Random_words:
            def __init__(self, noun, adjective, verb, turkish, explanation, phrase, num):
                self.turkish = turkish
                self.noun = noun
                self.adjective = adjective
                self.verb = verb
                self.explanation = explanation
                self.phrase = phrase
                self.frame = Frame(new_window, height=32, width=950)
                self.frame.propagate(0)
                self.frame.pack(padx=20, pady=9)
                self.turkish_label = Label(self.frame, text=self.turkish)
                self.turkish_label.grid(row=0, column=0, padx=20, pady=9)
                if self.noun:
                    self.noun_label = Label(self.frame, text=self.noun, bg="#FFD1D1")
                    self.noun_label.grid(row=0, column=1, padx=20, pady=9)
                if self.adjective:
                    self.adjective_label = Label(self.frame, text=self.adjective, bg="#C1FF9C")
                    self.adjective_label.grid(row=0, column=2, padx=20, pady=9)
                if self.verb:
                    self.verb_label = Label(self.frame, text=self.verb, bg="#6EFFE2")
                    self.verb_label.grid(row=0, column=3, padx=20, pady=9)
                if self.phrase:
                    self.phrase_label = Label(self.frame, text=self.phrase, bg="#8772FF")
                    self.phrase_label.grid(row=0, column=4, padx=20, pady=9)
                if len(self.explanation) > 60:
                    self.explanation = self.explanation[:60] + "\n" + self.explanation[60:]
                self.explanation_label = Label(self.frame, text=self.explanation)
                self.explanation_label.grid(row=0, column=5, padx=20, pady=9)

        choices = random.choices(result, k=10)
        for num, choice in enumerate(choices):
            Random_words(choice[0], choice[1], choice[2], choice[3], choice[4], choice[5], num)


x = Interface()




