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

x = int(ask_number('Πόσα μαθήματα θες να δηλώσεις; ', 1, 20))
        

for i in range(x):
    name = ask_question(f'Πως λέγεται το μάθημα {i+1}; ')
    names.append(name)
    k = ask_number(f'Βαθμός για το μάθημα {names[i]}: ', 0, 10)
    y = ask_number('ECTS SCORE: ', 0.1, 10)
    
    
    
    grades.append(k)
    ect.append(y)

for i in range(x):
    print(f'{names[i]}: Βαθμός {grades[i]}, ECTS {ect[i]}')

for i in range(len(grades)):
    
    gsum += grades[i]* ect[i]
    esum += ect[i]

average = gsum/ esum
print('Σταθμισμένος μέσος όρος: ' , round(average, 2))

with open('grades.txt', 'w', encoding = 'utf-8') as file:
    for i in range(x):
        file.write(f'{names[i]}, {grades[i]}, {ect[i]}\n')