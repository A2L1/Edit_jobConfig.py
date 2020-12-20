import yaml

def yaml_dump(filepath, data):
    """Ajoute des infos dans un YML"""
    with open("jobConfig.yml", 'w' , encoding='utf-8') as stream:
        yaml.dump(data, stream)
modification = True

while modification:
    with open("config.yml", 'r', encoding='utf-8') as config:
        metier = yaml.safe_load(config)['Jobs']
        print(metier)

        confirm = False
        job = str(input("Which job to modify: "))
        while job not in metier:
            job = str(input("Which job to modify: "))

        thing = str(input('What do you want to change ? (experience/points/income): '))
        while thing not in ['experience','points','income']:
            thing = str(input('What do you want to change ? (experience/points/income): '))

        ajout = str(input("Do you want to change with a percentage(%) or add/remove(+) a value: "))
        while ajout not in ['%','+']:
            ajout = str(input("Do you want to change with a percentage(%) or add/remove(+) a value: "))

        valeur = float(input(f'Enter your value ({ajout}): '))
        while not confirm:
            with open("jobConfig.yml", 'r', encoding='utf-8') as stream:
                data = yaml.safe_load(stream)
                if job in metier: 
                    for action in metier[job]:
                        for item in data['Jobs'][job][action]:
                            base = data['Jobs'][job][action][item][thing]
                            if data['Jobs'][job][action][item][thing] < 0:
                                positive = -1
                            else : positive = 1

                            if ajout in ['%']:
                                new = data['Jobs'][job][action][item][thing] * valeur
                                data['Jobs'][job][action][item][thing] *= valeur
                            else:
                                new = (abs(data['Jobs'][job][action][item][thing]) + valeur) * positive
                                data['Jobs'][job][action][item][thing] = (abs(data['Jobs'][job][action][item][thing]) + valeur) * positive
                            print (f'{item}: {base} -> {new}')
            answer = str(input('Change ? (y/n/leave): '))
            while answer not in ['y','n','leave']:
                answer = str(input('Change ? (y/n/leave): '))
            if answer == 'n':
                valeur = float(input(f'Enter your value ({ajout}): '))
            elif answer == 'y':
                confirm = True
            else:
                print ("No modification")
                break
        if confirm == True: 
            yaml_dump('jobConfig.yml', data)
        suite = str(input('Modify another job ?(y/n): '))
        while suite not in ['y','n']:
            suite = str(input('Modify another job ?(y/n/leave): '))
        if suite == 'n':
            modification = False

