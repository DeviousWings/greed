from game.casting.actor import Actor


class Artifact(Actor):
    def __int__(self):
        super().__init__()
    
    def calculate_points(self):
        """Calculates score"""
        points = 0
        
        if (self.get_text() == '*'):
            points = 1
            
        else: 
            points = -1
            
        return points
    
    # pie