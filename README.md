# ScriptNyelvekBeadando3
## 1. feladat
A feladat egy olyan python osztály elkészítése, amely egy egyszerű fordítási feladat elvégzésére képes. Az osztály neve legyen "Ford". Az osztály példányosításkor egy szótár szerkezetet várjon paraméterül. A szótárban a kulcsok és az értékek is legyenek szavak. Az osztálynak legyen egy "fordit" eljárása, amely két fájlnevet vár paraméterül és készítse el a második fájlt oly módon, hogy az első fájl szavain végighaladva minden, a szótárban kulcsként szereplő szót cseréljen le az adott kulcshoz értékként megadott szóra, a szótárban nem szereplő szavakat pedig hagyja változatlanul. A sorok végén pontok is szerepelhetnek, ezeket tartsa meg. Feltehető, hogy olyan sorok nem szerepelnek a bemeneti fájlban, melyekből egyetlen szó sem szerepel a szótárban. További követelmény, hogy ha a "fordit" eljárás első paramétere olyan fájlnév, amely nem létezik, adjon "Nincs input file!" hibaüzenetet.
Az osztálydefiníciót egy "bead.py" elnevezésű fájlba helyezve a test.py végrehajtása a mellékelt kimenetet kell eredményezze.
Az osztálydefiníció forráskódját (csak azt, más végrehajtható kód nélkül) kell feltölteni (UTF-8 kódolásnak megfelelően).
## 2. feladat
A feladat az első résznél leírt "Ford" osztály kiegészítése egy "visszafordit" eljárással, amely ugyanúgy két fájlnevet vár paraméterül és az eredeti szótárt használva úgy készíti el a második fájlt, hogy az első fájl szavain végighaladva minden a szótárban értékként szereplő szót cseréljen le az adott értékhez tartozó kulcsra, a szótárban nem szereplő szavakat pedig hagyja érintetlenül. A sorok végén lévő pontokat ugyanúgy tartsa meg, mint a "fordit" eljárás. Feltehető, hogy olyan sorok nem szerepelnek a bemeneti fájlban, melyekből egyetlen szó sem szerepel a szótárban, illetve feltehető, hogy egy érték csak egy kulcsnál szerepel. További követelmény, hogy ha a "visszafordit" eljárás első paramétere olyan fájlnév, amely nem létezik, adjon "Nincs input file!" hibaüzenetet.
Az osztálydefiníciót egy "bead.py" elnevezésű fájlba helyezve a test.py végrehajtása a mellékelt "vissza.txt" eredményt kell adja.
Az osztálydefiníció forráskódját (csak azt, más végrehajtható kód nélkül) kell feltölteni (UTF-8 kódolásnak megfelelően).