#!/usr/bin/python3

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
# taken from - https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/echo_bot.py
import telebot
from telebot import types
from vars import * 

user = User()

API_TOKEN = ################################

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
# @bot.message_handler(commands=['hi', 'help', 'hello'])

@bot.message_handler(commands=['start'])
def start_process(message):
    print("done2")
    cid = message.chat.id
    markup = telebot.types.ForceReply(selective=False)
    question = bot.send_message(cid, 'What is your name?', reply_markup=markup)
    bot.register_next_step_handler(question, process_name_step)

## Places second no to overrule the start_process handler
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print('done')
    bot.reply_to(message, """
Hi there, I am HepatoBot.
I am here to help you diagnose the underlying causes of your jaundice. type /start to start the process\
""")


def process_name_step(message):
    try:
        chat_id = message.chat.id
        user.name = message.text
        markup = telebot.types.ForceReply(selective=False)
        question = bot.reply_to(message, 'How old are you?', reply_markup=markup)
        bot.register_next_step_handler(question, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_age_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if not user.age.isdigit():
            msg = bot.reply_to(message, 'Age should be a number. How old are you?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        else: 
            user.age = int(message.text)

        menu_markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        menu_markup.add("male", "female")
        msg = bot.reply_to(message, 'What is your gender?', reply_markup=menu_markup)
        bot.register_next_step_handler(msg, process_sexe_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_sexe_step(message):
    try:
        chat_id = message.chat.id
        s = message.text
        if (s == u'male') or (s == u'female'):
            user.sex = s
        else:
            raise Exception()
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + "!\nI am going to ask you a few questions about your symptoms. Press Yes if you have the symptom in consideration and No otherwise.\n")
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, symp_acronyms["pruritus"], reply_markup=markup)
        bot.register_next_step_handler(question, process_pruritus_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_pruritus_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["pruritus"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, symp_acronyms["anorexia"], reply_markup=markup)
        bot.register_next_step_handler(question, process_anorexia_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_anorexia_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["anorexia"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, symp_acronyms["anorexia_1"] , reply_markup=markup)
        bot.register_next_step_handler(question, process_anorexia_1_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_anorexia_1_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["anorexia_1"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, symp_acronyms["fever"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_fever_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_fever_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["fever"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, symp_acronyms["soft_liver_edge"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_soft_liver_edge_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_soft_liver_edge_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["soft_liver_edge"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, symp_acronyms["liver_edge_extension"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_liver_edge_extension_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_liver_edge_extension_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["liver_edge_extension"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, symp_acronyms["painful_liver"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_painful_liver_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_painful_liver_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["painful_liver"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, symp_acronyms["firm_liver"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_firm_liver_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_firm_liver_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["firm_liver"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, symp_acronyms["nodular_liver"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_nodular_liver_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_nodular_liver_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["nodular_liver"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.reply_to(message, symp_acronyms["acholia"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_acholia_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_acholia_step(message):
    try:
        chat_id = message.chat.id
        user.symptoms["acholia"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        bot.send_message(chat_id, "Thanks! Now, I am going to ask you a few questions about risk factors associated with jaundice. Press Yes if you the risk factor in consideration applies to you and No otherwise.\n")
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, fact_acronyms["alcohol"], reply_markup=markup)
        bot.register_next_step_handler(question, process_alcohol_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_alcohol_step(message):
    try:
        chat_id = message.chat.id
        user.factors["alcohol"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id, fact_acronyms["chronic_hyperbilirubinemic_conditions"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_chronic_hyperbilirubinemic_conditions_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_chronic_hyperbilirubinemic_conditions_step(message):
    try:
        chat_id = message.chat.id
        user.factors["chronic_hyperbilirubinemic_conditions"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["autoimmune_disease"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_autoimmune_disease_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_autoimmune_disease_step(message):
    try:
        chat_id = message.chat.id
        user.factors["autoimmune_disease"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["tattoo"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_tattoo_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_tattoo_step(message):
    try:
        chat_id = message.chat.id
        user.factors["tattoo"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["sex"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_sex_step(message):
    try:
        chat_id = message.chat.id
        user.factors["sex"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["unsanitary_invironment"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_unsanitary_invironment_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_unsanitary_invironment_step(message):
    try:
        chat_id = message.chat.id
        user.factors["unsanitary_invironment"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["hepatitis"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_hepatitis_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_hepatitis_step(message):
    try:
        chat_id = message.chat.id
        user.factors["hepatitis"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["surgery"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_surgery_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_surgery_step(message):
    try:
        chat_id = message.chat.id
        user.factors["surgery"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        msg = bot.send_message(chat_id,fact_acronyms["fava"] , reply_markup=markup)
        bot.register_next_step_handler(msg, process_fava_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_fava_step(message):
    try:
        chat_id = message.chat.id
        user.factors["fava"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        msg = bot.send_message(chat_id, "Thanks! Now, I am going to ask you a few questions about blood and urine test results.\n")
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, test_acronyms["urine"], reply_markup=markup)
        bot.register_next_step_handler(msg, process_urine_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_urine_step(message):
    try:
        chat_id = message.chat.id
        user.tests["urine"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        if str2bool(message.text): 
            msg = bot.send_message(chat_id, test_acronyms["choluria"] , reply_markup=markup)
            bot.register_next_step_handler(msg, process_choluria_step)
        else: 
            msg = bot.send_message(chat_id, test_acronyms["blood"] , reply_markup=markup)
            bot.register_next_step_handler(msg, process_blood_step)          
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_blood_step(message):
    try:
        chat_id = message.chat.id
        user.tests["blood"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        if str2bool(message.text): 
            msg = bot.send_message(chat_id, test_acronyms["bilirubin"])
            bot.register_next_step_handler(msg, process_bilirubin_step)
        else: 
            msg = bot.send_message(chat_id, test_acronyms["murphy"] , reply_markup=markup)
            bot.register_next_step_handler(msg, process_murphy_step)          
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_choluria_step(message):
    try:
        chat_id = message.chat.id
        user.tests["choluria"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, test_acronyms["blood"], reply_markup=markup)
        bot.register_next_step_handler(question, process_blood_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_bilirubin_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["bilirubin"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_bilirubin_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["bilirubin_c"])
        bot.register_next_step_handler(msg, process_bilirubin_c_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_bilirubin_c_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["bilirubin_c"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_bilirubin_c_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["bilirubin_u"])
        bot.register_next_step_handler(msg, process_bilirubin_u_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_bilirubin_u_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["bilirubin_u"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_bilirubin_u_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["anemia"])
        bot.register_next_step_handler(msg, process_anemia_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_anemia_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["anemia"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_anemia_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["ast"])
        bot.register_next_step_handler(msg, process_ast_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_ast_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["ast"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_ast_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["alt"])
        bot.register_next_step_handler(msg, process_alt_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_alt_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["alt"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_alt_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["proth"])
        bot.register_next_step_handler(msg, process_proth_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_proth_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["proth"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_proth_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["alk"])
        bot.register_next_step_handler(msg, process_alk_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_alk_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["alk"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_alk_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["gamma"])
        bot.register_next_step_handler(msg, process_gamma_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_gamma_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["gamma"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_alk_step)
            return
        msg = bot.send_message(chat_id, test_acronyms["K"])
        bot.register_next_step_handler(msg, process_K_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_K_step(message):
    try:
        chat_id = message.chat.id
        user.age = message.text
        if isDigit(message.text): 
            user.tests["K"] = float(message.text)
        else: 
            msg = bot.reply_to(message, 'Oops! You answer should be a number. Please try again')
            bot.register_next_step_handler(msg, process_K_step)
            return
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        question = bot.send_message(chat_id, test_acronyms["murphy"], reply_markup=markup)
        bot.register_next_step_handler(question, process_murphy_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_murphy_step(message):
    try:
        chat_id = message.chat.id
        user.tests["murphy"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add("yes", "no")
        if str2bool(message.text): 
            question = bot.send_message(chat_id, test_acronyms["murphy_result"], reply_markup=markup)
            bot.register_next_step_handler(question, process_murphy_result_step)
        else: 
            diagnosis = user.diagnose(symp_acronyms, fact_acronyms, test_acronyms)
            bot.send_message(chat_id, diagnosis)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_murphy_result_step(message):
    try:
        global user
        chat_id = message.chat.id
        user.tests["murphy_result"] = str2bool(message.text)
        # if not user.age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        # print("user: \n", user)
        # print("symptoms: \n", symptoms)
        # print("symp_acronyms: \n", symp_acronyms)
        # print("factors: \n", factors)
        # print("fact_acronyms: \n",ß fact_acronyms)
        # print("tests: \n", tests)
        # print("test_acronyms: \n", test_acronyms)
        # print("underlying_causes: \n", underlying_causes)
        diagnosis = user.diagnose(symp_acronyms, fact_acronyms, test_acronyms)
        # print("Diagnosis: ", diagnosis)
        bot.send_message(chat_id, diagnosis)
        # bot.register_next_step_handler(msg, process_murphy_result_step)
        user = User()
    except Exception as e:
        bot.reply_to(message, 'oooops')

# keyboard = telebot.types.InlineKeyboardMarkup()
# keyboard.add(telebot.types.InlineKeyboardButton('Yes', callback_data='yes'),
#              telebot.types.InlineKeyboardButton('No', callback_data='no'))


# @bot.message_handler(commands=['like'])
# def like(message):

#   cid = message.chat.id
#   bot.send_message(cid, "Do you like it?", reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no'])
# def callback_handler(call):

#     cid = call.message.chat.id
#     mid = call.message.message_id
#     answer = call.data
#     # update_lang(cid, answer)
#     try:
#         bot.edit_message_text("You voted: " + answer, cid, mid, reply_markup=keyboard)
#     except:
#         pass


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)

bot.polling()
