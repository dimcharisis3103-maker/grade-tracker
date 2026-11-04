grades = []
ect = []
names = []

gsum = 0
esum = 0
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


x = int(ask_number('Πόσα μαθήματα θες να δηλώσεις; ', 0, 20))
        

for i in range(x):
    name = ask_question(f'Πως λέγεται το μάθημα {i+1}; ')
    names.append(name)
    k = ask_number(f'Βαθμός για το μάθημα {name}: ', 0, 10)
    y = ask_number('ECTS SCORE: ', 0.1, 10)
    
    
    
    grades.append(k)
    ect.append(y)
print()

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
    print('Δεν υπάρχχουν μαθήματα')

with open('grades.txt', 'w', encoding = 'utf-8') as file:
    for i in range(len(names)):
        file.write(f'{names[i]}, {grades[i]}, {ect[i]}\n')