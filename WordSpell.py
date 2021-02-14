def WordSpell(file, spell):
    arr=[]
    l_spell=len(spell)-1

    with open(file, 'r') as f:
        allLines = f.read().split('\n')
        for i in allLines:
            if spell in i:
                count=0
                x=True
                while count<=l_spell:
                    if spell[count] == i[count]:
                        count+=1
                        continue
                    else:
                        x=False
                        break
                if x == True:
                    arr.append(i)
                else:
                    continue
        print(arr)

WordSpell('Filename.txt', 'anyWord')