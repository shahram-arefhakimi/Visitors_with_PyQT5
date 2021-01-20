from  person_window_interface import *

save = False
class PersonWindow(QtWidgets.QDialog,Ui_FrmPerson):
    def __init__(self,parent=None):
        super(PersonWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.BtnExit.clicked.connect(self.closeform)
        self.BtnNew.clicked.connect(self.newrecord)
        self.BtnSave.clicked.connect(self.saverecord)
        self.BtnDelete.clicked.connect(self.deleterecord)

        self.txtName.setEnabled(False)
        self.txtFamily.setEnabled(False)
        self.txtWeight.setEnabled(False)
        



    def closeform(self):
        self.close()


    def newrecord(self):
        self.txtName.setText("")
        self.txtFamily.setText("")
        self.txtWeight.setText("")
        self.LblEncodeImage.clear()
        self.LblImage.clear()
        
        self.txtName.setEnabled(True)
        self.txtFamily.setEnabled(True)
        self.txtWeight.setEnabled(True)
     
        save=True

    def saverecord(self):
        
        self.txtName.setEnabled(False)
        self.txtFamily.setEnabled(False)
        self.txtWeight.setEnabled(False)
        
        save=False

    def deleterecord(self):
        self.txtName.setEnabled(False)
        self.txtFamily.setEnabled(False)
        self.txtWeight.setEnabled(False)

        save=False