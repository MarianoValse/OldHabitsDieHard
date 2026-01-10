import pandas as pd
from pathlib import Path


from src.models.habits import cHabits
from src.models.dificulty import cDificulty
from src.models.weigth import cWeigth



class ExcelLoader:
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def getdificultyList(self):
        df = pd.read_excel(self.data_dir / "dificultad.xlsx")
        
        dificultadList = []        
        for row in df.itertuples():
            dificultadList.append(cDificulty(row.DIF_ID, row.DIF_Nombre, row.DIF_Valor))
        
        return dificultadList
    

    def getDificulty(self,pid):        
        dificultyList= self.getdificultyList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for d in dificultyList:
            if d.id == pid:
                return d

        return None    
    
    def getWeigthList(self):
        df = pd.read_excel(self.data_dir / "peso.xlsx")

        wiegthList = []
        
        for row in df.itertuples():
            wiegthList.append(cWeigth(row.PESO_ID, row.PESO_Nombre, row.PESO_Valor))
        
        return wiegthList
    
    
    def getWiegth(self,pid):        
        wiegthList= self.getWeigthList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for w in wiegthList:
            if w.id == pid:
                return w

        return None

    def getHabitsList(self): 
        df = pd.read_excel(self.data_dir / "habitos.xlsx")
        habits = []

        for row in df.itertuples():
            habits.append(
                cHabits(
                    id=row.HAB_ID,                    
                    pDificultad=self.getDificulty(row.HAB_fk_dificultad),
                    pPeso=self.getWiegth(row.HAB_fk_peso),                    
                    pNombre=row.HAB_Nombre,
                    pActivo=row.HAB_Activo,
                )
            )

        return habits
