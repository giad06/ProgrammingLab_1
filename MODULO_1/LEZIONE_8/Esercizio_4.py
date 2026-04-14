# Esercizio 4

# Una tripletta pitagorica deve soddisfare la relazione del teorema di pitagora:
#(a,b,c) --> a^2+b^2 = c^2

def triplette_pitagoriche_rip():
    return [(a,b,c) for a in range(1,21)
             for b in range(1,21) 
             for c in range(1,21) 
             if a**2+b**2 == c**2] 

def triplette_pitagoriche_norip():
    return [(a,b,c) for a in range(1,21)
             for b in range(a,21) 
             for c in range(b,21) 
             if a**2+b**2 == c**2]


print(f"CON RIPETIZIONI: {triplette_pitagoriche_rip()}")
print(f"SENZA RIPETIZIONI: {triplette_pitagoriche_norip()}")
        

