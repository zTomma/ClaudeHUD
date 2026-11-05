# PROGRESS.md

Nota di sessione (4 nov 2026): il proprietario ha chiesto di non fermarsi a fine fase ("fai tutto tu,
fermati solo quando la HUD è pronta e fai la pull request"). Le fasi sono quindi state eseguite di
seguito, con un commit per fase, e la pull request fa da punto di approvazione. **Nulla è stato
provato in gioco.**

## Terzo giro (5 nov 2026, notte): "taccuino vivace" e controllo del contrasto nel contesto

Richiesta: più carattere ("più crazy"), menu di personalizzazione (mirini, indicatori di danno).

**Aggiunto** (DESIGN.md §11):
- ombre sfalsate "adesivo" dietro tutte le schede (in partita Moss, nei menu Ink/terracotta/salvia);
- schede che cambiano colore con lo stato: salute bassa (scheda terracotta, ombra che pulsa), overheal
  (salvia), munizioni basse, Über pronta;
- carta a quadretti e bande del brand nei menu chiari, titolo eroe con evidenziatore blush;
- **scheda Personalizza** nel menu principale: mirino (stile, colore, taglia), suono del colpo e
  dell'uccisione, numeri di danno e cure (con colore), ping, cambio arma rapido, FOV dell'arma, ricarica
  HUD. Tutte variabili di console verificate nel sorgente e salvate in `config.cfg`;
- **5 mirini ClaudeHUD originali** (punto, anello, croce aperta, angoli da taccuino, tacche), le prime
  texture della HUD: `.vtf` scritti da `tools/make_crosshairs.py` senza programmi esterni, tinti dal colore
  scelto in Personalizza. Anteprima: `docs/crosshairs.png`.

**Bug trovati e corretti** con due strumenti nuovi (`tools/context_contrast.py`, `tools/render_res.py`):
1. **Testo invisibile nei popup tutorial** (loadout, zaino, negozio, crafting, selezione classe, MOTD,
   notifiche): Valve li disegnava su carta chiara con testo scuro; la migrazione li aveva resi scuri ma il
   testo era rimasto scuro (Ink su Ink2, 1.2:1). Erano 1257 casi; ora 0. La correzione è nella migrazione,
   quindi vale anche per i file futuri.
2. **Personalizza copriva MOTD e notifiche**: i due popup del menu avevano z 1 e 10, la scheda 10-12.
   Ora la scheda sta sotto tutti i popup.
3. **Bottone dei codici promozionali** sotto la scheda: spostato sotto la barra superiore.
4. Etichette di squadra (fine partita, stato della partita) avorio su terracotta (2.96:1) → Ink.

## Secondo giro (5 nov 2026): verifica sul sorgente di TF2 e nuove schermate

Valve ha pubblicato nel 2025 il sorgente del client TF2 (Source SDK 2013). L'ho usato per controllare le
ipotesi che nel primo giro erano solo "probabili". **Quattro erano sbagliate e avrebbero prodotto bug
visibili in gioco.** Tutte sono corrette:

1. **Icone invisibili nei menu chiari.** `image_drawcolor` e `image_armedcolor` di `CExImageButton`
   leggono solo RGBA (`econ_controls.cpp`): i nomi dello scheme vengono ignorati e l'icona resta bianca su
   avorio. Ora la migrazione usa i nomi solo dove il codice li risolve (tabella in DESIGN.md §3), e il lint
   blocca gli altri casi.
2. **Target ID trasparente.** Lo sfondo `TargetIDBG` viene disegnato con `tf_hud_target_id_alpha`
   (100, cioè 39%). Ora la scheda opaca è lo sfondo della radice, che il codice ridimensiona sul contenuto, e
   così è anche arrotondata.
3. **Segno delle munizioni gonfiato.** Il codice ingrandisce `HudWeaponLowAmmoImage` fino a 5 px per lato
   quando i colpi calano: il Segno sarebbe diventato un blocco. Ora è un elemento separato (`AmmoSegno`).
4. **Riquadri della selezione armi senza fondo.** Il codice cambia i bordi di squadra dei riquadri, che in
   ClaudeHUD sono piatti: ora i riquadri hanno il proprio riempimento.

Altre verifiche: il raggio degli angoli **scala** con la risoluzione (4 unità, 9 px a 1080p; DESIGN.md §2
corretto). Le righe dello scoreboard sono colorate dal codice con costanti fisse, quindi le tabelle scure
erano la scelta giusta. Il bottone squadra deriva da `CExButton`, quindi le schede piatte funzionano. Menu
classe, squadra e principale non disattivano il proprio sfondo.

**Aggiunte** (8 pannelli riscritti in più, 61 in totale):
- percentuale Über nella scheda del Medic (`%charge%`, impostata dal codice);
- metallo dell'Engineer come scheda sopra le munizioni;
- numeri di danno, cura e metallo sul mondo in Plex con ombra (nuovi token `NumDamage`, `NumDamageBig`);
- offset corretto quando sono visibili più metri degli oggetti (`x_offset`);
- killfeed: colori con nomi verificati e fondo delle serie di uccisioni;
- attesa del respawn: chip centrata con il tempo e fascia inferiore calma;
- killcam: scheda dell'avversario con chip della salute; il file Valve aveva `FreezePanelBase` duplicato,
  resta solo il blocco effettivo;
- fine round: scheda neutra, punteggi nei colori pieni di squadra, classifica in Plex.

Tutti i controlli automatici sono passati di nuovo (lint 0 errori, contrasti, font, layout a 4 rapporti
d'aspetto).

## Fasi

| Fase | Stato | Contenuto |
|---|---|---|
| 0 | fatta | `CLAUDE.md` con le quattro sezioni del brief copiate fedelmente |
| 1 | fatta | analisi del repo, palette campionata dai riferimenti, `DESIGN.md` (10 sezioni), checklist generata |
| 2 | fatta | token (`tools/tokens.py`), `clientscheme`/`sourcescheme`/`chatscheme` generati, font installati e verificati, scheda di prova font, lint, migrazione ai token di tutti i pannelli |
| 3 | fatta | salute, munizioni, classe, target ID, layout HUD, mirino opzionale |
| 4 | fatta | killfeed, chat (posizione e scheme), timer, KOTH, CTF, carrello, obiettivo della squadra, avvisi |
| 5 | fatta | scoreboard chiaro (tabelle scure), selezione classe e squadra chiare; loadout scuro (superficie oggetti, stile migrato) |
| 6 | fatta | menu principale chiaro, barra del matchmaking, 34 dialoghi GameUI/replay/econ portati nella HUD e migrati |
| 7 | fatta | carica Medic, metri degli oggetti (tutte le varianti), bombe adesive, barre di carica, travestimento, edifici Engineer |
| 8 | fatta | animazioni (regola unica), verifica a 4:3/16:10/16:9/21:9, simulazione del daltonismo, anteprime, pulizia, README |

## File toccati

- **Generati dai token:** `resource/clientscheme.res`, `resource/sourcescheme.res`, `resource/chatscheme.res`.
- **Riscritti a mano (61):** vedi la checklist in DESIGN.md §10 (stato `[x]`) e i generatori in `tools/hand/`.
- **Migrati ai token, layout originale (714):** tutti gli altri `.res` di `resource/`, `scripts/`, `servers/`.
- **Animazioni:** `scripts/hudanimations_tf.txt` (19 eventi riscritti, interpolatori normalizzati, colori → token).
- **Nuovi:** `resource/fonts/` (6 TTF), `licenses/`, `LICENSES.md`, `tools/`, `docs/`, `resource/ui/claudehud_fonttest.res`.
- **Rimossi da `scripts/`:** 185 voci non legate alla HUD (suoni, soundscape, script armi e classi,
  missioni MvM, talker). In `tf/custom` avrebbero sovrascritto i file del gioco. Copie identiche
  restano in `#TF2 Files/scripts`.

## Verifiche automatiche (tutte passate all'ultimo build)

`python3 tools/build.py`: lint 0 errori (778 `.res`), contrasti dichiarati OK, contrasto nel contesto
0 errori (772 file), RED/BLU distinguibili con
protanopia, deuteranopia e tritanopia (ΔE2000 ≥ 32), font OK (statici, nomi interni, cifre tabulari,
glifi), layout OK a 4 rapporti d'aspetto. Gli avvisi del lint (~260) sono difetti già presenti negli
originali Valve (riferimenti a font o colori non definiti), non introdotti da ClaudeHUD.

## Cosa testare in gioco (in ordine)

1. **Font** (scheda di prova, spenta di default: in `resource/ui/mainmenuoverride.res` togli `// ` dalla
   riga `// #base "claudehud_fonttest.res"`): ogni riga deve avere il proprio font e la propria
   dimensione, con accenti `àèéìòù` e simboli `• × – — ← → %` visibili. Se una riga appare in un font
   di sistema, il nome famiglia non è stato riconosciuto: mandami lo screenshot e l'output di console.
2. **Console all'avvio**: errori su `clientscheme.res`, font mancanti o texture.
3. **Menu principale**: pagina avorio, titolo serif, colonna sinistra, bottoni, icone in basso, tooltip
   scuri, barra superiore ("Trova una partita" in Ink).
4. **In partita**: scheda salute (numero; sotto il 49% diventa terracotta e il Segno pulsa), overheal
   (numero verde salvia), munizioni (caricatore e riserva sulla stessa linea di base; munizioni basse),
   travestimento della Spy, carica Medic (terracotta quando è pronta), metri degli oggetti, cariche.
5. **Target ID**: scheda scura **arrotondata e opaca** (prima era trasparente al 39%) con nome colorato per
   squadra e chip della salute.
6. **Killfeed**: righe scure, la tua riga marrone caldo, nomi RED/BLU leggibili.
7. **Timer di round e KOTH**: schede in alto al centro, chip di stato (preparazione, supplementari).
8. **CTF e carrello**: scheda punteggi in basso al centro, binario piatto del carrello.
9. **Scoreboard (TAB)**: fasce di squadra, tabelle scure leggibili, scheda inferiore bianca.
10. **Selezione classe e squadra**: tela avorio, bottoni, schede squadra (in hover compare il Segno).
11. **Opzioni (GameUI)**: tutto chiaro, testo Ink leggibile, campi di input.
12. Risoluzioni 4:3 e 16:10 se puoi: niente fuori schermo.
13. **Nuove schermate**: percentuale Über (Medic), scheda metallo (Engineer), numeri di danno con ombra,
    chip del tempo di respawn da morto, killcam con la scheda dell'avversario, pannello di fine round.
14. **Personalizza** (menu principale): prova almeno un bottone per riga e controlla in console che
    la variabile cambi (es. `cl_crosshair_scale`). Il colore del mirino vale per i mirini a file
    (stili 1-7). Riapri il menu: i valori restano.
15. **Stati delle schede**: scendi sotto il 49% di salute (scheda terracotta, ombra che pulsa), prendi
    un overheal (numero salvia), svuota il caricatore, carica l'Über.
16. **Popup tutorial** (zaino o loadout la prima volta, o il "?" nel negozio): testo avorio leggibile.
17. **MOTD e notifiche** del menu: devono comparire sopra la scheda Personalizza.
18. **Mirini ClaudeHUD** (riga "ClaudeHUD" in Personalizza): ognuno deve apparire nitido al centro e
    prendere il colore scelto. Se vedi una **scacchiera viola/nera**, il gioco non legge il mio `.vtf`:
    dimmelo, li riconverto (i PNG sono in `tools/crosshairs/`). Errori in console su
    `vgui/crosshairs/claudehud_*` sono utili.

## Cosa potrebbe essere rotto (rischi noti)

- [Certo] **Raggio degli angoli**: 4 unità proporzionali (verificato nel sorgente). Se il raggio non scala
  in gioco, segnalamelo.
- [Probabile] **Pannelli il cui stato è forzato dal codice**: se il codice riaccende un elemento che ho
  nascosto (croce della salute, sfondi di squadra), riappare a dimensione zero, cioè invisibile. Se
  invece compare qualcosa della HUD di default, dimmi quale elemento.
- [Probabile] **Etichette in modalità chiara**: sono 656 quelle a cui ho dato un colore Ink esplicito.
  Dove una di queste sta sopra un'immagine scura del gioco potrebbe perdere contrasto.
- [Certo] **Righe dello scoreboard**: colorate dal codice con `COLOR_RED` e `COLOR_BLUE`, da cui le
  tabelle scure.
- [Ipotesi] **Percentuale Über con la Vaccinator**: il codice aggiorna `%charge%` solo per le mediguns a
  carica singola. Con la Vaccinator il numero può restare fermo: controlla.
- [Ipotesi] **Selezione squadra**: ho nascosto le porte 3D e reso le quattro schede bottoni piatti. Se
  le schede non rispondono al click, il problema è lì.
- [Ipotesi] **Killfeed in 4:3**: le righe molto lunghe possono arrivare fino al timer di round.
- [Certo] **Chat**: cambiano solo posizione e colori. Il file `BaseChat.res` non è nel repository e non
  l'ho inventato.
- [Certo] **Loadout, zaino, negozio**: layout di Valve con i colori migrati, non ridisegnati a mano.

- [Certo] **Personalizza è sempre visibile**: un bottone del `.res` non può aprire o chiudere un
  pannello senza codice. Se la trovi ingombrante, si può spostare o ridurre.
- [Certo] **Colore del mirino** sui mirini a file (stili 1-7 e ClaudeHUD): il codice li disegna con
  `cl_crosshair_red/green/blue`. [Probabile] Con il mirino di default dell'arma il colore può non cambiare.
- [Probabile] **Mirini ClaudeHUD**: il formato del `.vtf` segue l'header del SDK e lo script lo rilegge,
  ma non l'ho potuto aprire nel motore. Rischio: scacchiera viola al posto del mirino.
- [Ipotesi] **Quadretti e bande** su schermi molto larghi (oltre 21:9): le righe verticali arrivano a
  1136 unità; oltre resta tela liscia.

## Domande aperte per il proprietario

1. **BLU = Steel `#105889`**, campionato dalle cuffie della mascotte (riferimento 4) come "ardesia".
   Va bene, o hai un'altra ardesia da campionare?
2. Il **pericolo usa la terracotta**, come l'accento e RED. È coerente con "l'accento solo su ciò che
   conta", ma un pericolo distinto richiederebbe un colore che nei riferimenti non c'è. Confermi?
3. **Superfici oggetti scure** (loadout, zaino, negozio) anche se sono menu: lo impongono i colori di
   qualità del gioco. Ok?
4. **Menu principale senza illustrazione di classe e senza logo TF2** (pagina tipografica). Ok, o
   preferisci riavere l'illustrazione?
5. **Cartelle `#… Files`**: restano nel repository come originali per la migrazione. Vuoi una
   distribuzione "pulita" (solo `info.vdf`, `resource/`, `scripts/`, `servers/`) come ZIP di release?
6. **Colori derivati** (SteelLight, TerracottaDeep, CloudDeep, Ink2…): sono calcolati con una formula
   dai campionati, non presi dai riferimenti. Li approvi?
