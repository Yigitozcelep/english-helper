import datetime
import mysql.connector

data_b = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345qweasdzxc",
    database = "ingapp"
)

#ing ingapp
my_cursor = data_b.cursor()

def collect_all_words():
    my_cursor.execute("SELECT * FROM word")
    result = my_cursor.fetchall()
    for x in result:
        Words(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9])


class Words:
    today_words = []
    all_words = []
    def __init__(self, noun: str, adjective: str, verb: str, turkish: str, explanation: str, phrase: str, frequancy, shown: int,user_id:int,  day: str):
        if len(explanation) < 3:
            self.delete_word(user_id)
            return
        self.noun = noun
        if self.noun and self.noun[-1] == "\n":self.noun = self.noun[:-1]
        self.adjective = adjective
        if self.adjective and self.adjective[-1] == "\n":self.adjective = self.adjective[:-1]
        self.verb = verb
        if self.verb and self.verb[-1] == "\n":self.verb = self.verb[:-1]
        self.turkish = turkish.replace("  ", " ").replace("/", " ,").replace(" , ", ", ").replace("  ", " ")
        self.explanation = explanation.replace("  ", " ")
        if self.explanation[-1] == "\n":self.explanation = self.explanation[:-1]
        self.data = []
        if self.turkish[-1] == "\n":
            self.turkish = self.turkish[:-1]
        if "\n" not in self.turkish:self.split_turkish()
        if "\n" not in self.explanation:self.split_explanation()
        self.phrase = phrase
        if self.phrase and self.phrase[-1] == "\n":self.phrase = self.phrase[:-1]

        self.frequancy_count = frequancy.count("/")
        self.frequancy = frequancy.split("/")
        self.frequancy_str = frequancy
        self.shown = shown
        self.user_id = user_id
        self.day = day
        for x in self.frequancy:
            if x in ["/"] + [str(a) for a in range(365)]:pass
            else:
                self.delete_word(self.user_id)
                return
        if self.shown > self.frequancy_count:
            self.delete_word(self.user_id)
            return
        self.all_words.append(self)

        year,month,day = self.day.split("-")
        year,month,day = int(year),int(month),int(day)
        if datetime.date.today() - datetime.timedelta(days=int(self.frequancy[int(self.shown)])) >= datetime.date(year,month,day):
            self.today_words.append(self)


    def split_turkish(self):
        if len(self.turkish) < 32:
            self.data.append(self.turkish.strip())
            self.turkish = "\n".join(self.data)
            return
        for num, x in enumerate(reversed(self.turkish[:32]), start=1):
            if x == " ":
                self.data.append("".join([self.turkish[:32][:-num]]).strip())
                self.turkish = self.turkish.replace(self.turkish[:33][:-num], " ")
                break
        else:
            self.data.append(self.turkish)
            self.turkish = "\n".join(self.data)
            return

        self.split_turkish()



    def split_explanation(self):
        if len(self.explanation) > 110:
            result = self.explanation.find(" ", 110)
            if result == -1:return
            self.explanation = self.explanation[:result] + "\n" + self.explanation[result:]


    def delete_word(self, user_id):
        my_cursor.execute(f"DELETE from word WHERE user_id = " + str(user_id))
        data_b.commit()




def add_word(noun:str, adjective:str, verb:str, turkish:str, explanation:str, phrase:str, frequency:str):
    today = str(datetime.date.today())
    shown = 0
    sql_command = """INSERT INTO word(noun,adjective,verb,turkish,explanation,phrase,frequency,shown,day) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (noun,adjective,verb,turkish,explanation,phrase,frequency,shown,today)
    my_cursor.execute(sql_command,values)
    data_b.commit()


collect_all_words()