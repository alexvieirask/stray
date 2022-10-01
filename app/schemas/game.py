from services.config import *
from schemas.screenshot import Screenshot 

''' Game Schema:

atributes:
    id: Integer
    title: Text
    description: Text
    categorie: Text
    price: Text
    required_age: Integer
    launch_date: Text
    developer: Text
    available: Boolean <Default value: true>
'''

class Game(db.Model):
    __tablename__ = 'Game'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    categorie = db.Column(db.Text, nullable = False)
    price = db.Column(db.Text, nullable = False)
    required_age = db.Column(db.Integer, nullable = False)
    launch_date = db.Column(db.Text, nullable = False)
    developer = db.Column(db.Text, nullable = False)
    available = db.Column(db.Boolean, default = True)
    screenshots = db.relationship(Screenshot, backref = 'Game')


    ''' this function return datas in JSON format '''
    def json(self) -> dict:
        return { 
            "id": self.id,
            "title": self.title,
            "description": self.description, 
            "categorie": self.categorie,  
            "price":self.price,
            "required_age": self.required_age,
            "launch_date" : self.launch_date,
            "developer" : self.developer
        }
    
    ''' this func '''
    def create_game(title:str, description:str, categorie:str,price:str,required_age:int, 
                    launch_date:str, developer:str, available:bool) -> tuple:
        try:
            GAME = Game (
                title = title, 
                description = description, 
                categorie = categorie, 
                price = price, 
                required_age = required_age,
                launch_date = launch_date,
                developer = developer, 
                available = available
            )
            db.session.add(GAME)
            db.session.commit()
            return 200, GAME.json()
        
        except Exception as error:
            return str(error)
    
    ''' this func '''
    def set_unavailable_game(id) -> tuple:
        try:
            GAME = Game.query.get(id)
            GAME.available = False
            db.session.commit()
            return 200, GAME.json()

        except Exception as error:
            return str(error)
            
    ''' this func '''
    def default_games_add(games:list) -> int:
        try:
            for game in games:
                db.session.add(game)
            db.session.commit()
            return 200
        
        except Exception as error:
            return str(error)

    ''' this func '''
    def return_game_by_id(id:int) -> tuple:
        try:
            GAME = Game.query.get(id)
            return 200, GAME.json()
        
        except Exception as error:
            return str(error)

    ''' this func '''
    def return_all_games() -> tuple:
        try:
            GAMES = Game.query.all()
            json_games =[ game.json() for game in GAMES]
            return 200, json_games

        except Exception as error:
            return str(error) 