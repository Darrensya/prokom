#print function
def print_models(unprinted, completed):
   
    while unprinted:
        current_design = unprinted.pop()
        print(f"Printing model: {current_design}")
        completed.append(current_design)


def show_completed_models(completed):
    print("\nModel ini telah diprint:")
    for completed in completed:
        print(completed)
        
#????/??//