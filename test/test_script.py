import sys
from pathlib import Path

# Añadir la carpeta raíz del proyecto al path
sys.path.append(str(Path(__file__).parent.parent))

# Ahora funciona aunque script.py esté en la raíz
from script import main, suma

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hola" in captured.out

def test_suma():
    assert suma(2, 3) == 5