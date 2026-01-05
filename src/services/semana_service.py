from datetime import date, timedelta
import pandas as pd


class SemanaService:

    @staticmethod
    def obtener_semana_actual():
        hoy = date.today()
        lunes = hoy - timedelta(days=hoy.weekday())
        return [lunes + timedelta(days=i) for i in range(7)]

    @staticmethod
    def generar_dataframe_semana(habitos):
        dias = ["L", "M", "X", "J", "V", "S", "D"]

        data = []
        for h in habitos:
            fila = {
                "id": h.id,
                "habito": h.nombre
            }
            for d in dias:
                fila[d] = ""
            data.append(fila)

        return pd.DataFrame(data)

    @staticmethod
    def generar_excel_semana(habitos, ruta_salida):
        df = SemanaService.generar_dataframe_semana(habitos)
        df.to_excel(ruta_salida, index=False)
