class Computer:
    def __init__(self,ram,processor):
        self.ram=ram
        self.processor=processor
        print(f'my laptop has got {self.ram},{self.processor}')
        print('Class Computer is created.')
    def __del__(self,ram,processor):
    # def __del__(self):
        print('Computer is distroyed.')
object = Computer('16gb','i11')


del object

#Note: either self or all argument with del works in order to use destructor