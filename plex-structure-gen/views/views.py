from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QStandardItem, QStandardItemModel, QKeyEvent
from PySide2.QtWidgets import (
    QFileSystemModel,
    QListWidgetItem,
    QMainWindow,
    QFileDialog,
    QDialog,
)
import logging

from .ui_mainview import Ui_MainWindow
from .ui_addmediadialog import Ui_AddMediaDialog

from models.model import Model
from models.media_item import MediaItem
from controllers.controller import Controller
from services import TmdbProvider


logger = logging.getLogger(__name__)


class MainView(QMainWindow, Ui_MainWindow):
    def __init__(self, model: Model, controller: Controller):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.model = model
        self.controller = controller

        self.setWindowTitle("Plex Structure Generator")
        self.setGeometry(300, 300, 800, 400)

        # Init state
        self.addMediaBtn.setEnabled(False)
        self.tmp_model = QStandardItemModel()
        self.newMediaView.setModel(self.tmp_model)
        self.lib_model = QFileSystemModel()

        self.setMediaLibraryBtn.clicked.connect(self.set_media_library)
        self.addMediaBtn.clicked.connect(self.add_media)
        self.commitMediaBtn.clicked.connect(self.commit_media)
        # TODO should have the Library implement QAbstractItemModel
        self.model.library_changed.connect(self.update_model)

    def set_media_library(self):
        """Set the path for the local media library"""
        dir = QFileDialog.getExistingDirectory(
            caption="Set Media Library Directory"
        )
        self.controller.set_media_library(dir)
        if self.model.library:
            libpath_str = str(self.model.library.path.resolve())
            logger.info(f"Root Library path: {libpath_str}")

            self.mediaLibraryLbl.setText(libpath_str)
            self.libraryViewCurrentDirLbl.setText(self.model.library.path.name)

            # Update FileSystem viewer
            self.lib_model.setRootPath(libpath_str)
            self.libraryView.setModel(self.lib_model)
            self.libraryView.setRootIndex(self.lib_model.index(libpath_str))

            self.addMediaBtn.setEnabled(True)
        else:
            self.mediaLibraryLbl.clear()
            self.libraryView.setModel(None)
            self.addMediaBtn.setEnabled(False)

    def add_media(self):
        """Add Media to the proposed file structure"""
        dialog = AddMediaDialog(self, self.controller)
        result = dialog.exec_()
        if result == QDialog.Accepted and self.model.library:
            logger.info("Accepted Media Add")
            for item in dialog.foundMediaList.selectedItems():
                item: QListWidgetItem
                item_data: MediaItem = item.data(1)
                logger.info(f"media item is: {item}, data is: {item_data}")
                self.controller.add_media(item_data)

    def commit_media(self):
        """Commit media selected to the filesystem"""
        self.controller.create_collection()

    @Slot(str)
    def update_model(self, new_item: str):
        logger.info(f"updating model with {new_item}")
        # TODO naive approach (refresh)
        self.tmp_model.clear()
        for coll in self.model.library.collection:
            logger.info(f"Adding: {coll.qualified_name}")
            qsi: QStandardItem = QStandardItem(coll.display_name)
            qsi.setEditable(False)
            self.tmp_model.appendRow(qsi)


class AddMediaDialog(QDialog, Ui_AddMediaDialog):
    def __init__(self, parent, controller: Controller):
        QDialog.__init__(self, parent=parent)
        Ui_AddMediaDialog.__init__(self)
        self.setupUi(self)
        self.controller = controller

        self.searchBtn.clicked.connect(self.search)

        self.searchBtn.setFocus()

    def keyPressEvent(self, arg__1: QKeyEvent) -> None:
        # Don't process Enter unless Search button is the default
        if arg__1.key() == Qt.Key_Enter or arg__1.key() == Qt.Key_Return:
            if not self.searchBtn.isDefault():
                return
        return super().keyPressEvent(arg__1)

    def search(self):
        """Search for the media item

        Raises:
            NotImplementedError: Unimplemented database service
            Exception: Unknown database service
        """
        self.foundMediaList.clear()

        checked_button = self.dbBtnGrp.checkedButton()
        if checked_button is self.tmdbDbBtn:
            provider = TmdbProvider()
        elif checked_button is self.imdbDbBtn:
            raise NotImplementedError("Need to implement IMDB service")
        else:
            pass

        selection_btn = self.searchMediaBtnGrp.checkedButton()
        if selection_btn is self.searchMovieBtn:
            media_items = self.controller.search_movie(
                provider, self.searchMediaInput.text()
            )
        elif selection_btn is self.searchTvShowBtn:
            media_items = self.controller.search_shows(
                provider, self.searchMediaInput.text()
            )
        else:
            raise NotImplementedError("Unknown, Unimplemented media type")

        for media_item in media_items:
            item = QListWidgetItem(media_item.display_name, self.foundMediaList)
            item.setData(1, media_item)
