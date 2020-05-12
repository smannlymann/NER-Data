import xml.etree.ElementTree as ET
import glob

f = open("bmjcardio_ner_dataset.csv", "w")
count = 0

for file in glob.glob("raw-data/*.xml"):
    print('Parsing ' + file + '...')
    tree = ET.parse(file)
    root = tree.getroot()

    f.write('Sentence #,Word,POS,Tag' + "\n")

    for sentence in root.iter('sentence'):
        count = count + 1
        f.write('Sentence: ' + str(count))
        for word in sentence.iter('token'):
            text = word.get('text').replace(',', '')
            pos = word.get('pos')
            if pos in [',', ':', '']:
                continue
            if text in [';', '']:
                continue
            outcome = word.find("annotation[@type='outcome']")
            if outcome is None:
                outcome = 'O'
            else:
                outcome = 'OTC'
            if pos is None:
                pos = 'none'
            f.write(',' + text + ',' + pos + ',' + outcome + "\n")

f.close()