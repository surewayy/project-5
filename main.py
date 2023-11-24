from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("sure.kv")
class LoginPage(Screen):
    def show_call_instructor_popup(self):
        popup = Popup(
            title='       Call the Admin for assistance        ',
            content=Label(text="08062942039"),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()
class HomePage(Screen):
    def start_quiz(self):
        self.manager.current = "quiz"

    def reset_inputs(self):
        pass

    def logout(self):
        login_page = self.manager.get_screen("login")
        password_input = login_page.ids.passw

        # Reset the text in the password TextInput widget
        password_input.text = ""

        self.manager.current = "login"

    def start_quiz2(self):
        quiz_screen2 = self.manager.get_screen("quiz2")
        quiz_screen2.current_question = 0
        quiz_screen2.score = 0
        quiz_screen2.load_question()
        quiz_screen2.clear_buttons()
        self.manager.current = "quiz2"
class ResultScreen(Screen):
    pass

class ResultScreen2(Screen):
    pass
class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginPage())
        sm.add_widget(HomePage())
        sm.add_widget(ResultScreen())
        sm.add_widget(QuizScreen(name="quiz"))
        sm.add_widget(QuizScreen2(name="quiz2"))

        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"

        sm.current = "login"

        return sm

    def reset_quiz_and_go_home(self):
        screen_manager = self.root
        quiz_screen = screen_manager.get_screen("quiz")
        home_screen = screen_manager.get_screen("home")

        quiz_screen.reset_quiz_state()
        screen_manager.transition.direction = "right"
        home_screen.manager.current = "home"

    def set_username(self, username):
        self.username = username
