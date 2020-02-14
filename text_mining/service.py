from text_mining.model import SamsungReport
class Service:
    def __init__(self):
        self.sam = SamsungReport()

    def execute(self, option):
        if option == '1':
            self.sam.read_file()
        elif option == '2':
            self.sam.download()
        elif option == '3':
            self.sam.read_stopword()
        elif option == '4':
            self.sam.hook()
        elif option == '5':
            self.sam.draw_wordcloud()

