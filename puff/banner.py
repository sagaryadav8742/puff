from clint.textui import puts, colored, indent

class Banner:
    def banner(self):
        with indent(4, quote='>>>'):
            puts(colored.red(str(self.bannerdata())))


    def bannerdata(self):
        data = r"""
__________ ____ _________________________
\______   \    |   \_   _____/\_   _____/
 |     ___/    |   /|    __)   |    __)  
 |    |   |    |  / |     \    |     \   
 |____|   |______/  \___  /    \___  /   
                        \/         \/      
        """
        return data
