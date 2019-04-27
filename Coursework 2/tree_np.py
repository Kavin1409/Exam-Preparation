
from argparse import ArgumentParser
from math import sin, cos
from matplotlib import pyplot as plt
import numpy as np

class tree_of_life_numpy(object):
    
    def __init__(self,generation=5,change_in_angle=0.1,length_rescale=0.6,length=1):
        self.generation=generation
        self.change_in_angle=change_in_angle
        self.length_rescale=length_rescale
        self.length=length
        self.initial_point=np.array([[0],[1],[0]])
        
    def tree(self,generation=5,change_in_angle=0.1,length_rescale=0.6,length=1,plot=True):
        """ Generate the tree of life.

    Parameters
    ----------
    generation: int
        Number of generations in the tree. Default value=5.
    change_in_angle: float
        The increment or decrement of angle between branches. Default value=0.1.
    length_rescale: float
        The rescale of the length of subsequent branch. Default value=0.6.
    length: int
        The length of the branch. Default value=1.
    plot: bool
        Only plots if True. Default value=True.

    Returns
    -------
    plot(optional)
        The tree of life
    list
        List of new points of every branch       
    
    """           
        initial_point=np.array([[0],[1],[0]])
        while (generation!=0):
            x,y,angle=initial_point
            new_angle_left = np.subtract(angle,change_in_angle)
            new_x_left = x+length*np.sin(new_angle_left)
            new_y_left = y+length*np.cos(new_angle_left)
            
            new_angle_right = np.add(angle,change_in_angle)
            new_x_right = x+length*np.sin(new_angle_right)
            new_y_right = y+length*np.cos(new_angle_right)
            
            new_x_total = np.hstack([new_x_left,new_x_right])
            #concatenate the left and then the right side of the x-coordinates
            new_y_total = np.hstack([new_y_left,new_y_right])
            #concatenate the left and then the right side of the y-coordinates
            new_angle_total = np.hstack([new_angle_left,new_angle_right])
            #concatenate the angle on the right and the left

            #concatenating old xy-coordinates twice to be used in plotting
            old_x_point = np.hstack([x,x])
            old_y_point = np.hstack([y,y])
            
            new_point=np.array([new_x_total,new_y_total,new_angle_total])
              
            if plot:
                plt.plot([0,0],[0,1])
                plt.plot([old_x_point, new_x_total],[old_y_point, new_y_total])
                #plot from old xy-coordinate to new xy-coordinate
                plt.savefig('tree_np.png') 
            
            initial_point=new_point
            length*=length_rescale
            generation-=1
            
if __name__ == "__main__":
    parser = ArgumentParser(description="The tree of life")
    parser.add_argument('generation', nargs='?', const=5, type=int)
    parser.add_argument('change_in_angle', nargs='?', const=0.1, type=float)
    parser.add_argument('length_rescale', nargs='?', const=0.6, type=float)
    parser.add_argument('length', nargs='?', const=1, type=int)
    parser.add_argument('--plot', action = "store_true")
    arguments = parser.parse_args()
    
    initial=tree_of_life_numpy(arguments.generation,arguments.change_in_angle,arguments.length_rescale,arguments.length)
    initial.tree(False)
    
    if arguments.plot:
        initial.tree()

       