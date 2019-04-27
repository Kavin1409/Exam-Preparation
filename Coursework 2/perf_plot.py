
from tree_np import tree_of_life_numpy
from tree import tree_of_life
from matplotlib import pyplot as plt
import timeit 
import numpy as np

initial=tree_of_life()
initial_numpy=tree_of_life_numpy()

def time_to_generate_tree(object_name,generations):
    """ Time taken to run the code.

Parameters
----------
object_name: str
    The name of the object which instantiated the class
generation: int
    Number of generations in the tree.

Returns
-------
list
    -generations in ascending order
    -time taken to run the code for ascending order of generations      

"""   
    count = 1
    time_taken=[]
    generation=[]
    while count < (generations+1):
        start_time = timeit.default_timer() #time before the code runs
        object_name.tree(count,0.1,0.6,1,False)  
        end_time = timeit.default_timer() #time after the code runs
        time_taken_to_run = end_time - start_time 
        
        
        time_taken.append(time_taken_to_run)
        generation.append(count)
        count+=1
    return generation,time_taken

def plot_time(object_name, generations, title=None, label=None):
    """ Plot performance of the code.

Parameters
----------
object_name: str
    The name of the object which instantiated the class
generation: int
    Number of generations in the tree. 

Returns
-------
plot
    The plot of the performance of the code       

""" 
    number_of_generations,time = time_to_generate_tree(object_name,generations)
    plt.plot(number_of_generations,time,'o-', label=label)
    plt.ylabel('seconds ($s$)')
    plt.xlabel('Number of generations')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig('perf_plot.png')

plot_time(initial,10,'Number of iterations agaist time', 'Without using numpy')
plot_time(initial_numpy,10,'Number of iterations agaist time', 'Using numpy')