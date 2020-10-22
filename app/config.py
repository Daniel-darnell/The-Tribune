class Config:

    '''
    General configuration parent class
    '''
    pass

class ProdConfig(Config):

    '''
    A production configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):

    '''
    A development configuration child class

    Args:
        Config: The parent configuration class with the General configuration settings
    '''
    pass


    DEBUG = True