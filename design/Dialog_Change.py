from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_1(object):
    def setupUi_Dialog_1(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(742, 102)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Id = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Id.setFont(font)
        self.label_Id.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Id.setObjectName("label_Id")
        self.verticalLayout.addWidget(self.label_Id)
        self.lineEdit_Id = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Id.setMinimumSize(QtCore.QSize(31, 20))
        self.lineEdit_Id.setMaximumSize(QtCore.QSize(31, 20))
        self.lineEdit_Id.setText("")
        self.lineEdit_Id.setFrame(True)
        self.lineEdit_Id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Id.setReadOnly(True)
        self.lineEdit_Id.setObjectName("lineEdit_Id")
        self.verticalLayout.addWidget(self.lineEdit_Id)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_Booker = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Booker.sizePolicy().hasHeightForWidth())
        self.label_Booker.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Booker.setFont(font)
        self.label_Booker.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Booker.setTextFormat(QtCore.Qt.AutoText)
        self.label_Booker.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Booker.setObjectName("label_Booker")
        self.verticalLayout_2.addWidget(self.label_Booker)
        self.lineEdit_Booker = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Booker.setMinimumSize(QtCore.QSize(190, 0))
        self.lineEdit_Booker.setText("")
        self.lineEdit_Booker.setObjectName("lineEdit_Booker")
        self.verticalLayout_2.addWidget(self.lineEdit_Booker)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Date = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Date.setFont(font)
        self.label_Date.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label_Date.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_Date.setAutoFillBackground(False)
        self.label_Date.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_Date.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Date.setObjectName("label_Date")
        self.verticalLayout_3.addWidget(self.label_Date)
        self.lineEdit_Date = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Date.setMinimumSize(QtCore.QSize(62, 0))
        self.lineEdit_Date.setText("")
        self.lineEdit_Date.setObjectName("lineEdit_Date")
        self.verticalLayout_3.addWidget(self.lineEdit_Date)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_Costs = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Costs.setFont(font)
        self.label_Costs.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Costs.setObjectName("label_Costs")
        self.verticalLayout_4.addWidget(self.label_Costs)
        self.lineEdit_Costs = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Costs.setText("")
        self.lineEdit_Costs.setObjectName("lineEdit_Costs")
        self.verticalLayout_4.addWidget(self.lineEdit_Costs)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_Status = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Status.setFont(font)
        self.label_Status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Status.setObjectName("label_Status")
        self.verticalLayout_5.addWidget(self.label_Status)
        self.lineEdit_Status = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Status.setMinimumSize(QtCore.QSize(115, 0))
        self.lineEdit_Status.setText("")
        self.lineEdit_Status.setObjectName("lineEdit_Status")
        self.verticalLayout_5.addWidget(self.lineEdit_Status)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_Email = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Email.setFont(font)
        self.label_Email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Email.setObjectName("label_Email")
        self.verticalLayout_6.addWidget(self.label_Email)
        self.lineEdit_Email = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Email.setMinimumSize(QtCore.QSize(133, 0))
        self.lineEdit_Email.setText("")
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.verticalLayout_6.addWidget(self.lineEdit_Email)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_7.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "???????????????? ????????????"))
        self.label_Id.setText(_translate("Dialog", "Id"))
        self.label_Booker.setText(_translate("Dialog", "????????????????"))
        self.label_Date.setText(_translate("Dialog", "???????? ????????????????"))
        self.label_Costs.setText(_translate("Dialog", "????????????"))
        self.label_Status.setText(_translate("Dialog", "????????????"))
        self.label_Email.setText(_translate("Dialog", "Email"))
