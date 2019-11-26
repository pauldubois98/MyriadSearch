#temporary AI: random (no time for a proper one)
import random

def lawBot(query):
    seed=1
    for ch in query.lower():
        seed*=ord(ch)
    random.seed(seed)

    if random.random()>0.5:
        answer='Yes'
    else:
        answer='No'
    rely = 15+random.random()*30

    q = ' '.join([w for w in query[1:-1].split(' ') if len(w)>3]).replace(' ', '%20')
    link = "https://www.legislation.gov.uk/all?text="+q

    return answer, rely, link