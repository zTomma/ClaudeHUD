# DESIGN.md — ClaudeHUD

Regole del linguaggio visivo. Ogni pannello si costruisce da qui; se una scelta contraddice questo
documento si corregge la scelta, non il documento (CLAUDE.md, regola di lavoro 7).
Tutti i valori citati sono generati da `tools/tokens.py`: questo documento li spiega, non li definisce.

---

## 1. Concept

**Il taccuino sul campo.** In partita la HUD è una manciata di piccole schede scure e calde ai margini
dello schermo, con numeri chiari a cifre fisse e un solo segnale terracotta quando qualcosa
richiede attenzione. Fuori dalla partita diventa una pagina avorio con titoli serif, come un taccuino
editoriale.

*Perché questo concept:* i riferimenti (carta, mano che scrive, quaderno a quadretti, avorio e
terracotta) parlano di un compagno di pensiero calmo. TF2 chiede velocità. Le schede in combattimento
e le pagine nei menu sono la stessa metafora a due velocità.

### Dai principi alle regole

| Principio (CLAUDE.md) | Regola concreta |
|---|---|
| Calma | In condizioni normali, in combattimento è visibile al massimo **un** elemento terracotta. Niente gradienti, ombre o contorni. L'unico movimento ripetuto è il segnale di pericolo (§7). |
| Calore | Nessuna superficie nero puro o bianco puro in gioco: le schede sono `#272624` (Ink lifted) e il testo è avorio `#FAF9F5`. Nei menu la tela è avorio, il bianco è riservato alle schede. |
| Chiarezza | Una scheda, un numero grande. Le etichette compaiono solo se il numero da solo è ambiguo. |
| Ordine tipografico | Due famiglie, una scala di 15 passi (§4). Ogni testo usa un passo della scala, niente dimensioni ad hoc. |
| Generosità di spazio dove non c'è azione | Nei menu il padding delle schede è 16 unità e i margini 24–48. In combattimento il padding è 4. |
| In combattimento: piccolo, compatto, non al centro | Nessun elemento permanente nel rettangolo centrale `c-120…c+120 × c-80…c+80`. Lì passano solo transitori: target ID sotto il mirino, avvisi di cattura. |
| L'accento solo su ciò che conta | Terracotta = "agisci adesso" (§3, regole d'uso). |
| Menu chiari ed editoriali | Divisione delle modalità in §9. |
| La leggibilità vince | Schede di combattimento **opache** (il contrasto non dipende dalla mappa), numeri sempre in Plex Sans SemiBold a cifre tabulari, contrasti verificati da script (§3). |

---

## 2. Forme

**Grammatica:** superfici piene, piatte, con angoli arrotondati. Le superfici si separano per
salto tonale (scheda su gioco, chip dentro la scheda; scheda bianca su tela avorio), mai con un contorno.

| Elemento | Costruzione nel motore | Note |
|---|---|---|
| Scheda arrotondata | `paintbackgroundtype "2"` oppure bordo `ClCard` (bordo senza linee con `backgroundtype "2"`). Il colore viene dal `bgcolor_override` del pannello. | Angoli selezionabili con `RoundedCorners`: 15 tutti, 5 sinistra, 10 destra, 3 sopra, 12 sotto. |
| Superficie squadrata | `paintbackgroundtype "0"` / bordo `ClSquare` / `ImagePanel` con `fillcolor` | Obbligatoria per barre di progresso, filetti e pannelli sotto le 12 unità. |
| Filetto | Pannello alto 1 unità (`DkLine` / `LtLine`), oppure i bordi `ClRuleDk` / `ClRuleLt` | Solo come divisore interno a una scheda. |
| Contorno | Bordi `ClInputDk` / `ClInputLt` / `ClInputFocus` | **Solo campi di input** (testo, combo, checkbox). |

**Raggio (verificato nel sorgente TF2, `Panel::GetCornerTextureSize`):** il motore ne disegna uno solo.
Per i pannelli proporzionali (tutta la HUD) vale `max(scala(8 unità) / 2, 8 px)`: **4 unità proporzionali**,
cioè 9 px a 1080p, 12 px a 1440p e il minimo di 8 px a 720p. Scala con la risoluzione e non si imposta da
`.res`. La HUD usa **un solo raggio**, quello del motore, ovunque.
*Limite del motore:* su pannelli più piccoli di due raggi (8 unità) gli angoli si sovrappongono. Da qui la
regola delle superfici squadrate sotto le 12 unità, con un margine di sicurezza.
*Target ID (verificato):* il codice ridimensiona la radice sul contenuto e disegna lo sfondo `TargetIDBG`
con l'alfa di `tf_hud_target_id_alpha` (100, cioè 39%). La scheda opaca arrotondata è quindi lo sfondo della
radice (`hudlayout.res`, `CMainTargetID`), e `TargetIDBG` resta vuoto.

**Il Segno (motivo grafico):** una barra terracotta verticale, larga 2 unità, sul bordo sinistro di
ciò che è attivo o importante: voce di menu selezionata, riga del giocatore locale, scheda in pericolo.
È il segno a matita a margine di un taccuino. È geometrico e originale, e non è radiale, quindi non
somiglia al logo di Claude. Si costruisce con un `ImagePanel` `fillcolor` (scala con la risoluzione)
oppure, nei bottoni, con i bordi `ClMarkDk` / `ClMarkLt` (3 px fissi: i bordi a linee sono in pixel).
Variante puntuale: il glifo `•` (U+2022, presente in Plex) in terracotta come indicatore di stato.

**Vietato:** contorni attorno alle schede; ombre, gradienti, bisellature; texture della HUD di default
(pannelli marroni, fumetti, bottoni color cuoio); superfici nero puro o bianco puro in gioco; elementi
ruotati; più di un raggio; qualsiasi forma radiale a raggi o asterisco (troppo vicina al logo di
Claude); il logo di Claude o Anthropic.

---

## 3. Colori