class QuizScreen(Screen):
    current_question = 0
    score = 0

    questions = [
        {"question": "1. The Pacific is the ......\n ocean in the world",
         "options": ["large", "Larger", "Largest", "more large"], "correct_answer": 2},
        {"question": "2. Mr. Mensah has ..... \nmoney than Mr. Abu.", "options": ["more", "Much", "Most", "Mucher"],
         "correct_answer": 0},
        {"question": "3. He was looking sad, now he is ......",
         "options": ["happier", "happy", "more happy", "more happier"], "correct_answer": 1},
        {"question": "4. Bananas are not as ......\nas pineapples",
         "options": ["sweetest", "Sweet", "Sweeter", "much sweet"], "correct_answer": 1},
        {"question": "5. The sun gives a\n..... light than the moon.",
         "options": ["brightest", "Brighter", "more brighter", "Bright"], "correct_answer": 1},
        {"question": "6. I have seen mine; have\n you seen ..... ?",
         "options": ["your", "Yours", "your's", "yours'"], "correct_answer": 1},
        {"question": "7. Roni is a good friend of.....", "options": ["hers", "he's", "She", "We"],
         "correct_answer": 0},
        {"question": "8. Show me the boy ....\n slapped you without just cause.",
         "options": ["which", "Who", "Whom", "Whose"], "correct_answer": 1},
        {"question": "9. Is that the man ..... \ncar was stolen last week.?",
         "options": ["who's", "Whose", "Whom", "Which"], "correct_answer": 1},
        {"question": "10. The pencil ...... was broken\n belongs to her.",
         "options": ["who", "Whom", "Whose", "which"], "correct_answer": 3},
        {"question": "11. To ..... it may concern", "options": ["whom", "who", "who's", "Who"],
         "correct_answer": 0},
        {
            "question": "12. The passive form of the \nstatement, 'The boy broke the ruler'\n is, ' The ruler ......... broken by the boy.",
            "options": ["has been", "was", "Is", "was being"], "correct_answer": 1},
        {
            "question": "13. The statement, 'Mr. Bako \nis killing a ram', is best\n written in the passive form as,\n ' A ram ...........by Mr. Bako.",
            "options": ["is being killed", "was being killed", "has been killed", "had been killed"],
            "correct_answer": 0},
        {"question": "14. 'My mother cooks rice' when \nwritten in passive form will be ",
         "options": ["Rice is cooked by my mother", "Rice is being cooked by my mother", "Rice was cooked by my mother",
                     "Rice was being cooked by my mother"], "correct_answer": 0},
        {"question": "15. 'The girl opened the door'\n is written in passive form as .........",
         "options": ["The door is opened by the girl", "The door was being opened by the girl",
                     "The door was opened by the girl", "The door has been opened by the girl"], "correct_answer": 2},
        {"question": "CHOOSE THE WORD WHICH IS\n ALMOST OPPOSITE IN MEANING\n TO THE WORD IN QUESTION 16-20.\n16. The clerk is on (permanent)\nappointment.",
         "options": ["attractive", "Lasting", "Fixed", "temporary"], "correct_answer": 3},
        {"question": "17. Our team (won) the match.", "options": ["lost", "played", "watched", "Abandoned"],
         "correct_answer": 0},
        {"question": "18. I do not think that ship will ( float).", "options": ["capsize", "Leak", "sink", "Wreck"],
         "correct_answer": 2},
        {"question": "19. His cocoa farm brought him \ngreat (profit).",
         "options": ["discomfort", "Disturbance", "loss", "Problem"], "correct_answer": 2},
        {"question": "20. My friends (praised) me \nfor paying them a visit.",
         "options": ["attacked", "blamed", "disturb", "Worried"], "correct_answer": 1},
        {"question": "21.The water in the fridge has .........",
         "options": ["freezer", "Frozen", "Froze", "Freeze"], "correct_answer": 1},
        {"question": "22. The thieves have ..... away.", "options": ["run", "Ran", "Running", "runs"],
         "correct_answer": 0},
        {"question": "23. The money was ..... under the bed.", "options": ["hide", "hidden", "Hiding", "Hid"],
         "correct_answer": 1},
        {"question": "24. Why have you .... the red biro?","options": ["choose", "Chose", "chosen", "Choice"],
         "correct_answer": 2},
        {"question": "25. A dog ..... Mary yesterday","options": ["bite", "Bitting", "bitten", "Bit"],
         "correct_answer": 3}
    ]
    def on_pre_enter(self):
        self.load_question()
    def load_question(self):
        question = self.questions[self.current_question]
        self.ids.question_label.text = question["question"]
        for i, option in enumerate(question["options"]):
            self.ids[f'option_{i + 1}'].text = option

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]

        if selected_option == correct_answer:
            self.ids[f'option_{selected_option + 1}'].background_color = (0, 1, 0, 1)  # Green for correct
            self.score += 1
        else:
            self.ids[f'option_{selected_option + 1}'].background_color = (1, 0, 0, 1)  # Red for incorrect

        # Disable buttons after an option is selected
        for i in range(4):
            self.ids[f'option_{i + 1}'].disabled = False

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()
    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False
    def show_result(self):
        result_label = self.manager.get_screen("result_screen").ids.result_label
        result_label.text = f"Result: {self.score}/25"
        self.manager.current = "result_screen"
    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0
        self.load_question()
        self.clear_buttons()

