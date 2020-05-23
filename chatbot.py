###################################################################
#                                                                 #
#                            LIBRARIES                            #
#                                                                 #
###################################################################
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from textblob import TextBlob

###################################################################
#                                                                 #
#                           DEFINITIONS                           #
#                                                                 #
###################################################################
robot_name = "Robot {} {}"
seperator = "->"
info_text = "To quit, type 'bye'. Now, you are able to start to chat. :-)"
chatbot = ChatBot(robot_name)

###################################################################
#                                                                 #
#                            TRAININGS                            #
#                                                                 #
###################################################################
print("##########################################################")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")
print("##########################################################")

###################################################################
#                                                                 #
#                             PROGRAM                             #
#                                                                 #
###################################################################
print(info_text)
flag = True
while flag is True:
    client = input("\t\t")

    # Use for translations: .translate(to="en")
    if not client.lower().__eq__("bye"):
        if client.lower().__eq__("thanks") or client.lower().__eq__("thanks you"):
            flag = False
            print("You'ree welcomee!")
        else:
            if chatbot.get_response(client) is not None:
                answer = chatbot.get_response(client)
                answer = TextBlob(str(answer))
                print(robot_name.format(seperator, str(answer)))
            else:
                print(robot_name, end="")
                print(TextBlob(chatbot.get_response(client)).translate(to="tr"))
                sent_tokens.remove(client)
    else:
        flag = False
        print("Bbye!")
