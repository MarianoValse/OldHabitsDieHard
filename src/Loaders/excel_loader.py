import pandas as pd
from pathlib import Path


from src.models.habito import cHabito
from src.models.dificultad import cDificultad
from src.models.peso import cPeso
# from models.medida import Medida


class ExcelLoader:
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def cargar_dificultadList(self):
        df = pd.read_excel(self.data_dir / "dificultad.xlsx")
        
        dificultadList = []        
        for row in df.itertuples():
            dificultadList.append(cDificultad(row.DIF_ID, row.DIF_Nombre, row.DIF_Valor))
        
        return dificultadList
    

    def getDificultad(self,pid):        
        dificultadList= self.cargar_dificultadList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for d in dificultadList:
            if d.id == pid:
                return d

        return None    
    
    def cargar_pesoList(self):
        df = pd.read_excel(self.data_dir / "peso.xlsx")

        pesoList = []
        
        for row in df.itertuples():
            pesoList.append(cPeso(row.PESO_ID, row.PESO_Nombre, row.PESO_Valor))
        
        return pesoList
    
    
    def getPeso(self,pid):        
        pesoList= self.cargar_pesoList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for p in pesoList:
            if p.id == pid:
                return p

        return None

    def cargar_habitos(self): 
        df = pd.read_excel(self.data_dir / "habitos.xlsx")
        habitos = []

        for row in df.itertuples():
            habitos.append(
                cHabito(
                    id=row.HAB_ID,                    
                    pDificultad=self.getDificultad(row.HAB_fk_dificultad),
                    pPeso=self.getPeso(row.HAB_fk_peso),                    
                    pNombre=row.HAB_Nombre,
                    pActivo=row.HAB_Activo,
                )
            )

        return habitos