class QuizScreen2(Screen):
    current_question = 0
    score = 0

    questions = [
        {
            "question": "1. Express eighty three million,\neight hundred and thirteen thousand in figures",
            "options": ["80380013", "83800013", "8300013", "800380013"], "correct_answer": 1},
        {"question": "2. Covert DXIV to Arabic numerals",
         "options": ["545", "514", "404", "245"], "correct_answer": 1},
        {"question": "3. Divide 625.75 by 5",
         "options": ["125.15", "121.55", "15.15", "109.5"], "correct_answer": 0},
        {"question": "4. Find the H.C.F of 13 and 33", "options": ["64", "3", "13", "33"],
         "correct_answer": 2},
        {"question": "5. What is the quotient of \n576 and 12?",
         "options": ["12", "49", "48", "60"], "correct_answer": 2},
        {
            "question": "6. What is the place value \nof 7 in 5,670,038?",
            "options": ["Million", "Hundred of thousand", "Tens", "Tens of thousand"], "correct_answer": 3},
        {"question": "7. State the common factors\n of 15, 30 and 60",
         "options": ["15, 30, 60", "3, 5, 10", "3, 5, 15", "5, 15, 20"], "correct_answer": 1},
        {"question": "8. If x + 17 = 27. What is x?", "options": ["9", "0", "10", "17"],
         "correct_answer": 2},
        {"question": "9. Calculate the value of x\n in the equation x/4 =42/4",
         "options": ["42", "8", "52", "168"], "correct_answer": 0},
        {"question": "10. Find the difference \nbetween 13 2/3 and 2 1/3 ",
         "options": ["15 11/15", "11 3/2", "11 6/15", "11 1/15"], "correct_answer": 3},
        {"question": "11. Find the L.C.M of 18, 27 and 36", "options": ["3", "9", "108", "54"],
         "correct_answer": 2},
        {
            "question": "12. The prime numbers \nbetween 50 and 60 are ..... and ....",
            "options": ["51, 53", "51, 57", "53, 59", "53, 57"], "correct_answer": 2},
        {"question": "13. What is the place value \nof 1 in 1476.25?",
         "options": ["thousandths", "Hundredths", "Tens", "thousands"], "correct_answer": 3},
        {"question": "14. Find the product of 52 and 13",
         "options": ["676", "767", "776", "667"], "correct_answer": 0},
        {"question": "15. What is the 6th multiple of 7 ?",
         "options": ["24", "42", "55", "44"], "correct_answer": 1},
        {"question": "16. Simplify 2½- ¼", "options": ["2 1/3", "2 1/2", "2 1/4", "2 1/9"],
         "correct_answer": 2},
        {
            "question": "17. Write 5065 in words",
            "options": ["Five hundred and sixty five", "Fifty and sixty five five", "Five thousand and sixty five",
                        "Five hundred and sixty five"], "correct_answer": 2},
        {"question": "18. If a - 5 =3. What is y² ?", "options": ["64", "45", "8", "4"],
         "correct_answer": 0},
        {
            "question": "19. What is the 6th multiple of 10 ",
            "options": ["16", "600", "60", "61"], "correct_answer": 2},
        {
            "question": "20. How many prime numbers are\nthere in the set of numbers below?\n 12,13,14,15,16,17,18,19,20 ",
            "options": ["2", "3", "4", "5"], "correct_answer": 1},
        {
            "question": "21. What is the smallest number\n which when  divided by  15 and 24,\n leave a remainder of 1? ",
            "options": ["120", "121", "122", "124"], "correct_answer": 1},
        {
            "question": "22. Find the largest number which\n when divided by 9 and 27, \nleave s no remainder.",
            "options": ["3", "6", "9", "18"], "correct_answer": 2},
        {"question": "23. Write CMLXXXII In Arabic numerals",
         "options": ["1532", "1182", "982", "778"], "correct_answer": 2},
        {"question": "24. Covert 2023 to Roman numerals ",
         "options": ["MMXXIII", "CCXXIII", "MCXII", "MDCIII"], "correct_answer": 0},
        {"question": "25. Arrange 2/3,5/6,1/2,1/4\n in ascending order ",
         "options": ["1/4,5/6,2/3,1/2", "1/4,2/3,1/2,5/6", "1/2,2/3,1/4,5/6", "1/4,1/2,2/3,5/6"], "correct_answer": 3},
    ]

    def on_pre_enter(self):
        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question]
        self.ids.question_label.text = question["question"]
        for i, option in enumerate(question["options"]):
            self.ids[f'option_{i + 1}'].text = option

    def check_answer(self, selected_option):
        correct_answer = self.questions[self.current_question]["correct_answer"]

        if selected_option == correct_answer:
            self.ids[f'option_{selected_option + 1}'].background_color = (0, 1, 0, 1)  # Green for correct
            self.score += 1
        else:
            self.ids[f'option_{selected_option + 1}'].background_color = (1, 0, 0, 1)  # Red for incorrect

        # Disable buttons after an option is selected
        for i in range(4):
            self.ids[f'option_{i + 1}'].disabled = False

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()
    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False
    def show_result(self):
        result_label = self.manager.get_screen("result_screen").ids.result_label
        result_label.text = f"Result: {self.score}/25"
        self.manager.current = "result_screen"
    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0
        self.load_question()
        self.clear_buttons()
    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = "home"

if __name__ == '__main__':
    MainApp().run()