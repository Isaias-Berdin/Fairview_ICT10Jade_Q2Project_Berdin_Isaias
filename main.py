#Drill 2 PY Code
from pyscript import document, display

def add_glee_member(e):
    document.getElementById("output1").innerHTML = ""
    g7={'Punzalan, Zeauss', 'Delin, Maria', 'Saludar, Kendra', 'Tagle, Ronald'}
    g8={'Abdul, Jibril', 'Eligino, Erich', 'Ballesteros, Nina', 'Moncupa Bella'}
    g9={'Mendoza, Orange', 'Basuil, Anya', 'Llaguno, Alezandra', 'Bacani, Rhiana'}
    g10={'Arada, Hans', 'Berdin, Isaias', 'David, Carlos', 'Taguiga, Gavin'}
    all_grades = g7 | g8 | g9 | g10
    lastname = document.getElementById("input1").value
    firstname = document.getElementById("input2").value
    member_name = (f"{lastname.title()}, {firstname.title()}")
    confirm_member = member_name in all_grades
    new_member_set = {member_name}
    all_members = all_grades | new_member_set
    total_members = len(all_grades | new_member_set)
    member_list = "<br>".join(sorted(all_members))
    document.getElementById("output1").innerHTML = f'All members:<br><br> {member_list}'
    display(f'Total members: {total_members}',target="output1")
    
#Seatwork 1 PY Code
from pyscript import document, display

def checkmember(e):
    
    name= ["Isaias Berdin", "Hans Arada", "Gavin Taguiga", "Lexi Cunanan", "Carlos Borromeo"]
    first= document.getElementById("first").value
    last= document.getElementById("last").value
    
    
    fullname = (f"{first.title()} {last.title()}")
    
    confirm_member = fullname in name
    
    message = (f'Sorry, {fullname}, your name does not appear to be on this list.' , f'Congratulations, {fullname}, welcome to the OBMC Glee Club!')
    
    document.getElementById("output1").innerHTML = message[confirm_member] 
    
#Skills Test PY Code
from pyscript import document

element = {
    "H" : ("Hydrogen", 1.008, 1),
    "He" : ("Helium", 4.003, 8),
    "C" : ("Carbon", 12.01, 4),
    "N" : ("Nitrogen", 14.01, 5),
    "O" : ("Oxygen", 16, 6),
    "F" : ("Fluorine", 19, 7),
    "Ne" : ("Neon", 20.18, 8),
    "P" : ("Phosphorus", 30.98, 5),
    "S" : ("Sulfur", 32.07, 6),
    "Cl" : ("Chlorine", 35.45, 7),
    "Ar" : ("Argon", 39.95, 8),
    "Se" : ("Selenium", 78.96, 6),
    "Br" : ("Bromine", 79.9, 7),
    "Kr" : ("Krypton", 83.8, 8),
    "I" : ("Iodine", 126.9, 7),
    "Xe" : ("Xenon", 131.3, 8),
    "Rn" : ("Radon", 222, 8)
}
   
def verify_element(e):
    element_name = document.getElementById("symbol").value.strip().title()
         
    var2 = element.get(element_name,("Element Not Found","-","-"))   

    document.getElementById("output1").innerHTML = f"""
        Symbol: {element_name}<br>
        Element: {var2[0]}<br>
        Group Number: {var2[2]}<br>
        Atomic Mass: {var2[1]}<br>
    """ 
