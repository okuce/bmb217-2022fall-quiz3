class Box:
    """Cargo box desi and price calculator class"""



    def __init__(self,adepth:float,aheight:float,awidth:float,acontent:str) -> None:
        """Box constructor it assigns start values of a box. 
        Calls methods by order:

        calculate_desi()
        calculate_price()
        print()

        Args:
            adepth (float): depth of box
            aheight (float): height of box
            awidth (float): width of box
            acontent (str): content of box
        """


    def calculate_desi(self):
        """calculates desi of box with formula:
                desi = depth*height*width / 3000 
        """


    def calculate_price(self):
        """Calculate cargo price of box
            desi=0,   price = 0
            desi<10,  price = 20
            desi<20,  price = 30
            desi<30,  price = 40
            desi>=30, price = 50
        """ 


    def print(self):
        """Prints the content,desi and price of a box
        ex : 
        makarna,5,20TL
        """

