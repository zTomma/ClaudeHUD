# CLAUDE.md — ClaudeHUD

Rileggere questo file all'inizio di ogni sessione e prima di ogni fase.
Le quattro sezioni seguenti sono copiate fedelmente dal brief del proprietario del repo.

# PRINCIPIO GUIDA
Tradurre i principi di Claude, non le sue superfici:
- Calma, calore, chiarezza, ordine tipografico, generosità di spazio dove non c'è azione.
- In combattimento: elementi piccoli, compatti, ad alta leggibilità, scuri e caldi (non nero puro), che non coprono la vista centrale. L'accento arancio va solo su ciò che conta.
- Nei menu e nelle schermate di pausa (classe, team, scoreboard, opzioni, menu principale): variante chiara e più editoriale.
- Leggibilità in combattimento batte sempre l'estetica. Se confliggono, vince la leggibilità.

# REGOLE DI BRAND
1. Tipografia:
   - Serif per titoli e numeri grandi nei menu: Source Serif 4. Sans per UI e numeri di combattimento: IBM Plex Sans. Fallback se il serif non rende in gioco: Newsreader, mantenendo Plex Sans per i numeri.
   - Usa SOLO file .ttf statici (un file per peso) presi dalle release ufficiali dei progetti, mai variable font. Se non riesci a scaricarli, dimmi quali file mettere e dove.
   - Caricali con CustomFontFiles in ClientScheme.res e verifica che il nome famiglia usato in Fonts coincida con quello interno al file, non con il nome del file.
   - Salute, munizioni e timer devono usare cifre a larghezza fissa (tabulari), così i numeri non tremano quando cambiano. Mai font a cifre proporzionali per quegli elementi.
   - Verifica che i glifi accentati (àèìòù) e i simboli usati nella HUD siano coperti dal font.
   - Dichiara font, versioni e licenze in LICENSES.md e includi i testi di licenza OFL nel repo.
   - Se un font non si carica o è illeggibile in gioco, proponimi un sostituto OFL, mai un font di sistema.
2. Logo e marchi: non disegnare né riprodurre il logo di Claude o Anthropic. Se serve una texture di logo, lascia un segnaposto e dimmi dove metterla io. Come motivo grafico ricorrente usa una forma radiale/geometrica originale, definita in DESIGN.md.
3. Squadre: RED e BLU derivano dalla palette (terracotta per RED, ardesia per BLU) ma devono restare chiaramente distinguibili, anche per daltonismo rosso-verde. Verifica il contrasto con calcolo e riportami i rapporti.
4. Forme: angoli arrotondati dove il motore lo permette (`paintbackgroundtype "2"`). Dichiara i raggi usati e dove il motore li limita.
5. Contrasto: rapporto minimo per ogni coppia testo/sfondo, dichiarato in DESIGN.md e verificato con script.

# REGOLE DI LAVORO
1. Tutti i valori stilistici (colori, font, bordi) stanno in `ClientScheme.res` e vengono referenziati da lì. Niente valori hardcoded ripetuti nei singoli file.
2. Non inventare nomi di elementi, controlli o proprietà. Se non li trovi nel repo o non sei certo, dillo e chiedimelo.
3. Lavora a fasi e FERMATI alla fine di ognuna. Io testo in gioco e ti riporto screenshot ed errori della console. Non puoi vedere il rendering: non dire mai "sembra bello" o "funziona", dì cosa devo verificare.
4. Mantieni `PROGRESS.md` (fasi fatte, file toccati, problemi aperti, cosa testare) e aggiorna la checklist in DESIGN.md.
5. Valida la sintassi VDF prima di dichiarare pronta una fase (parentesi bilanciate, virgolette, chiavi duplicate). Scrivi uno script di linting.
6. Texture e icone (.vtf/.vmt): dimmi come le produci. Se non puoi generarle direttamente, scrivi lo script o dammi i PNG con istruzioni di conversione.
7. Prima di riscrivere un pannello rileggi DESIGN.md. Se una scelta lo contraddice, correggi la scelta, non il documento, salvo mia approvazione.
8. Non toccare nulla fuori dal repo della HUD.

# FORMATO
Rispondi in italiano, in modo breve. A fine fase: cosa hai fatto, cosa devo testare, cosa potrebbe essere rotto.
