def convert_farenheit_to_cel(val):
    """ Converts a number in farenheit to celsius.

    Args:
      val (float): The value in celsius that our functions will convert.
    
    Returns:
      float: The value converted to farneheit.
    
    """
    c = (val-32)* (5/9.0)
    return round(c,2)