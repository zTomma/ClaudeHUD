# LICENSES.md

## Font inclusi (`resource/fonts/`)

Tutti i file sono TTF **statici** (un file per peso), presi dalle release ufficiali dei progetti e
redistribuiti **senza modifiche**, come permette la SIL Open Font License 1.1. I nomi riservati
("Plex", "Source") restano quindi validi: un'eventuale versione modificata andrebbe rinominata.

| File | Famiglia interna | Versione | Fonte ufficiale | Licenza | Testo di licenza |
|---|---|---|---|---|---|
| `IBMPlexSans-Regular.ttf` | IBM Plex Sans | 3.005 | github.com/IBM/plex, release `@ibm/plex-sans@1.1.0`, asset `ibm-plex-sans.zip` → `fonts/complete/ttf/` | SIL OFL 1.1, Reserved Font Name "Plex" | [`licenses/OFL-IBM-Plex-Sans.txt`](licenses/OFL-IBM-Plex-Sans.txt) |
| `IBMPlexSans-Medium.ttf` | IBM Plex Sans Medm | 3.005 | come sopra | SIL OFL 1.1 | come sopra |
| `IBMPlexSans-SemiBold.ttf` | IBM Plex Sans SmBld | 3.005 | come sopra | SIL OFL 1.1 | come sopra |
| `SourceSerif4-Regular.ttf` | Source Serif 4 | 4.005 | github.com/adobe-fonts/source-serif, release `4.005R`, asset `source-serif-4.005_Desktop.zip` → `TTF/` | SIL OFL 1.1, Reserved Font Name "Source" | [`licenses/OFL-Source-Serif-4.md`](licenses/OFL-Source-Serif-4.md) |
| `SourceSerif4-Semibold.ttf` | Source Serif 4 Semibold | 4.005 | come sopra | SIL OFL 1.1 | come sopra |
| `SourceSerif4Display-Semibold.ttf` | Source Serif 4 Display Semibold | 4.005 | come sopra | SIL OFL 1.1 | come sopra |

SHA-256 dei file inclusi:

```
975dcda37d80f038dcd143c22e33ca2d97a0cc5a929aace1c749153b0fe1afa5  IBMPlexSans-Regular.ttf
331c8639d7598b2cde62a911a71db195e30cb655cd6bdf2e324a7e984955f907  IBMPlexSans-Medium.ttf
a20caf8286023a6a7a85e40b1d2a4ae9fc3e3b1f9eda8f4c542dd4986af67bb1  IBMPlexSans-SemiBold.ttf
e5a4ee6a3d87bb9024796be390c6771e2a0eb1883dae25effaf57ca01668e24b  SourceSerif4-Regular.ttf
36db62940cb5728b12b1802476dc7fcf4c6c519a7bdd476ba23a4e555fc4655f  SourceSerif4-Semibold.ttf
ba711c7443224e9c95bc5fcd24a98f3d921e50b3873c27667884351067927a03  SourceSerif4Display-Semibold.ttf
```

Font di riserva previsto dal brief se il serif non rende in gioco: **Newsreader** (SIL OFL 1.1).
Non è incluso: si aggiunge solo se Source Serif 4 risulta illeggibile nei test.

## File del gioco

Le cartelle `#TF2 Files`, `#HL2 Files`, `#Platform Files`, `#Map Files` e i file `.res` di partenza
sono estratti dai VPK di Team Fortress 2 (© Valve Corporation) e servono da riferimento. I file
`resource/tf.ttf` e `resource/tfd.ttf` citati in ClientScheme sono font di icone del gioco: non sono
inclusi in questo repository e li carica il gioco dai propri VPK.

## Marchi

ClaudeHUD è un progetto di fan non affiliato ad Anthropic né a Valve. Non contiene e non riproduce
il logo di Claude o di Anthropic: il motivo grafico (il "Segno", vedi DESIGN.md §2) è originale. Gli
screenshot di riferimento usati per campionare la palette non sono inclusi nel repository
(`reference/` è in `.gitignore`) perché contengono quei loghi.

## Strumenti (`tools/`)

Script scritti per questo progetto, sotto la stessa licenza del repository.
