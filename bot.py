import os
from twilio.rest import Client
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import Levenshtein

apbot = Flask(__name__)
def sendMessage(text : str, to: str, fromwwp: str):

    account_sid = "AC9db2603c4e9d8758fc629c78d77c2e92"
    auth_token = "1d39effac65729ebaa495660da527f6f"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_ ='whatsapp:+558586964555',
        body=text,
        to=to
        )
    print(message.sid)

@apbot.route("/sms", methods = ["get","post"])
def reply():
    valid_words = ["oi","ola","olá", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "sim", "não", "bom dia", "boa tarde", "boa noite", "peças", "ferramenta", "hidráulica", "massa", "tinta", "ver os produtos", "enviar lista de produtos", "utilitários", "ferramentas?", "porcelana", "tintas", "cores", "mesa", "eu quero ver os preços", "quero os preços", "preço das ferramentas", "valor dos itens", "tem como ter desconto?", "valores?", "qual o valor dos produtos", "atendente", "atendimento", "atendente", "quero falar com um atendente", "eu quero falar com um atendente", "quero falar com o atendente", "quero falar com a atendente", "quero atendimento", "solicito atendimento", "eu preciso falar com um atendente", "eu preciso falar com uma atendente", "eu preciso falar com o gerente", "eu quero falar com um vendedor", "como eu falo com um atendente?", "como eu falo com um vendedor?", "como eu falo com uma atendente?", "como eu falo com o atendente?", "quero ser atendido", "quero falar com alguem", "preciso falar com um atendente","como solicitar o estoque", "eu quero ver o estoque", "gostaria de ver o estoque", "preciso do estoque"]
    msgt = request.form.get("Body")
    msgt.lower()
    sen_num= request.form.get("From")
    me_num = request.form.get("To")
    print(msgt)
    print(sen_num)

    if(msgt == "1" or msgt == "2" or msgt == "3" or msgt == "4" or msgt == "5" or msgt == "6"):
            secondReply(msgt)
    elif(msgt == "sim" or msgt == "Sim" or msgt == "s" or msgt == "ss" or msgt == "SIm" or msgt == "SIM" or msgt == "sIM" or msgt == "siM"):
           ajuda()    

    elif(msgt == "não" or msgt == "Não" or msgt == "nao" or msgt == "Nao" or msgt == "n" or msgt == "nn"):
            msg = "Muito obrigado por estar conosco!!"
            sendMessage(msg, sen_num, me_num)
            msg = "Se precisar de algo a mais so mandar um olá!"
            sendMessage(msg, sen_num, me_num)

    elif(msgt == "OI" or msgt == "Oi" or msgt == "oi" or msgt == "Olá" or msgt == "olá" or msgt == "Ola" or msgt == "ola" or msgt == "fala" or msgt == "opa" or msgt == "Fala" or msgt == "Opa" or msgt == "Bom dia" or msgt == "bom dia" or msgt == "bomdia" or msgt == "Boa tarde" or msgt == "boa tarde" or msgt == "boatarde" or msgt == "Bom tarde" or msgt == "bom tarde" or msgt == "bomtarde" or msgt == "Boa noite" or msgt == "boa noite" or msgt == "boanoite" or msgt == "Bom noite" or msgt == "bom noite" or msgt == "bomnoite" or msgt == "Boa dia" or msgt == "boa dia" or msgt == "boadia" or msgt == "Boadia" or msgt == "Bomtarde" or msgt == "Bomnoite" or msgt == "cuida" or msgt == "chama" or msgt == "agiliza" or msgt == "Pode me ajudar?" or msgt == "Pode me ajudar" or msgt == "pode me ajudar?" or msgt == "pode me ajudar" ):
        intro()
        ajuda()
  
    else:
        sugestion = find_closest_match(msgt, valid_words) 
        msg = 'Desculpa nao entendi a sua duvida, voce quis dizer "'+sugestion+'"?\n(se a palavra for essa, redigite-a)' 
        sendMessage(msg, sen_num, me_num) 
def secondReply(msgtext):
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    if(msgtext == "1"):
        msg = "Para achar a loja mais perto de você, consulte: \n https://www.google.com/maps/search/Simplifique+Home+Center+/@-3.5175806,-40.3351838,9.5z?utm_medium=social&utm_source=heylink.me"
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "2"):
        msg = """Para acessar nosso site e ficar por dentro de todas as novidades, acesse: \n https://simplifiquehomecenter.com.br"""
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "3"):
        msg = "Problemas com sua entrega? por favor entre em contato através do: \n https://api.whatsapp.com/send?phone=558599010139&utm_medium=social&utm_source=heylink.me"
        sendMessage(msg, sen_num, me_num) 
        loop()
    elif(msgtext == "4"):
        msg = "Para atendimento específico e prioritário ou comprar pelo whatssap, acesse: \n https://api.whatsapp.com/send/?phone=5585989023771&text=&app_absent=0&utm_medium=social&utm_source=heylink.me"
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "5"):
        msg = "Acesse nosso instagram para ficar ligado de todas as promoções e cupons: \n https://www.instagram.com/simplifiquehomecenter?igshid=NGVhN2U2NjQ0Yg%3D%3D"
        sendMessage(msg, sen_num, me_num)

    
def ajuda():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    
    msg = "1 - Onde fica localizado?\n2 - Site\n3 - Problemas com sua entrega?\n4 - Atendimento específico ou Compras \n5 - Instagram\n"
    sendMessage(msg, sen_num, me_num)

def intro():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = 'Olá, tudo bem?'
    sendMessage(msg, sen_num, me_num)
    msg = "Prazer eu sou o assistente virtual da da Simplifica Distribuidora e estou aqui pra ajudar!"
    sendMessage(msg, sen_num, me_num)
    msg = 'Qual serviço você deseja?'
    sendMessage(msg, sen_num, me_num)
    
def loop():
    
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = "Você precisa de mais alguma ajuda?\n (digite 'sim' ou 'não')"
    sendMessage(msg, sen_num, me_num)

def find_closest_match(user_input, valid_words):
   
    closest_match = min(valid_words, key=lambda word: Levenshtein.distance(user_input, word))
    return closest_match
if(__name__=="__main__"):
    port = int(os.environ.get("PORT", 5000))
    apbot.run(host='0.0.0.0', port=port)