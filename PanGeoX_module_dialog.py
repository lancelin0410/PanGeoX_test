# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PanGeoXDialog
                                 A QGIS plugin
 Panoramic Geodata eXtractor
                             -------------------
        begin                : 2015-07-08
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Klas Karlsson, Enrico Ferreguti
        email                : enricofer@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from PyQt4 import QtCore, QtGui
from PanGeoX_dialog_base import Ui_PanGeoXDialogBase
# create the dialog for zoom to point

class PanGeoXDialog(QtGui.QDialog, Ui_PanGeoXDialogBase):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)