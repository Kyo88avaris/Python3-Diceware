import random
import datetime

def generate_passphrase(x):
    d = open('code.txt', encoding='utf-8').readlines()

    data_dict = {}

    for data in d:
        key, value = data.split('\t')
        value = value[:-1]
        data_dict[key] = value

    diceware_password = []
    diceware = []

    counter = 0
    while counter < int(x):
        diceware_value = ""
        dice_count = 0
        while dice_count < 5:
            dice_face = random.randint(1,6)
            if dice_count == 0:
                diceware_value = str(dice_face)
            else:
                diceware_value = diceware_value + str(dice_face)
            dice_count +=1
        diceware.append(str(diceware_value))
        diceware_password.append(data_dict[str(diceware_value)])
        counter += 1

    print("Diceware Value is {}".format(diceware))
    return(" ".join(diceware_password))

x = input("select number of phrases to find: ")

secret_word = generate_passphrase(x)

now = datetime.datetime.now()

txt_writer = open('pw.txt','a')
txt_writer.write('\nLogged Date / Time {}\n'.format(str(now)))
txt_writer.write('{}\n'.format(secret_word))
txt_writer.close()

print("Your Secret Phase is: {}".format(secret_word))