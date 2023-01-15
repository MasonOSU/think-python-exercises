"""takes strings, prints letters in decreasing frequencies"""

from __future__ import print_function

def frequency(string):
    """sorts letters and numbers in decreasing frequency"""
    string = clean(string)
    dvar = {}
    for char in string:
        dvar[char] = dvar.get(char, 0) + 1
    dvar = sorted(dvar.items(), key = lambda dvar:dvar[1], reverse = True)
    for (key, value) in dvar:
        print(key, value)

def clean(string):
    """strips text of non-alpha-numeric characters"""
    new_string = ""
    for char in string:
        if char.isalpha() is True:
            new_string += char
    new_string = new_string.lower()
    new_string = ''.join(sorted(new_string))
    return new_string

def eng_str():
    """outputs English text"""
    return "Letter frequency is the number of times letters of the alphabet " \
           "appear on average in written language. Letter frequency analysis " \
           "dates back to the Arab mathematician Al-Kindi (c. 801–873 AD), " \
           "who formally developed the method to break ciphers. Letter frequency " \
           "analysis gained importance in Europe with the development of movable " \
           "type in 1450 AD, where one must estimate the amount of type required " \
           "for each letterform. Linguists use letter frequency analysis as a " \
           "rudimentary technique for language identification, where it is " \
           "particularly effective as an indication of whether an unknown writing " \
           "system is alphabetic, syllabic, or ideographic."

def fre_str():
    """outputs French text"""
    return "La fréquence d'apparition des lettres est une donnée statistique utilisée en " \
           "linguistique, en typographie et en cryptographie liée au fait que les utilisateurs " \
           "de la langue écrite n'utilisent pas les lettres disponibles au hasard, mais selon " \
           "l'ordonnancement de la langue, du langage et de la parole. Bien que l'alphabet ne " \
           "soit pas hiérarchisé, les lettres écrites ne sont pas utilisées à la même fréquence, " \
           "en français comme dans les autres langues. Ainsi, si l'on prend un texte en " \
           "français composé de 100 lettres, on n'aura pas 100 lettres différentes mais environ " \
           "12 fois la lettre E, 7 fois la lettre A, 7 fois la lettre I, 7 fois la lettre S, " \
           "etc., selon une loi de distribution qu'il n'est pas facile à déterminer."

def rom_str():
    """outputs Romanian text"""
    return "Articolul 26: 1) Orice persoana are dreptul la învăţătură. Invăţămîntul trebuie să " \
           "fie gratuit, cel puţin în ceea ce priveşte invăţămîntul elementar şi general. " \
           "Invăţămîntul elementar trebuie să fie obligatoriu. Invăţămîntul tehnic şi " \
           "profesional trebuie să fie la îndemîna tuturor, iar învăţămîntul superior trebuie " \
           "să fie de asemenea egal, accesibil tuturora, pe bază de merit. 2) Învăţămîntul " \
           "trebuie să urmărească dezvoltarea deplină a personalităţii umane şi întărirea " \
           "respectului faţă de drepturile omului şi libertăţile fundamentale. El trebuie să " \
           "promoveze înţelegerea, toleranţa, prietenia între toate popoarele şi toate " \
           "grupurile rasiale sau religioase, precum şi dezvoltarea activităţii Organizaţiei " \
           "Naţiunilor Unite pentru menţirenea păcii. 3) Părinţii au dreptul de prioritate " \
           "în alegerea felului de învăţămînt pentru copiii lor minori. Articolul 27: 1) " \
           "Orice persoană are dreptul de a lua parte în mod liber la viaţa culturală a " \
           "colectivităţii, de a se bucura de arte şi de a participa la progresul ştiinţific " \
           "şi la binefacerile lui. 2) Fiecare om are dreptul la ocrotirea intereselor " \
           "morale şi materiale care decurg din orice lucrare ştiinţifică, literară sau " \
           "artistică al cărei autor este."

def rus_str():
    """outputs Russian text"""
    return "Частотность (или относительная частотность) — отношение количества экземпляров " \
           "данного объекта полному количеству экземпляров всех объектов в данном множестве. " \
           "Иногда количество экземпляров данного объекта называют абсолютной частотностью " \
           "этого объекта. В лингвистике и лексикостатистике в качестве таких объектов " \
           "понимаются слова, буквы, словосочетания, в криптографии и информатике - также " \
           "сочетания букв и просто любые символы. Под множеством может пониматься какой-либо " \
           "текст, совокупность текстов (корпус) или даже язык."

frequency(rom_str())
