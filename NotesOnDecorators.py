'''
The target here is to use Decorator in a code I have done before 
to screen all possible use of Decorator and how it can improve the code
'''
import time


#------------------------------------------------------------------------------
# DECORATORS
#------------------------------------------------------------------------------

#------------Decorator Singleton------------
def dec_singletonsCLass(input_classe):
    '''
    Singeltons decorators: prendre toujours que la premiere instance 
    (exemple : instance de connexion a database, on ne veut pas plusieurs instances
    , mais tjrs la premiere si elle existe)
    '''    
    d_instances = {}
    def wrap_getInstances(*l_paramInput, **d_paramInput):
        if input_classe not in d_instances:
            # Add instances as value in the dictionary where the key is the class
            d_instances[input_classe] = input_classe(*l_paramInput, **d_paramInput)
        # If an instance already exist for ones class, just use this instance
        return d_instances[input_classe]
    return wrap_getInstances

#------------Performance in a function------------
def dec_getTimePerf(input_fct):
    '''
    Time Performance Decorators on a function
    You can calculate and compare Performance on any function just by decorating it
    '''    
    def wrap_modifiedFunction(*l_paramInput, **d_paramInput):
        # Before Function Execution...
        time_Debut = time.time()
        # Function execution 
        #   If you want to make stuff after execution of the function, you need to call function before returning it    
        launchFunction = input_fct(*l_paramInput, **d_paramInput)
        # After Function Execution...
        time_Fin = time.time()
        time_duree = time_Fin - time_Debut
        sec_duree = int(time_duree)
        milli_duree = (time_duree - sec_duree) * 1000
        print('Execution time for the function: {} = {} sec, {} milliSec'.format(input_fct, sec_duree, milli_duree))
        # Return the Function at the end
        return launchFunction
    return wrap_modifiedFunction

#------------Execute function if logged in------------
def dec_checkUserIsLogged(input_fct):
    '''
    This decorator check if a user is logged in 
    And apply the fonction only on that condition
    '''
    def wrap_modifiedFunction(*l_paramInput, **d_paramInput):
        if bl_userIsLoged:
            # Before Function Execution...
            launchFunction = input_fct(*l_paramInput, **d_paramInput)
            # After Function Execution...
            return launchFunction
        else:   
            print('ERROR: you need to be connected to access to the function: {}'.format(input_fct))
    return wrap_modifiedFunction



#------------------------------------------------------------------------------
# Using Decorators
#------------------------------------------------------------------------------

#Decore une classe
@dec_singletonsCLass
class c_ConnexionDatabase():
    def __init__(self, str_server):
        self._server = str_server
    
    # Decorators @property and @_get_server.setter used in place of the last row : "_server = property(get_server, set_server)"
    @property
    def _get_server(self):
        return self._server
    @_get_server.setter
    def _set_server(self, str_server):
        self._server = str_server
        
def TryDbConnexion():    
    db1 = c_ConnexionDatabase('Connex1')
    db2 = c_ConnexionDatabase('Connex2')
    # Why _Server is accessible while it should pass by _get_server to be served ?????????????????????
    #db1._server = 'abc'
    print('db1 = {} || db2 = {}'.format(db1._server, db2._server))
    
    
#Decore une fonction - Performance Function
@dec_getTimePerf
def fInt_SumFor(int_in):
    int_tot = 0
    for i in range(int_in):
        int_tot += i
    return (int_tot)

@dec_getTimePerf
def fInt_SumWhile(int_in):
    int_tot = 0
    i = 1
    while i < int_in:
        int_tot += i
        i += 1
    return (int_tot)

#Decore une fonction - Only Apply if Looged In
@dec_checkUserIsLogged
def AccessProfile():
    print('We access to the profile')


    
#------------------------------------------------------------------------------
# Appel
#------------------------------------------------------------------------------
    
#TryDbConnexion()

## For is twice faster than While
#fInt_SumFor(10000000)
#fInt_SumWhile(10000000)

bl_userIsLoged = False
AccessProfile()








