from PySide import QtGui, QtCore

from functools import partial

from .ui_datatrimmerwidget import Ui_DataTrimmer


class DataTrimmer(QtGui.QWidget):

    def __init__(self, model, parent=None):
        super(DataTrimmer, self).__init__(parent)
        self._model = model
        self._ui = Ui_DataTrimmer()
        self._ui.setupUi(self)
        self._ui.sceneviewerWidget.setContext(self._model.get_context())
        self._ui.sceneviewerWidget.graphicsInitialized.connect(self._graphics_initialized)
        self._done_callback = None
        self._scene_change_callback = None
        self._checked_groups = []
        self._unchecked_groups = []
        self._settings = {'view-parameters': {}}
        self._make_connections()

    def _make_connections(self):
        self._ui.doneButton.clicked.connect(self._done_clicked)

    def _destroy_groups(self):
        group_to_delete = []
        for item in self._ui.groupOptions_frame.children():
            if isinstance(item, QtGui.QCheckBox):
                if not item.isChecked():
                    group_to_delete.append(item.objectName())
        self._model.destroy_groups(group_to_delete)

    def _done_clicked(self):
        self._model.done()
        self._destroy_groups()
        self._model.write_model()
        self._done_callback()

    def _get_checked_groups(self):
        for item in self._ui.groupOptions_frame.children():
            if isinstance(item, QtGui.QCheckBox):
                if item.isChecked():
                    self._checked_groups.append(item.objectName())

    def _get_groups(self):
        layout = self._ui.groupOptions_frame.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        checkbox = QtGui.QCheckBox()
        checkbox.setCheckState(QtCore.Qt.Checked)
        checkbox.setObjectName('all_groups')
        checkbox.setText('All')
        font = QtGui.QFont()
        font.setBold(True)
        checkbox.setFont(font)
        callback = partial(self._group_display_changed, checkbox)
        checkbox.clicked.connect(callback)
        layout.addWidget(checkbox)
        data_groups = self._model.get_group_names()
        settings = self._model.get_settings()
        for row in range(len(data_groups)):
            if data_groups[row] != 'marker':
                checkbox = QtGui.QCheckBox()
                if settings[data_groups[row]]:
                    checkbox.setCheckState(QtCore.Qt.Checked)
                else:
                    checkbox.setCheckState(QtCore.Qt.Unchecked)
                checkbox.setObjectName(data_groups[row])
                checkbox.setText(str(data_groups[row]))
                callback = partial(self._group_display_changed, checkbox)
                checkbox.clicked.connect(callback)
                layout.addWidget(checkbox)

    def _group_display_changed(self, checkbox):
        if checkbox.objectName() == 'all_groups':
            if not checkbox.isChecked():
                for child in self._ui.groupOptions_frame.children():
                    if isinstance(child, QtGui.QCheckBox):
                        child.setCheckState(QtCore.Qt.Unchecked)
                        self._model.remove_graphics(self._model.get_group_names())
            elif checkbox.isChecked():
                for child in self._ui.groupOptions_frame.children():
                    if isinstance(child, QtGui.QCheckBox):
                        child.setCheckState(QtCore.Qt.Checked)
                        self._model.show_graphics(self._model.get_group_names())
            return
        if not checkbox.isChecked():
            self._model.remove_graphics([checkbox.objectName()])
        elif checkbox.isChecked():
            self._model.show_graphics([checkbox.objectName()])

    def _graphics_initialized(self):
        self._get_groups()
        self._get_checked_groups()
        self._scene_changed()
        scene_viewer = self._ui.sceneviewerWidget.getSceneviewer()
        if scene_viewer is not None:
            scene_viewer.viewAll()

    def _refresh_graphics(self):
        self._ui.sceneviewerWidget.paintGL()

    def _scene_changed(self):
        sceneviewer = self._ui.sceneviewerWidget.getSceneviewer()
        if sceneviewer is not None:
            self._model.create_graphics(self._model.get_group_names())
            sceneviewer.setScene(self._model.get_scene())
            self._refresh_graphics()

    def _view_all(self):
        if self._ui.sceneviewerWidget.getSceneviewer() is not None:
            self._ui.sceneviewerWidget.viewAll()

    def register_done_execution(self, done_callback):
        self._done_callback = done_callback
