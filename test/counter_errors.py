err1 = "HTTP Error 404" # lien valide mais qui redirige vers aucune video existante
count1 = 0
err2 = "urlopen error" # pas d'extracteur existant pour ce type de site 
count2 = 0
err3 = "JSON" # videos privée ou 
count3 = 0
err4 = "Unsupported URL" # erreur regex
count4 = 0
general_str = "Mutated url"
general_count = 0
with open("logs.txt", 'r') as file:
    for line in file:
        if err1 in line:
            count1+=1
        if err2 in line:
            count2+=1
        if err3 in line:
            count3+=1
        if err4 in line:
            count4+=1    
        if general_str in line: 
            general_count+=1

print(f'{err1} : {count1}\n {err2} : {count2}\n {err3} : {count3}\n {err4} : {count4}\n total fuzzing : {general_count}')
