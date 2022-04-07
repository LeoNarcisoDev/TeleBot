import telebot
from telegram import CHAVE_API

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["Segurança"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, texto)
    pass

@bot.message_handler(commands=["Eletrica"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, texto)
    pass

@bot.message_handler(commands=["Energia Solar"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, texto)
    pass



@bot.message_handler(commands=["Orcamentos"])
def responder(mensagem):
    texto = '''
    Escolha uma opção:
        /1 - Segurança
        /2 - Eletrica
        /3 - Energia Solar
        '''
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["Perguntas_Frequentes"])
def responder(mensagem):
    texto = '''
    Escolha uma opção:    
        /1 - pergunta 1
        /2 - pergunta 2
        /3 - pergunta 3
        
        '''
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Duvidas"])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Para dúvidas enviar email para.....")


@bot.message_handler(commands=["Observacoes"])
def responder(mensagem):
    # print(mensagem)  todas as informaçoes do chat estao aqui
    bot.send_message(mensagem.chat.id, "Obrigado pela atenção!!")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '''
    Olá, em que posso ajudar?
    /Orcamentos
    /Duvidas
    /Observacoes
    /Perguntas_Frequentes   
    '''
    bot.send_message(mensagem.chat.id, texto)

# loop de leitura das conversas, interacao com o bot
bot.polling()

# rodar em servidor(hiroko)ou no replit
