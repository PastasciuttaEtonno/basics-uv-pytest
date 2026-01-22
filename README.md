# Guida Operativa: Gestione Dipendenze (UV) e Testing (Pytest)

Esplorando **uv** (un package manager estremamente veloce) per gestire le dipendenze di Python e come eseguire dei test basici con **pytest**.

---

## 1. Gestione Dipendenze con UV

L'approccio moderno prevede di separare le dipendenze *astratte* (quelle che vuoi) da quelle *concrete* (quelle che installi, con versioni specifiche).

### Installazione di uv
```bash
# MacOS / Linux
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh

# Windows
powershell -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"

# Crea la cartella .venv
uv venv

# Attiva l'ambiente (MacOS/Linux)
source .venv/bin/activate

# Attiva l'ambiente (Windows)
.venv\Scripts\activate

# In alternativa si possono lanciare script e comandi senza attivare l' ambiente manualmente
uv run "comando" 

### A. Il file requirements.in
Crea un file chiamato `requirements.in`. Qui elenchi solo le librerie principali che usi, senza preoccuparti troppo delle versioni o delle sottodipendenze.

Esempio `requirements.in`:
```text
fastapi
uvicorn
pandas
pytest

### B. Compilare (Locking)
Genera il file requirements.txt risolvendo tutte le versioni. Esegui questo comando ogni volta che modifichi requirements.in.

Bash

uv pip compile requirements.in -o requirements.txt


### C. Installare (Prima volta)
Se hai appena clonato il repository e hai già il requirements.txt.

Bash

uv pip install -r requirements.txt

### D. Sincronizzare (Allineamento)
Questo è il comando più importante. Allinea il tuo ambiente virtuale esattamente al requirements.txt. Rimuove pacchetti non necessari e installa quelli mancanti.

Bash

uv pip sync requirements.txt --allow-empty-requirements