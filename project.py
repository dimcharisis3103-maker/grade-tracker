grades = []
ect = []
names = []


def ask_number(question, min, max):
    while True:
        try:
            k = float(input(question))
            if k >= min and k <= max:
                return k 
            else:
                print(f'Δώσε έναν αριθμό από το {min} έως το {max}')
        except ValueError:
            print('Αυτό δεν είναι αριθμός')
def ask_question(question):
    while True:
        
        x = input(question).strip()
        if x!='':
            return x
        else:                
            print('Μη δεκτό όνομα')

def load_courses():
    try:
        with open('grades.txt', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                names.append(parts[0])
                grades.append(float(parts[1]))
                ect.append(float(parts[2]))
            print(f'Φορτώθηκαν {len(names)} μαθήματα')
    except FileNotFoundError:
        print('Δεν βρέθηκαν αποθηκευμένα μαθήματα')

def add_courses():
    x = int(ask_number('Πόσα μαθήματα θες να δηλώσεις; ', 0, 20))
    for i in range(x):
        name = ask_question(f'Πως λέγεται το μάθημα {i+1}; ')
        names.append(name)
        k = ask_number(f'Βαθμός για το μάθημα {name}: ', 0, 10)
        y = ask_number('ECTS SCORE: ', 0.1, 10)
        grades.append(k)
        ect.append(y)
    print()

def show_courses():
    gsum = 0
    esum = 0
    for i in range(len(names)):
        print(f'{names[i]}: Βαθμός {grades[i]}, ECTS {ect[i]}')
    for i in range(len(grades)):
        gsum += grades[i]* ect[i]
        esum += ect[i]
    print()
    if len(names)!=0:
        average = gsum/ esum
        print('Σταθμισμένος μέσος όρος: ' , round(average, 2))
    else:
        print('Δεν υπάρχουν μαθήματα')
        
def save_courses():
    with open('grades.txt', 'w', encoding = 'utf-8') as file:
        for i in range(len(names)):
            file.write(f'{names[i]}, {grades[i]}, {ect[i]}\n')

def clear_courses():
    names.clear()
    grades.clear()
    ect.clear()
    save_courses()
    
def needed_grade():
    gsum = 0
    esum = 0
    for i in range(len(names)):
        print(f'{names[i]}: Βαθμός {grades[i]}, ECTS {ect[i]}')
    for i in range(len(grades)):
        gsum += grades[i]* ect[i]
        esum += ect[i]
    print()
    st  = ask_number(('Ποιός είναι ο στόχος σου; '), 0 , 10)
    e = ask_number(('Ποσα ECTS έχεις; '), 0.1, 10)
    x = (st *(esum + e) - gsum) / e
    if x > 10:
        print('Ο μέσος όρος δεν είναι εφικτός με ένα μάθημα')
    elif x <= 5:
        print('Αρκεί απλώς να περάσεις το μάθημα με 5')
    else:
        print('Πρέπει να γράψεις: ', round(x , 2))
    print()
    

load_courses()
while True:
    print('1. Προβολή μαθημάτων μέσου όρου')
    print('2. Προσθήκη μαθήματων')
    print('3. Διαγραφή μαθημάτων')
    print('4. Τι βαθμό χρειάζομαι;')
    print('5. Έξοδος')
    i = input('Επίλεξε: ')
    if i =='1':
        show_courses()
    elif i == '2':
        add_courses()
        save_courses()
    elif i =='3':
        n = input('Είσαι σίγουρος ότι θες να σβήσεις τα μαθήματα; ν/ο ').strip().lower()
        if n in ['ν', 'n']:
            clear_courses()
            print('Διαγράγθηκαν επιτυχώς')
            print()
        else:
            print('Ακυρώθηκε')
            print()
    elif i == '4':
        needed_grade()
    elif i == '5':
        save_courses()
        break
    else:
        print('Μη έγκυρη επιλογή')
    

    
    