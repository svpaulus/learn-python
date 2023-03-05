import datetime
import time

def time_as_sentence(hour, minute):
    hour_as_text = ['nula', 'jedna', 'dvě', 'tři', 'čtyři', 
                    'pět', 'šest', 'sedm', 'osm', 'devět',
                    'deset', 'jedenáct', 'dvanáct']
    if hour > 12:
        hour -= 12

    if hour > 1 and hour < 5:
        result = ['jsou']
    else:
        result = ['je']

    result.append(hour_as_text[hour])
    nearest_5minute = 5 * (minute // 5)

    minute_as_text = ['nula', 'deset', 'dvacet', 'třicet', 'čtyřicet', 'padesát']

    if nearest_5minute == 0:
        pass
    elif nearest_5minute == 15:
        result.append('patnáct')
    else:
        index_10minute = minute // 10
        result.append(minute_as_text[index_10minute])
        if nearest_5minute % 10 == 5:
            result.append('pět')

    return result

def capitalized_sentence(words):
    sentence = []
    for word in words:
        capitalized = [letter.capitalize() for letter in word]    
        sentence.append(''.join(capitalized))
    return sentence

def test_hours():
    for hour in range(24):
        print(time_as_sentence(hour, 0))

def test_minutes():
    for minute in range(60):
        time_words = time_as_sentence(11, minute)
        print(capitalized_sentence(time_words))

def create_table():
    return ['JEJSOUJEDNA',
            'DEVĚTPĚTDVĚ',
            'SEDMDVANÁCT',
            'DESETŘIŠEST',
            'OSMJEDENÁCT',
            'ČTYŘIADESET',
            'DVACETŘICET',
            'PATNÁCTNULA',
            'MEČTYŘICETM',
            'PADESÁTDPĚT']

def create_lights():
    result = []
    for r in range(10):
        result.append('00000000000')
    return result

def simulate_oclock(letters, lights):
    for r in range(10):
        for c in range(11):
            if lights[r][c] == '1':
                print(letters[r][c], end=' ')
            else:
                print('.', end=' ')
        print()


def convert_sentence_to_lights(sentence):
    words_to_pos = {}
    lights = create_lights()
    words_to_pos['JE'] = [0, 0]
    words_to_pos['JSOU'] = [0, 2]
    words_to_pos['JEDNA'] = [0, 6]
    words_to_pos['DEVĚT'] = [1, 0]
    words_to_pos['PĚT'] = [1, 5]
    words_to_pos['DVĚ'] = [1, 8]
    words_to_pos['SEDM'] = [2, 0]
    words_to_pos['DVANÁCT'] = [2, 4]
    words_to_pos['DESET'] = [3, 0]
    words_to_pos['TŘI'] = [3, 4]
    words_to_pos['ŠEST'] = [3, 7]
    words_to_pos['OSM'] = [4, 0]
    words_to_pos['JEDENÁCT'] = [4, 3]
    words_to_pos['ČTYŘI'] = [5, 0]
    words_to_pos['DESET'] = [5, 6]
    words_to_pos['DVACET'] = [6, 0]
    words_to_pos['TŘICET'] = [6, 5]
    words_to_pos['PATNÁCT'] = [7, 0]
    words_to_pos['NULA'] = [7, 7]
    words_to_pos['ČTYŘICET'] = [8, 2]
    words_to_pos['PADESÁT'] = [9, 0]
    words_to_pos['PĚT'] = [9, 8]
    for word in sentence:
        pos = words_to_pos[word]
        r = pos[0]
        c = pos[1]
        row_of_lights = list(lights[r])
        row_of_lights[c:c+len(word)] = len(word) * '1'
        lights[r] = ''.join(row_of_lights)
    return lights


# lights = create_lights()
# letters = create_table()
# lights[0] = '00111100000'
# lights[5] = '11111000000'

# print(letters)
# print(lights)

# letters = create_table()
# sentence = time_as_sentence(20, 48)
# sentence = capitalized_sentence(sentence)
# lights = convert_sentence_to_lights(sentence)
# simulate_oclock(letters, lights)


# test_minutes()

letters = create_table()
last_sentence = []

while True:
    now = datetime.datetime.now()
    hours = now.hour
    minutes = now.minute
    words = time_as_sentence(hours, minutes)
    sentence = capitalized_sentence(words)
    if sentence != last_sentence:
        lights = convert_sentence_to_lights(sentence)
        simulate_oclock(letters, lights)
        last_sentence = sentence
        print()
    time.sleep(1)
