from src.models.dificulty import cDificulty
from src.models.weigth import cWeigth

class cHabits:
    def __init__(
        self,
        id: int,        
        pDificulty: cDificulty,
        pWeigth: cWeigth,  
        pName: str,                     
        pActive: bool,                     
    ): 
        self.id = id                
        self.dificulty = pDificulty
        self.weigth = pWeigth
        self.name = pName
        self.active = pActive   
        
        
    


