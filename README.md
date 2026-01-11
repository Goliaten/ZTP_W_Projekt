# Uruchamianie
## Zależności
### Przy użyciu uv
```
uv venv &&
source .venv/bin/activate
uv sync
```

### Przy użyciu pip
```
python -m venv venv &&
source .venv/bin/activate &&
python -m pip install -r requirements.txt
```

## Próbki dźwiękowe
Próbki powinny znaleźć się w folderze `input` lub jeśli klucz `INPUT_PATH` w `config.py` został zmieniony, w tamtejszym folderze.

Struktura jest następująca:
`input/<nazwa_instrumentu>/<plik_dźwiękowy>`

## Uruchamianie skryptu
```python
python -m src.main
```
