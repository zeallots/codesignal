def addBorder(picture):
    """  Given a rectangular matrix of characters, 
    add a border of asterisks(*) to it.
    """
    picture = ["*" + word + "*" for word in picture]
    picture = [("*" * len(picture[0]))] + picture + [("*" * len(picture[0]))]
    return picture

