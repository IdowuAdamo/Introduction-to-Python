def favorite_sport(first_name, *sports): 
    """Displays the favorite game of the user"""
    print(f"My favorite sport is {sports}.")
    print(f"{first_name}'s favorite sport is/are: ") 
    
    for sport in sports:
        print(f" {sport}")