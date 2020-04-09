def get_inputs(item_filtering_question, filtering_item_list):
    """
    obtains user specific input values for city name, month, day
    Args:
        (str) item_filtering_question - asks the user for the specified filtering item
        (lst) filtering_item_list - contains different options for the specified filtering item
    Returns:
        (str) user_input_filtering_item - specific user input
    """
    while True:
        user_input_filtering_item = input(item_filtering_question).lower()
        if user_input_filtering_item in filtering_item_list:
            break
        else:
            print('Invalid entry, please enter a valid input')
            continue
    return user_input_filtering_item
