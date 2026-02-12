from abc import ABC, abstractmethod

class BaseDataClass(ABC):
    @abstractmethod
    def submit_data(self, data):
        pass

    @property
    def data(self):
        pass

    