Nessun valore è scritto a memoria. I colori di base sono **campionati** dagli screenshot di riferimento
(`tools/sample_reference.py` li ricampiona); tutti gli altri sono **derivati** da quelli con una formula
(`mix(a, b, t)` = interpolazione in sRGB, la stessa che usa il gioco per l'alfa). Dove serviva un
contrasto minimo, `t` è risolto numericamente dallo script.

### Palette campionata

| Nome | Valore | Fonte |
|---|---|---|
| `Ivory` | `#FAF9F5` | ref 5 (anthropic.com), page background, 91.6% of pixels |
| `Pampas` | `#F4F3EE` | ref 3, swatch labelled #F4F3EE |
| `White` | `#FFFFFF` | ref 3, swatch labelled #FFFFFF |
| `Cloud` | `#B1ADA1` | ref 3, swatch labelled #B1ADA1 |
| `Ink` | `#141413` | ref 5, body text and 'Try Claude' button fill |
| `Terracotta` | `#D97757` | ref 3, swatch labelled #D97757; ref 5 blob (identical pixel) |
| `Coral` | `#E18166` | ref 4, pixel mascot body |
| `Blush` | `#F3C6B5` | ref 4, light stripe at bottom |
| `Sage` | `#BCD2CB` | ref 2, right panel background |
| `Green` | `#519B86` | ref 4, dark green bar at bottom |
| `Moss` | `#64736B` | ref 2, halftone dots (bottom right), modal value |
| `Steel` | `#105889` | ref 4, mascot headphones (l'"ardesia" di BLU) |

### Colori derivati

| Nome | Valore | Formula |
|---|---|---|
| `Ink2` | `#272624` | `mix(Ink, Cloud, 0.12)` |
| `Ink3` | `#373632` | `mix(Ink, Cloud, 0.22)` |
| `InkLine` | `#4D4B46` | `mix(Ink, Cloud, 0.36)` |
| `InkWarm` | `#34241E` | `mix(Ink, Terracotta, 0.16)` |
| `CloudDeep` | `#6F6D65` | `mix(Cloud, Ink, 0.42)`, risolto per ≥4.6:1 su Pampas/Ivory/White |
| `TerracottaDeep` | `#A05A43` | `mix(Terracotta, Ink, 0.29)`, risolto per ≥4.6:1 su Pampas/Ivory/White |
| `SteelLight` | `#80A5BD` | `mix(Steel, Ivory, 0.48)`, risolto per ≥4.6:1 su Ink2/Ink3/InkWarm |
| `CloudFaint` | `#74726A` | `mix(Ink2, Cloud, 0.56)`, risolto per ≥3.1:1 su Ink2 (solo testo disabilitato) |
| `InkFaint` | `#8B8A87` | `mix(Pampas, Ink, 0.47)`, risolto per ≥3.1:1 su Pampas/Ivory (solo testo disabilitato) |
| `CloudLine` | `#D2CFC7` | `mix(Ivory, Cloud, 0.55)` |
| `PampasDeep` | `#E0DED7` | `mix(Pampas, Cloud, 0.30)` |

### Ruoli (i nomi che usano i file .res)

`Dk*` = modalità scura (in gioco), `Lt*` = modalità chiara (menu). Le varianti di trasparenza si
chiamano `<Token>A<percentuale>` (per esempio `DkCardA50`) e sono generate su richiesta della migrazione.

| Token | Colore | Alfa | | Token | Colore | Alfa |
|---|---|---|---|---|---|---|
| `DkCard` | Ink2 | 100% | | `LtCanvas` | Ivory | 100% |
| `DkCardSoft` | Ink2 | 91% | | `LtCanvasVeil` | Ivory | 93% |
| `DkCardGhost` | Ink2 | 59% | | `LtCard` | White | 100% |
| `DkChip` | Ink3 | 100% | | `LtCardAlt` | Pampas | 100% |
| `DkLine` | InkLine | 100% | | `LtCardPressed` | PampasDeep | 100% |
| `DkCardLocal` | InkWarm | 100% | | `LtLine` / `LtLineStrong` | CloudLine / Cloud | 100% |
| `DkText` | Ivory | 100% | | `LtText` | Ink | 100% |
| `DkTextMuted` | Cloud | 100% | | `LtTextMuted` | CloudDeep | 100% |
| `DkTextFaint` | CloudFaint | 100% | | `LtTextFaint` | InkFaint | 100% |
| `DkAccent` / `DkAccentSoft` | Terracotta | 100% / 38% | | `LtAccent` (riempimenti) / `LtAccentText` (testo) | Terracotta / TerracottaDeep | 100% |
| `DkPositive` / `DkPositiveFill` | Sage / Green | 100% | | `LtPositive` | Green | 100% |
| `DkInfo` | SteelLight | 100% | | `LtButton` / `LtOnButton` | Ink / Ivory | 100% |
| `DkRedText` / `DkRedFill` | Terracotta | 100% | | `LtButtonHover` / `LtOnButtonHover` | Terracotta / Ink | 100% |
| `DkBluText` / `DkBluFill` | SteelLight / Steel | 100% | | `LtRedText` / `LtRedFill` | TerracottaDeep / Terracotta | 100% |
| `DkOnRed` / `DkOnBlu` | Ink / Ivory | 100% | | `LtBluText` / `LtBluFill` | Steel | 100% |
| `DkScrim` | Ink | 63% | | `LtScrim` | Ink | 43% |
| `Untinted` | White | 100% (tinta neutra per texture di gioco) | | `Clear` | — | 0% |

### Regole d'uso

1. **Terracotta significa "agisci adesso"**: salute sotto il 49%, munizioni basse, carica pronta
   (Über, Kritzkrieg, carica dello scudo…), cattura in corso contro di te, voce selezionata o in hover nei
   menu, riga del giocatore locale. Mai decorazione.
2. In modalità chiara la terracotta pura (`LtAccent`) è solo riempimento o segno: come testo piccolo su
   avorio non raggiunge 4.5:1 (2.9:1). Per il testo si usa `LtAccentText`.
3. Sage / Green indicano solo stati positivi: overheal, buff, cura ricevuta.
4. Il blu Steel è riservato a BLU. In modalità scura il testo BLU usa `SteelLight`, perché Steel puro su
   scuro arriva solo a 2.5:1.
5. I colori di qualità e rarità degli oggetti (Unique giallo, Unusual viola…) sono semantica di gioco e
   restano invariati. Per questo le superfici oggetti sono scure (§9).
6. Le schede di combattimento sono opache. Le superfici traslucide (`DkCardSoft`: chat, overlay) sono
   verificate contro lo sfondo di gioco peggiore, bianco e nero.

### Nomi di colore: dove il motore li accetta (verificato nel sorgente TF2)

Nei `.res` un colore si può scrivere come nome dello scheme solo dove il codice lo risolve:

- tutte le chiavi `*_override` registrate da Panel, Button, Label, Frame e TextEntry
  (`REGISTER_COLOR_AS_OVERRIDABLE`);
- `fillcolor` e `drawcolor` degli `ImagePanel`;
- `fgcolor` di CExLabel, CExButton e CExRichText;
- le variabili colore degli elementi HUD (`CPanelAnimationVar`, per esempio quelle del killfeed).

Le `image_*color` dei bottoni con icona (`CExImageButton`) leggono **solo** RGBA: un nome viene ignorato
in silenzio, e anche alcuni file di Valve hanno questo errore. Ovunque il nome non sia garantito,
`tools/migrate.py` scrive l'RGBA generato dal token, con il commento `// token: X`. Il lint segnala ogni
nome messo dove il motore non lo accetta.

### Contrasti verificati (`python3 tools/contrast.py --markdown`)

Minimo dichiarato: **7:1** per numeri di combattimento e testo primario, **4.5:1** per ogni altro testo,
**3:1** solo per testo disabilitato e icone. Gli sfondi traslucidi sono calcolati nel caso peggiore.

| Testo | Sfondo | Rapporto | Minimo | Esito | Uso |
|---|---|---:|---:|:-:|---|
| `DkText` #FAF9F5 | `DkCard` #272624 | 14.35:1 | 7.0:1 | OK | numeri di combattimento, testo primario |
| `DkText` #FAF9F5 | `DkChip` #373632 | 11.48:1 | 7.0:1 | OK | testo su chip |
| `DkText` #FAF9F5 | `DkCardLocal` #34241E | 14.07:1 | 7.0:1 | OK | killfeed locale |
| `DkText` #FAF9F5 | `DkCardSoft` #272624 @91% | 10.82:1 | 4.5:1 | OK | chat (card traslucida, sfondo peggiore) |
| `DkTextMuted` #B1ADA1 | `DkCard` #272624 | 6.74:1 | 4.5:1 | OK | etichette, riserva munizioni |
| `DkTextMuted` #B1ADA1 | `DkChip` #373632 | 5.39:1 | 4.5:1 | OK | etichette su chip |
| `DkTextMuted` #B1ADA1 | `DkCardSoft` #272624 @91% | 5.08:1 | 4.5:1 | OK | testo secondario chat |
| `DkTextFaint` #74726A | `DkCard` #272624 | 3.14:1 | 3.0:1 | OK | solo stati disabilitati |
| `DkAccent` #D97757 | `DkCard` #272624 | 4.84:1 | 4.5:1 | OK | pericolo: salute/munizioni basse |
| `DkAccent` #D97757 | `DkCardLocal` #34241E | 4.75:1 | 4.5:1 | OK | accento su riga locale |
| `DkPositive` #BCD2CB | `DkCard` #272624 | 9.52:1 | 4.5:1 | OK | overheal / buff |
| `DkInfo` #80A5BD | `DkCard` #272624 | 5.78:1 | 4.5:1 | OK | informazioni neutre |
| `DkRedText` #D97757 | `DkCard` #272624 | 4.84:1 | 4.5:1 | OK | nome RED su card |
| `DkBluText` #80A5BD | `DkCard` #272624 | 5.78:1 | 4.5:1 | OK | nome BLU su card |
| `DkRedText` #D97757 | `DkCardLocal` #34241E | 4.75:1 | 4.5:1 | OK | nome RED su riga locale |
| `DkBluText` #80A5BD | `DkCardLocal` #34241E | 5.67:1 | 4.5:1 | OK | nome BLU su riga locale |
| `DkOnRed` #141413 | `DkRedFill` #D97757 | 5.90:1 | 4.5:1 | OK | testo su fascia RED |
| `DkOnBlu` #FAF9F5 | `DkBluFill` #105889 | 7.17:1 | 4.5:1 | OK | testo su fascia BLU |
| `LtText` #141413 | `LtCanvas` #FAF9F5 | 17.50:1 | 7.0:1 | OK | testo primario menu |
| `LtText` #141413 | `LtCard` #FFFFFF | 18.43:1 | 7.0:1 | OK | testo su card |
| `LtText` #141413 | `LtCardAlt` #F4F3EE | 16.59:1 | 7.0:1 | OK | testo su card secondaria |
| `LtText` #141413 | `LtCardPressed` #E0DED7 | 13.69:1 | 4.5:1 | OK | testo su bottone premuto |
| `LtTextMuted` #6F6D65 | `LtCanvas` #FAF9F5 | 4.92:1 | 4.5:1 | OK | testo secondario |
| `LtTextMuted` #6F6D65 | `LtCard` #FFFFFF | 5.18:1 | 4.5:1 | OK | testo secondario su card |
| `LtTextMuted` #6F6D65 | `LtCardAlt` #F4F3EE | 4.67:1 | 4.5:1 | OK | testo secondario su card secondaria |
| `LtTextFaint` #8B8A87 | `LtCardAlt` #F4F3EE | 3.11:1 | 3.0:1 | OK | solo stati disabilitati |
| `LtAccentText` #A05A43 | `LtCanvas` #FAF9F5 | 4.94:1 | 4.5:1 | OK | accento come testo |
| `LtAccentText` #A05A43 | `LtCardAlt` #F4F3EE | 4.68:1 | 4.5:1 | OK | accento come testo su card |
| `LtRedText` #A05A43 | `LtCard` #FFFFFF | 5.20:1 | 4.5:1 | OK | nome RED su scoreboard |
| `LtBluText` #105889 | `LtCard` #FFFFFF | 7.56:1 | 4.5:1 | OK | nome BLU su scoreboard |
| `LtRedText` #A05A43 | `LtCardAlt` #F4F3EE | 4.68:1 | 4.5:1 | OK | nome RED su riga alternata |
| `LtBluText` #105889 | `LtCardAlt` #F4F3EE | 6.80:1 | 4.5:1 | OK | nome BLU su riga alternata |
| `LtOnRed` #141413 | `LtRedFill` #D97757 | 5.90:1 | 4.5:1 | OK | testo su fascia RED |
| `LtOnBlu` #FAF9F5 | `LtBluFill` #105889 | 7.17:1 | 4.5:1 | OK | testo su fascia BLU |
| `LtOnButton` #FAF9F5 | `LtButton` #141413 | 17.50:1 | 7.0:1 | OK | bottone primario |
| `LtOnButtonHover` #141413 | `LtButtonHover` #D97757 | 5.90:1 | 4.5:1 | OK | bottone primario in hover |
| `LtPositive` #519B86 | `LtCard` #FFFFFF | 3.29:1 | 3.0:1 | OK | icone/stati positivi |

### RED e BLU (anche con daltonismo)

Distanza percettiva CIEDE2000 tra i colori di squadra, con visione normale e simulata
(Machado, Oliveira & Fernandes 2009, severità 1.0). Soglia di distinguibilità adottata: ΔE ≥ 20.

| Coppia | Luminanza | ΔE normale | protanopia | deuteranopia | tritanopia | Esito |
|---|---:|---:|---:|---:|---:|:-:|
| `DkRedText` #D97757 / `DkBluText` #80A5BD (nomi su scheda scura) | 1.19:1 | 39.1 | 32.2 | 36.2 | 47.6 | OK |
| `DkRedFill` #D97757 / `DkBluFill` #105889 (fasce, riempimenti) | 2.42:1 | 48.0 | 42.3 | 53.7 | 59.7 | OK |
| `LtRedText` #A05A43 / `LtBluText` #105889 (nomi su scheda chiara) | 1.45:1 | 39.2 | 35.7 | 43.4 | 52.3 | OK |

*Attenzione:* i testi RED e BLU su scuro hanno luminanza simile (1.19:1). Si distinguono per tinta:
gialla/arancio contro blu, che resta separata anche per protanopia e deuteranopia. Nei punti dove la
squadra conta più del nome (scoreboard, target ID) la squadra è indicata anche da una fascia piena,
dove la differenza di luminanza è 2.42:1.

---

## 4. Tipografia

| File (`resource/fonts/`) | Nome famiglia interno (name ID 1) | Peso | Versione | Uso |
|---|---|---:|---|---|
| `IBMPlexSans-Regular.ttf` | IBM Plex Sans | 400 | 3.005 (release `@ibm/plex-sans@1.1.0`) | testo UI |
| `IBMPlexSans-Medium.ttf` | IBM Plex Sans Medm | 500 | 3.005 | enfasi UI, etichette |
| `IBMPlexSans-SemiBold.ttf` | IBM Plex Sans SmBld | 600 | 3.005 | numeri di combattimento |
| `SourceSerif4-Regular.ttf` | Source Serif 4 | 400 | 4.005 (release `4.005R`) | testo editoriale |
| `SourceSerif4-Semibold.ttf` | Source Serif 4 Semibold | 600 | 4.005 | titoli di sezione, numeri grandi nei menu |
| `SourceSerif4Display-Semibold.ttf` | Source Serif 4 Display Semibold | 600 | 4.005 | titoli ≥ 20 unità |

*Nota sui nomi:* ClientScheme usa il nome famiglia **interno** letto dal file, non il nome del file:
`IBM Plex Sans SmBld` e non "IBM Plex Sans SemiBold". `tools/check_fonts.py` lo riverifica ogni volta,
insieme a file statici (niente `fvar`), peso, cifre tabulari (Plex: 600 unità per ogni cifra, Source
Serif 4 Semibold: 520) e copertura di `àèéìòù ÀÈÉÌÒÙ` e dei simboli usati.
Glifi **assenti** in Plex, quindi vietati nelle etichette: `▲ ▼ ● ○ ◆ ◇ ★ ✕`. Disponibili:
`• · × – — ← → ↑ ↓ % / : + -`.

### Scala (tall in unità proporzionali su 480 righe; il motore scala con l'altezza dello schermo)

| Nome | Famiglia | Peso | Tall | Uso |
|---|---|---|---:|---|
| `TypeDisplay` | Source Serif 4 Display Semibold | 600 | 34 | titolo menu principale |
| `TypeTitle` | Source Serif 4 Display Semibold | 600 | 24 | titoli di schermata (classe, team, scoreboard) |
| `TypeHeading` | Source Serif 4 Semibold | 600 | 16 | titoli di sezione |
| `TypeSerifNum` | Source Serif 4 Semibold | 600 | 20 | numeri grandi nei menu (punteggi) |
| `TypeSerifBody` | Source Serif 4 | 400 | 11 | testo editoriale |
| `TypeBodyL` | IBM Plex Sans | 400 | 11 | testo UI grande |
| `TypeBody` | IBM Plex Sans | 400 | 9 | testo UI |
| `TypeBodyStrong` | IBM Plex Sans Medm | 500 | 9 | testo UI in evidenza, bottoni |
| `TypeCaption` | IBM Plex Sans | 400 | 8 | didascalie |
| `TypeLabel` | IBM Plex Sans Medm | 500 | 7 | micro-etichette maiuscole |
| `NumXL` | IBM Plex Sans SmBld | 600 | 26 | salute, caricatore |
| `NumL` | IBM Plex Sans SmBld | 600 | 18 | timer di round, carica |
| `NumM` | IBM Plex Sans SmBld | 600 | 13 | riserva, metallo, contatori |
| `NumS` | IBM Plex Sans SmBld | 600 | 10 | numeri piccoli in card |
| `NumXS` | IBM Plex Sans Medm | 500 | 8 | micro-numeri |
| `NumDamage` | IBM Plex Sans SmBld | 600 | 13 | numeri di danno, cura e metallo sul mondo (con ombra) |
| `NumDamageBig` | IBM Plex Sans SmBld | 600 | 18 | critici e numeri grandi sul mondo (con ombra) |

*Ombra:* i numeri che fluttuano sul mondo 3D non hanno una scheda dietro, quindi sono l'unico testo della
HUD con `dropshadow`. È l'unico caso in cui la leggibilità richiede di rinunciare alla grammatica piatta.

I 150 font **legacy** che il codice del gioco chiede per nome (`HudFontSmall`, `TargetID`…) restano
definiti e sono rimappati automaticamente: famiglia TF2 → Plex SemiBold, TF2 Secondary → Plex Regular,
Verdana/Tahoma → Plex, titoli dei soli menu → Source Serif 4, con fattore di dimensione per famiglia
(`tools/build_scheme.py --report` stampa la mappa completa). I font di icone (Marlett, tfd, Team
Fortress, glifi controller) restano invariati.

### Regole

1. **Numeri di combattimento** (salute, munizioni, timer, carica, metallo): solo `Num*`, cioè Plex
   SemiBold a cifre tabulari. Mai serif in combattimento.
2. **Serif** solo in modalità chiara: titoli e numeri grandi (punteggi nello scoreboard).
3. Allineamento: numeri isolati in una scheda centrati in verticale e allineati a destra quando c'è
   un'unità o una riserva accanto; colonne di numeri (scoreboard) allineate a destra; testo allineato a
   sinistra. Centrato solo per titoli display e numeri singoli dentro chip quadrate.
4. Maiuscolo solo per `TypeLabel` (micro-etichette, `allcaps "1"`). Il resto in maiuscola iniziale.
5. Contrasto: si applica la tabella del §3. Una dimensione sotto `TypeCaption` (8) non porta mai
   informazioni necessarie al combattimento.

---

## 5. Griglia e spaziatura

- **Unità di base: 4** unità proporzionali (su 480 righe; 9 px a 1080p). Posizioni e dimensioni sono
  multipli di 4. La mezza unità (2) è ammessa solo per inset interni e per lo spessore del Segno.
- Scala delle distanze: `2 · 4 · 8 · 12 · 16 · 24 · 32 · 48`.
- **Margine dal bordo dello schermo** delle schede di combattimento: 12.
- **Padding:** scheda di combattimento 4, scheda di menu 16, voce di lista 8 orizzontale × 4 verticale.
- **Distanza tra schede vicine:** 4 in combattimento, 8–16 nei menu.
- **Binario inferiore:** tutte le schede di combattimento in basso condividono il bordo inferiore
  (`r12`) e l'altezza base 36. Le schede di classe (cariche, metri) si impilano sopra la scheda munizioni
  a passi di 4, con la stessa larghezza.
- Posizioni relative: `c±N` per gli elementi centrati, `rN` per quelli ancorati a destra o in basso,
  in modo da adattarsi a 16:9, 16:10 e 4:3 senza file separati.
- **Verifica:** `python3 tools/layout_check.py` calcola i rettangoli delle schede principali a 4:3, 16:10,
  16:9 e 21:9 e segnala elementi fuori schermo, sovrapposti o nel rettangolo centrale.
- **Colonna sinistra**, dal basso: blocco salute (r76–r12), arma trasportata (r108), stato del
  travestimento (r144), chat (r272). **Binario destro:** munizioni (r100/r48), metro oggetto (r184/r48),
  barre di carica sottili (r56), carica Medic (r88).

---

## 6. Gerarchia

**Leggibile in 0.2 secondi**, in ordine:

1. Salute (`NumXL`, avorio; terracotta sotto il 49%).
2. Caricatore (`NumXL`).
3. Stato di classe critico: Über o carica pronta, metallo dell'Engineer, cloak della Spy (`NumL`/`NumM`, terracotta quando è pronto).
4. Avvisi di pericolo: cattura nemica in corso, bomba o carrello vicino al traguardo.

**Discreto ma sempre disponibile:** riserva munizioni (`NumM`, `DkTextMuted`), timer di round (`NumL`,
diventa terracotta solo negli ultimi 30 secondi tramite le animazioni del gioco), killfeed, chat,
punteggi, stato dei punti di controllo.

**Solo su richiesta:** scoreboard, menu, statistiche, loadout.

Le dimensioni seguono la gerarchia: livello 1 = `NumXL` 26, livello 2 = `NumL` 18, livello 3 =
`NumM` 13, livello 4 = testo 8–9 in `DkTextMuted`.

---

## 7. Movimento

**Regola unica:** *tutto entra in 0.20 s con curva `Deaccel` ed esce in 0.15 s con `Accel`; i cambi di
stato di colore durano 0.12 s `Linear`; l'unico movimento ripetuto è il pericolo, un ciclo a 2 Hz
(0.5 s) che fa pulsare il Segno e riporta sempre al colore di base.*

| Caso | Durata | Interpolatore |
|---|---:|---|
| Comparsa (pannello, notifica, voce) | 0.20 s | `Deaccel` |
| Scomparsa | 0.15 s | `Accel` |
| Cambio colore di stato (hover, danno, cura, carica pronta) | 0.12 s | `Linear` |
| Pericolo (salute sotto il 49%, munizioni basse) | ciclo di 0.5 s | `Linear` 0.12 s verso l'alfa piena e ritorno, sul Segno; il numero resta terracotta fisso |
| Niente | — | rimbalzi, `Flicker`, `Spline`, `Gain`, `Bias`, lampeggi di stato, movimenti oltre 8 unità |

Le animazioni stanno in `scripts/hudanimations_tf.txt`. Gli eventi di salute, munizioni, carica Medic,
timer, supplementari e frecce dei menu sono riscritti a mano (`tools/hand/patch_anims.py`); negli altri
eventi del gioco gli interpolatori vietati sono sostituiti in blocco (`Spline`/`Bounce`/`Gain` →
`Deaccel`, `Flicker` → `Linear`, `Bias` → `Accel`/`Deaccel`). Le loro durate restano quelle di Valve,
perché molti eventi sono sequenze temporizzate dal codice. Ogni colore animato è un token dello scheme,
mai un letterale: il lint lo controlla.

---

## 8. Iconografia

- Le icone sono texture del gioco (classi, killfeed, buff, edifici) usate come **maschere monocromatiche**
  colorate con `drawcolor` / `image_drawcolor`: `DkText` o `DkTextMuted` su scuro, `LtText` su chiaro.
  Le icone con colori di significato (qualità degli oggetti, buff di squadra) restano `Untinted`.
- Le nuove icone si costruiscono **solo** con primitive geometriche (pannelli pieni, il Segno) e con i
  glifi Plex verificati (§4), su riquadri da 8, 12 o 16 unità, con tratto di 2 unità.
- Mai icone multicolore, mai contorni, mai ombre.
- **Texture nuove (.vtf/.vmt):** in questa versione **nessuna**. Ogni forma si ottiene con primitive del
  motore, così non c'è rischio di texture mancanti (scacchiera viola). Se in futuro servissero (un raggio
  che scala con la risoluzione, per esempio), la procedura prevista è: PNG 32×32 bianco con alfa →
  conversione con VTFEdit o `vtfcmd` in RGBA8888 con flag `NoMip`, `NoLOD`, `Clamp S/T` → `.vmt`
  `UnlitGeneric` con `$translucent 1`, `$vertexcolor 1`, `$vertexalpha 1`, `$ignorez 1` → bordo
  `scalable_image` con `"color"` dal token.
- **Logo:** nessuna texture di logo. Il menu principale usa un titolo tipografico.

---

## 9. Divisione delle modalità

**Regola:** *scuro dove c'è la partita o ci sono gli oggetti del gioco; chiaro dove si naviga e si legge.*
L'assegnazione file per file è codice (`tools/modes.py`) ed è riportata nella checklist (§10).

| Modalità | Superfici |
|---|---|
| **Scura** (`Dk*`) | Tutta la HUD di gioco: salute, munizioni, armi, target ID, killfeed, chat, obiettivi, timer, notifiche, avvisi CTF e passtime. Spettatore, killcam e freezecam, pannelli di vittoria, statistiche di fine vita, menu rapidi di Engineer e Spy, menu vocali e provocazioni, HUD MvM e stazione potenziamenti. Superfici oggetti: zaino, negozio, crafting, scambi, loadout degli oggetti, quest. |
| **Chiara** (`Lt*`) | Menu principale e i suoi pannelli, selezione classe, selezione squadra, scoreboard (anche MvM), opzioni e altri dialoghi GameUI (`sourcescheme.res`), server browser, MOTD, info mappa, matchmaking e lobby, gradi e statistiche, dialoghi aperti dai menu. |
| **Sempre scuro** | Tooltip e popover, anche sopra i menu chiari (come su claude.ai). |
| **Scuro dentro una pagina chiara** | Le due tabelle giocatori dello scoreboard: il gioco colora le righe per squadra dal codice, con colori pensati per sfondi scuri. Restano schede `DkCard` sulla pagina avorio (eccezione di leggibilità, vedi CLAUDE.md: la leggibilità vince). |

*Perché le superfici oggetti restano scure:* i colori di qualità e rarità sono definiti dal gioco e
calibrati per sfondi scuri. Su avorio il giallo Unique arriverebbe a 1.5:1.

*Colori espliciti in modalità chiara:* nei file chiari ogni label e ogni bottone senza colore proprio
riceve un token `Lt*` esplicito (`tools/migrate.py`), perché altrimenti erediterebbe il default dello
scheme, che è scuro (testo avorio), e sparirebbe su una scheda bianca. Dentro un popover scuro l'intero
sottoalbero torna in modalità scura.

*Chat:* lo stile delle righe viene da `chatscheme.res` (generato, scuro). Il file di layout dei
messaggi (`BaseChat.res`) non è nel repository: non lo ricreo per non inventare nomi di elementi
(CLAUDE.md, regola 2). La posizione della chat è in `hudlayout.res`.

---

## 10. Checklist di copertura

Generata da `python3 tools/coverage.py` (stato calcolato dal lint, non scritto a mano).
Fase per fase vedi `PROGRESS.md`.

<!-- COVERAGE:BEGIN (generato da tools/coverage.py, non modificare a mano) -->

Legenda: `[x]` riscritto a mano o generato dai token · `[~]` layout originale, stile interamente migrato ai token · `[ ]` da fare.

**Totale 778 file .res** — riscritti 61 · generati 3 · migrati 714 · da fare 0.

<details><summary><code>resource/</code> — 25 file (generato 3, migrato 22)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `askconnectpanel.res` | chiara |
| [x] | `chatscheme.res` | scura |
| [x] | `clientscheme.res` | scura |
| [~] | `commentaryexplanationdialog.res` | chiara |
| [~] | `commentaryitem.res` | chiara |
| [~] | `createofflinepracticepage.res` | chiara |
| [~] | `g15.res` | scura |
| [~] | `gamelogo.res` | chiara |
| [~] | `gamemenu.res` | chiara |
| [~] | `loadcommentarydialog.res` | chiara |
| [~] | `loadingdialog.res` | chiara |
| [~] | `loadingdialognobanner.res` | chiara |
| [~] | `modevents.res` | scura |
| [~] | `muteplayerdialog.res` | chiara |
| [~] | `newgamechapterpanel.res` | chiara |
| [~] | `newgamedialog.res` | chiara |
| [~] | `offline_practice.res` | chiara |
| [~] | `optionssubmultiplayer.res` | chiara |
| [~] | `pdacontrolpanelscheme.res` | scura |
| [~] | `playerlistdialog.res` | chiara |
| [~] | `reportplayerdialog.res` | chiara |
| [x] | `sourcescheme.res` | chiara |
| [~] | `spectatormenu.res` | scura |
| [~] | `spectatormodes.res` | scura |
| [~] | `training.res` | chiara |

</details>

<details><summary><code>resource/roundinfo/</code> — 1 file (migrato 1)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `tc_hydro.res` | scura |

</details>

<details><summary><code>resource/ui/</code> — 307 file (migrato 247, riscritto 60)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `abusereportsubmitdialog.res` | chiara |
| [~] | `achievementgroup.res` | chiara |
| [~] | `achievementitem.res` | chiara |
| [~] | `achievementsdialog.res` | chiara |
| [~] | `annotationspanelcallout.res` | scura |
| [~] | `badgepanel.res` | chiara |
| [~] | `casualrankpanel.res` | chiara |
| [~] | `casualwelcomedialog.res` | chiara |
| [~] | `charinfoarmorysubpanel.res` | scura |
| [~] | `charinfoloadoutsubpanel.res` | scura |
| [~] | `charinfopanel.res` | scura |
| [~] | `chatpopup.res` | scura |
| [~] | `cheatdetectiondialog.res` | chiara |
| [~] | `classloadoutpanel.res` | scura |
| [~] | `classmenu.res` | chiara |
| [x] | `classselection.res` | chiara |
| [~] | `classselection_sc.res` | chiara |
| [~] | `classtipsitem.res` | chiara |
| [~] | `classtipslist.res` | chiara |
| [x] | `claudehud_fonttest.res` | scura |
| [~] | `coachedbypanel.res` | scura |
| [~] | `commentarymodelviewer.res` | chiara |
| [~] | `competitiveaccessinfo.res` | chiara |
| [~] | `competitivewelcomedialog.res` | chiara |
| [~] | `comprankpanel.res` | chiara |
| [~] | `comprankstooltip.res` | chiara |
| [~] | `compstats.res` | chiara |
| [~] | `confirmabandondialog.res` | chiara |
| [~] | `controlpointcountdown.res` | scura |
| [~] | `controlpointicon.res` | scura |
| [~] | `controlpointprogressbar.res` | scura |
| [~] | `craftingpanel.res` | scura |
| [~] | `craftingstatusdialog.res` | scura |
| [~] | `dashboardpartymember.res` | chiara |
| [x] | `disguisestatuspanel.res` | scura |
| [~] | `dynamicrecipepanel.res` | scura |
| [~] | `enemycountpanel.res` | scura |
| [~] | `explanationpopup.res` | chiara |
| [~] | `flagcalloutpanel.res` | scura |
| [x] | `flagstatus.res` | scura |
| [x] | `freezepanel_basic.res` | scura |
| [~] | `freezepanelcallout.res` | scura |
| [x] | `freezepanelkillerhealth.res` | scura |
| [~] | `giveawayitempanel.res` | scura |
| [~] | `globalchat.res` | scura |
| [~] | `globalexplanations.res` | chiara |
| [~] | `healthiconpanel.res` | scura |
| [x] | `hud_obj_dispenser.res` | scura |
| [x] | `hud_obj_sapper.res` | scura |
| [x] | `hud_obj_sentrygun.res` | scura |
| [x] | `hud_obj_sentrygun_disp.res` | scura |
| [x] | `hud_obj_tele.res` | scura |
| [x] | `hud_obj_tele_entrance.res` | scura |
| [x] | `hud_obj_tele_exit.res` | scura |
| [x] | `hudaccountpanel.res` | scura |
| [~] | `hudachievementfloatingnumber.res` | scura |
| [~] | `hudachievementtrackeritem.res` | scura |
| [x] | `hudalert.res` | scura |
| [x] | `hudammoweapons.res` | scura |
| [~] | `hudarenacappointcountdown.res` | scura |
| [~] | `hudarenaclasslayout.res` | scura |
| [~] | `hudarenanotification.res` | scura |
| [~] | `hudarenaplayercount.res` | scura |
| [~] | `hudarenateammenu.res` | chiara |
| [~] | `hudarenateammenu_sc.res` | chiara |
| [~] | `hudarenavspanel.res` | scura |
| [~] | `hudarenawinpanel.res` | scura |
| [~] | `hudbosshealth.res` | scura |
| [x] | `hudbowcharge.res` | scura |
| [~] | `hudcurrencyaccount.res` | scura |
| [x] | `huddamageaccount.res` | scura |
| [x] | `huddemomancharge.res` | scura |
| [x] | `huddemomanpipes.res` | scura |
| [x] | `hudhealthaccount.res` | scura |
| [~] | `hudinspectpanel.res` | scura |
| [~] | `huditemattributetracker.res` | scura |
| [x] | `huditemeffectmeter.res` | scura |
| [x] | `huditemeffectmeter_cleaver.res` | scura |
| [x] | `huditemeffectmeter_demoman.res` | scura |
| [x] | `huditemeffectmeter_engineer.res` | scura |
| [x] | `huditemeffectmeter_halloweensouls.res` | scura |
| [x] | `huditemeffectmeter_heavy.res` | scura |
| [x] | `huditemeffectmeter_kartcharge.res` | scura |
| [x] | `huditemeffectmeter_killstreak.res` | scura |
| [x] | `huditemeffectmeter_organs.res` | scura |
| [x] | `huditemeffectmeter_particlecannon.res` | scura |
| [x] | `huditemeffectmeter_pomson.res` | scura |
| [x] | `huditemeffectmeter_powerupbottle.res` | scura |
| [x] | `huditemeffectmeter_pyro.res` | scura |
| [x] | `huditemeffectmeter_raygun.res` | scura |
| [x] | `huditemeffectmeter_sapper.res` | scura |
| [x] | `huditemeffectmeter_scout.res` | scura |
| [x] | `huditemeffectmeter_sniper.res` | scura |
| [x] | `huditemeffectmeter_sniperfocus.res` | scura |
| [x] | `huditemeffectmeter_sodapopper.res` | scura |
| [x] | `huditemeffectmeter_spy.res` | scura |
| [x] | `huditemeffectmeter_spyknife.res` | scura |
| [~] | `hudkillstreaknotice.res` | scura |
| [~] | `hudmannvsmachinestatus.res` | scura |
| [x] | `hudmatchstatus.res` | scura |
| [~] | `hudmatchsummary.res` | scura |
| [x] | `hudmediccharge.res` | scura |
| [~] | `hudmenutauntselection.res` | scura |
| [~] | `hudmenutauntselection_sc.res` | scura |
| [~] | `hudminigame_base.res` | scura |
| [~] | `hudminigame_collection.res` | scura |
| [~] | `hudminigame_platform.res` | scura |
| [~] | `hudminigame_soccer.res` | scura |
| [~] | `hudminigame_soccersuddendeath.res` | scura |
| [x] | `hudobjectiveflagpanel.res` | scura |
| [x] | `hudobjectivekothtimepanel.res` | scura |
| [~] | `hudobjectiveplayerdestruction.res` | scura |
| [~] | `hudobjectiverobotdestruction.res` | scura |
| [~] | `hudobjectivestatus.res` | scura |
| [x] | `hudobjectivetimepanel.res` | scura |
| [~] | `hudpasstime.res` | scura |
| [~] | `hudpasstimeballstatus.res` | scura |
| [~] | `hudpasstimeoffscreenarrow.res` | scura |
| [~] | `hudpasstimepassnotify.res` | scura |
| [~] | `hudpasstimeteamscore.res` | scura |
| [x] | `hudplayerclass.res` | scura |
| [x] | `hudplayerhealth.res` | scura |
| [~] | `hudpowerupeffectmeter.res` | scura |
| [~] | `hudpvewinpanel.res` | scura |
| [~] | `hudrocketpack.res` | scura |
| [~] | `hudroundcounter.res` | scura |
| [~] | `hudspellselection.res` | scura |
| [~] | `hudstalemate.res` | scura |
| [~] | `hudstopwatch.res` | scura |
| [x] | `hudteamgoal.res` | scura |
| [~] | `hudteamgoaltournament.res` | scura |
| [~] | `hudteamswitch.res` | scura |
| [~] | `hudtournament.res` | scura |
| [~] | `hudtournamentsetup.res` | scura |
| [~] | `hudtraining.res` | scura |
| [~] | `hudtrainingmsg.res` | scura |
| [~] | `hudupgradepanel.res` | scura |
| [~] | `hudwarcount.res` | scura |
| [x] | `hudweaponselection.res` | scura |
| [~] | `importfiledialog.res` | chiara |
| [~] | `importfiletexteditdialog.res` | chiara |
| [~] | `importmaterialeditdialog.res` | chiara |
| [~] | `importpreviewitempanel.res` | chiara |
| [~] | `ingamequeuestatus.res` | scura |
| [~] | `intromenu.res` | chiara |
| [~] | `intromenu_sc.res` | chiara |
| [~] | `invitenotification.res` | chiara |
| [~] | `itemoptionspanel.res` | scura |
| [~] | `itemquickswitch.res` | scura |
| [~] | `itemrenameconfirmationdialog.res` | scura |
| [~] | `itemrenamedialog.res` | scura |
| [~] | `itemrenameinvaliddialog.res` | scura |
| [~] | `itemselectionpanel.res` | scura |
| [~] | `itemslotpanel.res` | scura |
| [~] | `layeredmappanel.res` | scura |
| [~] | `layeredmappanelitem.res` | scura |
| [~] | `layeredmappaneltooltip.res` | scura |
| [~] | `leaderboardentry.res` | chiara |
| [~] | `leaderboardentryrank.res` | chiara |
| [~] | `leaderboardentryscore.res` | chiara |
| [~] | `leaderboardspreadentry.res` | chiara |
| [~] | `loadoutpresetpanel.res` | scura |
| [~] | `lobbycontainerframe.res` | chiara |
| [~] | `lobbycontainerframe_casual.res` | chiara |
| [~] | `lobbycontainerframe_comp.res` | chiara |
| [~] | `lobbycontainerframe_mvm.res` | chiara |
| [~] | `lobbypanel.res` | chiara |
| [~] | `lobbypanel_casual.res` | chiara |
| [~] | `lobbypanel_comp.res` | chiara |
| [~] | `lobbypanel_mvm.res` | chiara |
| [~] | `mainmenu_saxxyawards.res` | chiara |
| [~] | `mainmenueventplaylistentry.res` | chiara |
| [x] | `mainmenuoverride.res` | chiara |
| [~] | `mainmenuplaylistentry.res` | chiara |
| [~] | `mapinfomenu.res` | chiara |
| [~] | `mapinfomenu_sc.res` | chiara |
| [~] | `matchhistoryentrypanel.res` | chiara |
| [~] | `matchmakingcasualcriteria.res` | chiara |
| [~] | `matchmakingcategorymappanel.res` | chiara |
| [~] | `matchmakingcategorypanel.res` | chiara |
| [x] | `matchmakingdashboard.res` | chiara |
| [~] | `matchmakingdashboardcasualcriteria.res` | chiara |
| [~] | `matchmakingdashboardcomp.res` | chiara |
| [~] | `matchmakingdashboardcompaccess.res` | chiara |
| [~] | `matchmakingdashboardeventmatch.res` | chiara |
| [~] | `matchmakingdashboardleftsidepanel.res` | chiara |
| [~] | `matchmakingdashboardmvmcriteria.res` | chiara |
| [~] | `matchmakingdashboardmvmmodeselect.res` | chiara |
| [~] | `matchmakingdashboardplaylist.res` | chiara |
| [~] | `matchmakingdashboardpopup.res` | chiara |
| [~] | `matchmakingdashboardpopup_mapvotepanel.res` | chiara |
| [~] | `matchmakingdashboardpopup_newmatch.res` | chiara |
| [~] | `matchmakingdashboardpopup_nextmapvoting.res` | chiara |
| [~] | `matchmakingdashboardpopup_nextmapwinner.res` | chiara |
| [~] | `matchmakingdashboardsidepanel.res` | chiara |
| [~] | `matchmakingdatacenterpopulationpanel.res` | chiara |
| [~] | `matchmakinggrouppanel.res` | chiara |
| [~] | `matchmakingpanel.res` | chiara |
| [~] | `matchmakingpingpanel.res` | chiara |
| [~] | `matchmakingplaylist.res` | chiara |
| [~] | `matchmakingtooltip.res` | chiara |
| [~] | `mediccallerpanel.res` | scura |
| [~] | `mmissuedialog.res` | chiara |
| [~] | `mvmbombcarrierprogresspanel.res` | scura |
| [~] | `mvmcreditspendpanel.res` | scura |
| [~] | `mvmcreditsubpanel.res` | scura |
| [~] | `mvmcriteria.res` | scura |
| [~] | `mvmeconrequirementdialog.res` | scura |
| [~] | `mvminworldcurrency.res` | scura |
| [~] | `mvmscoreboard.res` | chiara |
| [~] | `mvmscoreboardenemyinfo.res` | chiara |
| [~] | `mvmstatentry.res` | scura |
| [~] | `mvmvictorycontainer.res` | scura |
| [~] | `mvmvictorymannupentry.res` | scura |
| [~] | `mvmvictorymannuploot.res` | scura |
| [~] | `mvmvictorymannuppanel.res` | scura |
| [~] | `mvmvictorymannuptab.res` | scura |
| [~] | `mvmvictorypanel.res` | scura |
| [~] | `mvmvictorysplash.res` | scura |
| [~] | `mvmwavelosspanel.res` | scura |
| [~] | `navigationpaneltest.res` | chiara |
| [~] | `newrecipefounddialog.res` | scura |
| [x] | `objectivestatusescort.res` | scura |
| [~] | `objectivestatusmultipleescort.res` | scura |
| [~] | `playerticketstatus.res` | scura |
| [~] | `publishedfilebrowserdialog.res` | chiara |
| [~] | `publishfiledialog.res` | chiara |
| [~] | `pvpcasualrankpanel.res` | chiara |
| [~] | `pvpcomprankpanel.res` | chiara |
| [~] | `pvprankpanel.res` | chiara |
| [~] | `quickplaybusydialog.res` | chiara |
| [~] | `quickplaydialog.res` | chiara |
| [~] | `replayinputpanel.res` | chiara |
| [~] | `replaymessage.res` | chiara |
| [~] | `replaymessagedlg.res` | chiara |
| [~] | `replayrenderoverlay.res` | scura |
| [~] | `revivedialog.res` | scura |
| [~] | `robotdestructionstatus.res` | scura |
| [~] | `roundinfo.res` | scura |
| [~] | `saxxyawards_submitform.res` | chiara |
| [x] | `scoreboard.res` | chiara |
| [~] | `selectmosthelpfulfrienddialog.res` | chiara |
| [~] | `selectplayerdialog.res` | chiara |
| [~] | `selectplayerdialog_coach.res` | chiara |
| [~] | `selectplayerdialog_duel.res` | chiara |
| [~] | `servernotconnectedtosteam.res` | chiara |
| [x] | `spectator.res` | scura |
| [~] | `spectator_sc.res` | scura |
| [~] | `spectatorcoach.res` | scura |
| [x] | `spectatorguihealth.res` | scura |
| [~] | `spectatortournament.res` | scura |
| [~] | `spectatortournamentguihealth.res` | scura |
| [~] | `stampdonationadd.res` | scura |
| [~] | `staticbadgepanel.res` | chiara |
| [~] | `statitem.res` | chiara |
| [~] | `statpanel_base.res` | scura |
| [~] | `statsummary.res` | chiara |
| [~] | `statsummary_embedded.res` | chiara |
| [~] | `steamfriendpanel.res` | chiara |
| [~] | `steamworkshopdialog.res` | chiara |
| [~] | `steamworkshopitem.res` | scura |
| [~] | `streamlistpanel.res` | chiara |
| [~] | `streampanel.res` | chiara |
| [~] | `supportnotificationdialog.res` | chiara |
| [~] | `surveypanel_base.res` | chiara |
| [~] | `surveypanel_casualinquiry.res` | chiara |
| [~] | `surveypanel_compinquiry.res` | chiara |
| [~] | `surveypanel_mapquality.res` | chiara |
| [~] | `surveypanel_matchquality.res` | chiara |
| [~] | `surveypanel_randomcrit.res` | chiara |
| [~] | `tankprogressbar.res` | scura |
| [~] | `tankstatuspanel.res` | scura |
| [x] | `targetid.res` | scura |
| [~] | `tauntcallerpanel.res` | scura |
| [x] | `teammenu.res` | chiara |
| [~] | `teammenu_sc.res` | chiara |
| [~] | `testitembotcontrols.res` | scura |
| [~] | `testitemdialog.res` | scura |
| [~] | `testitemroot.res` | scura |
| [~] | `textwindow.res` | chiara |
| [~] | `textwindow_sc.res` | chiara |
| [~] | `textwindowcustomserver.res` | chiara |
| [~] | `textwindowcustomserver_sc.res` | chiara |
| [~] | `tfadvancedoptionsdialog.res` | chiara |
| [~] | `tfhudrobotdestruction_activestate.res` | scura |
| [~] | `tfhudrobotdestruction_deadstate.res` | scura |
| [~] | `tfhudrobotdestruction_robotindicator.res` | scura |
| [~] | `tfhudrobotdestruction_shieldedstate.res` | scura |
| [~] | `trainingcomplete.res` | chiara |
| [~] | `trainingdialog.res` | chiara |
| [~] | `trainingdialog_old.res` | chiara |
| [~] | `trainingitempanel.res` | chiara |
| [~] | `upgradeboxdialog.res` | scura |
| [~] | `upgradebuypanel.res` | scura |
| [~] | `videopanel.res` | chiara |
| [~] | `viewrecipespanel.res` | scura |
| [~] | `votehud.res` | scura |
| [~] | `vrcalibration.res` | chiara |
| [~] | `waitingforplayerspanel.res` | scura |
| [~] | `wavecompletesummarypanel.res` | scura |
| [~] | `wavestatuspanel.res` | scura |
| [x] | `winpanel.res` | scura |
| [~] | `xboxdialogs.res` | chiara |
| [~] | `xpsourcepanel.res` | chiara |
| [~] | `youtubelogindialog.res` | chiara |
| [~] | `youtubeuploaddialog.res` | chiara |
| [~] | `youtubeuploadwaitingdialog.res` | chiara |

</details>

<details><summary><code>resource/ui/build_menu/</code> — 32 file (migrato 32)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_active.res` | scura |
| [~] | `base_active_teleport_target.res` | scura |
| [~] | `base_already_built.res` | scura |
| [~] | `base_cant_afford.res` | scura |
| [~] | `base_selectable.res` | scura |
| [~] | `base_unavailable.res` | scura |
| [~] | `base_unavailable_teleport_target.res` | scura |
| [~] | `dispenser_active.res` | scura |
| [~] | `dispenser_already_built.res` | scura |
| [~] | `dispenser_cant_afford.res` | scura |
| [~] | `dispenser_selectable.res` | scura |
| [~] | `dispenser_unavailable.res` | scura |
| [~] | `eureka_target_home_avail.res` | scura |
| [~] | `eureka_target_home_unavail.res` | scura |
| [~] | `eureka_target_tele_exit_avail.res` | scura |
| [~] | `eureka_target_tele_exit_unavail.res` | scura |
| [~] | `hudmenuengybuild.res` | scura |
| [~] | `hudmenueurekaeffect.res` | scura |
| [~] | `sentry_active.res` | scura |
| [~] | `sentry_already_built.res` | scura |
| [~] | `sentry_cant_afford.res` | scura |
| [~] | `sentry_selectable.res` | scura |
| [~] | `sentry_unavailable.res` | scura |
| [~] | `tele_entrance_active.res` | scura |
| [~] | `tele_entrance_already_built.res` | scura |
| [~] | `tele_entrance_cant_afford.res` | scura |
| [~] | `tele_entrance_unavailable.res` | scura |
| [~] | `tele_exit_active.res` | scura |
| [~] | `tele_exit_already_built.res` | scura |
| [~] | `tele_exit_cant_afford.res` | scura |
| [~] | `tele_exit_unavailable.res` | scura |
| [~] | `tele_selectable.res` | scura |

</details>

<details><summary><code>resource/ui/build_menu/pipboy/</code> — 32 file (migrato 32)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_active.res` | scura |
| [~] | `base_active_teleport_target.res` | scura |
| [~] | `base_already_built.res` | scura |
| [~] | `base_cant_afford.res` | scura |
| [~] | `base_selectable.res` | scura |
| [~] | `base_unavailable.res` | scura |
| [~] | `base_unavailable_teleport_target.res` | scura |
| [~] | `dispenser_active.res` | scura |
| [~] | `dispenser_already_built.res` | scura |
| [~] | `dispenser_cant_afford.res` | scura |
| [~] | `dispenser_selectable.res` | scura |
| [~] | `dispenser_unavailable.res` | scura |
| [~] | `eureka_target_home_avail.res` | scura |
| [~] | `eureka_target_home_unavail.res` | scura |
| [~] | `eureka_target_tele_exit_avail.res` | scura |
| [~] | `eureka_target_tele_exit_unavail.res` | scura |
| [~] | `hudmenuengybuild.res` | scura |
| [~] | `hudmenueurekaeffect.res` | scura |
| [~] | `sentry_active.res` | scura |
| [~] | `sentry_already_built.res` | scura |
| [~] | `sentry_cant_afford.res` | scura |
| [~] | `sentry_selectable.res` | scura |
| [~] | `sentry_unavailable.res` | scura |
| [~] | `tele_entrance_active.res` | scura |
| [~] | `tele_entrance_already_built.res` | scura |
| [~] | `tele_entrance_cant_afford.res` | scura |
| [~] | `tele_entrance_unavailable.res` | scura |
| [~] | `tele_exit_active.res` | scura |
| [~] | `tele_exit_already_built.res` | scura |
| [~] | `tele_exit_cant_afford.res` | scura |
| [~] | `tele_exit_unavailable.res` | scura |
| [~] | `tele_selectable.res` | scura |

</details>

<details><summary><code>resource/ui/build_menu_360/</code> — 16 file (migrato 16)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_active.res` | scura |
| [~] | `base_already_built.res` | scura |
| [~] | `base_cant_afford.res` | scura |
| [~] | `dispenser_active.res` | scura |
| [~] | `dispenser_already_built.res` | scura |
| [~] | `dispenser_cant_afford.res` | scura |
| [~] | `hudmenuengybuild.res` | scura |
| [~] | `sentry_active.res` | scura |
| [~] | `sentry_already_built.res` | scura |
| [~] | `sentry_cant_afford.res` | scura |
| [~] | `tele_entrance_active.res` | scura |
| [~] | `tele_entrance_already_built.res` | scura |
| [~] | `tele_entrance_cant_afford.res` | scura |
| [~] | `tele_exit_active.res` | scura |
| [~] | `tele_exit_already_built.res` | scura |
| [~] | `tele_exit_cant_afford.res` | scura |

</details>

<details><summary><code>resource/ui/build_menu_sc/</code> — 23 file (migrato 23)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_active.res` | scura |
| [~] | `base_active_teleport_target.res` | scura |
| [~] | `base_already_built.res` | scura |
| [~] | `base_cant_afford.res` | scura |
| [~] | `base_unavailable_teleport_target.res` | scura |
| [~] | `dispenser_active.res` | scura |
| [~] | `dispenser_already_built.res` | scura |
| [~] | `dispenser_cant_afford.res` | scura |
| [~] | `eureka_target_home_avail.res` | scura |
| [~] | `eureka_target_home_unavail.res` | scura |
| [~] | `eureka_target_tele_exit_avail.res` | scura |
| [~] | `eureka_target_tele_exit_unavail.res` | scura |
| [~] | `hudmenuengybuild.res` | scura |
| [~] | `hudmenueurekaeffect.res` | scura |
| [~] | `sentry_active.res` | scura |
| [~] | `sentry_already_built.res` | scura |
| [~] | `sentry_cant_afford.res` | scura |
| [~] | `tele_entrance_active.res` | scura |
| [~] | `tele_entrance_already_built.res` | scura |
| [~] | `tele_entrance_cant_afford.res` | scura |
| [~] | `tele_exit_active.res` | scura |
| [~] | `tele_exit_already_built.res` | scura |
| [~] | `tele_exit_cant_afford.res` | scura |

</details>

<details><summary><code>resource/ui/destroy_menu/</code> — 11 file (migrato 11)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_active.res` | scura |
| [~] | `base_inactive.res` | scura |
| [~] | `dispenser_active.res` | scura |
| [~] | `dispenser_inactive.res` | scura |
| [~] | `hudmenuengydestroy.res` | scura |
| [~] | `sentry_active.res` | scura |
| [~] | `sentry_inactive.res` | scura |
| [~] | `tele_entrance_active.res` | scura |
| [~] | `tele_entrance_inactive.res` | scura |
| [~] | `tele_exit_active.res` | scura |
| [~] | `tele_exit_inactive.res` | scura |

</details>

<details><summary><code>resource/ui/destroy_menu/pipboy/</code> — 11 file (migrato 11)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_active.res` | scura |
| [~] | `base_inactive.res` | scura |
| [~] | `dispenser_active.res` | scura |
| [~] | `dispenser_inactive.res` | scura |
| [~] | `hudmenuengydestroy.res` | scura |
| [~] | `sentry_active.res` | scura |
| [~] | `sentry_inactive.res` | scura |
| [~] | `tele_entrance_active.res` | scura |
| [~] | `tele_entrance_inactive.res` | scura |
| [~] | `tele_exit_active.res` | scura |
| [~] | `tele_exit_inactive.res` | scura |

</details>

<details><summary><code>resource/ui/disguise_menu/</code> — 19 file (migrato 19)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `demoman_blue.res` | scura |
| [~] | `demoman_red.res` | scura |
| [~] | `engineer_blue.res` | scura |
| [~] | `engineer_red.res` | scura |
| [~] | `heavy_blue.res` | scura |
| [~] | `heavy_red.res` | scura |
| [~] | `hudmenuspydisguise.res` | scura |
| [~] | `medic_blue.res` | scura |
| [~] | `medic_red.res` | scura |
| [~] | `pyro_blue.res` | scura |
| [~] | `pyro_red.res` | scura |
| [~] | `scout_blue.res` | scura |
| [~] | `scout_red.res` | scura |
| [~] | `sniper_blue.res` | scura |
| [~] | `sniper_red.res` | scura |
| [~] | `soldier_blue.res` | scura |
| [~] | `soldier_red.res` | scura |
| [~] | `spy_blue.res` | scura |
| [~] | `spy_red.res` | scura |

</details>

<details><summary><code>resource/ui/disguise_menu_360/</code> — 20 file (migrato 20)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base.res` | scura |
| [~] | `demoman_blue.res` | scura |
| [~] | `demoman_red.res` | scura |
| [~] | `engineer_blue.res` | scura |
| [~] | `engineer_red.res` | scura |
| [~] | `heavy_blue.res` | scura |
| [~] | `heavy_red.res` | scura |
| [~] | `hudmenuspydisguise.res` | scura |
| [~] | `medic_blue.res` | scura |
| [~] | `medic_red.res` | scura |
| [~] | `pyro_blue.res` | scura |
| [~] | `pyro_red.res` | scura |
| [~] | `scout_blue.res` | scura |
| [~] | `scout_red.res` | scura |
| [~] | `sniper_blue.res` | scura |
| [~] | `sniper_red.res` | scura |
| [~] | `soldier_blue.res` | scura |
| [~] | `soldier_red.res` | scura |
| [~] | `spy_blue.res` | scura |
| [~] | `spy_red.res` | scura |

</details>

<details><summary><code>resource/ui/disguise_menu_sc/</code> — 20 file (migrato 20)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base.res` | scura |
| [~] | `demoman_blue.res` | scura |
| [~] | `demoman_red.res` | scura |
| [~] | `engineer_blue.res` | scura |
| [~] | `engineer_red.res` | scura |
| [~] | `heavy_blue.res` | scura |
| [~] | `heavy_red.res` | scura |
| [~] | `hudmenuspydisguise.res` | scura |
| [~] | `medic_blue.res` | scura |
| [~] | `medic_red.res` | scura |
| [~] | `pyro_blue.res` | scura |
| [~] | `pyro_red.res` | scura |
| [~] | `scout_blue.res` | scura |
| [~] | `scout_red.res` | scura |
| [~] | `sniper_blue.res` | scura |
| [~] | `sniper_red.res` | scura |
| [~] | `soldier_blue.res` | scura |
| [~] | `soldier_red.res` | scura |
| [~] | `spy_blue.res` | scura |
| [~] | `spy_red.res` | scura |

</details>

<details><summary><code>resource/ui/econ/</code> — 71 file (migrato 71)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `backpackpanel.res` | scura |
| [~] | `collectioncraftingdialog.res` | scura |
| [~] | `collectioncraftingdialog_base.res` | scura |
| [~] | `comboboxbackpackoverlaydialog.res` | scura |
| [~] | `confirmapplycardupgradeapplicationdialog.res` | scura |
| [~] | `confirmapplydecodedialog.res` | scura |
| [~] | `confirmapplyducktokendialog.res` | scura |
| [~] | `confirmapplygiftwrapdialog.res` | scura |
| [~] | `confirmapplypaintcandialog.res` | scura |
| [~] | `confirmapplypaintkitdialog.res` | scura |
| [~] | `confirmapplystrangepartapplicationdialog.res` | scura |
| [~] | `confirmapplystrangerestrictionapplicationdialog.res` | scura |
| [~] | `confirmapplystrangifierdialog.res` | scura |
| [~] | `confirmapplyteamcolorpaintcandialog.res` | scura |
| [~] | `confirmcustomizetexturedialog.res` | scura |
| [~] | `confirmdialog.res` | scura |
| [~] | `confirmdialog_sc.res` | scura |
| [~] | `confirmdialogabandonnopenalty.res` | scura |
| [~] | `confirmdialogabandonpenalty.res` | scura |
| [~] | `confirmdialogabandonsafe.res` | scura |
| [~] | `confirmdialogoptout.res` | scura |
| [~] | `confirmitempreviewdialog.res` | scura |
| [~] | `confirmspellbookpageapplicationdialog.res` | scura |
| [~] | `confirmtransmogrifyapplicationdialog.res` | scura |
| [~] | `cyclingadcontainer.res` | scura |
| [~] | `ducksleaderboardpanel.res` | scura |
| [~] | `ducksleaderboards.res` | scura |
| [~] | `genericnotificationtoast.res` | scura |
| [~] | `genericnotificationtoastmainmenu.res` | scura |
| [~] | `genericwaitingdialog.res` | scura |
| [~] | `halloweenofferingdialog.res` | scura |
| [~] | `inputstringforitembackpackoverlaydialog.res` | scura |
| [~] | `inspectionpanel.res` | scura |
| [~] | `inspectionpanel_cosmetic.res` | scura |
| [~] | `itemaddefault.res` | scura |
| [~] | `itemdiscardpanel.res` | scura |
| [~] | `itemmodelpanel.res` | scura |
| [~] | `itemmodelpanelcollectioncosmeticitem.res` | scura |
| [~] | `itemmodelpanelcollectionitem.res` | scura |
| [~] | `itempickuppanel.res` | scura |
| [~] | `leaderboardpanel.res` | scura |
| [~] | `lobbyleaderboard.res` | scura |
| [~] | `manncotrade_commonstatclock.res` | scura |
| [~] | `messageboxdialog.res` | scura |
| [~] | `messageboxdialog_sc.res` | scura |
| [~] | `notificationqueuepanel.res` | scura |
| [~] | `notificationspresentpanel.res` | scura |
| [~] | `notificationtoastcontainer.res` | scura |
| [~] | `notificationtoastcontrol.res` | scura |
| [~] | `paintkitconsumedialog.res` | scura |
| [~] | `questdefinitionviewpanel.res` | scura |
| [~] | `questdetailspanel.res` | scura |
| [~] | `questeditor.res` | scura |
| [~] | `questlogpanel.res` | scura |
| [~] | `questlogpanel_halloween.res` | scura |
| [~] | `questmapnodepanel.res` | scura |
| [~] | `questmapnodetooltippanel.res` | scura |
| [~] | `questmappanel.res` | scura |
| [~] | `questmaprewarditempanel.res` | scura |
| [~] | `questnotificationpanel_base.res` | scura |
| [~] | `questnotificationpanel_pauling_standard.res` | scura |
| [~] | `questviewsubpanel.res` | scura |
| [~] | `scrollablequestdetails.res` | scura |
| [~] | `scrollablequestlist.res` | scura |
| [~] | `scrollablequestlist_halloween.res` | scura |
| [~] | `scrollablequestlist_toughbreak.res` | scura |
| [~] | `strangecounttransferdialog.res` | scura |
| [~] | `tradingpanel.res` | scura |
| [~] | `tradingstartdialog.res` | scura |
| [~] | `warjoinpanel.res` | scura |
| [~] | `warstandingpanel.res` | scura |

</details>

<details><summary><code>resource/ui/econ/store/v1/</code> — 26 file (migrato 26)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `storehome.res` | scura |
| [~] | `storehome_freetrial.res` | scura |
| [~] | `storehome_winter1.res` | scura |
| [~] | `storehome_winter2.res` | scura |
| [~] | `storehome_winter3.res` | scura |
| [~] | `storeitemcontrols.res` | scura |
| [~] | `storepage.res` | scura |
| [~] | `storepage_bundles.res` | scura |
| [~] | `storepage_cgtrading.res` | scura |
| [~] | `storepage_drgrordbort.res` | scura |
| [~] | `storepage_halloween.res` | scura |
| [~] | `storepage_maps.res` | scura |
| [~] | `storepage_new.res` | scura |
| [~] | `storepage_popular.res` | scura |
| [~] | `storepage_previewable.res` | scura |
| [~] | `storepage_summer.res` | scura |
| [~] | `storepanel.res` | scura |
| [~] | `storepreviewitempanel.res` | scura |
| [~] | `storepreviewitempanel_maps.res` | scura |
| [~] | `storeprice.res` | scura |
| [~] | `storeprice_bundles.res` | scura |
| [~] | `storeprice_jumbo.res` | scura |
| [~] | `storeprice_new.res` | scura |
| [~] | `storeprice_popular.res` | scura |
| [~] | `storestatusdialog.res` | scura |
| [~] | `storeviewcartpanel.res` | scura |

</details>

<details><summary><code>resource/ui/econ/store/v2/</code> — 14 file (migrato 14)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `storehome_base.res` | scura |
| [~] | `storehome_freetrial.res` | scura |
| [~] | `storehome_premium.res` | scura |
| [~] | `storeitemcontrols.res` | scura |
| [~] | `storemapstampsinfodialog.res` | scura |
| [~] | `storepage.res` | scura |
| [~] | `storepage_bundles.res` | scura |
| [~] | `storepage_items.res` | scura |
| [~] | `storepage_maps.res` | scura |
| [~] | `storepanel.res` | scura |
| [~] | `storepreviewitempanel.res` | scura |
| [~] | `storepreviewitempanel_fullscreen.res` | scura |
| [~] | `storepreviewitempanel_maps.res` | scura |
| [~] | `storeviewcartpanel.res` | scura |

</details>

<details><summary><code>resource/ui/notifications/</code> — 42 file (migrato 42)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `base_notification.res` | scura |
| [~] | `notify_competitive_gc_down.res` | scura |
| [~] | `notify_enemy_flag_captured_blue.res` | scura |
| [~] | `notify_enemy_flag_captured_red.res` | scura |
| [~] | `notify_enemy_flag_dropped_blue.res` | scura |
| [~] | `notify_enemy_flag_dropped_red.res` | scura |
| [~] | `notify_enemy_flag_returned_blue.res` | scura |
| [~] | `notify_enemy_flag_returned_red.res` | scura |
| [~] | `notify_enemy_flag_taken_blue.res` | scura |
| [~] | `notify_enemy_flag_taken_red.res` | scura |
| [~] | `notify_golden_wrench.res` | scura |
| [~] | `notify_how_to_control_ghost.res` | scura |
| [~] | `notify_how_to_control_ghost_no_respawn.res` | scura |
| [~] | `notify_how_to_control_kart.res` | scura |
| [~] | `notify_no_invuln_with_flag_blue.res` | scura |
| [~] | `notify_no_invuln_with_flag_red.res` | scura |
| [~] | `notify_no_tele_with_flag_blue.res` | scura |
| [~] | `notify_no_tele_with_flag_red.res` | scura |
| [~] | `notify_passtime_howto.res` | scura |
| [~] | `notify_passtime_no_carry.res` | scura |
| [~] | `notify_passtime_no_cloak.res` | scura |
| [~] | `notify_passtime_no_disguise.res` | scura |
| [~] | `notify_passtime_no_holster.res` | scura |
| [~] | `notify_passtime_no_invuln.res` | scura |
| [~] | `notify_passtime_no_oob.res` | scura |
| [~] | `notify_passtime_no_taunt.res` | scura |
| [~] | `notify_passtime_no_tele.res` | scura |
| [~] | `notify_rd_robot_attacked_blue.res` | scura |
| [~] | `notify_rd_robot_attacked_red.res` | scura |
| [~] | `notify_special.res` | scura |
| [~] | `notify_touching_enemy_ctf_cap_blue.res` | scura |
| [~] | `notify_touching_enemy_ctf_cap_red.res` | scura |
| [~] | `notify_truce_end.res` | scura |
| [~] | `notify_truce_start.res` | scura |
| [~] | `notify_your_flag_captured_blue.res` | scura |
| [~] | `notify_your_flag_captured_red.res` | scura |
| [~] | `notify_your_flag_dropped_blue.res` | scura |
| [~] | `notify_your_flag_dropped_red.res` | scura |
| [~] | `notify_your_flag_returned_blue.res` | scura |
| [~] | `notify_your_flag_returned_red.res` | scura |
| [~] | `notify_your_flag_taken_blue.res` | scura |
| [~] | `notify_your_flag_taken_red.res` | scura |

</details>

<details><summary><code>resource/ui/quests/</code> — 11 file (migrato 11)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `lineitem_credits.res` | scura |
| [~] | `lineitem_item.res` | scura |
| [~] | `lineitem_objective.res` | scura |
| [~] | `lineitem_points.res` | scura |
| [~] | `questitempanel_base.res` | scura |
| [~] | `questitemtrackerpanel_base.res` | scura |
| [~] | `questitemtrackerpanel_ingame_base.res` | scura |
| [~] | `questitemtrackerpanel_questlog_base.res` | scura |
| [~] | `questobjectivepanel_ingame_base.res` | scura |
| [~] | `questobjectivepanel_questlog_base.res` | scura |
| [~] | `questobjectivescorer.res` | scura |

</details>

<details><summary><code>resource/ui/quests/cyoa/</code> — 3 file (migrato 3)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `questitemtrackerpanel_cyoa.res` | scura |
| [~] | `questmapregionlink.res` | scura |
| [~] | `questobjectivepanel_cyoa.res` | scura |

</details>

<details><summary><code>resource/ui/quests/cyoa/regions/</code> — 12 file (migrato 12)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `region_base.res` | scura |
| [~] | `region_campaign_3_home.res` | scura |
| [~] | `region_defense.res` | scura |
| [~] | `region_halloween.res` | scura |
| [~] | `region_halloween_bosses.res` | scura |
| [~] | `region_halloween_community_maps.res` | scura |
| [~] | `region_halloween_official_maps.res` | scura |
| [~] | `region_maps.res` | scura |
| [~] | `region_offense.res` | scura |
| [~] | `region_overworld.res` | scura |
| [~] | `region_pyroland.res` | scura |
| [~] | `region_support.res` | scura |

</details>

<details><summary><code>resource/ui/quests/merasmus/</code> — 9 file (migrato 9)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `questitempanel_merasmus_base.res` | scura |
| [~] | `questitempanel_merasmus_general.res` | scura |
| [~] | `questitempanel_merasmus_hhh.res` | scura |
| [~] | `questitempanel_merasmus_merasmus.res` | scura |
| [~] | `questitempanel_merasmus_monoculus.res` | scura |
| [~] | `questitemtrackerpanel_ingame.res` | scura |
| [~] | `questitemtrackerpanel_questlog.res` | scura |
| [~] | `questobjectivepanel_ingame.res` | scura |
| [~] | `questobjectivepanel_questlog.res` | scura |

</details>

<details><summary><code>resource/ui/quests/pauling/</code> — 20 file (migrato 20)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `questitempanel_pauling_base.res` | scura |
| [~] | `questitempanel_pauling_borneo.res` | scura |
| [~] | `questitempanel_pauling_demo.res` | scura |
| [~] | `questitempanel_pauling_engineer.res` | scura |
| [~] | `questitempanel_pauling_headhunter.res` | scura |
| [~] | `questitempanel_pauling_heavy.res` | scura |
| [~] | `questitempanel_pauling_medic.res` | scura |
| [~] | `questitempanel_pauling_playanyclass.res` | scura |
| [~] | `questitempanel_pauling_powerhouse.res` | scura |
| [~] | `questitempanel_pauling_pyro.res` | scura |
| [~] | `questitempanel_pauling_scout.res` | scura |
| [~] | `questitempanel_pauling_sniper.res` | scura |
| [~] | `questitempanel_pauling_snowplow.res` | scura |
| [~] | `questitempanel_pauling_soldier.res` | scura |
| [~] | `questitempanel_pauling_spy.res` | scura |
| [~] | `questitempanel_pauling_suijin.res` | scura |
| [~] | `questitemtrackerpanel_ingame.res` | scura |
| [~] | `questitemtrackerpanel_questlog.res` | scura |
| [~] | `questobjectivepanel_ingame.res` | scura |
| [~] | `questobjectivepanel_questlog.res` | scura |

</details>

<details><summary><code>resource/ui/quests/pauling/operation 2/</code> — 18 file (migrato 18)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `questitempanel_pauling_base.res` | scura |
| [~] | `questitempanel_pauling_community_map_1.res` | scura |
| [~] | `questitempanel_pauling_community_map_2.res` | scura |
| [~] | `questitempanel_pauling_community_map_3.res` | scura |
| [~] | `questitempanel_pauling_community_map_4.res` | scura |
| [~] | `questitempanel_pauling_cp.res` | scura |
| [~] | `questitempanel_pauling_demo.res` | scura |
| [~] | `questitempanel_pauling_engineer.res` | scura |
| [~] | `questitempanel_pauling_headhunter.res` | scura |
| [~] | `questitempanel_pauling_heavy.res` | scura |
| [~] | `questitempanel_pauling_medic.res` | scura |
| [~] | `questitempanel_pauling_payload.res` | scura |
| [~] | `questitempanel_pauling_playanyclass.res` | scura |
| [~] | `questitempanel_pauling_pyro.res` | scura |
| [~] | `questitempanel_pauling_scout.res` | scura |
| [~] | `questitempanel_pauling_sniper.res` | scura |
| [~] | `questitempanel_pauling_soldier.res` | scura |
| [~] | `questitempanel_pauling_spy.res` | scura |

</details>

<details><summary><code>resource/ui/replaybrowser/</code> — 11 file (migrato 11)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `confirmquitdlg.res` | chiara |
| [~] | `cutspanel.res` | chiara |
| [~] | `listthumbnail.res` | chiara |
| [~] | `mainpanel.res` | chiara |
| [~] | `playbackpanelslideshow.res` | chiara |
| [~] | `previewpanel.res` | chiara |
| [~] | `recordspanel.res` | chiara |
| [~] | `renderdialog.res` | chiara |
| [~] | `thumbnailcollection.res` | chiara |
| [~] | `thumbnailrow.res` | chiara |
| [~] | `titleeditpanel.res` | chiara |

</details>

<details><summary><code>resource/ui/replayperformanceeditor/</code> — 6 file (migrato 6)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `camsettings_free.res` | scura |
| [~] | `main.res` | scura |
| [~] | `reclight.res` | scura |
| [~] | `savedlg.res` | scura |
| [~] | `settings_timescale.res` | scura |
| [~] | `tip.res` | scura |

</details>

<details><summary><code>resource/ui/training/</code> — 1 file (migrato 1)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `main.res` | chiara |

</details>

<details><summary><code>resource/ui/training/basictraining/</code> — 3 file (migrato 3)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `classdetails.res` | chiara |
| [~] | `classpanel.res` | chiara |
| [~] | `classselection.res` | chiara |

</details>

<details><summary><code>resource/ui/training/modeselection/</code> — 2 file (migrato 2)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `modepanel.res` | chiara |
| [~] | `modeselection.res` | chiara |

</details>

<details><summary><code>resource/ui/training/offlinepractice/</code> — 2 file (migrato 2)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `mapselection.res` | chiara |
| [~] | `practicemodeselection.res` | chiara |

</details>

<details><summary><code>scripts/</code> — 1 file (riscritto 1)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [x] | `hudlayout.res` | scura |

</details>

<details><summary><code>scripts/screens/</code> — 8 file (migrato 8)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `obj_dispenser_blue.res` | scura |
| [~] | `obj_dispenser_red.res` | scura |
| [~] | `pda_spy.res` | scura |
| [~] | `pda_spy_invis.res` | scura |
| [~] | `pda_spy_invis_pocket.res` | scura |
| [~] | `pda_spy_invis_pocket_hm.res` | scura |
| [~] | `pda_spy_invis_pocket_ttg.res` | scura |
| [~] | `screen_pda.res` | scura |

</details>

<details><summary><code>servers/</code> — 1 file (migrato 1)</summary>

| Stato | File | Modalità |
|:-:|---|---|
| [~] | `quicklistpanel.res` | chiara |

</details>

**Cartelle di riferimento** (non caricate dal gioco: i loro percorsi non coincidono con nessun percorso del gioco): `#TF2 Files/` 754 .res, `#HL2 Files/` 208 .res, `#Platform Files/` 171 .res, `#Map Files/` 21 .res. Restano invariate come sorgente degli originali usata da `tools/migrate.py`.

<!-- COVERAGE:END -->

---

## 11. Variante v2: "taccuino vivace"

Approvata dal proprietario il 5 nov 2026 ("carta bianca", "più crazy, non solo lineare"). Non cambia
palette, font, ruoli né contrasti: aggiunge **cinque motivi** presi dai riferimenti, tutti generati da
`tools/hand/gen_v2.py` (elementi `ClaudeV2*`, rimossi e ricreati a ogni build).

| Motivo | Dove | Regola |
|---|---|---|
| **Ombra sfalsata** ("adesivo") | dietro ogni scheda di combattimento e ogni scheda dei menu | pannello pieno della stessa forma, spostato di 3 unità (4 nei menu) in basso a destra, z sotto la scheda. In partita: Moss (`DkShadow`). Nei menu: Ink, terracotta, salvia o acciaio, mai due uguali vicine. |
| **Schede che cambiano stato** | salute, munizioni, carica Medic | lo stato si legge dal colore della scheda intera, non da un'icona: salute sotto il 49% → scheda terracotta, numeri Ink, ombra che pulsa a 2 Hz; overheal → numero e ombra salvia; munizioni basse → terracotta; Über pronta → terracotta. Animazioni in `scripts/hudanimations_tf.txt` (`BgColor` sulle schede). |
| **Carta a quadretti** | menu principale, selezione classe e squadra, scoreboard | righe di 1 unità ogni 16, `LtGrid` (CloudLine al 59%), sotto tutto. Solo nelle pagine chiare: in partita mai (leggibilità). |
| **Bande del brand** | fondo dei menu chiari | quattro strisce sovrapposte, come la tavola del riferimento 4: menta (4), verde (2, solo a sinistra), terracotta (10), blush (4, solo a destra). |
| **Titolo eroe** | menu principale | "Team Fortress 2" in `TypeHero` (Source Serif 4, 46), evidenziatore blush sotto la metà inferiore delle lettere, occhiello in maiuscoletto terracotta, Segno verticale. Retino di punti `•` (Plex) nella scheda Personalizza. |

### Scheda Personalizza (menu principale)

Bottoni piatti (`CExButton`) con `"command" "engine …"`: il menu principale passa i comandi che non
conosce a GameUI, che li esegue in console (verificato nel sorgente, `tf_hud_mainmenuoverride.cpp`). Ogni
variabile è stata cercata nel sorgente del client ed è `FCVAR_ARCHIVE`, quindi resta salvata in
`config.cfg` come se la si cambiasse da console.

| Riga | Variabili |
|---|---|
| Mirino: stile, colore, taglia | `cl_crosshair_file crosshair1…7`, `crosshair 0/1`, `cl_crosshair_red/green/blue`, `cl_crosshair_scale 24/32/40/48` |
| Suono colpo, uccisione | `tf_dingalingaling 0/1`, `tf_dingalingaling_effect 0…8`, `tf_dingalingaling_lasthit 0/1` |
| Numeri di danno, cure, colore | `hud_combattext`, `hud_combattext_batching` (1 = unisce i numeri vicini), `hud_combattext_healing`, `hud_combattext_red/green/blue` |
| HUD | `tf_scoreboard_ping_as_text`, `hud_fastswitch`, `viewmodel_fov 54/70/80/90` (in competitivo il gioco lo limita a 54-70), `hud_reloadscheme` |

I campioni colore usano gli RGB dei colori campionati (Avorio, Terracotta, Salvia, Acciaio chiaro, Blush,
Verde). La scheda sta a z -45…-42: **sotto** i popup del menu (MOTD z 1, notifiche z 10, tooltip degli
oggetti z 100), sopra tela, quadretti e bande.

### Limiti dichiarati

- Il motore non permette di aprire e chiudere un pannello da un bottone del `.res` senza codice: la
  scheda Personalizza è sempre visibile (non ho trovato un comando del menu che lo faccia; `testhudanim`
  è `FCVAR_CHEAT`).
- Le ombre sono pannelli pieni, non sfocature: il motore non ha ombre morbide.

### Contrasto nel contesto

`tools/context_contrast.py` controlla ogni colore di testo di ogni file contro lo sfondo su cui viene
davvero disegnato (il proprio, quello dei genitori dipinti, quello di un fratello dipinto che lo contiene;
un controllo disegnato dal codice sotto il testo rende lo sfondo sconosciuto e il testo non viene
giudicato). Errore sotto 3:1. La stessa logica corregge gli elementi di Valve durante la migrazione: un
testo finito su una superficie dello stesso colore diventa il token di testo leggibile per quella
superficie (il "muted" resta muted se passa 4.5:1).
