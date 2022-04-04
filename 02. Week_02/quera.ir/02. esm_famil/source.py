import csv
player_answers = []

def ready_up():
    global esm
    esm = []
    global famil
    famil = []
    global keshvar
    keshvar = []
    global rang
    rang = []
    global ashia
    ashia= []
    global ghaza
    ghaza = []

    with open('esm_famil_data.csv', 'r', encoding='utf-8') as csvfile:      # opens the csv file and inserts each column data in a seperated list
        data = csv.reader(csvfile)
        next(data)
        for i in data:
            esm.append(i[0].replace(' ',''))
            famil.append(i[1].replace(' ',''))
            keshvar.append(i[2].replace(' ',''))
            rang.append(i[3].replace(' ',''))
            ashia.append(i[4].replace(' ',''))
            ghaza.append(i[5].replace(' ',''))

def add_participant(participant, answers):                                  # creates a list of players, each element is a sub-list (element 0 is player's name and element 1 is a dictionary containing his/her answers)
    global player_answers
    player_answers.append([participant,answers])


def calculate_all():
    scores = {}                                                             # creates scores dictionary (key: player's name, value: player's score)
    for i in player_answers:
        scores[i[0]] = 0
    
    e = []
    f = []
    k = []
    r =[]
    a = []
    g = []
    for i in player_answers:                                                # keeps player's answers of each field in a seperated list, hence it could be compared
        if len(i[1]['esm'].replace(' ','')) > 0:
            e.append(i[1]['esm'].replace(' ',''))
        if len(i[1]['famil'].replace(' ','')) > 0:
            f.append(i[1]['famil'].replace(' ',''))
        if len(i[1]['keshvar'].replace(' ','')) > 0:
            k.append(i[1]['keshvar'].replace(' ',''))
        if len(i[1]['rang'].replace(' ','')) > 0:
            r.append(i[1]['rang'].replace(' ',''))
        if len(i[1]['ashia'].replace(' ','')) > 0:
            a.append(i[1]['ashia'].replace(' ',''))
        if len(i[1]['ghaza'].replace(' ','')) > 0:
            g.append(i[1]['ghaza'].replace(' ',''))


    for i in player_answers:                                                # moves through players list and calculates his/her score for each field
        if len(e) == len(player_answers):
            if (i[1]['esm'].replace(' ','') in esm) and (e.count(i[1]['esm'].replace(' ','')) == 1):
                scores[i[0]] += 10
            elif (i[1]['esm'].replace(' ','') in esm) and (e.count(i[1]['esm'].replace(' ','')) > 1):
                scores[i[0]] += 5
        else:
            if (i[1]['esm'].replace(' ','') in esm) and (e.count(i[1]['esm'].replace(' ','')) == 1):
                scores[i[0]] += 15
            elif (i[1]['esm'].replace(' ','') in esm) and (e.count(i[1]['esm'].replace(' ','')) > 1):
                scores[i[0]] += 10

        if len(f) == len(player_answers):
            if (i[1]['famil'].replace(' ','') in famil) and (f.count(i[1]['famil'].replace(' ','')) == 1):
                scores[i[0]] += 10
            elif (i[1]['famil'].replace(' ','') in famil) and (f.count(i[1]['famil'].replace(' ','')) > 1):
                scores[i[0]] += 5
        else:
            if (i[1]['famil'].replace(' ','') in famil) and (f.count(i[1]['famil'].replace(' ','')) == 1):
                scores[i[0]] += 15
            elif (i[1]['famil'].replace(' ','') in famil) and (f.count(i[1]['famil'].replace(' ','')) > 1):
                scores[i[0]] += 10

        if len(k) == len(player_answers):
            if (i[1]['keshvar'].replace(' ','') in keshvar) and (k.count(i[1]['keshvar'].replace(' ','')) == 1):
                scores[i[0]] += 10
            elif (i[1]['keshvar'].replace(' ','') in keshvar) and (k.count(i[1]['keshvar'].replace(' ','')) > 1):
                scores[i[0]] += 5
        else:
            if (i[1]['keshvar'].replace(' ','') in keshvar) and (k.count(i[1]['keshvar'].replace(' ','')) == 1):
                scores[i[0]] += 15
            elif (i[1]['keshvar'].replace(' ','') in keshvar) and (k.count(i[1]['keshvar'].replace(' ','')) > 1):
                scores[i[0]] += 10

        if len(r) == len(player_answers):
            if (i[1]['rang'].replace(' ','') in rang) and (r.count(i[1]['rang'].replace(' ','')) == 1):
                scores[i[0]] += 10
            elif (i[1]['rang'].replace(' ','') in rang) and (r.count(i[1]['rang'].replace(' ','')) > 1):
                scores[i[0]] += 5
        else:
            if (i[1]['rang'].replace(' ','') in rang) and (r.count(i[1]['rang'].replace(' ','')) == 1):
                scores[i[0]] += 15
            elif (i[1]['rang'].replace(' ','') in rang) and (r.count(i[1]['rang'].replace(' ','')) > 1):
                scores[i[0]] += 10

        if len(a) == len(player_answers):
            if (i[1]['ashia'].replace(' ','') in ashia) and (a.count(i[1]['ashia'].replace(' ','')) == 1):
                scores[i[0]] += 10
            elif (i[1]['ashia'].replace(' ','') in ashia) and (a.count(i[1]['ashia'].replace(' ','')) > 1):
                scores[i[0]] += 5
        else:
            if (i[1]['ashia'].replace(' ','') in ashia) and (a.count(i[1]['ashia'].replace(' ','')) == 1):
                scores[i[0]] += 15
            elif (i[1]['ashia'].replace(' ','') in ashia) and (a.count(i[1]['ashia'].replace(' ','')) > 1):
                scores[i[0]] += 10

        if len(g) == len(player_answers):
            if (i[1]['ghaza'].replace(' ','') in ghaza) and (g.count(i[1]['ghaza'].replace(' ','')) == 1):
                scores[i[0]] += 10
            elif (i[1]['ghaza'].replace(' ','') in ghaza) and (g.count(i[1]['ghaza'].replace(' ','')) > 1):
                scores[i[0]] += 5
        else:
            if (i[1]['ghaza'].replace(' ','') in ghaza) and (g.count(i[1]['ghaza'].replace(' ','')) == 1):
                scores[i[0]] += 15
            elif (i[1]['ghaza'].replace(' ','') in ghaza) and (g.count(i[1]['ghaza'].replace(' ','')) > 1):
                scores[i[0]] += 10

    print(scores)

### tests
ready_up()
add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})
calculate_all()
