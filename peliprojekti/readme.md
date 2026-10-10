The Dungeon

Leevi Luukkonen

---

-- RAKENNE --

The Dungeonin rakenne koostuu päätiedostosta TheDungeon.py, jossa on hahmojen dialogi, polkuvalinnat ja asevalinnat
Hahmot, aseet ja monsterit luodaan TheDungeon koodissa käyttäen importattua koodia PlayerInfo.py, monsters.py ja weapons.py
Näille määritetään arvot kuten nimi, elämäpisteet ja kuinka paljon vahinkoa tekee TheDungeon.py:ssä ennen pelin alkua.
Asepäivitykset ovat kovakoodattuja TheDungeon.py tiedostoon -- weapon_choice.damage + 10 -- tyylillä

Pelillä on 2 eri loppua ja 3 eri reittiä voi kulkea pelissä. Valinta level1Centerissä määrittää pelin lopun.
Huoneet on luotu python tiedostossa room.py luomalla luokka, jolla parametrit nimi, kuvaus.
Muuttujiin on lisätty self.exit, self.monster ja self.item_collected, jotta arvoja voidaan seurata pääkoodissa
Eli huoneesta poistuminen, onko huoneessa hirviö ja onko huoneen esine kerätty.

---

-- KASVAVANKEHITYKSEN AIHE --

Pelissä on otettu huomioon kasvavankehityksen aihe: Ekologinen kestävyys, eli vastuullinen kulutus ja ilmastoteot.
Tuhoamalla Mestari Peikon generaattori, joka on luonut saastumista kylän alueelle. Voidaan kierrättää generaattorin osat ja luoda hahmolle parempi ase ja haarniskaat.
Pelin lopussa opetetaan Mestari peikolle, miten hän voi jatkaa kaivostöitä hiilineutraalisti ja vesistö puhdistetaan.

---

Pelitallennus

Tallennus tapahtuu päätiedostossa, joka luo tai muokkaa olemassa olevaa .json tiedostoa ja tallentaa sinne arvot: nimi, ikä, ase, aseen vahinko, elämäpisteet, tavaraluettelo, sijainti ja onko Gratos liittynyt hahmon mukaan. Tämä toteutettu import json kirjaston avulla.

---
