

class Converter:

    def __init__(self):
        pass

    def getBinaryData(self, filename):
        
        binary_data = []

        with open(filename, 'rb') as file:
            while (byte := file.read(1)):
                binary_data.append(ord(byte))
        
        return binary_data