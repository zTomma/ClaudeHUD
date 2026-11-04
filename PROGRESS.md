# PROGRESS.md

Nota di sessione (4 nov 2026): il proprietario ha chiesto di non fermarsi a fine fase ("fai tutto tu,
fermati solo quando la HUD è pronta e fai la pull request"). Le fasi sono quindi state eseguite di
seguito, con un commit per fase, e la pull request fa da punto di approvazione. **Nulla è stato
provato in gioco.**

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
- **Riscritti a mano (53):** vedi la checklist in DESIGN.md §10 (stato `[x]`) e i generatori in `tools/hand/`.
- **Migrati ai token, layout originale (722):** tutti gli altri `.res` di `resource/`, `scripts/`, `servers/`.
- **Animazioni:** `scripts/hudanimations_tf.txt` (19 eventi riscritti, interpolatori normalizzati, colori → token).
- **Nuovi:** `resource/fonts/` (6 TTF), `licenses/`, `LICENSES.md`, `tools/`, `docs/`, `resource/ui/claudehud_fonttest.res`.
- **Rimossi da `scripts/`:** 185 voci non legate alla HUD (suoni, soundscape, script armi e classi,
  missioni MvM, talker). In `tf/custom` avrebbero sovrascritto i file del gioco. Copie identiche
  restano in `#TF2 Files/scripts`.

## Verifiche automatiche (tutte passate all'ultimo build)

`python3 tools/build.py`: lint 0 errori (778 `.res`), 37 contrasti OK, RED/BLU distinguibili con
protanopia, deuteranopia e tritanopia (ΔE2000 ≥ 32), font OK (statici, nomi interni, cifre tabulari,
glifi), layout OK a 4 rapporti d'aspetto. Gli avvisi del lint (~260) sono difetti già presenti negli
originali Valve (riferimenti a font o colori non definiti), non introdotti da ClaudeHUD.

## Cosa testare in gioco (in ordine)

1. **Font** (scheda di prova nel menu principale): ogni riga deve avere il proprio font e la propria
   dimensione, con accenti `àèéìòù` e simboli `• × – — ← → %` visibili. Se una riga appare in un font
   di sistema, il nome famiglia non è stato riconosciuto: mandami lo screenshot e l'output di console.
2. **Console all'avvio**: errori su `clientscheme.res`, font mancanti o texture.
3. **Menu principale**: pagina avorio, titolo serif, colonna sinistra, bottoni, icone in basso, tooltip
   scuri, barra superiore ("Trova una partita" in Ink).
4. **In partita**: scheda salute (numero; sotto il 49% diventa terracotta e il Segno pulsa), overheal
   (numero verde salvia), munizioni (caricatore e riserva sulla stessa linea di base; munizioni basse),
   travestimento della Spy, carica Medic (terracotta quando è pronta), metri degli oggetti, cariche.
5. **Target ID**: scheda scura con nome colorato per squadra e chip della salute.
6. **Killfeed**: righe scure, la tua riga marrone caldo, nomi RED/BLU leggibili.
7. **Timer di round e KOTH**: schede in alto al centro, chip di stato (preparazione, supplementari).
8. **CTF e carrello**: scheda punteggi in basso al centro, binario piatto del carrello.
9. **Scoreboard (TAB)**: fasce di squadra, tabelle scure leggibili, scheda inferiore bianca.
10. **Selezione classe e squadra**: tela avorio, bottoni, schede squadra (in hover compare il Segno).
11. **Opzioni (GameUI)**: tutto chiaro, testo Ink leggibile, campi di input.
12. Risoluzioni 4:3 e 16:10 se puoi: niente fuori schermo.

## Cosa potrebbe essere rotto (rischi noti)

- [Probabile] **Raggio degli angoli**: dipende dalle texture `vgui/hud/800corner*` del motore. Può
  sembrare piccolo ad alta risoluzione.
- [Probabile] **Pannelli il cui stato è forzato dal codice**: se il codice riaccende un elemento che ho
  nascosto (croce della salute, sfondi di squadra), riappare a dimensione zero, cioè invisibile. Se
  invece compare qualcosa della HUD di default, dimmi quale elemento.
- [Probabile] **Etichette in modalità chiara**: sono 656 quelle a cui ho dato un colore Ink esplicito.
  Dove una di queste sta sopra un'immagine scura del gioco potrebbe perdere contrasto.
- [Ipotesi] **Righe dello scoreboard**: i colori di squadra delle righe vengono dal codice. Per questo
  le tabelle sono scure; se il gioco usa colori diversi da quelli previsti, segnalamelo.
- [Ipotesi] **Selezione squadra**: ho nascosto le porte 3D e reso le quattro schede bottoni piatti. Se
  le schede non rispondono al click, il problema è lì.
- [Ipotesi] **Killfeed in 4:3**: le righe molto lunghe possono arrivare fino al timer di round.
- [Certo] **Chat**: cambiano solo posizione e colori. Il file `BaseChat.res` non è nel repository e non
  l'ho inventato.
- [Certo] **Loadout, zaino, negozio**: layout di Valve con i colori migrati, non ridisegnati a mano.

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
