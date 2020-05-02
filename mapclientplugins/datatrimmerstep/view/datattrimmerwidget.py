from PySide import QtGui, QtCore

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
        self._settings = {'view-parameters': {}}
        self._make_connections()

    def _make_connections(self):
        self._ui.doneButton.clicked.connect(self._done_clicked)
        self._ui.destroyButton.clicked.connect(self._destroy_groups)
        # self._ui.resetButton.clicked.connect(self._reset)

    def _destroy_groups(self):
        group_to_delete = []
        for item in self._ui.groupOptions_frame.children():
            if isinstance(item, QtGui.QCheckBox):
                if item.isChecked():
                    group_to_delete.append(item.objectName())
                    item.setEnabled(False)
        self._model.destroy_groups(group_to_delete)

    def _graphics_initialized(self):
        self._scene_changed()
        self._get_groups()
        scene_viewer = self._ui.sceneviewerWidget.getSceneviewer()
        if scene_viewer is not None:
            scene_viewer.viewAll()

    def _scene_changed(self):
        sceneviewer = self._ui.sceneviewerWidget.getSceneviewer()
        if sceneviewer is not None:
            self._model.create_graphics()
            sceneviewer.setScene(self._model.get_scene())
            self._refresh_graphics()

    def _refresh_graphics(self):
        self._ui.sceneviewerWidget.paintGL()

    def _view_all(self):
        if self._ui.sceneviewerWidget.getSceneviewer() is not None:
            self._ui.sceneviewerWidget.viewAll()

    def _done_clicked(self):
        self._model.write_model()
        self._done_callback()

    def register_done_execution(self, done_callback):
        self._done_callback = done_callback

    def _get_groups(self):
        layout = self._ui.groupOptions_frame.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        data_groups = self._model.get_group_names()
        for row in range(len(data_groups)):
            if data_groups[row] != 'marker':
                checkbox = QtGui.QCheckBox()
                checkbox.setCheckState(QtCore.Qt.Unchecked)
                checkbox.setObjectName(data_groups[row])
                checkbox.setText(str(data_groups[row]))
                layout.addWidget(checkbox)
