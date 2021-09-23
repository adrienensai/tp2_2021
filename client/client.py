import requests


proxyDict = {
    "http": 'http://pxcache-02.ensai.fr:3128',
    "https": 'http://pxcache-02.ensai.fr:3128'
}

def getAttack(entier):
    return requests.get('http://web-services.domensai.ecole/attack/'+str(entier),proxies=proxyDict)






reponse  = getAttack(1)

print(reponse)
print(reponse.status_code)
print(reponse.text)