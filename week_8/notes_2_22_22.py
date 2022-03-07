




"""




Instagram
    this uses: 
    Location
    User credentails
    User profile 
    People you follow 
    Pictures
        Discriptions, 
        titles, 
        dates, 
        comments, 
            content 
            user 
            replies
                contnt 
                user
        locations, 
        likes, 

iMessage

    phone numbers
    text messages
        time
        user 
        content 
        read/not read 


Steam
    games 
    user credntials
    friends 
        name 
        profile pic 
        active status

Venmo
    User credentials 
    transaction history 
        sender
            user name
            priflie pic 
        recever
            user name
            priflie pic 
        money amount 
        time stamp 


netflix 
    user credentails 
    personilzed movies and shows 
        movies adn tv 
            a summary of the movie
            a preview 
            ratings 
            favorites 
            film time 
            related movies 
    list of recomeations 
    list of viewed 


______________________________________________________________

iMessage

    phone numbers - dictonary 
    text messages - dictonary
        time -  int var 
        user - string var 
        content - string var 
        read/not read - bool var 



* a dictonary is a list of pared components that go together and a list is a mixed location for data or anything * 
"""
"""
# netflix 

from xml.dom.minidom import Element


user = {
    "firstName": "Jenny", 
    "lastName": "Smith", 
    "phone": "555-555-5555",
    "email": "jennysmith@gmail.com",  
    "userName": "jennySmith",
    "password": "23gfdswerdfg"
}

user2 = {
    "firstName": "J", 
    "lastName": "Anderson", 
    "phone": "555-515-1255",
    "email": "janderson@gmail.com",  
    "userName": "andyJ",
    "password": "23g`1234dfg"
}

user_list = [user, user2]

#print(user_list)
#print(user2)

for key, value in user2.items(): 
    print(key)

    
for key, value in user2.items():
    if value == 'lastName':  
        print(value)


movies = {
    "summary": " this is a fun movie",
    'preview' : " google.com/wregt",
    'ratings' : 'PG',
    'favorites' : True,  
    'film_time': 123, 
    'related_movies': [12,123,12342536] 
}
"""

element_list = [
        {"Ag", "Silver", 107.8682},
        {"Al", "Aluminum", 26.9815386},
        {"Ac", "Actinium", 227},
        {"Ar",	"Argon",	39.948},
        {"As",	"Arsenic",	74.9216},            
        {"At",	"Astatine",	210},
        {"Au",	"Gold",	196.966569},
        {"B",	"Boron",	10.811},
        {"Ba",	"Barium",	137.327},
        {"Be",	"Beryllium",	9.012182},
        {"Bi",	"Bismuth",	208.9804},
        {"Br",	"Bromine",	79.904},
        {"C",	"Carbon",	12.0107},
        {"Ca",	"Calcium",	40.078},
        {"Cd",	"Cadmium",	112.411},
        {"Ce",	"Cerium",	140.116},
        {"Cl",	"Chlorine",	35.453},
        {"Co",	"Cobalt",	58.933195},
        {"Cr",	"Chromium",	51.9961},
        {"Cs",	"Cesium",	132.9054519},
        {"Cu",	"Copper",	63.546},
        {"Dy",	"Dysprosium",	162.5},
        {"Er",	"Erbium",	167.259},
        {"Eu",	"Europium",	151.964},
        {"F",	"Fluorine",	18.9984032},
        {"Fe",	"Iron",	55.845},
        {"Fr",	"Francium",	223},
        {"Ga",	"Gallium",	69.723},
        {"Gd",	"Gadolinium",	157.25},
        {"Ge",	"Germanium",	72.64},
        {"H",	"Hydrogen",	1.00794},
        {"He",	"Helium",	4.002602},
        {"Hf",	"Hafnium",	178.49},
        {"Hg",	"Mercury",	200.59},
        {"Ho",	"Holmium",	164.93032},
        {"I",	"Iodine",	126.90447},
        {"In",	"Indium",	114.818},
        {"Ir",	"Iridium",	192.217},
        {"K",	"Potassium",	39.0983},
        {"Kr",	"Krypton",	83.798},
        {"La",	"Lanthanum",	138.90547},
        {"Li",	"Lithium",	6.941},
        {"Lu",	"Lutetium",	174.9668},
        {"Mg",	"Magnesium",	24.305},
        {"Mn",	"Manganese",	54.938045},
        {"Mo",	"Molybdenum",	95.96},
        {"N",	"Nitrogen",	14.0067},
        {"Na",	"Sodium",	22.98976928},
        {"Nb",	"Niobium",	92.90638},
        {"Nd",	"Neodymium",	144.242},
        {"Ne",	"Neon",	20.1797},
        {"Ni",	"Nickel",	58.6934},
        {"Np",	"Neptunium",	237},
        {"O",	"Oxygen",	15.9994},
        {"Os",	"Osmium",	190.23},
        {"P",	"Phosphorus",	30.973762},
        {"Pa",	"Protactinium",	231.03588},
        {"Pb",	"Lead",	207.2},
        {"Pd",	"Palladium",	106.42},
        {"Pm",	"Promethium",	145},
        {"Po",	"Polonium",	209},
        {"Pr",	"Praseodymium",	140.90765},
        {"Pt",	"Platinum",	195.084},
        {"Pu",	"Plutonium",	244},
        {"Ra",	"Radium",	226},
        {"Rb",	"Rubidium",	85.4678},
        {"Re",	"Rhenium",	186.207},
        {"Rh",	"Rhodium",	102.9055},
        {"Rn",	"Radon",	222},
        {"Ru",	"Ruthenium",	101.07},
        {"S",	"Sulfur",	32.065},
        {"Sb",	"Antimony",	121.76},
        {"Sc",	"Scandium",	44.955912},
        {"Se",	"Selenium",	78.96},
        {"Si",	"Silicon",	28.0855},
        {"Sm",	"Samarium",	150.36},
        {"Sn",	"Tin",	118.71},
        {"Sr",	"Strontium",	87.62},
        {"Ta",	"Tantalum",	180.94788},
        {"Tb",	"Terbium",	158.92535},
        {"Tc",	"Technetium",	98},
        {"Te",	"Tellurium",	127.6},
        {"Th",	"Thorium",	232.03806},
        {"Ti",	"Titanium",	47.867},
        {"Tl",	"Thallium",	204.3833},
        {"Tm",	"Thulium",	168.93421},
        {"U",	"Uranium",	238.02891},
        {"V",	"Vanadium",	50.9415},
        {"W",	"Tungsten",	183.84},
        {"Xe",	"Xenon",	131.293},
        {"Y",	"Yttrium",	88.90585},
        {"Yb",	"Ytterbium",	173.054},
        {"Zn",	"Zinc",	65.38},
        {"Zr",	"Zirconium",	91.224},
                # sysmol name and atomic_mass
]

user_symbol = input("please enter an atomic symbol: ")


for element in element_list: 
   if element['symbol']== user_symbol: 
       print(element["atomic_mass"])



elements_d= {
    "Zr" : {"name": "Zirconium", "atomic_masss": 91.224 },

}

user_input = input("please enter an atomic symbol: ")
print(elements_d[user_input]['atomic_mass']) 
   #  print(element["symbol"]) 