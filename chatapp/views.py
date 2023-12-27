from django.http import HttpResponse
from django.shortcuts import render

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import spacy





nlp = spacy.load('en-core-web-sm')

bot = ChatBot('chatApplication', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

list_to_train = [
    "hi",
    "hi there! How may i help you?",
    "what is django?",
    "Django is a free and open source Python based web framework that follows the model template views (MTV) ",
    "who is the best teacher for django?",
    "According to my experience sir shakib is best one for django",

]

list_train = ListTrainer(bot)
list_train.train(list_to_train)


def index(request):
    #  usermessage=request.GET.get('userMessage')
    #  print(usermessage)
    #  return HttpResponse('usermessage')

    return render(request, "index.html")


def getresponse(request):
    usermessage = request.GET.get('userMessage')
    # print(usermessage)
    ChatResponse = str(bot.get_response(usermessage))
    return HttpResponse(ChatResponse)

# Create your views here.acativate
