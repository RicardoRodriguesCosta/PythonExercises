from taskw import TaskWarrior
w = TaskWarrior()
q = ['Arrumar a Cama','Meditar','Escovar os Dentes Dia','Escovar os Dentes Noite','Fazer Exercicio','Tomar Banho','Varrer o Quarto']
#e = ['Habito','Bom']
for i in q:
    try:
        w.task_add(i,due='tomorrow',recur='daily',until='now+1yr',project='Habitos Essenciais', tags=("Bom", "Habito"))
    except:
        continue
