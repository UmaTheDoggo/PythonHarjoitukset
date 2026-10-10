The Dungeon

Leevi Luukkonen

---
-- Tarina --

Pelissä hahmo teleporttaa toiseen maailmaan. Hän tapaa Gratoksen, joka on ystävällinen örkki. Hän tarjoaa apua antamalle pelaajalle aseen. Pelaaja joutuu yhtäkkiä luolastoon, jossa hän saa pelin päätavoitteen,
joka on pysäyttää kylän alueen saastuminen tuhoamalla Mestari Peikon generaattori. Pelaaja valitsee polun luolastossa, taistelee ja päivittää halutessaan pelihahmoa. Pelin loppuvaiheessa generaattori tuhotaan
ja generaattorin romut hyötykäytetään luomalla parannettu haarniska ja ase, eli parannetaan elämäpisteiden ja aseen vahinkoa. Mestari Peikon selätyksen jälkeen hänelle opetetaan miten tuhotun generaattorin
voi korvata hiilineutraalisti ja vesistö puhdistetaan kyläläisten ja peikkojen yhteistyöllä.

---

-- Rakenne --

The Dungeonin rakenne koostuu päätiedostosta TheDungeon.py, jossa on hahmojen dialogi, polkuvalinnat ja asevalinnat
Hahmot, aseet ja monsterit luodaan TheDungeon koodissa käyttäen importattua koodia PlayerInfo.py, monsters.py ja weapons.py
Näille määritetään arvot kuten nimi, elämäpisteet ja kuinka paljon vahinkoa tekee TheDungeon.py:ssä ennen pelin alkua.
Asepäivitykset ovat kovakoodattuja TheDungeon.py tiedostoon -- weapon_choice.damage + 10 -- tyylillä

Pelillä on 2 eri loppua ja 3 eri reittiä voi kulkea pelissä. Valinta level1Centerissä määrittää pelin lopun.
Huoneet on luotu python tiedostossa room.py luomalla luokka, jolla parametrit nimi, kuvaus.
Muuttujiin on lisätty self.exit, self.monster ja self.item_collected, jotta arvoja voidaan seurata pääkoodissa
Eli huoneesta poistuminen, onko huoneessa hirviö ja onko huoneen esine kerätty.

---

-- Kasvavan kehityksen aihe --

Pelissä on otettu huomioon kasvavankehityksen aihe: Ekologinen kestävyys, eli vastuullinen kulutus ja ilmastoteot.
Tuhoamalla Mestari Peikon generaattori, joka on luonut saastumista kylän alueelle. Voidaan kierrättää generaattorin osat ja luoda hahmolle parempi ase ja haarniskaat.
Pelin lopussa opetetaan Mestari peikolle, miten hän voi jatkaa kaivostöitä hiilineutraalisti ja vesistö puhdistetaan.

---

Pelitallennus

Tallennus tapahtuu päätiedostossa, joka luo tai muokkaa olemassa olevaa .json tiedostoa ja tallentaa sinne arvot: nimi, ikä, ase, aseen vahinko, elämäpisteet, tavaraluettelo, sijainti ja onko Gratos liittynyt hahmon mukaan. Tämä toteutettu import json kirjaston avulla.

---
