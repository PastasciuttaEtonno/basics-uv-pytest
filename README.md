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
```

### B. Compilare (Locking)
Genera il file requirements.txt risolvendo tutte le versioni. Esegui questo comando ogni volta che modifichi requirements.in.

```bash
uv pip compile requirements.in -o requirements.txt
```

### C. Installare (Prima volta)
Se hai appena clonato il repository e hai già il requirements.txt.

```bash
uv pip install -r requirements.txt
```

### D. Sincronizzare (Allineamento)
Questo è il comando più importante. Allinea il tuo ambiente virtuale esattamente al requirements.txt. Rimuove pacchetti non necessari e installa quelli mancanti.

```bash
uv pip sync requirements.txt --allow-empty-requirements
```

# Pytest – Guida alle funzionalità di base

Pytest è un framework di testing per Python semplice da usare, molto potente e largamente adottato. Permette di scrivere test leggibili, modulari e facili da mantenere, senza richiedere classi o boilerplate complessi.

---

## Installazione

```bash
pip install pytest
```

Per eseguire i test:

```bash
pytest
```

Pytest rileva automaticamente i file di test seguendo alcune convenzioni.

---

## Convenzioni di naming

Pytest trova automaticamente i test se:

* I file si chiamano `test_*.py` oppure `*_test.py`
* Le funzioni di test iniziano con `test_`

Esempio:

```python
# test_math.py

def test_sum():
    assert 1 + 1 == 2
```

---

## Uso di `assert`

Pytest utilizza direttamente l’istruzione `assert` di Python.
Quando un test fallisce, pytest mostra automaticamente il confronto dettagliato tra valori attesi e ottenuti.

```python
def test_string():
    assert "ciao".upper() == "CIAO"
```

---

## Eseguire test specifici

Eseguire un file:

```bash
pytest test_math.py
```

Eseguire un singolo test:

```bash
pytest test_math.py::test_sum
```

---

## Fixture

Le fixture sono uno dei concetti più importanti di pytest. Servono a preparare dati o risorse riutilizzabili nei test.

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]


def test_len(sample_data):
    assert len(sample_data) == 3
```

La fixture viene "iniettata" automaticamente nel test tramite il nome del parametro.

### Scope delle fixture

È possibile controllare quante volte viene eseguita una fixture:

```python
@pytest.fixture(scope="function")  # default
@pytest.fixture(scope="module")
@pytest.fixture(scope="session")
```

---

## Parametrizzazione dei test

Permette di eseguire lo stesso test con input diversi.

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (10, 5, 15),
])
def test_sum(a, b, expected):
    assert a + b == expected
```

---

## Marker

I marker permettono di etichettare i test.

```python
import pytest

@pytest.mark.slow
def test_big_operation():
    ...
```

Eseguire solo i test con un marker:

```bash
pytest -m slow
```

---

## Gestione delle eccezioni

Per verificare che venga sollevata un’eccezione:

```python
import pytest


def divide(a, b):
    return a / b


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
```

---

## Setup e teardown (alternativa alle fixture)

Si possono usare funzioni speciali:

```python
def setup_function():
    print("Setup")


def teardown_function():
    print("Teardown")
```

Tuttavia, l’uso delle fixture è preferito.

---

## Output verboso

```bash
pytest -v
```

Mostra il dettaglio di ogni test eseguito.

---

## Struttura tipica di un progetto

```
project/
│
├── app/
│   └── math_utils.py
│
└── tests/
    └── test_math_utils.py
```

---

## Best practice

* Un test deve verificare un solo comportamento
* Usare le fixture per evitare duplicazioni
* Evitare dipendenze tra test
* Usare la parametrizzazione quando possibile
* Mantenere i test leggibili e semplici

---

## Conclusione

Pytest funziona seguendo convenzioni semplici, sfrutta l’`assert` nativo di Python e introduce strumenti potenti come fixture e parametrizzazione, rendendo il testing rapido da scrivere e facile da mantenere.
