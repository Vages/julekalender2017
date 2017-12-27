Julenissen kommer til Island og oppdager at han mangler en gave til den snilleste gutten på hele øya. Derfor sender han en kryptert melding til hjelperne sine med informasjon om hva de skal ettersende. Den krypterte meldingen består av char bokstaver (8 bit). Du må hjelpe alvene med å dekryptere meldingen.

Teksten i vedlagt fil er bygget av 32 unike islandske blokkbokstaver. Dekrypteringsnøkkelen består av de unike bokstavene i denne [filen](https://s3-eu-west-1.amazonaws.com/julekalender-knowit-2017-vedlegg/text.txt), sortert synkende på antall forekomster i teksten, og hver bokstav er representert av 5 bits. For eksempel, hvis bokstav N er brukt flere ganger i vedlagt tekst enn bokstav A, så kommer N før A i dekrypteringsnøkkelen.

Meldingen er kortere eller lik nøkkelen og dekrypteringen gjøres ved å XORe den krypterte meldingen med dekrypteringsnøkkelen. Svaret skal oppgis med char tegn (8bit).


Kryptert melding:

1110010101000001011000000011101110100101010011011010101101100000010001111101000001010010001011101001100100100011010000110101111101010011100010110001100111110010

Det islandske alfabetet: AÁBDÐEÉFGHIÍJKLMNOÓPRSTUÚVXYÝÞÆÖ

Hint: pass på å bruke unicode. 

---
Oppgaven er laget av Daniel Bugajski.
Daniel jobber i Knowit som utvikler i et av våre team!