# Klassenraumchat (MVP)

Ein minimaler, webbasierter Chat für den Klassenraum.

## Features
- Echtzeit-Nachrichten
- Emoji-Reaktionen
- Teilnehmerliste
- Benutzerfreundliches UI

## Deployment

### Vorraussetzungen
- [Python 3.8+](https://www.python.org/downloads/)
- [Render-Konto](https://render.com/) (für Deployment)

### Lokale Ausführung
1. Repository klonen:
   ```bash
   git clone <repository-url>
   cd klassenraumchat
   ```
2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
3. Applikation starten:
   ```bash
   python app.py
   ```
4. Im Browser öffnen: [http://localhost:5000](http://localhost:5000)

### Deployment auf Render
1. Repository auf GitHub pushen.
2. Auf [Render](https://render.com/) einloggen.
3. Neues "Web Service" erstellen und mit dem GitHub-Repository verbinden.
4. Die `render.yaml`-Datei wird automatisch erkannt und die Applikation wird deployt.

## Dateistruktur
```
klassenraumchat/
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Limitierungen
- Nachrichten gehen bei Neustart oder Redeployment verloren.

## Lizenz
MIT