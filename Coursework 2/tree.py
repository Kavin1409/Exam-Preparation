
from argparse import ArgumentParser
from math import sin, cos
from matplotlib import pyplot as plt

class tree_of_life(object):
    
    def __init__(self,generation=5,change_in_angle=0.1,length_rescale=0.6,length=1):
        self.generation=generation
        self.change_in_angle=change_in_angle
        self.length_rescale=length_rescale
        self.length=length
        self.initial_point=[[0,1,0]]
        
    def plots(self,x,y,new_point):
        """ Plot new branches.

    Parameters
    ----------
    x: int
        x-coordinate of the previous branch
    y: int
        y-coordinate of the previous branch
    new_point: list
        coordinates of new branch
    
    Returns
    -------
    plot
        plot of new branch      
    
    """       
        plt.plot([0,0],[0,1])
        plt.plot([x, new_point[-2][0]],[y, new_point[-2][1]]) 
        #plot from previous xy-coordinate to new xy-coordinate for the left hand side
        plt.plot([x, new_point[-1][0]],[y, new_point[-1][1]])
        #plot from previous xy-coordinate to new xy-coordinate for the right hand side
        plt.savefig('tree.png')

    def new_points(self,x,y,angle,length,change_in_angle,new_point): 
        """ Generate the new points of the new branches.

    Parameters
    ----------
    x: int
        x-coordinate of the previous branch
    y: int
        y-coordinate of the previous branch
    angle: float
        angle of the previous branch
    length: int
        The length of the branch. 
    new_point: list
        A empty list to be filled with the new points of the new branches
    
    Returns
    -------
    list
        New points of current branch       
    
    """                  
        new_point.append([x+length*sin(angle-change_in_angle), y+length*cos(angle-change_in_angle), 
        angle-change_in_angle])
        new_point.append([x+length*sin(angle+change_in_angle), y+length*cos(angle+change_in_angle), 
        angle+change_in_angle])

    def tree_branch(self,initial_point,length,change_in_angle,new_point,plot):
        """ Output the new points of the branches.

    Parameters
    ----------
    initial_point: list
        List containing the x,y and angle value of each point in the branch
    length: int
        The length of the branch.
    change_in_angle: float
        The increment or decrement of angle between branches. Default value=0.1.
    new_point: list
        A empty list to be filled with the new points of the new branches
    plot: bool
        Only plots if True. Default value=True.

    Returns
    -------
    list
        New points of current branch    
    plot(optional)
        The new branches
    
    """  
        for point in initial_point:
            x,y,angle=point
            self.new_points(x,y,angle,length,change_in_angle,new_point) 
            if plot:
                self.plots(x,y,new_point)

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
        initial_point=self.initial_point
        while (generation!=0):
            new_point=[]
            self.tree_branch(initial_point,length,change_in_angle,new_point,plot)
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
    
    initial=tree_of_life(arguments.generation,arguments.change_in_angle,arguments.length_rescale,arguments.length)
    initial.tree(False)
    
    if arguments.plot:
        initial.tree()