import aiml, os , marshal
BOT_SESSION_PATH = "/py/PycharmProject/TugasNLP/sesi"
id_sessi ="123456"
from pprint import pprint

kern = aiml.Kernel()

if os.path.isfile(BOT_SESSION_PATH+id_sessi+".ses"):
        kern.bootstrap(brainFile="bot_brain.brn")
else:
        kern.bootstrap(learnFiles="start.xml", commands="pmb")
        kern.saveBrain("bot_brain.brn")

        user_input=kern.respond(input("USER>"), id_sessi)
        sessionData=kern.getSessionData(id_sessi)
        pprint(sessionData)
        sessionFile=open(BOT_SESSION_PATH + id_sessi + '.ses', "wb")
        marshal.dump(sessionData, sessionFile)
        sessionFile.close()

        if user_input:
            pprint("Bot>" + user_input)
        else:
            pprint("Bot > Maaf kak, saya ga mengerti ")
