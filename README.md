# data-science-viz

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Virtual enviroments

Usage of virtual enviroments to make sure that the project is compatible in every machine.

To create a new virtual enviroment `python -m venv <directory>` In this case it is important to use the naming convention for the directory as .venv or .env. (This folder will be ignore in the .gitignore file).

How to activate the virtual enviroment?

- Windows venv activation:

```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

- Linux and MacOS venv activation:

```
source myvenv/bin/activate
```

For all platforms it is needed just to call `deactivate` and you are out from this env.

Everytime a package is installed, for example: `pip install numpy`, the requirements.txt file should be updated. To catch up the updated version in a new virtual enviroment you can call `pip install -r requirements.txt` and that is, you project is ready to go.

## Software Requirements

- Python 3.12.2
- anaconda Command line client (version 1.12.3)
- pip 24.0

All the required packages will be listed on the `requirements.txt` file.

## Our Project:

Ideen:

- Auswertung der Daten des Deutchen Wetterdienstes (DWD)
- Vergleich zwischen Prognosen und tatsächlich eingetroffenem Wetter.
  ->statistische Wahrscheinlichkeit für Abweichung/ Fehler der Prognosen ->guter Einstieg
- Eigene Prognosen erstellen? -> sehr komplex
- Einfluss von Umweltkatastrophen (ggf. Nachrichten auf Naturkatastrophen absuchen?) auf politisches Meinungsbild(Politibarometer in deutschland) -> glaube ich machbar aber kein machine learning, nur statistik glaube ich

- Daten gibt es hier:
  - Politisches Meinungsbild: [article](https://search.gesis.org/research_data/ZA7970?doi=10.4232/1.14103)
  - Wetterdaten: [Daten](https://opendata.dwd.de/climate_environment/CDC/)

## References:

- [Virtual Env](https://python.land/virtual-environments/virtualenv)
- [Classes Slides](https://nc.uni-bremen.de/index.php/s/MWxosSLCQxKPapZ)
