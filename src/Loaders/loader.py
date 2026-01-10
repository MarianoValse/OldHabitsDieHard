# import pandas as pd
from pathlib import Path

from src.models.habits import cHabits
from src.models.dificulty import cDificulty
from src.models.weigth import cWeigth
from src.services.db import getConnection

class cDDBBLoader:
    
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir

    def getDificultyList(self):
                
        with getConnection() as conn:
            rows = conn.execute(
                "SELECT DIF_ID, DIF_name, DIF_value FROM Dificulty"
            ).fetchall()

        return [cDificulty(r[0], r[1], r[2]) for r in rows]

        # df = pd.read_excel(self.data_dir / "dificultad.xlsx")
        
        # dificultadList = []        
        # for row in df.itertuples():
        #     dificultadList.append(cDificulty(row.DIF_ID, row.DIF_Nombre, row.DIF_Valor))
        
        # return dificultadList
    

    def getDificulty(self,pid):        
        dificultyList= self.getDificultyList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for d in dificultyList:
            if d.id == pid:
                return d

        return None    
    
    def getWeigthList(self):

        with getConnection() as conn:
            rows = conn.execute(
                "SELECT WEI_ID, WEI_name, WEI_value  FROM Weigth"
            ).fetchall()

        return [cWeigth(r[0], r[1], r[2]) for r in rows]
        
        # df = pd.read_excel(self.data_dir / "peso.xlsx")

        # wiegthList = []
        
        # for row in df.itertuples():
        #     wiegthList.append(cWeigth(row.PESO_ID, row.PESO_Nombre, row.PESO_Valor))
        
        # return wiegthList
        
    def getWiegth(self,pid):        
        wiegthList= self.getWeigthList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for w in wiegthList:
            if w.id == pid:
                return w

        return None

    def getHabitsList(self): 
    
        with getConnection() as conn:
            rows = conn.execute(
                "SELECT HAB_ID,HAB_fk_dificulty,HAB_fk_weight,HAB_name,HAB_active FROM Habits"
            ).fetchall()

        return [cHabits(
                    r[0],
                    self.getDificulty(r[1]),
                    self.getWiegth(r[2]),
                    r[3],
                    r[4]
                ) for r in rows]
    
    # def getHabitsToday(self,date): 
            
    #     with getConnection() as conn:
    #         with getConnection() as conn:
    #             conn.execute(
    #             "select HAB_ID , HAB_name , ENTRY_fk_grade from Habits hab LEFT JOIN Entries entry on hab.HAB_ID = entry.ENTRY_fk_habits where hab.HAB_active  and entry.ENTRY_date = ? " ,            
    #             (date,)).fetchall()

    #     return [r[0],r[3],r[4] for r in rows]


        # df = pd.read_excel(self.data_dir / "habitos.xlsx")
        # habits = []

        # for row in df.itertuples():
        #     habits.append(
        #         cHabits(
        #             id=row.HAB_ID,                    
        #             pDificultad=self.getDificulty(row.HAB_fk_dificultad),
        #             pPeso=self.getWiegth(row.HAB_fk_peso),                    
        #             pNombre=row.HAB_Nombre,
        #             pActivo=row.HAB_Activo,
        #         )
        #     )

        # return habits

    def getHabit(self,pid):        
        habitsList= self.getHabitsList()
        # dificultad = Enumerable(dificultadList).where(lambda x: x.id = pid).tolist()
    
        for h in habitsList:
            if h.id == pid:
                return h

        return None
