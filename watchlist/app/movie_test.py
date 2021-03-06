import unittest
from models import movie
movie = movie.Movie

class MovieTest(unittest.TestCase):
    
    '''
    tests the behavior of the movie class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_movie = Movie( 1234, 'python must be crazy'  ,'A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
        
        def test_instance(self):
            self.assertTrue(isinstance(self.new_movie,Movie))
            
            if __name__ =='__main__':
                unittest.main()
        