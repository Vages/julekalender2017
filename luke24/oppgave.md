Du starter spillet i *(0,0)* og mål er i *(n-1,n-1)*, hvor *n* er størrelsen på brettet. *(0,0)* er i øvre venstre hjørne, og *(n,n)* i nedre høyre hjørne.
Det er mulig å bevege seg i fire retninger: opp (O), ned (N), høyre (H) og venstre (V)

Et koordinat kan være en portal.
Den går bare én vei (fra inngang til utgang), og et felt kan bare være med i én portal, enten som inn- eller utgang.
Hvis du går til et felt med inngang til en portal, så flyttes du umiddelbart til utgangen av portalen.  

En portal er definert slik: (&lt;x inn&gt;, &lt;y inn&gt;) -> (&lt;x ut&gt;, &lt;y ut&gt;). </br>
Eksempelvis: *(1,1)* -> (5,7)

Gitt et portalspill med *10.000*x*10.000* ruter og portaler plassert i disse [koordinatene](https://gist.github.com/knowitkodekalender/a93950d462355312740cc9a93d516f61). </br>
Hva er korteste vei fra start til mål?

Svar: Antall steg for å nå mål.


---
Eksempel:
Gitt et *20*x*20* brett, med følgende portaler, trenger man *8* steg for å nå mål. Med for eksempel denne stien: **HNNNHHHH**.
```
(4,4)   -> (12,17)
(1,3)   -> (15,19)
(10,10) -> (18,15)
```
---
Oppgaven er laget av Daniel Bugajski.
Daniel jobber i Knowit som utvikler i et av våre team!

---
Vi ønsker alltid å forbedre oss, [her](https://goo.gl/forms/20Kj9M1Wb6Xi9ntq2) kan du hjelpe oss med det. Tusen takk for alle besvarelser!

