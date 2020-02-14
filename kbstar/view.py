import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
from kbstar.service import Service
from kbstar.model import Model
rc('font', family =
   font_manager
   .FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf')
   .get_name())

class View:
    def __init__(self, fname):
        service = Service()
        self._model = service.new_model(fname)


