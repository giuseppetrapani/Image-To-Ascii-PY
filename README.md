# Image-to-ASCII Converter

Questo è un semplice script in Python che converte un'immagine in arte ASCII da visualizzare nel terminale.

<img src="image.png" alt="image" width="500" />


## Funzionalità
- **Conversione in ASCII**: Prende un'immagine in input e la converte in una rappresentazione ASCII.
- **Ridimensionamento automatico**: Ridimensiona l'immagine per adattarla al terminale, mantenendo il rapporto d'aspetto.
- **Miglioramento visivo**: Utilizza una mappatura dei caratteri ottimizzata e corregge le proporzioni per una migliore leggibilità.

## Requisiti
Per eseguire lo script, è necessario avere installato Python e la libreria `Pillow`.
Puoi installare `Pillow` con pip:
```bash
pip install Pillow
```

## Utilizzo
Per convertire un'immagine, esegui lo script dal terminale passando il percorso dell'immagine come argomento:
```bash
python main.py path/to/your/image.jpg
```
Sostituisci il path con il percorso del file immagine che vuoi convertire.

