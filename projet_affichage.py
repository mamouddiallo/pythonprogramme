# FONCTON QUI PERMET D'EFFECTUER UNE MULTIPLICATION

def table_multiplication(n):
    for i in range(1,11):
        print(i,"x",n,"=",i*n)
        
table_multiplication(3)
print("--------------------------------------------------------------------------------------------------")
 # FONCTION QUI PERMET D'EFFECTUER UNE ADDITION 
def addition_table(n):
    for i in range(1,11):
        print(i,"+",n,"=",i+n)

addition_table(5)   

print("--------------------------------------------------------------------------------------------------")

# FONCTION CALLBACK

def afficher_table(n,opperateur,opperation_cbk):
    for i in range(1,11):
        print(i,opperateur,n,"=",opperation_cbk(i,n))
        

def multi_cbk(a,b): # la fonction callback de la multiplication
    return a*b   

def add_cbk(a,b):# la fonction callback de l'addition 
    return a+b  

afficher_table(2,"x",multi_cbk)    
print("")
afficher_table(5,"+",add_cbk)
print("")
print("--------------------------------------------------------------------------------------------------")
print("")
# UTILISATION DE LA FONCTION LAMBDA DANS UNE MULTIPLICATION
afficher_table(2,"x",lambda a,b:a*b)
print("")
afficher_table(5,"+",lambda a,b:a+b)

   