#!/usr/bin/env python3

import sys
import logging

from PySide2.QtWidgets import (
    QApplication,
    QPushButton,
    QDialog,
    QMainWindow,
    QFileDialog,
)

from views.views import MainView
from models.model import Model
from controllers.controller import Controller

logger = logging.getLogger(__name__)


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = MainView(self.model, self.controller)
        logger.info(f"Done with init")
        self.view.show()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, filename="plex-structure-gen.log", filemode="w"
    )

    app = App(sys.argv)
    sys.exit(app.exec_())
