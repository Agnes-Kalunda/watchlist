import configparser

from click import confirm


class Config:
    '''
    parent configuraton  class
    
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/550?api_key=35925db6a79b8cb1682d3f145ca93fc8'
    
    class ProdConfig(configparser):
        '''
        product configuration class
        
        Args:
        Config : the parent class with general configuration settings
        
        '''
        pass
    class DevConfig(confirm):
        '''
        Development configuration child class
        '''
        
        DEBUG = True