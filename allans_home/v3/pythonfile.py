from allan import Smartlearning

class Assistant:

    def __init__(self, name):
        self.name = name
        
    
    def reply(self,text):
        intent = intentclassifier.predict(text)

        replies = {
            'one thousand seven hundred' : damage1700,
            'one thousand six hundred and seventy-five' : damage1675,
            'one thousand six hundred and fifty' : damage1650,
            'one thousand six hundred and thirty-five' : damage1635,
            'one thousand six hundred' : damage1600,
            'one thousand five hundred and fifty' : damage1550,
            'one thousand five hundred and thirty-five' : damage1535,
            'one thousand three hundred and fifty-six' : damage1356,
            'one thousand three hundred and forty-five' : damage1345,
            'one thousand two hundred and sixty-five' : damage1265,
            'one thousand two hundred and five' : damage1205,
            'one thousand one hundred and ninety-five' : damage1195,
            'one thousand one hundred and fifty-two' : damage1152
            }##add lower (69) and doc (114) back to text.py in machine learning code
            ##"C:\Users\joshu\AppData\Local\Programs\Python\Python310\Lib\site-packages\sklearn\feature_extraction\text.py"## 
            

        try:
            reply_func = replies[intent]

            if callable(reply_func):
                reply_func(text, intent)
        except KeyError:
            print("Sorry, I didn't understand")
        except Exception as e:
            print("There has been an error, you can keep on using the program just please report this to Joe :D")
            print("Error: " + str(e))
    
 

intentclassifier = Smartlearning()
assistant = Assistant("Badger")

def damage1700():
    print("1700")
def damage1675():
    print("1675")
def damage1650():
    print("1650")
def damage1635():
    print("1635")
def damage1600():
    print("1600")
def damage1550():
    print("1550")
def damage1535():
    print("1535")
def damage1356():
    print("1356")
def damage1345():
    print("1345")
def damage1265():
    print("1265")
def damage1205():
    print("1205")
def damage1195():
    print("1195")
def damage1152():
    print("1152")


text = input("hhfghhhy: ")
assistant.reply(text)