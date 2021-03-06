
from argparse import ArgumentParser
from .laboratory import Laboratory # Note python 3 relative import
import yaml

def process():   
    
    parser = ArgumentParser(description="Potion Master Trial")
    parser.add_argument('filename')
    parser.add_argument('--reactions', action = "store_true")
    arguments = parser.parse_args()

    shelves = yaml.load(open(arguments.filename))

    initial = Laboratory(shelves)
    final = initial.run_full_experiment()
    
    if arguments.reactions:
        final_shelves = initial.print_reaction_number()
    else:
        reaction_number = initial.total_reactions()
            
if __name__ == "__main__":
    process()