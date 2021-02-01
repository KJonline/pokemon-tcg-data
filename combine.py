import os
import json

dir = os.getcwd() + '/json/cards/'
output_filename = 'cards.json'
numberFiles = len(os.listdir(dir))

with open(output_filename, "w") as outfile:
    first = True
    for infile_name in os.listdir(dir):
        if infile_name != 'fr':
            cards = dir + infile_name
            with open(cards) as infile:
                if first == True:
                    outfile.write('[')
                    first = False

                tmp = json.loads(infile.read())
                for card in tmp:
                    lastCard = len(tmp)
                    json.dump(card, outfile)
                    outfile.write(',')
    outfile.write(']')
