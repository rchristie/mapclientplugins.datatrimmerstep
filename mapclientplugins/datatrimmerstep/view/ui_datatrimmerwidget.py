# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datatrimmerwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget


class Ui_DataTrimmer(object):
    def setupUi(self, DataTrimmer):
        if not DataTrimmer.objectName():
            DataTrimmer.setObjectName(u"DataTrimmer")
        DataTrimmer.resize(1310, 998)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataTrimmer.sizePolicy().hasHeightForWidth())
        DataTrimmer.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(DataTrimmer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(DataTrimmer)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy1)
        self.dockWidget.setMinimumSize(QSize(468, 135))
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 466, 948))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy1.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy1)
        self.toolBox.setStyleSheet(u"QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.dataTrimmerPage = QWidget()
        self.dataTrimmerPage.setObjectName(u"dataTrimmerPage")
        self.dataTrimmerPage.setGeometry(QRect(0, 0, 462, 876))
        sizePolicy1.setHeightForWidth(self.dataTrimmerPage.sizePolicy().hasHeightForWidth())
        self.dataTrimmerPage.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.dataTrimmerPage)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 3, 0, 3)
        self.dataGroupsFrame = QFrame(self.dataTrimmerPage)
        self.dataGroupsFrame.setObjectName(u"dataGroupsFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dataGroupsFrame.sizePolicy().hasHeightForWidth())
        self.dataGroupsFrame.setSizePolicy(sizePolicy3)
        self.dataGroupsFrame.setMinimumSize(QSize(0, 0))
        self.dataGroupsFrame.setFrameShape(QFrame.StyledPanel)
        self.dataGroupsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.dataGroupsFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.modifyOptions_frame = QFrame(self.dataGroupsFrame)
        self.modifyOptions_frame.setObjectName(u"modifyOptions_frame")
        self.modifyOptions_frame.setFrameShape(QFrame.StyledPanel)
        self.modifyOptions_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.modifyOptions_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, -1, 0, -1)

        self.gridLayout_7.addWidget(self.modifyOptions_frame, 3, 0, 1, 1)

        self.groupOptions_frame = QFrame(self.dataGroupsFrame)
        self.groupOptions_frame.setObjectName(u"groupOptions_frame")
        self.groupOptions_frame.setFrameShape(QFrame.StyledPanel)
        self.groupOptions_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.groupOptions_frame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, 0, -1)

        self.gridLayout_7.addWidget(self.groupOptions_frame, 1, 0, 1, 1)

        self.dataFrame_line_2 = QFrame(self.dataGroupsFrame)
        self.dataFrame_line_2.setObjectName(u"dataFrame_line_2")
        self.dataFrame_line_2.setFrameShape(QFrame.HLine)
        self.dataFrame_line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.dataFrame_line_2, 2, 0, 1, 1)

        self.dataFrame_line_1 = QFrame(self.dataGroupsFrame)
        self.dataFrame_line_1.setObjectName(u"dataFrame_line_1")
        self.dataFrame_line_1.setFrameShape(QFrame.HLine)
        self.dataFrame_line_1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.dataFrame_line_1, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.dataGroupsFrame)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.deleteResetWidget = QWidget(self.dataTrimmerPage)
        self.deleteResetWidget.setObjectName(u"deleteResetWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.deleteResetWidget.sizePolicy().hasHeightForWidth())
        self.deleteResetWidget.setSizePolicy(sizePolicy4)
        self.gridLayout = QGridLayout(self.deleteResetWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.deleteResetWidget)

        self.toolBox.addItem(self.dataTrimmerPage, u"Control Panel")

        self.verticalLayout_3.addWidget(self.toolBox)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.viewAllButton = QPushButton(self.frame)
        self.viewAllButton.setObjectName(u"viewAllButton")

        self.horizontalLayout_2.addWidget(self.viewAllButton)

        self.doneButton = QPushButton(self.frame)
        self.doneButton.setObjectName(u"doneButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.doneButton)


        self.verticalLayout_3.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.sceneviewerWidget = SceneviewerWidget(DataTrimmer)
        self.sceneviewerWidget.setObjectName(u"sceneviewerWidget")
        self.sceneviewerWidget.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy6)
        self.sceneviewerWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.sceneviewerWidget)


        self.retranslateUi(DataTrimmer)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(DataTrimmer)
    # setupUi

    def retranslateUi(self, DataTrimmer):
        DataTrimmer.setWindowTitle(QCoreApplication.translate("DataTrimmer", u"Form", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("DataTrimmer", u"Data Trimmer Step", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.dataTrimmerPage), QCoreApplication.translate("DataTrimmer", u"Control Panel", None))
#if QT_CONFIG(tooltip)
        self.viewAllButton.setToolTip(QCoreApplication.translate("DataTrimmer", u"Adjust the view to see the whole model", None))
#endif // QT_CONFIG(tooltip)
        self.viewAllButton.setText(QCoreApplication.translate("DataTrimmer", u"View All", None))
#if QT_CONFIG(tooltip)
        self.doneButton.setToolTip(QCoreApplication.translate("DataTrimmer", u"Finish this step", None))
#endif // QT_CONFIG(tooltip)
        self.doneButton.setText(QCoreApplication.translate("DataTrimmer", u"Done", None))
    # retranslateUi

