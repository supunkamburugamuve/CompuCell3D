# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewSimulationWizard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewSimulationWizard(object):
    def setupUi(self, NewSimulationWizard):
        NewSimulationWizard.setObjectName("NewSimulationWizard")
        NewSimulationWizard.resize(615, 555)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wizardPage1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.nameLE = QtWidgets.QLineEdit(self.wizardPage1)
        self.nameLE.setObjectName("nameLE")
        self.gridLayout.addWidget(self.nameLE, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.wizardPage1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dirLE = QtWidgets.QLineEdit(self.wizardPage1)
        self.dirLE.setObjectName("dirLE")
        self.horizontalLayout_2.addWidget(self.dirLE)
        self.dirPB = QtWidgets.QPushButton(self.wizardPage1)
        self.dirPB.setObjectName("dirPB")
        self.horizontalLayout_2.addWidget(self.dirPB)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.wizardPage1)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.xmlRB = QtWidgets.QRadioButton(self.groupBox)
        self.xmlRB.setObjectName("xmlRB")
        self.verticalLayout.addWidget(self.xmlRB)
        self.pythonXMLRB = QtWidgets.QRadioButton(self.groupBox)
        self.pythonXMLRB.setChecked(True)
        self.pythonXMLRB.setObjectName("pythonXMLRB")
        self.verticalLayout.addWidget(self.pythonXMLRB)
        self.pythonOnlyRB = QtWidgets.QRadioButton(self.groupBox)
        self.pythonOnlyRB.setObjectName("pythonOnlyRB")
        self.verticalLayout.addWidget(self.pythonOnlyRB)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        NewSimulationWizard.addPage(self.wizardPage1)
        self.wizardPage_9 = QtWidgets.QWizardPage()
        self.wizardPage_9.setObjectName("wizardPage_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.wizardPage_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_27 = QtWidgets.QLabel(self.wizardPage_9)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 0, 0, 1, 1)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.groupBox_7 = QtWidgets.QGroupBox(self.wizardPage_9)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_24.addWidget(self.label_28)
        self.xDimSB = QtWidgets.QSpinBox(self.groupBox_7)
        self.xDimSB.setMinimum(1)
        self.xDimSB.setMaximum(10000000)
        self.xDimSB.setProperty("value", 100)
        self.xDimSB.setObjectName("xDimSB")
        self.horizontalLayout_24.addWidget(self.xDimSB)
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_24.addWidget(self.label_29)
        self.yDimSB = QtWidgets.QSpinBox(self.groupBox_7)
        self.yDimSB.setMinimum(1)
        self.yDimSB.setMaximum(10000000)
        self.yDimSB.setProperty("value", 100)
        self.yDimSB.setObjectName("yDimSB")
        self.horizontalLayout_24.addWidget(self.yDimSB)
        self.label_30 = QtWidgets.QLabel(self.groupBox_7)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_24.addWidget(self.label_30)
        self.zDimSB = QtWidgets.QSpinBox(self.groupBox_7)
        self.zDimSB.setMinimum(1)
        self.zDimSB.setMaximum(10000000)
        self.zDimSB.setObjectName("zDimSB")
        self.horizontalLayout_24.addWidget(self.zDimSB)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_24)
        self.verticalLayout_19.addWidget(self.groupBox_7)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_31 = QtWidgets.QLabel(self.wizardPage_9)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 1, 0, 1, 1)
        self.membraneFluctuationsLE = QtWidgets.QLineEdit(self.wizardPage_9)
        self.membraneFluctuationsLE.setObjectName("membraneFluctuationsLE")
        self.gridLayout_6.addWidget(self.membraneFluctuationsLE, 1, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.wizardPage_9)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 2, 0, 1, 1)
        self.neighborOrderSB = QtWidgets.QSpinBox(self.wizardPage_9)
        self.neighborOrderSB.setMinimum(1)
        self.neighborOrderSB.setMaximum(10)
        self.neighborOrderSB.setObjectName("neighborOrderSB")
        self.gridLayout_6.addWidget(self.neighborOrderSB, 2, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.wizardPage_9)
        self.label_33.setObjectName("label_33")
        self.gridLayout_6.addWidget(self.label_33, 3, 0, 1, 1)
        self.mcsSB = QtWidgets.QSpinBox(self.wizardPage_9)
        self.mcsSB.setMaximum(1000000000)
        self.mcsSB.setProperty("value", 1000)
        self.mcsSB.setObjectName("mcsSB")
        self.gridLayout_6.addWidget(self.mcsSB, 3, 1, 1, 1)
        self.latticeTypeCB = QtWidgets.QComboBox(self.wizardPage_9)
        self.latticeTypeCB.setObjectName("latticeTypeCB")
        self.latticeTypeCB.addItem("")
        self.latticeTypeCB.addItem("")
        self.gridLayout_6.addWidget(self.latticeTypeCB, 0, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.wizardPage_9)
        self.label_44.setObjectName("label_44")
        self.gridLayout_6.addWidget(self.label_44, 0, 0, 1, 1)
        self.verticalLayout_19.addLayout(self.gridLayout_6)
        self.line_3 = QtWidgets.QFrame(self.wizardPage_9)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_19.addWidget(self.line_3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.wizardPage_9)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uniformRB = QtWidgets.QRadioButton(self.groupBox_8)
        self.uniformRB.setChecked(True)
        self.uniformRB.setObjectName("uniformRB")
        self.gridLayout_5.addWidget(self.uniformRB, 0, 0, 1, 1)
        self.blobRB = QtWidgets.QRadioButton(self.groupBox_8)
        self.blobRB.setObjectName("blobRB")
        self.gridLayout_5.addWidget(self.blobRB, 0, 1, 1, 1)
        self.piffRB = QtWidgets.QRadioButton(self.groupBox_8)
        self.piffRB.setObjectName("piffRB")
        self.gridLayout_5.addWidget(self.piffRB, 0, 2, 1, 1)
        self.piffLE = QtWidgets.QLineEdit(self.groupBox_8)
        self.piffLE.setObjectName("piffLE")
        self.gridLayout_5.addWidget(self.piffLE, 1, 1, 1, 2)
        self.piffPB = QtWidgets.QPushButton(self.groupBox_8)
        self.piffPB.setObjectName("piffPB")
        self.gridLayout_5.addWidget(self.piffPB, 1, 0, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout_5)
        self.verticalLayout_19.addWidget(self.groupBox_8)
        self.gridLayout_7.addLayout(self.verticalLayout_19, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(238, 54, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 155, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 2, 0, 1, 1)
        NewSimulationWizard.addPage(self.wizardPage_9)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.wizardPage2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.wizardPage2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cellTypeTable = QtWidgets.QTableWidget(self.wizardPage2)
        self.cellTypeTable.setEnabled(True)
        self.cellTypeTable.setBaseSize(QtCore.QSize(256, 171))
        self.cellTypeTable.setObjectName("cellTypeTable")
        self.cellTypeTable.setColumnCount(2)
        self.cellTypeTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cellTypeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cellTypeTable.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_4.addWidget(self.cellTypeTable)
        self.clearCellTypeTablePB = QtWidgets.QPushButton(self.wizardPage2)
        self.clearCellTypeTablePB.setObjectName("clearCellTypeTablePB")
        self.horizontalLayout_4.addWidget(self.clearCellTypeTablePB)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.wizardPage2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cellTypeLE = QtWidgets.QLineEdit(self.wizardPage2)
        self.cellTypeLE.setObjectName("cellTypeLE")
        self.horizontalLayout_3.addWidget(self.cellTypeLE)
        self.freezeCHB = QtWidgets.QCheckBox(self.wizardPage2)
        self.freezeCHB.setObjectName("freezeCHB")
        self.horizontalLayout_3.addWidget(self.freezeCHB)
        self.cellTypeAddPB = QtWidgets.QPushButton(self.wizardPage2)
        self.cellTypeAddPB.setObjectName("cellTypeAddPB")
        self.horizontalLayout_3.addWidget(self.cellTypeAddPB)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        NewSimulationWizard.addPage(self.wizardPage2)
        self.wizardPage_7 = QtWidgets.QWizardPage()
        self.wizardPage_7.setObjectName("wizardPage_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.wizardPage_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_17 = QtWidgets.QLabel(self.wizardPage_7)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fieldTable = QtWidgets.QTableWidget(self.wizardPage_7)
        self.fieldTable.setMinimumSize(QtCore.QSize(300, 0))
        self.fieldTable.setBaseSize(QtCore.QSize(300, 0))
        self.fieldTable.setObjectName("fieldTable")
        self.fieldTable.setColumnCount(2)
        self.fieldTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fieldTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fieldTable.setHorizontalHeaderItem(1, item)
        self.horizontalLayout_5.addWidget(self.fieldTable)
        self.clearFieldTablePB = QtWidgets.QPushButton(self.wizardPage_7)
        self.clearFieldTablePB.setObjectName("clearFieldTablePB")
        self.horizontalLayout_5.addWidget(self.clearFieldTablePB)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.pdeSolverCallerCHB = QtWidgets.QCheckBox(self.wizardPage_7)
        self.pdeSolverCallerCHB.setObjectName("pdeSolverCallerCHB")
        self.verticalLayout_11.addWidget(self.pdeSolverCallerCHB)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_18 = QtWidgets.QLabel(self.wizardPage_7)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_15.addWidget(self.label_18)
        self.fieldNameLE = QtWidgets.QLineEdit(self.wizardPage_7)
        self.fieldNameLE.setMinimumSize(QtCore.QSize(120, 0))
        self.fieldNameLE.setObjectName("fieldNameLE")
        self.horizontalLayout_15.addWidget(self.fieldNameLE)
        self.label_19 = QtWidgets.QLabel(self.wizardPage_7)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_15.addWidget(self.label_19)
        self.solverCB = QtWidgets.QComboBox(self.wizardPage_7)
        self.solverCB.setObjectName("solverCB")
        self.solverCB.addItem("")
        self.solverCB.addItem("")
        self.solverCB.addItem("")
        self.solverCB.addItem("")
        self.solverCB.addItem("")
        self.horizontalLayout_15.addWidget(self.solverCB)
        self.fieldAddPB = QtWidgets.QPushButton(self.wizardPage_7)
        self.fieldAddPB.setObjectName("fieldAddPB")
        self.horizontalLayout_15.addWidget(self.fieldAddPB)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        NewSimulationWizard.addPage(self.wizardPage_7)
        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setObjectName("wizardPage")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.wizardPage)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_6 = QtWidgets.QLabel(self.wizardPage)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 2)
        self.groupBox_9 = QtWidgets.QGroupBox(self.wizardPage)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_34 = QtWidgets.QLabel(self.groupBox_9)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_6.addWidget(self.label_34)
        self.contactCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.contactCHB.setObjectName("contactCHB")
        self.verticalLayout_6.addWidget(self.contactCHB)
        self.internalContactCB = QtWidgets.QCheckBox(self.groupBox_9)
        self.internalContactCB.setObjectName("internalContactCB")
        self.verticalLayout_6.addWidget(self.internalContactCB)
        self.adhesionFlexCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.adhesionFlexCHB.setObjectName("adhesionFlexCHB")
        self.verticalLayout_6.addWidget(self.adhesionFlexCHB)
        self.contactLocalProductCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.contactLocalProductCHB.setObjectName("contactLocalProductCHB")
        self.verticalLayout_6.addWidget(self.contactLocalProductCHB)
        self.compartmentCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.compartmentCHB.setObjectName("compartmentCHB")
        self.verticalLayout_6.addWidget(self.compartmentCHB)
        self.fppCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.fppCHB.setObjectName("fppCHB")
        self.verticalLayout_6.addWidget(self.fppCHB)
        self.elasticityCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.elasticityCHB.setObjectName("elasticityCHB")
        self.verticalLayout_6.addWidget(self.elasticityCHB)
        self.contactMultiCadCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.contactMultiCadCHB.setCheckable(True)
        self.contactMultiCadCHB.setObjectName("contactMultiCadCHB")
        self.verticalLayout_6.addWidget(self.contactMultiCadCHB)
        self.label_35 = QtWidgets.QLabel(self.groupBox_9)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_6.addWidget(self.label_35)
        self.chemotaxisCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.chemotaxisCHB.setObjectName("chemotaxisCHB")
        self.verticalLayout_6.addWidget(self.chemotaxisCHB)
        self.label_36 = QtWidgets.QLabel(self.groupBox_9)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_6.addWidget(self.label_36)
        self.secretionCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.secretionCHB.setObjectName("secretionCHB")
        self.verticalLayout_6.addWidget(self.secretionCHB)
        self.label_37 = QtWidgets.QLabel(self.groupBox_9)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_6.addWidget(self.label_37)
        self.growthCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.growthCHB.setObjectName("growthCHB")
        self.verticalLayout_6.addWidget(self.growthCHB)
        self.label_38 = QtWidgets.QLabel(self.groupBox_9)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_6.addWidget(self.label_38)
        self.mitosisCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.mitosisCHB.setObjectName("mitosisCHB")
        self.verticalLayout_6.addWidget(self.mitosisCHB)
        self.label_39 = QtWidgets.QLabel(self.groupBox_9)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_6.addWidget(self.label_39)
        self.deathCHB = QtWidgets.QCheckBox(self.groupBox_9)
        self.deathCHB.setObjectName("deathCHB")
        self.verticalLayout_6.addWidget(self.deathCHB)
        self.gridLayout_8.addWidget(self.groupBox_9, 1, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.wizardPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_40 = QtWidgets.QLabel(self.groupBox_2)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_13.addWidget(self.label_40)
        self.volumeFlexCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.volumeFlexCHB.setObjectName("volumeFlexCHB")
        self.verticalLayout_13.addWidget(self.volumeFlexCHB)
        self.volumeLocalFlexCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.volumeLocalFlexCHB.setObjectName("volumeLocalFlexCHB")
        self.verticalLayout_13.addWidget(self.volumeLocalFlexCHB)
        self.label_41 = QtWidgets.QLabel(self.groupBox_2)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_13.addWidget(self.label_41)
        self.surfaceFlexCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.surfaceFlexCHB.setObjectName("surfaceFlexCHB")
        self.verticalLayout_13.addWidget(self.surfaceFlexCHB)
        self.surfaceLocalFlexCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.surfaceLocalFlexCHB.setObjectName("surfaceLocalFlexCHB")
        self.verticalLayout_13.addWidget(self.surfaceLocalFlexCHB)
        self.label_42 = QtWidgets.QLabel(self.groupBox_2)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_13.addWidget(self.label_42)
        self.extPotCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.extPotCHB.setObjectName("extPotCHB")
        self.verticalLayout_13.addWidget(self.extPotCHB)
        self.extPotLocalFlexCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.extPotLocalFlexCHB.setObjectName("extPotLocalFlexCHB")
        self.verticalLayout_13.addWidget(self.extPotLocalFlexCHB)
        self.label_43 = QtWidgets.QLabel(self.groupBox_2)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_13.addWidget(self.label_43)
        self.connectGlobalCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.connectGlobalCHB.setObjectName("connectGlobalCHB")
        self.verticalLayout_13.addWidget(self.connectGlobalCHB)
        self.connectGlobalByIdCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.connectGlobalByIdCHB.setObjectName("connectGlobalByIdCHB")
        self.verticalLayout_13.addWidget(self.connectGlobalByIdCHB)
        self.connect2DCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.connect2DCHB.setObjectName("connect2DCHB")
        self.verticalLayout_13.addWidget(self.connect2DCHB)
        self.label_45 = QtWidgets.QLabel(self.groupBox_2)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_13.addWidget(self.label_45)
        self.lengthConstraintCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.lengthConstraintCHB.setObjectName("lengthConstraintCHB")
        self.verticalLayout_13.addWidget(self.lengthConstraintCHB)
        self.lengthConstraintLocalFlexCHB = QtWidgets.QCheckBox(self.groupBox_2)
        self.lengthConstraintLocalFlexCHB.setObjectName("lengthConstraintLocalFlexCHB")
        self.verticalLayout_13.addWidget(self.lengthConstraintLocalFlexCHB)
        self.gridLayout_8.addWidget(self.groupBox_2, 1, 1, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.wizardPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comCHB = QtWidgets.QCheckBox(self.groupBox_4)
        self.comCHB.setChecked(True)
        self.comCHB.setObjectName("comCHB")
        self.verticalLayout_5.addWidget(self.comCHB)
        self.neighborCHB = QtWidgets.QCheckBox(self.groupBox_4)
        self.neighborCHB.setObjectName("neighborCHB")
        self.verticalLayout_5.addWidget(self.neighborCHB)
        self.momentOfInertiaCHB = QtWidgets.QCheckBox(self.groupBox_4)
        self.momentOfInertiaCHB.setObjectName("momentOfInertiaCHB")
        self.verticalLayout_5.addWidget(self.momentOfInertiaCHB)
        self.pixelTrackerCHB = QtWidgets.QCheckBox(self.groupBox_4)
        self.pixelTrackerCHB.setObjectName("pixelTrackerCHB")
        self.verticalLayout_5.addWidget(self.pixelTrackerCHB)
        self.boundaryPixelTrackerCHB = QtWidgets.QCheckBox(self.groupBox_4)
        self.boundaryPixelTrackerCHB.setObjectName("boundaryPixelTrackerCHB")
        self.verticalLayout_5.addWidget(self.boundaryPixelTrackerCHB)
        self.gridLayout_8.addWidget(self.groupBox_4, 1, 2, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.wizardPage)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.boxWatcherCHB = QtWidgets.QCheckBox(self.groupBox_10)
        self.boxWatcherCHB.setObjectName("boxWatcherCHB")
        self.verticalLayout_12.addWidget(self.boxWatcherCHB)
        self.pifDumperCHB = QtWidgets.QCheckBox(self.groupBox_10)
        self.pifDumperCHB.setObjectName("pifDumperCHB")
        self.verticalLayout_12.addWidget(self.pifDumperCHB)
        self.gridLayout_8.addWidget(self.groupBox_10, 2, 2, 1, 1)
        NewSimulationWizard.addPage(self.wizardPage)
        self.wizardPage_8 = QtWidgets.QWizardPage()
        self.wizardPage_8.setObjectName("wizardPage_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.wizardPage_8)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_24 = QtWidgets.QLabel(self.wizardPage_8)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_17.addWidget(self.label_24)
        self.secretionTable = QtWidgets.QTableWidget(self.wizardPage_8)
        self.secretionTable.setBaseSize(QtCore.QSize(580, 0))
        self.secretionTable.setObjectName("secretionTable")
        self.secretionTable.setColumnCount(5)
        self.secretionTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.secretionTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.secretionTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.secretionTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.secretionTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.secretionTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_17.addWidget(self.secretionTable)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.wizardPage_8)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.secrUniformRB = QtWidgets.QRadioButton(self.groupBox_6)
        self.secrUniformRB.setChecked(True)
        self.secrUniformRB.setObjectName("secrUniformRB")
        self.horizontalLayout_20.addWidget(self.secrUniformRB)
        self.secrOnContactRB = QtWidgets.QRadioButton(self.groupBox_6)
        self.secrOnContactRB.setObjectName("secrOnContactRB")
        self.horizontalLayout_20.addWidget(self.secrOnContactRB)
        self.secrConstConcRB = QtWidgets.QRadioButton(self.groupBox_6)
        self.secrConstConcRB.setObjectName("secrConstConcRB")
        self.horizontalLayout_20.addWidget(self.secrConstConcRB)
        self.verticalLayout_16.addLayout(self.horizontalLayout_20)
        self.gridLayout_4.addWidget(self.groupBox_6, 0, 0, 1, 2)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_25 = QtWidgets.QLabel(self.wizardPage_8)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_21.addWidget(self.label_25)
        self.secrFieldCB = QtWidgets.QComboBox(self.wizardPage_8)
        self.secrFieldCB.setObjectName("secrFieldCB")
        self.horizontalLayout_21.addWidget(self.secrFieldCB)
        self.label_26 = QtWidgets.QLabel(self.wizardPage_8)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_21.addWidget(self.label_26)
        self.secrCellTypeCB = QtWidgets.QComboBox(self.wizardPage_8)
        self.secrCellTypeCB.setObjectName("secrCellTypeCB")
        self.horizontalLayout_21.addWidget(self.secrCellTypeCB)
        self.secrRateLB = QtWidgets.QLabel(self.wizardPage_8)
        self.secrRateLB.setObjectName("secrRateLB")
        self.horizontalLayout_21.addWidget(self.secrRateLB)
        self.secrRateLE = QtWidgets.QLineEdit(self.wizardPage_8)
        self.secrRateLE.setObjectName("secrRateLE")
        self.horizontalLayout_21.addWidget(self.secrRateLE)
        self.gridLayout_4.addLayout(self.horizontalLayout_21, 1, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 1, 2, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.secrAddOnContactPB = QtWidgets.QPushButton(self.wizardPage_8)
        self.secrAddOnContactPB.setObjectName("secrAddOnContactPB")
        self.horizontalLayout_22.addWidget(self.secrAddOnContactPB)
        self.secrOnContactCellTypeCB = QtWidgets.QComboBox(self.wizardPage_8)
        self.secrOnContactCellTypeCB.setObjectName("secrOnContactCellTypeCB")
        self.horizontalLayout_22.addWidget(self.secrOnContactCellTypeCB)
        self.secrOnContactLE = QtWidgets.QLineEdit(self.wizardPage_8)
        self.secrOnContactLE.setObjectName("secrOnContactLE")
        self.horizontalLayout_22.addWidget(self.secrOnContactLE)
        self.gridLayout_4.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 2, 1, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_4)
        self.line_2 = QtWidgets.QFrame(self.wizardPage_8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_17.addWidget(self.line_2)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.secrAddRowPB = QtWidgets.QPushButton(self.wizardPage_8)
        self.secrAddRowPB.setObjectName("secrAddRowPB")
        self.horizontalLayout_23.addWidget(self.secrAddRowPB)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem9)
        self.secrRemoveRowsPB = QtWidgets.QPushButton(self.wizardPage_8)
        self.secrRemoveRowsPB.setObjectName("secrRemoveRowsPB")
        self.horizontalLayout_23.addWidget(self.secrRemoveRowsPB)
        self.secrClearTablePB = QtWidgets.QPushButton(self.wizardPage_8)
        self.secrClearTablePB.setObjectName("secrClearTablePB")
        self.horizontalLayout_23.addWidget(self.secrClearTablePB)
        self.verticalLayout_17.addLayout(self.horizontalLayout_23)
        NewSimulationWizard.addPage(self.wizardPage_8)
        self.wizardPage_6 = QtWidgets.QWizardPage()
        self.wizardPage_6.setObjectName("wizardPage_6")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.wizardPage_6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.wizardPage_6)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_15.addWidget(self.label_16)
        self.chamotaxisTable = QtWidgets.QTableWidget(self.wizardPage_6)
        self.chamotaxisTable.setObjectName("chamotaxisTable")
        self.chamotaxisTable.setColumnCount(6)
        self.chamotaxisTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.chamotaxisTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.chamotaxisTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.chamotaxisTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.chamotaxisTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.chamotaxisTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.chamotaxisTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_15.addWidget(self.chamotaxisTable)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.wizardPage_6)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.chemRegRB = QtWidgets.QRadioButton(self.groupBox_5)
        self.chemRegRB.setChecked(True)
        self.chemRegRB.setObjectName("chemRegRB")
        self.horizontalLayout_17.addWidget(self.chemRegRB)
        self.chemSatRB = QtWidgets.QRadioButton(self.groupBox_5)
        self.chemSatRB.setObjectName("chemSatRB")
        self.horizontalLayout_17.addWidget(self.chemSatRB)
        self.chemSatLinRB = QtWidgets.QRadioButton(self.groupBox_5)
        self.chemSatLinRB.setObjectName("chemSatLinRB")
        self.horizontalLayout_17.addWidget(self.chemSatLinRB)
        self.verticalLayout_14.addLayout(self.horizontalLayout_17)
        self.gridLayout_3.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_20 = QtWidgets.QLabel(self.wizardPage_6)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)
        self.chemFieldCB = QtWidgets.QComboBox(self.wizardPage_6)
        self.chemFieldCB.setObjectName("chemFieldCB")
        self.gridLayout_2.addWidget(self.chemFieldCB, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.wizardPage_6)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 2, 1, 1)
        self.chemCellTypeCB = QtWidgets.QComboBox(self.wizardPage_6)
        self.chemCellTypeCB.setObjectName("chemCellTypeCB")
        self.gridLayout_2.addWidget(self.chemCellTypeCB, 0, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.wizardPage_6)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 1, 0, 1, 1)
        self.lambdaChemLE = QtWidgets.QLineEdit(self.wizardPage_6)
        self.lambdaChemLE.setObjectName("lambdaChemLE")
        self.gridLayout_2.addWidget(self.lambdaChemLE, 1, 1, 1, 1)
        self.satCoefLB = QtWidgets.QLabel(self.wizardPage_6)
        self.satCoefLB.setObjectName("satCoefLB")
        self.gridLayout_2.addWidget(self.satCoefLB, 1, 2, 1, 1)
        self.satChemLE = QtWidgets.QLineEdit(self.wizardPage_6)
        self.satChemLE.setObjectName("satChemLE")
        self.gridLayout_2.addWidget(self.satChemLE, 1, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 1, 1, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.chemotaxTowardsPB = QtWidgets.QPushButton(self.wizardPage_6)
        self.chemotaxTowardsPB.setObjectName("chemotaxTowardsPB")
        self.horizontalLayout_18.addWidget(self.chemotaxTowardsPB)
        self.label_23 = QtWidgets.QLabel(self.wizardPage_6)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_18.addWidget(self.label_23)
        self.chemTowardsCellTypeCB = QtWidgets.QComboBox(self.wizardPage_6)
        self.chemTowardsCellTypeCB.setObjectName("chemTowardsCellTypeCB")
        self.horizontalLayout_18.addWidget(self.chemTowardsCellTypeCB)
        self.chemotaxTowardsLE = QtWidgets.QLineEdit(self.wizardPage_6)
        self.chemotaxTowardsLE.setObjectName("chemotaxTowardsLE")
        self.horizontalLayout_18.addWidget(self.chemotaxTowardsLE)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem11, 2, 1, 1, 1)
        self.verticalLayout_15.addLayout(self.gridLayout_3)
        self.line = QtWidgets.QFrame(self.wizardPage_6)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_15.addWidget(self.line)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.chemotaxisAddRowPB = QtWidgets.QPushButton(self.wizardPage_6)
        self.chemotaxisAddRowPB.setObjectName("chemotaxisAddRowPB")
        self.horizontalLayout_19.addWidget(self.chemotaxisAddRowPB)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem12)
        self.chemotaxisRemoveRowsPB = QtWidgets.QPushButton(self.wizardPage_6)
        self.chemotaxisRemoveRowsPB.setObjectName("chemotaxisRemoveRowsPB")
        self.horizontalLayout_19.addWidget(self.chemotaxisRemoveRowsPB)
        self.chemotaxisClearTablePB = QtWidgets.QPushButton(self.wizardPage_6)
        self.chemotaxisClearTablePB.setObjectName("chemotaxisClearTablePB")
        self.horizontalLayout_19.addWidget(self.chemotaxisClearTablePB)
        self.verticalLayout_15.addLayout(self.horizontalLayout_19)
        NewSimulationWizard.addPage(self.wizardPage_6)
        self.wizardPage_2 = QtWidgets.QWizardPage()
        self.wizardPage_2.setObjectName("wizardPage_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.wizardPage_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.wizardPage_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.afTable = QtWidgets.QTableWidget(self.wizardPage_2)
        self.afTable.setEnabled(True)
        self.afTable.setBaseSize(QtCore.QSize(256, 171))
        self.afTable.setObjectName("afTable")
        self.afTable.setColumnCount(1)
        self.afTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.afTable.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_8.addWidget(self.afTable)
        self.clearAFTablePB = QtWidgets.QPushButton(self.wizardPage_2)
        self.clearAFTablePB.setObjectName("clearAFTablePB")
        self.horizontalLayout_8.addWidget(self.clearAFTablePB)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.wizardPage_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.afMoleculeLE = QtWidgets.QLineEdit(self.wizardPage_2)
        self.afMoleculeLE.setText("")
        self.afMoleculeLE.setObjectName("afMoleculeLE")
        self.horizontalLayout_7.addWidget(self.afMoleculeLE)
        self.afMoleculeAddPB = QtWidgets.QPushButton(self.wizardPage_2)
        self.afMoleculeAddPB.setObjectName("afMoleculeAddPB")
        self.horizontalLayout_7.addWidget(self.afMoleculeAddPB)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.wizardPage_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.bindingFormulaLE = QtWidgets.QLineEdit(self.wizardPage_2)
        self.bindingFormulaLE.setObjectName("bindingFormulaLE")
        self.horizontalLayout_6.addWidget(self.bindingFormulaLE)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        NewSimulationWizard.addPage(self.wizardPage_2)
        self.wizardPage_4 = QtWidgets.QWizardPage()
        self.wizardPage_4.setObjectName("wizardPage_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.wizardPage_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.wizardPage_4)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.cmcTable = QtWidgets.QTableWidget(self.wizardPage_4)
        self.cmcTable.setEnabled(True)
        self.cmcTable.setBaseSize(QtCore.QSize(256, 171))
        self.cmcTable.setObjectName("cmcTable")
        self.cmcTable.setColumnCount(1)
        self.cmcTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cmcTable.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_10.addWidget(self.cmcTable)
        self.clearCMCTablePB = QtWidgets.QPushButton(self.wizardPage_4)
        self.clearCMCTablePB.setObjectName("clearCMCTablePB")
        self.horizontalLayout_10.addWidget(self.clearCMCTablePB)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.wizardPage_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.cmcMoleculeLE = QtWidgets.QLineEdit(self.wizardPage_4)
        self.cmcMoleculeLE.setText("")
        self.cmcMoleculeLE.setObjectName("cmcMoleculeLE")
        self.horizontalLayout_9.addWidget(self.cmcMoleculeLE)
        self.cmcMoleculeAddPB = QtWidgets.QPushButton(self.wizardPage_4)
        self.cmcMoleculeAddPB.setObjectName("cmcMoleculeAddPB")
        self.horizontalLayout_9.addWidget(self.cmcMoleculeAddPB)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        NewSimulationWizard.addPage(self.wizardPage_4)
        self.wizardPage_3 = QtWidgets.QWizardPage()
        self.wizardPage_3.setObjectName("wizardPage_3")
        self.label_7 = QtWidgets.QLabel(self.wizardPage_3)
        self.label_7.setGeometry(QtCore.QRect(9, 9, 228, 25))
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.wizardPage_3)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 391, 192))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName("textBrowser")
        NewSimulationWizard.addPage(self.wizardPage_3)

        self.retranslateUi(NewSimulationWizard)
        # self.piffRB.toggled['bool'].connect(self.piffPB.setShown)
        # self.piffRB.toggled['bool'].connect(self.piffLE.setShown)
        self.piffRB.toggled['bool'].connect(self.piffPB.setVisible)
        self.piffRB.toggled['bool'].connect(self.piffLE.setVisible)

        QtCore.QMetaObject.connectSlotsByName(NewSimulationWizard)

    def retranslateUi(self, NewSimulationWizard):
        _translate = QtCore.QCoreApplication.translate
        NewSimulationWizard.setWindowTitle(_translate("NewSimulationWizard", "Simulation Wizard"))
        self.label.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#0000ff;\">CompuCell3D Simulation Wizard</span></p></body></html>"))
        self.label_2.setText(_translate("NewSimulationWizard", "Simulation Name"))
        self.nameLE.setText(_translate("NewSimulationWizard", "NewSimulation"))
        self.label_3.setText(_translate("NewSimulationWizard", "Simulation Directory"))
        self.dirLE.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Directory where simulation files will be written to. E.g. if you pick <span style=\" font-weight:600;\">C:\\CC3DProject</span>s then simulation files will be written to directory <span style=\" font-weight:600;\">C:\\CC3DProjects\\&lt;SimulationName&gt;</span></p></body></html>"))
        self.dirPB.setText(_translate("NewSimulationWizard", "Browse..."))
        self.groupBox.setTitle(_translate("NewSimulationWizard", "Simulation Type"))
        self.xmlRB.setToolTip(_translate("NewSimulationWizard", "Only XML Script will be generated"))
        self.xmlRB.setText(_translate("NewSimulationWizard", "XML only"))
        self.pythonXMLRB.setToolTip(_translate("NewSimulationWizard", "The following files will be generated:\n"
"1. XMLScript\n"
"2. Python Main script\n"
"3. Python Steppable File\n"
""))
        self.pythonXMLRB.setText(_translate("NewSimulationWizard", "Python+XML"))
        self.pythonOnlyRB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The following files will be generated:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1. Python Main script (including configureSim function which replaces XML )</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2. Python Steppable File</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>"))
        self.pythonOnlyRB.setText(_translate("NewSimulationWizard", "Python only"))
        self.label_27.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">General Simulation Properties</span></p></body></html>"))
        self.groupBox_7.setTitle(_translate("NewSimulationWizard", "Lattice Dimensions"))
        self.label_28.setText(_translate("NewSimulationWizard", "x"))
        self.label_29.setText(_translate("NewSimulationWizard", "y"))
        self.label_30.setText(_translate("NewSimulationWizard", "z"))
        self.label_31.setText(_translate("NewSimulationWizard", "Average Membrane Fluctuations"))
        self.membraneFluctuationsLE.setToolTip(_translate("NewSimulationWizard", "Also known as so called temperature parameter in the acceptance probability expresion:  exp(-delta E/(k*T))"))
        self.membraneFluctuationsLE.setText(_translate("NewSimulationWizard", "10"))
        self.label_32.setText(_translate("NewSimulationWizard", "Pixel Copy Range (NeighborOrder)"))
        self.label_33.setText(_translate("NewSimulationWizard", "Number of MC Steps"))
        self.latticeTypeCB.setItemText(0, _translate("NewSimulationWizard", "Square"))
        self.latticeTypeCB.setItemText(1, _translate("NewSimulationWizard", "Hexagonal"))
        self.label_44.setText(_translate("NewSimulationWizard", "LatticeType"))
        self.groupBox_8.setTitle(_translate("NewSimulationWizard", "Initial Cell Layout"))
        self.uniformRB.setText(_translate("NewSimulationWizard", "Rectangular Slab"))
        self.blobRB.setText(_translate("NewSimulationWizard", "Blob"))
        self.piffRB.setText(_translate("NewSimulationWizard", "Custom Layout (PIFF file)"))
        self.piffPB.setText(_translate("NewSimulationWizard", "PIFF file..."))
        self.label_5.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">Cell Type Specification</span></p></body></html>"))
        item = self.cellTypeTable.horizontalHeaderItem(0)
        item.setText(_translate("NewSimulationWizard", "Cell Type"))
        item = self.cellTypeTable.horizontalHeaderItem(1)
        item.setText(_translate("NewSimulationWizard", "Freeze"))
        self.clearCellTypeTablePB.setText(_translate("NewSimulationWizard", "Clear Table"))
        self.label_4.setText(_translate("NewSimulationWizard", "Cell Type"))
        self.freezeCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Indicates whether cells of this type should remain frozen during simulation</span></p></body></html>"))
        self.freezeCHB.setText(_translate("NewSimulationWizard", "Freeze"))
        self.cellTypeAddPB.setText(_translate("NewSimulationWizard", "Add"))
        self.label_17.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">Chemical Fields (diffusants)</span></p></body></html>"))
        item = self.fieldTable.horizontalHeaderItem(0)
        item.setText(_translate("NewSimulationWizard", "Field Name"))
        item = self.fieldTable.horizontalHeaderItem(1)
        item.setText(_translate("NewSimulationWizard", "Solver"))
        self.clearFieldTablePB.setText(_translate("NewSimulationWizard", "Clear Table"))
        self.pdeSolverCallerCHB.setToolTip(_translate("NewSimulationWizard", "Inserts PDESolver plugin into generated code. "))
        self.pdeSolverCallerCHB.setText(_translate("NewSimulationWizard", "Enable multiple calls of PDE solvers"))
        self.label_18.setText(_translate("NewSimulationWizard", "Field Name"))
        self.label_19.setText(_translate("NewSimulationWizard", "Solver"))
        self.solverCB.setItemText(0, _translate("NewSimulationWizard", "DiffusionSolverFE"))
        self.solverCB.setItemText(1, _translate("NewSimulationWizard", "FlexibleDiffusionSolverFE"))
        self.solverCB.setItemText(2, _translate("NewSimulationWizard", "FastDiffusionSolver2DFE"))
        self.solverCB.setItemText(3, _translate("NewSimulationWizard", "KernelDiffusionSolver"))
        self.solverCB.setItemText(4, _translate("NewSimulationWizard", "SteadyStateDiffusionSolver"))
        self.fieldAddPB.setText(_translate("NewSimulationWizard", "Add"))
        self.label_6.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">Cell Properties and Behaviors</span></p></body></html>"))
        self.groupBox_9.setTitle(_translate("NewSimulationWizard", "Cellular Behaviors"))
        self.label_34.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Adhesion</span></p></body></html>"))
        self.contactCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Most commonly used energy term for contact (adhesive) cell-cell/cell-Medium interactions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Note (when using compartmental cells): it calculates energy between members (compartments) belonging to different clusters (compartmental cells).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>"))
        self.contactCHB.setText(_translate("NewSimulationWizard", "Contact"))
        self.internalContactCB.setToolTip(_translate("NewSimulationWizard", "Adhesion energy term - calculated betwee members (compartments) of the same cluster (compartmental cell)\n"
"You may use it together with Contact energy term"))
        self.internalContactCB.setText(_translate("NewSimulationWizard", "ContactInternal"))
        self.adhesionFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Calculates adhesion energy based on concentration of adhesion moolecules on the cell membrane. Works fine for complartmental and non compartmental cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Users can specifymultiple adhesion molecules and customize interactions between them. Adhesion molecules concentrations can be modified/accessed using Python scripting</span></p></body></html>"))
        self.adhesionFlexCHB.setText(_translate("NewSimulationWizard", "AdhesionFlex"))
        self.contactLocalProductCHB.setToolTip(_translate("NewSimulationWizard", "Older version of AdhesionFlex. Please consider switching to AdhesionFlex plugin"))
        self.contactLocalProductCHB.setText(_translate("NewSimulationWizard", "ContactLocalProduct"))
        self.compartmentCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Combined Contact and ContactInternal plugin.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Allows users to specify adhesions between members of same and different clusters at the same time.</span></p></body></html>"))
        self.compartmentCHB.setText(_translate("NewSimulationWizard", "Compartments"))
        self.fppCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Emulates focal junctions by dynamically linking (via elastic constraint) center of masses of neighboring cells. Elastic constraint is based on the distance between linked cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Links\' parameters can be accessed and modified through Python.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Links can be brokeneither due to exceeding max distance between cells or manually.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Links are established when two cells come in contact and max number of links for the two cells is smaller than the number of links they have already formed.</span></p></body></html>"))
        self.fppCHB.setText(_translate("NewSimulationWizard", "FocalPointPlasticity"))
        self.elasticityCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Applies elastic constraint between cell\'s center of masses of participating cells. Elastic constraint is based on the distance between linked cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Elastic links are initially formed between those cells which touch each other when first pixel copy is about to happen. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Links can be later modified, added/removed using Python scripting. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The list of links is static i.e. once two cells are linked they will remain linked until one of them disappears or the linkis broken manually by Python script.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p></body></html>"))
        self.elasticityCHB.setText(_translate("NewSimulationWizard", "Elasticity"))
        self.contactMultiCadCHB.setToolTip(_translate("NewSimulationWizard", "Deprecetad plauing. Please use AdhesionFlex"))
        self.contactMultiCadCHB.setText(_translate("NewSimulationWizard", "ContactMultiCad (deprecated)"))
        self.label_35.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Chemotaxis</span></p></body></html>"))
        self.chemotaxisCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Implements energy term which emulates Chemotaxis. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Note, you need to define chemical fields for this plugin to work.</span></p></body></html>"))
        self.chemotaxisCHB.setText(_translate("NewSimulationWizard", "Chemotaxis"))
        self.label_36.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Secretion</span></p></body></html>"))
        self.secretionCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A module which implements secretion. You need to make sure you have defined chemical fields to which you are trying to secrete. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Secretion can be deinied for particular cell types using XML/Python configureSim  or on a cell-by-cell basis using Python </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Notice it implicitely calls PixelTracker and BoundaryPixelTracker plugins</span></p></body></html>"))
        self.secretionCHB.setText(_translate("NewSimulationWizard", "Secretion"))
        self.label_37.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Growth</span></p></body></html>"))
        self.growthCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Example of a Python steppable which implements cell growth.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> Users can modify the code to refine cell growth behavior. </span></p></body></html>"))
        self.growthCHB.setText(_translate("NewSimulationWizard", "Growth (Python)"))
        self.label_38.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Mitosis</span></p></body></html>"))
        self.mitosisCHB.setToolTip(_translate("NewSimulationWizard", "Python Steppable implementing cell division. "))
        self.mitosisCHB.setText(_translate("NewSimulationWizard", "Mitosis (Python)"))
        self.label_39.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Death</span></p></body></html>"))
        self.deathCHB.setToolTip(_translate("NewSimulationWizard", "Python Steppable implementing cell death"))
        self.deathCHB.setText(_translate("NewSimulationWizard", "Death (Python)"))
        self.groupBox_2.setTitle(_translate("NewSimulationWizard", "Constraints and Forces"))
        self.label_40.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Volume</span></p></body></html>"))
        self.volumeFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Volume constraint energy term. E=Lambda*(v-V</span><span style=\" font-size:8pt; vertical-align:sub;\">T</span><span style=\" font-size:8pt;\">)</span><span style=\" font-size:8pt; vertical-align:super;\">2 </span><span style=\" font-size:8pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Lambda and V</span><span style=\" font-size:8pt; vertical-align:sub;\">T </span><span style=\" font-size:8pt;\">are</span><span style=\" font-size:8pt; vertical-align:super;\"> </span><span style=\" font-size:8pt;\">specified for each cell type separately</span></p></body></html>"))
        self.volumeFlexCHB.setText(_translate("NewSimulationWizard", "VolumeFlex"))
        self.volumeLocalFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Volume constraint energy term. E=Lambda*(v-V</span><span style=\" font-size:8pt; vertical-align:sub;\">T</span><span style=\" font-size:8pt;\">)</span><span style=\" font-size:8pt; vertical-align:super;\">2 </span><span style=\" font-size:8pt;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> Lambda and V</span><span style=\" font-size:8pt; vertical-align:sub;\">T </span><span style=\" font-size:8pt;\">are</span><span style=\" font-size:8pt; vertical-align:super;\"> </span><span style=\" font-size:8pt;\">specified for each cell separately. Lambda and target volume are specified in Python.</span></p></body></html>"))
        self.volumeLocalFlexCHB.setText(_translate("NewSimulationWizard", "VolumeLocalFlex"))
        self.label_41.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Surface</span></p></body></html>"))
        self.surfaceFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surface constraint energy term. E=Lambda*(s-S</span><span style=\" font-size:8pt; vertical-align:sub;\">T</span><span style=\" font-size:8pt;\">)</span><span style=\" font-size:8pt; vertical-align:super;\">2 </span><span style=\" font-size:8pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Lambda and S</span><span style=\" font-size:8pt; vertical-align:sub;\">T </span><span style=\" font-size:8pt;\">are</span><span style=\" font-size:8pt; vertical-align:super;\"> </span><span style=\" font-size:8pt;\">specified for each cell type separately</span></p></body></html>"))
        self.surfaceFlexCHB.setText(_translate("NewSimulationWizard", "SurfaceFlex"))
        self.surfaceLocalFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Surface constraint energy term. E=Lambda*(s-S</span><span style=\" font-size:8pt; vertical-align:sub;\">T</span><span style=\" font-size:8pt;\">)</span><span style=\" font-size:8pt; vertical-align:super;\">2 </span><span style=\" font-size:8pt;\">. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Lambda and S</span><span style=\" font-size:8pt; vertical-align:sub;\">T </span><span style=\" font-size:8pt;\">are</span><span style=\" font-size:8pt; vertical-align:super;\"> </span><span style=\" font-size:8pt;\">specified for each cell separately. Lambda and target surface are specified in Python.</span></p></body></html>"))
        self.surfaceLocalFlexCHB.setText(_translate("NewSimulationWizard", "SurfaceLocalFlex"))
        self.label_42.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Ext. Force</span></p></body></html>"))
        self.extPotCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term emulating force applied to cells. Force components are specified for cell types.</span></p></body></html>"))
        self.extPotCHB.setText(_translate("NewSimulationWizard", "ExternalPotential"))
        self.extPotLocalFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term emulating force applied to cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Force components are specified (in Python) for each cell individuelly</span></p></body></html>"))
        self.extPotLocalFlexCHB.setText(_translate("NewSimulationWizard", "ExternalPotentialLocalFlex"))
        self.label_43.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Connectivity</span></p></body></html>"))
        self.connectGlobalCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term which adds high penalty to change of energy when cells are about to fragment. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">It ensures that cells remain connected . </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Works in 2D and 3D and on square and hex lattice. Energy penalty specifications are on a per-cell type basis.</span></p></body></html>"))
        self.connectGlobalCHB.setText(_translate("NewSimulationWizard", "Global (2D/3D)"))
        self.connectGlobalByIdCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term which adds high penalty to change of energy when cells are about to fragment. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">It ensures that cells remain connected. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Works in 2D and 3D and on square and hex lattice. Energy penalty specifications are on a per-cell basis and thus require Python scripting.</span></p></body></html>"))
        self.connectGlobalByIdCHB.setText(_translate("NewSimulationWizard", "Global (by cell id)"))
        self.connect2DCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term which adds high penalty to change of energy when cells are about to fragment. It ensures that cells remain connected. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Works only in  2D on square. Energy penalty specification is global for all cells. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">There is a more flexible version of this plugin which allows specification of penalties on a per-cell basis it is called ConnectivityLocalFlex and reuqires Python scripting</span></p></body></html>"))
        self.connect2DCHB.setText(_translate("NewSimulationWizard", "Fast (2D square lattice)"))
        self.label_45.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">Elongation</span></p></body></html>"))
        self.lengthConstraintCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term which favors pixel copies that elongate cells according to specified paramters.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This constraint often requires connectivity constraint for large cell elongations.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Parameter specifications are on per-cell type basis.</span></p></body></html>"))
        self.lengthConstraintCHB.setText(_translate("NewSimulationWizard", "LengthConstraint"))
        self.lengthConstraintLocalFlexCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Energy term which favors pixel copies that elongate cells according to specified paramters.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This constraint often requires connectivity constraint for large cell elongations.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Parameter specifications are on per-cell basis and require Python scripting. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This energy term works only in 2D</span></p></body></html>"))
        self.lengthConstraintLocalFlexCHB.setText(_translate("NewSimulationWizard", "LengthConstraintLocalFlex (2D)"))
        self.groupBox_4.setTitle(_translate("NewSimulationWizard", "Cellular Property Trackers"))
        self.comCHB.setToolTip(_translate("NewSimulationWizard", "Module tracking center of mass of each cell in the smiulation"))
        self.comCHB.setText(_translate("NewSimulationWizard", "Center Of Mass"))
        self.neighborCHB.setToolTip(_translate("NewSimulationWizard", "Module tracking neighbors of each cell"))
        self.neighborCHB.setText(_translate("NewSimulationWizard", "Cell Neighbors"))
        self.momentOfInertiaCHB.setToolTip(_translate("NewSimulationWizard", "Module tracking tensor of inertia of each cell"))
        self.momentOfInertiaCHB.setText(_translate("NewSimulationWizard", "Moment Of Inertia"))
        self.pixelTrackerCHB.setToolTip(_translate("NewSimulationWizard", "Module tracking and storing pixels of each cell"))
        self.pixelTrackerCHB.setText(_translate("NewSimulationWizard", "Cell Pixel Tracker"))
        self.boundaryPixelTrackerCHB.setToolTip(_translate("NewSimulationWizard", "Module tracking and storing those pixels of a cell which are at the cell boundary"))
        self.boundaryPixelTrackerCHB.setText(_translate("NewSimulationWizard", "Cell Boundary Pixel Tracker"))
        self.groupBox_10.setTitle(_translate("NewSimulationWizard", "Aux. Modules"))
        self.boxWatcherCHB.setToolTip(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Module computing minimal box enclosing all cells in the simulation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Can be used to speed up some simulations</span></p></body></html>"))
        self.boxWatcherCHB.setText(_translate("NewSimulationWizard", "BoxWatcher"))
        self.pifDumperCHB.setToolTip(_translate("NewSimulationWizard", "Module which outputs periodically cell lattice in thee PIFF format"))
        self.pifDumperCHB.setText(_translate("NewSimulationWizard", "PIFDumper"))
        self.label_24.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">Secretion Plugin</span></p></body></html>"))
        item = self.secretionTable.horizontalHeaderItem(0)
        item.setText(_translate("NewSimulationWizard", "Field"))
        item = self.secretionTable.horizontalHeaderItem(1)
        item.setText(_translate("NewSimulationWizard", "CellType"))
        item = self.secretionTable.horizontalHeaderItem(2)
        item.setText(_translate("NewSimulationWizard", "Rate"))
        item = self.secretionTable.horizontalHeaderItem(3)
        item.setText(_translate("NewSimulationWizard", "On Contact With"))
        item = self.secretionTable.horizontalHeaderItem(4)
        item.setText(_translate("NewSimulationWizard", "Type"))
        self.groupBox_6.setTitle(_translate("NewSimulationWizard", "Secretion Type"))
        self.secrUniformRB.setText(_translate("NewSimulationWizard", "uniform"))
        self.secrOnContactRB.setText(_translate("NewSimulationWizard", "on contact"))
        self.secrConstConcRB.setText(_translate("NewSimulationWizard", "constant concentration"))
        self.label_25.setText(_translate("NewSimulationWizard", "Field"))
        self.label_26.setText(_translate("NewSimulationWizard", "Cell type"))
        self.secrRateLB.setText(_translate("NewSimulationWizard", "Secretion Rate"))
        self.secrAddOnContactPB.setText(_translate("NewSimulationWizard", "Add On Contact"))
        self.secrAddRowPB.setText(_translate("NewSimulationWizard", "Add Entry"))
        self.secrRemoveRowsPB.setText(_translate("NewSimulationWizard", "Remove Rows"))
        self.secrClearTablePB.setText(_translate("NewSimulationWizard", "Clear Table"))
        self.label_16.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">Chemotaxis Plugin</span></p></body></html>"))
        item = self.chamotaxisTable.horizontalHeaderItem(0)
        item.setText(_translate("NewSimulationWizard", "Field"))
        item = self.chamotaxisTable.horizontalHeaderItem(1)
        item.setText(_translate("NewSimulationWizard", "CellType"))
        item = self.chamotaxisTable.horizontalHeaderItem(2)
        item.setText(_translate("NewSimulationWizard", "Lambda"))
        item = self.chamotaxisTable.horizontalHeaderItem(3)
        item.setText(_translate("NewSimulationWizard", "ChemotaxTowards"))
        item = self.chamotaxisTable.horizontalHeaderItem(4)
        item.setText(_translate("NewSimulationWizard", "Sat. Coef."))
        item = self.chamotaxisTable.horizontalHeaderItem(5)
        item.setText(_translate("NewSimulationWizard", "Type"))
        self.groupBox_5.setTitle(_translate("NewSimulationWizard", "Chemotaxis Type"))
        self.chemRegRB.setText(_translate("NewSimulationWizard", "regular"))
        self.chemSatRB.setText(_translate("NewSimulationWizard", "saturation"))
        self.chemSatLinRB.setText(_translate("NewSimulationWizard", "saturation linear"))
        self.label_20.setText(_translate("NewSimulationWizard", "Field"))
        self.label_21.setText(_translate("NewSimulationWizard", "Cell type"))
        self.label_22.setText(_translate("NewSimulationWizard", "Lambda"))
        self.satCoefLB.setText(_translate("NewSimulationWizard", "Saturation Coef."))
        self.chemotaxTowardsPB.setText(_translate("NewSimulationWizard", "Chemotax Towards"))
        self.label_23.setText(_translate("NewSimulationWizard", "Cell Type"))
        self.chemotaxisAddRowPB.setText(_translate("NewSimulationWizard", "Add Entry"))
        self.chemotaxisRemoveRowsPB.setText(_translate("NewSimulationWizard", "Remove Rows"))
        self.chemotaxisClearTablePB.setText(_translate("NewSimulationWizard", "Clear Table"))
        self.label_8.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">AdhesionFlex Plugin</span></p></body></html>"))
        item = self.afTable.horizontalHeaderItem(0)
        item.setText(_translate("NewSimulationWizard", "Adhesion Molecule"))
        self.clearAFTablePB.setText(_translate("NewSimulationWizard", "Clear Table"))
        self.label_9.setText(_translate("NewSimulationWizard", "Molecule"))
        self.afMoleculeLE.setToolTip(_translate("NewSimulationWizard", "Specify names of the adhesion molecules you want to use int he simulation"))
        self.afMoleculeAddPB.setText(_translate("NewSimulationWizard", "Add"))
        self.label_10.setText(_translate("NewSimulationWizard", "Binding Formula"))
        self.bindingFormulaLE.setToolTip(_translate("NewSimulationWizard", "This is binary function that takes atwo arguments -  Molecule1 and Molecule2. The allowed functions are those given by muParser - see http://muparser.sourceforge.net/"))
        self.bindingFormulaLE.setText(_translate("NewSimulationWizard", "min(Molecule1,Molecule2)"))
        self.label_12.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">ContactMultiCad Plugin</span></p></body></html>"))
        item = self.cmcTable.horizontalHeaderItem(0)
        item.setText(_translate("NewSimulationWizard", "Cadherin"))
        self.clearCMCTablePB.setText(_translate("NewSimulationWizard", "Clear Table"))
        self.label_11.setText(_translate("NewSimulationWizard", "Cadherin"))
        self.cmcMoleculeLE.setToolTip(_translate("NewSimulationWizard", "Specify names of the adhesion molecules you want to use int he simulation"))
        self.cmcMoleculeAddPB.setText(_translate("NewSimulationWizard", "Add"))
        self.label_7.setText(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#0000ff;\">Configuration Complete!</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("NewSimulationWizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">CC3D project will be generated now</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">NOTE:</span><span style=\" font-size:12pt;\"> The parameters in the XML and Python scripts will have to be changed to be realistic. Please see CC3D manual on how to choose simulation parameters</span></p></body></html>"))

