import sqlite3

conn = sqlite3.connect('projett666DB.db')

cur = conn.cursor()  

# # creation de la table contact 

def create_table():
    req1="CREATE TABLE contact(id INTEGER PRIMARY KEY, prenom TEXT, nom TEXT, email TEXT UNIQUE, adresse TEXT, telephone NUMBER UNIQUE)" 
    cur.execute(req1) 
    conn.commit()
    
create_table()

def ajouter_contact():
    prenom = input("veuiller donner votre prenom")
    nom = input("veuiller donner votre nom  ")
    email = input("veuiller donner votre email")
    adresse = input("veuiller donner votre adresse ")
    telephone = int(input("veuiller donner telephone "))
    req1="INSERT INTO contact(prenom, nom, email, adresse, telephone) Values (?,?,?,?,?)"
    cur.execute(req1,(prenom, nom, email, adresse,telephone))
    conn.commit() 
    
ajouter_contact() 

def modifier_contact():
    nouveau_numero = "767324056"
    ancien_numero = "784059847"
    cur.execute(
        "UPDATE contact SET telephone = ? WHERE telephone = ?",
        (nouveau_numero, ancien_numero)
    )
    conn.commit()
    
modifier_contact()

def supprimer_contact():
    telephone =int(input("veuiller dooner votre numero"))
    cur.execute(
        "DELETE FROM contact WHERE telephone = ?", 
        (telephone,)
    )
    conn.commit()
    
supprimer_contact()

def afficher_un_contact():
    row = cur.execute(
        "SELECT * FROM contact WHERE telephone  = 785904536").fetchone() 
    print(row)
       
afficher_un_contact()

def afficher_tous_contacts():
    rows = cur.execute("SELECT * FROM contact").fetchall()
    print(rows)
    
afficher_tous_contacts()

def rechercher_un_contact():
    rows = cur.execute("SELECT * FROM contact WHERE telephone ='773452389' ").fetchone()
    
    print(rows)
    
    conn.commit()
    
rechercher_un_contact()

conn.close()