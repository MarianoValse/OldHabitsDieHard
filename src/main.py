from pathlib import Path

from Loaders.excel_loader import ExcelLoader
from services.habito_service import HabitoService
from services.semana_service import SemanaService

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

OUT_DIR = BASE_DIR / "output"

OUT_DIR.mkdir(exist_ok=True)

def main():
    loader = ExcelLoader(DATA_DIR)

    habitos = loader.cargar_habitos()

    habitos_activos = [h for h in habitos if h.activo]

    archivo = OUT_DIR / "semana_actual.xlsx"

    SemanaService.generar_excel_semana(habitos_activos, archivo)

    print("Excel semanal generado:", archivo)

if __name__ == "__main__":
    main()


# def main():
#     habitos = cargar_habitos()

#     activos = habitos[habitos["activo"] == True]

#     print("Hábitos activos:")
#     print(activos[["id", "nombre"]])

# if __name__ == "__main__":
#     main()