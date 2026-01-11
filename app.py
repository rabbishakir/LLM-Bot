import google.generativeai as genai

from dotenv import load_dotenv
import os

import database as db;

load_dotenv()

class BaseModel:

    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        print("API KEY LOADED:", bool(self.GEMINI_API_KEY))

    def getModel(self):
        try:
            genai.configure(api_key=self.GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-2.0-flash')
            return model
        except Exception as e:
            print(e)

class AppFeatures(BaseModel):

    def __init__(self): # since the parent has a constructor. I will have to set an explicit constructor
        super().__init__()
        self.database = db.MongoDB()
        self.current_user = None


    def get_database(self):
        return self.__database

    def first_menu(self):

        first_input = input(
            '''
            How would you like to proceed?
            1: registration
            2: login
            3: exit
            '''
        )

        if first_input == "1":
            #registration
            self.__register()
        elif first_input == "2":
            #login
            self.__login()
        else:
            exit()

    def __register(self):

       user_name = input("Enter Your Name:  ")
       user_email = input("Enter Your Email:  ")
       user_password = input("Enter Your Passwor:  ")

       user = self.database.find_user({"email": user_email})

    
       if user:
            print("User already Exists")
            app.first_menu()
       else:
           self.database.insert_user({
                "name": user_name,
                "email": user_email,
                "password": user_password
            })
           print("Registered successfully")
           self.first_menu()
           

    def __login(self):
        email = input("Enter your email: ")
        user = self.database.find_user({"email": email})
        self.current_user = user
        if user:
            print("User exist")
            password = input("Enter your password: ")
            if password == user['password']:
                print("Welcome to Gemini App")
                self.second_menu()
            else:
                print("Password Does not match")
                self.first_menu()

        else:
            print("User not found")
    
    def second_menu(self):

        second_input = input(
            '''
            What do you want to do?
            1: Sentiment Analysis
            2: Language Translate
            3: exit
            '''
        )

        if second_input == "1":
            #sentimant analysis
            self.__sentiment_analysis()
            
        elif second_input == "2":
            #Language Translate 
            self.__translate_language() 
        else:
            exit()

    def __sentiment_analysis(self):
        user_text = input("Enter the sentense to analyze the sentiment: ")
        model = self.getModel()
        response = model.generate_content(f"Determine the emotional sentiment expressed in this sentence: {user_text}")
        result = response.text
        # inserting the log to the database
        self.database.insert_sentiment_log(
                {
                    "user_id": self.current_user["_id"],
                    "ask":user_text,
                    "relpy":result
                
                }
            )
        print(result)
        self.second_menu()

    def __translate_language(self):
        user_text = input("Enter the sentense to translate: ")
        language = input("Enter the language to translate into: ")
        model = self.getModel()
        response = model.generate_content(f"Determine the language of this sentence: {user_text} and translate to {language}")
        result = response.text
        self.database.insert_translation(
            {
                "user_id": self.current_user["_id"],
                "ask":user_text,
                "reply":result
            }
        )
        print(result)
        self.second_menu()
       
app = AppFeatures()
app.first_menu()














