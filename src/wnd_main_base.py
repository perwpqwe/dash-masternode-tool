# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/wnd_main_base.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 468)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cboMasternodes = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboMasternodes.sizePolicy().hasHeightForWidth())
        self.cboMasternodes.setSizePolicy(sizePolicy)
        self.cboMasternodes.setMinimumSize(QtCore.QSize(140, 0))
        self.cboMasternodes.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboMasternodes.setEditable(False)
        self.cboMasternodes.setObjectName("cboMasternodes")
        self.horizontalLayout_4.addWidget(self.cboMasternodes)
        self.btnNewMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewMn.sizePolicy().hasHeightForWidth())
        self.btnNewMn.setSizePolicy(sizePolicy)
        self.btnNewMn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnNewMn.setObjectName("btnNewMn")
        self.horizontalLayout_4.addWidget(self.btnNewMn)
        self.btnDeleteMn = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDeleteMn.setObjectName("btnDeleteMn")
        self.horizontalLayout_4.addWidget(self.btnDeleteMn)
        self.btnEditConfiguration = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEditConfiguration.sizePolicy().hasHeightForWidth())
        self.btnEditConfiguration.setSizePolicy(sizePolicy)
        self.btnEditConfiguration.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnEditConfiguration.setObjectName("btnEditConfiguration")
        self.horizontalLayout_4.addWidget(self.btnEditConfiguration)
        self.btnImportMasternodeConf = QtWidgets.QPushButton(self.groupBox_3)
        self.btnImportMasternodeConf.setObjectName("btnImportMasternodeConf")
        self.horizontalLayout_4.addWidget(self.btnImportMasternodeConf)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtMnIp = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnIp.sizePolicy().hasHeightForWidth())
        self.edtMnIp.setSizePolicy(sizePolicy)
        self.edtMnIp.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnIp.setMaximumSize(QtCore.QSize(150, 16777215))
        self.edtMnIp.setObjectName("edtMnIp")
        self.horizontalLayout_3.addWidget(self.edtMnIp)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.edtMnPort = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnPort.sizePolicy().hasHeightForWidth())
        self.edtMnPort.setSizePolicy(sizePolicy)
        self.edtMnPort.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnPort.setMaximumSize(QtCore.QSize(40, 16777215))
        self.edtMnPort.setObjectName("edtMnPort")
        self.horizontalLayout_3.addWidget(self.edtMnPort)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edtMnCollateralBip32Path = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralBip32Path.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralBip32Path.setSizePolicy(sizePolicy)
        self.edtMnCollateralBip32Path.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnCollateralBip32Path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralBip32Path.setObjectName("edtMnCollateralBip32Path")
        self.horizontalLayout_2.addWidget(self.edtMnCollateralBip32Path, 0, QtCore.Qt.AlignVCenter)
        self.btnReadAddressFromTrezor = QtWidgets.QToolButton(self.groupBox_3)
        self.btnReadAddressFromTrezor.setText("")
        self.btnReadAddressFromTrezor.setObjectName("btnReadAddressFromTrezor")
        self.horizontalLayout_2.addWidget(self.btnReadAddressFromTrezor)
        self.edtMnCollateralAddress = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralAddress.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralAddress.setSizePolicy(sizePolicy)
        self.edtMnCollateralAddress.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnCollateralAddress.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralAddress.setReadOnly(True)
        self.edtMnCollateralAddress.setObjectName("edtMnCollateralAddress")
        self.horizontalLayout_2.addWidget(self.edtMnCollateralAddress, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.setStretch(2, 2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.edtMnName = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnName.sizePolicy().hasHeightForWidth())
        self.edtMnName.setSizePolicy(sizePolicy)
        self.edtMnName.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnName.setObjectName("edtMnName")
        self.gridLayout_2.addWidget(self.edtMnName, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.btnGenerateMNPrivateKey = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenerateMNPrivateKey.sizePolicy().hasHeightForWidth())
        self.btnGenerateMNPrivateKey.setSizePolicy(sizePolicy)
        self.btnGenerateMNPrivateKey.setMinimumSize(QtCore.QSize(110, 0))
        self.btnGenerateMNPrivateKey.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btnGenerateMNPrivateKey.setObjectName("btnGenerateMNPrivateKey")
        self.gridLayout_2.addWidget(self.btnGenerateMNPrivateKey, 3, 2, 1, 1)
        self.edtMnStatus = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnStatus.sizePolicy().hasHeightForWidth())
        self.edtMnStatus.setSizePolicy(sizePolicy)
        self.edtMnStatus.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnStatus.setObjectName("edtMnStatus")
        self.gridLayout_2.addWidget(self.edtMnStatus, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 0, 1, 1)
        self.edtMnPrivateKey = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnPrivateKey.sizePolicy().hasHeightForWidth())
        self.edtMnPrivateKey.setSizePolicy(sizePolicy)
        self.edtMnPrivateKey.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnPrivateKey.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnPrivateKey.setObjectName("edtMnPrivateKey")
        self.gridLayout_2.addWidget(self.edtMnPrivateKey, 3, 1, 1, 1)
        self.btnRefreshMnStatus = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRefreshMnStatus.setObjectName("btnRefreshMnStatus")
        self.gridLayout_2.addWidget(self.btnRefreshMnStatus, 6, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edtMnCollateralTx = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralTx.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralTx.setSizePolicy(sizePolicy)
        self.edtMnCollateralTx.setMinimumSize(QtCore.QSize(300, 24))
        self.edtMnCollateralTx.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralTx.setText("")
        self.edtMnCollateralTx.setObjectName("edtMnCollateralTx")
        self.horizontalLayout_7.addWidget(self.edtMnCollateralTx)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.edtMnCollateralTxIndex = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralTxIndex.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralTxIndex.setSizePolicy(sizePolicy)
        self.edtMnCollateralTxIndex.setMinimumSize(QtCore.QSize(0, 24))
        self.edtMnCollateralTxIndex.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.edtMnCollateralTxIndex.setFont(font)
        self.edtMnCollateralTxIndex.setObjectName("edtMnCollateralTxIndex")
        self.horizontalLayout_7.addWidget(self.edtMnCollateralTxIndex)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnBroadcastMn = QtWidgets.QPushButton(self.groupBox_3)
        self.btnBroadcastMn.setMinimumSize(QtCore.QSize(0, 40))
        self.btnBroadcastMn.setMaximumSize(QtCore.QSize(16777215, 200))
        self.btnBroadcastMn.setObjectName("btnBroadcastMn")
        self.verticalLayout_3.addWidget(self.btnBroadcastMn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 7, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_9.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 4)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btnConfigureDashdConnection = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConfigureDashdConnection.sizePolicy().hasHeightForWidth())
        self.btnConfigureDashdConnection.setSizePolicy(sizePolicy)
        self.btnConfigureDashdConnection.setMinimumSize(QtCore.QSize(140, 0))
        self.btnConfigureDashdConnection.setMaximumSize(QtCore.QSize(140, 16777215))
        self.btnConfigureDashdConnection.setObjectName("btnConfigureDashdConnection")
        self.gridLayout.addWidget(self.btnConfigureDashdConnection, 0, 2, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lblConnectionType = QtWidgets.QLabel(self.groupBox)
        self.lblConnectionType.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lblConnectionType.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblConnectionType.setObjectName("lblConnectionType")
        self.horizontalLayout_8.addWidget(self.lblConnectionType)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.btnCheckConnection = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCheckConnection.sizePolicy().hasHeightForWidth())
        self.btnCheckConnection.setSizePolicy(sizePolicy)
        self.btnCheckConnection.setMinimumSize(QtCore.QSize(140, 0))
        self.btnCheckConnection.setMaximumSize(QtCore.QSize(140, 16777215))
        self.btnCheckConnection.setObjectName("btnCheckConnection")
        self.gridLayout.addWidget(self.btnCheckConnection, 1, 2, 1, 1)
        self.hlHwType = QtWidgets.QHBoxLayout()
        self.hlHwType.setContentsMargins(6, -1, -1, -1)
        self.hlHwType.setObjectName("hlHwType")
        self.chbHwTrezor = QtWidgets.QRadioButton(self.groupBox)
        self.chbHwTrezor.setMinimumSize(QtCore.QSize(60, 0))
        self.chbHwTrezor.setMaximumSize(QtCore.QSize(70, 16777215))
        self.chbHwTrezor.setChecked(True)
        self.chbHwTrezor.setObjectName("chbHwTrezor")
        self.hlHwType.addWidget(self.chbHwTrezor)
        self.chbHwKeepKey = QtWidgets.QRadioButton(self.groupBox)
        self.chbHwKeepKey.setMinimumSize(QtCore.QSize(70, 0))
        self.chbHwKeepKey.setMaximumSize(QtCore.QSize(90, 16777215))
        self.chbHwKeepKey.setObjectName("chbHwKeepKey")
        self.hlHwType.addWidget(self.chbHwKeepKey)
        self.btnHwCheck = QtWidgets.QToolButton(self.groupBox)
        self.btnHwCheck.setText("")
        self.btnHwCheck.setObjectName("btnHwCheck")
        self.hlHwType.addWidget(self.btnHwCheck)
        self.btnHwDisconnect = QtWidgets.QToolButton(self.groupBox)
        self.btnHwDisconnect.setText("")
        self.btnHwDisconnect.setObjectName("btnHwDisconnect")
        self.hlHwType.addWidget(self.btnHwDisconnect)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlHwType.addItem(spacerItem4)
        self.gridLayout.addLayout(self.hlHwType, 2, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lblConnectionStatus = QtWidgets.QLabel(self.groupBox)
        self.lblConnectionStatus.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lblConnectionStatus.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblConnectionStatus.setObjectName("lblConnectionStatus")
        self.horizontalLayout_10.addWidget(self.lblConnectionStatus)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout)
        self.horizontalLayout_11.addWidget(self.groupBox)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblAbout = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAbout.sizePolicy().hasHeightForWidth())
        self.lblAbout.setSizePolicy(sizePolicy)
        self.lblAbout.setMinimumSize(QtCore.QSize(64, 64))
        self.lblAbout.setMaximumSize(QtCore.QSize(64, 64))
        self.lblAbout.setText("")
        self.lblAbout.setObjectName("lblAbout")
        self.horizontalLayout_13.addWidget(self.lblAbout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAbout = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAbout.sizePolicy().hasHeightForWidth())
        self.btnAbout.setSizePolicy(sizePolicy)
        self.btnAbout.setMinimumSize(QtCore.QSize(140, 0))
        self.btnAbout.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnAbout.setObjectName("btnAbout")
        self.verticalLayout.addWidget(self.btnAbout)
        self.btnSaveConfiguration = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveConfiguration.sizePolicy().hasHeightForWidth())
        self.btnSaveConfiguration.setSizePolicy(sizePolicy)
        self.btnSaveConfiguration.setMinimumSize(QtCore.QSize(140, 0))
        self.btnSaveConfiguration.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnSaveConfiguration.setObjectName("btnSaveConfiguration")
        self.verticalLayout.addWidget(self.btnSaveConfiguration)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_13.addLayout(self.verticalLayout)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11.setStretch(0, 1)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Masternode"))
        self.cboMasternodes.setToolTip(_translate("MainWindow", "List of configured masternodes"))
        self.btnNewMn.setToolTip(_translate("MainWindow", "Create a new Masternode configuration"))
        self.btnNewMn.setText(_translate("MainWindow", "New"))
        self.btnDeleteMn.setToolTip(_translate("MainWindow", "Delete current Masternode configuration"))
        self.btnDeleteMn.setText(_translate("MainWindow", "Delete"))
        self.btnEditConfiguration.setToolTip(_translate("MainWindow", "Enable editing"))
        self.btnEditConfiguration.setText(_translate("MainWindow", "Edit"))
        self.btnImportMasternodeConf.setToolTip(_translate("MainWindow", "Import Masternodes from masternode.conf file"))
        self.btnImportMasternodeConf.setText(_translate("MainWindow", "Import"))
        self.edtMnIp.setToolTip(_translate("MainWindow", "The Masternode\'s IP address for incoming communication with other nodes"))
        self.label_11.setText(_translate("MainWindow", "port:"))
        self.edtMnPort.setToolTip(_translate("MainWindow", "The Masternode\'s TCP port number for incoming communication with other nodes"))
        self.edtMnCollateralBip32Path.setToolTip(_translate("MainWindow", "BIP32 path of the 1000 Dash collateral (e.g. 44\'/5\'/0\'/0/0)"))
        self.edtMnCollateralBip32Path.setPlaceholderText(_translate("MainWindow", "BIP32 path"))
        self.btnReadAddressFromTrezor.setToolTip(_translate("MainWindow", "Convert BIP32 path to Dash address using hardware wallet"))
        self.edtMnCollateralAddress.setToolTip(_translate("MainWindow", "Dash address of the 1000 Dash collateral, coverted from BIP32 path with hardware wallet."))
        self.edtMnCollateralAddress.setPlaceholderText(_translate("MainWindow", "Dash address"))
        self.label_4.setText(_translate("MainWindow", "Collateral:"))
        self.label_9.setText(_translate("MainWindow", "MN private key:"))
        self.label_8.setText(_translate("MainWindow", "Masternode status:"))
        self.label_12.setText(_translate("MainWindow", "Name:"))
        self.edtMnName.setToolTip(_translate("MainWindow", "The Masternode\'s configuration name"))
        self.label_6.setText(_translate("MainWindow", "Collateral TX ID:"))
        self.btnGenerateMNPrivateKey.setToolTip(_translate("MainWindow", "Generate a new private key"))
        self.btnGenerateMNPrivateKey.setText(_translate("MainWindow", "Generate new"))
        self.edtMnStatus.setToolTip(_translate("MainWindow", "Status of the Masternode. To get current status click the button <Get status>."))
        self.label_5.setText(_translate("MainWindow", "Masternodes:"))
        self.label_10.setText(_translate("MainWindow", "IP:"))
        self.edtMnPrivateKey.setToolTip(_translate("MainWindow", "Masternode\'s private key. Use your own or click the button <Generate new> to create a new and random private key with the use of \'bitcoin\' library."))
        self.btnRefreshMnStatus.setToolTip(_translate("MainWindow", "Get Masternode\'s status"))
        self.btnRefreshMnStatus.setText(_translate("MainWindow", "Get status"))
        self.edtMnCollateralTx.setToolTip(_translate("MainWindow", "The collateral transaction hash from the 1000 Dash deposit"))
        self.label_7.setText(_translate("MainWindow", "TX index:"))
        self.edtMnCollateralTxIndex.setToolTip(_translate("MainWindow", "The collateral transaction\'s (unspent) output index with the 1000 Dash deposit (usally 0)"))
        self.btnBroadcastMn.setToolTip(_translate("MainWindow", "Broadcast information about the Masternode"))
        self.btnBroadcastMn.setText(_translate("MainWindow", "Start Masternode using Hardware Wallet"))
        self.groupBox.setTitle(_translate("MainWindow", "Configuration"))
        self.label_3.setText(_translate("MainWindow", "Hardware wallet:"))
        self.label.setText(_translate("MainWindow", "Connection type:"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.btnConfigureDashdConnection.setToolTip(_translate("MainWindow", "Open configuration window of communication with a Dash daemon"))
        self.btnConfigureDashdConnection.setText(_translate("MainWindow", "Configure"))
        self.lblConnectionType.setText(_translate("MainWindow", "not configured"))
        self.btnCheckConnection.setToolTip(_translate("MainWindow", "Check communication with Dash daemon"))
        self.btnCheckConnection.setText(_translate("MainWindow", "Check connection"))
        self.chbHwTrezor.setText(_translate("MainWindow", "Trezor"))
        self.chbHwKeepKey.setText(_translate("MainWindow", "KeepKey"))
        self.btnHwCheck.setToolTip(_translate("MainWindow", "Check Hardware Wallet connection"))
        self.btnHwDisconnect.setToolTip(_translate("MainWindow", "Close Hardware Wallet session "))
        self.lblConnectionStatus.setText(_translate("MainWindow", "not connected"))
        self.btnAbout.setText(_translate("MainWindow", "About"))
        self.btnSaveConfiguration.setText(_translate("MainWindow", "Save configuration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
