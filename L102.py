#author is kalena
classmates={"Anna":"Sullivan", "J":"Shutz", "Cadyn":"Reger", "E1":"Kevin", "C":"Shadid", "Adrianne":"V", "Julia":"Bub", "Cathy":"Doherty", "K":"Nyhuis", "E":"Rusch", "Britney": "Salazar", "A":"Chambers", "Haley": "Greene", "Cody":"Brown", "Ami":"Loserny", "Chur":"Ley", "Sward":"Low", "Maggie":"Dunn"}
ke=classmates.keys()

def histogram(classmates):
    keys=dict()
    for char in classmates:
        if char not in keys:
            classmates[char]=1
        else:
            classmates[char]+=1
    return keys

histogram
<function histogram at 0x00000237DDC723B0>
freq={}
def countfrequency(classmates):
    for item in classmates:
        if (item in freq):
            freq[item]+=1
        else:
            freq[item]=1


for key, value in freq.items():
    print("%d: %d"%(key,value))
