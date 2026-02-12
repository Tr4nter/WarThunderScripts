import tkinter
from tkinter import ttk
class UI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.mainFrame = ttk.Frame(self.root)
        self.mainFrame.grid()

        self._rowCount = 0
        self._values = {}

        self._labels = {}
        self._valueLabels = {}

    def make_label(self, valueName: str):
        valueRef = tkinter.StringVar()

        labelText = ttk.Label(self.mainFrame, text=f"{valueName} ")
        labelText.grid(column=0,row=self._rowCount, sticky=(tkinter.W))

        self._labels[valueName] = labelText
        
        labelValue = ttk.Label(self.mainFrame, textvariable=valueRef)
        labelValue.grid(column=1, row=self._rowCount, sticky=("n"))

        self._valueLabels[valueName] = labelValue

        self._rowCount += 1
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        return valueRef


    def get_label(self, valueName: str):
        if valueName in self._labels: return self._labels[valueName]


    def destroy_label(self, valueName):
        label = self.get_label(valueName)
        if not label: return

        label.destroy()

        del self._labels[valueName]
        del self._valueLabels[valueName]
        self._rowCount -= 1

        for valueName, label in self._labels.items():
            label.grid(column=0, row=self._rowCount)
            self._valueLabels[valueName].grid(column=1, row=self._rowCount)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)



    def run(self):
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.mainloop()




    
