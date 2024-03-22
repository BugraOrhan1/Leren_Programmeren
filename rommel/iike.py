import random
def genarator_compilimente(naam: str) -> str:
    COM = ('bla','bna','mmm')
    a = random.choice(COM) 
    return a + naam

print(genarator_compilimente('bugra'))
    

