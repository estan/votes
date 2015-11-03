from argparse import ArgumentParser
from sys import argv

from autobahn.twisted.wamp import ApplicationSession
from autobahn.twisted.wamp import ApplicationRunner
from autobahn.wamp.types import SessionDetails
from autobahn.wamp.types import CloseDetails

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

import qt5reactor

from votes.ui.votes_window_ui import Ui_VotesWindow


class VotesSession(QObject, ApplicationSession):
    """Votes WAMP application session.

    Simply bridges the Autobahn join and leave signals to Qt signals.
    """

    joinedSession = pyqtSignal(SessionDetails)
    leftSession = pyqtSignal(CloseDetails)

    def __init__(self, config=None, parent=None):
        QObject.__init__(self, parent)
        ApplicationSession.__init__(self, config)

    def onJoin(self, details):
        self.joinedSession.emit(details)

    def onLeave(self, details):
        self.leftSession.emit(details)


class VotesWindow(QMainWindow, Ui_VotesWindow):
    """Main window of the votes demo."""

    closed = pyqtSignal()  # Emitted when window is closed.

    def __init__(self, url, realm, parent=None):
        super(VotesWindow, self).__init__(parent)
        self.setupUi(self)

        self.url = url
        self.realm = realm
        self.session = None
        self.votes = {
            'Banana': self.bananaVotes,
            'Chocolate': self.chocolateVotes,
            'Lemon': self.lemonVotes
        }

        # Factory method for ApplicationRunner.run(..)
        def make(config):
            self.session = VotesSession(config)
            self.session.joinedSession.connect(self.onJoinedSession)
            self.session.leftSession.connect(self.onLeftSession)
            return self.session

        runner = ApplicationRunner(url, realm)
        runner.run(make, start_reactor=False)

    def onJoinedSession(self):
        self.setEnabled(True)
        self.session.subscribe(self.onVoteMessage, u'io.crossbar.demo.vote.onvote')
        self.session.subscribe(self.onResetMessage, u'io.crossbar.demo.vote.onreset')
        self.statusBar().showMessage('Connected to realm {} at {}'
                                     .format(self.realm, self.url))

    def onLeftSession(self):
        print('leave')

    def onVoteMessage(self, result):
        self.votes[result[u'subject']].setText(str(result[u'votes']))

    def onResetMessage(self):
        self.bananaVotes.setText('0')
        self.chocolateVotes.setText('0')
        self.lemonVotes.setText('0')

    def closeEvent(self, event):
        self.session.leave()
        self.closed.emit()
        event.accept()

    @pyqtSlot()
    def on_resetButton_clicked(self):
        self.session.call(u'io.crossbar.demo.vote.reset')

    @pyqtSlot()
    def on_bananaButton_clicked(self):
        self.session.call(u'io.crossbar.demo.vote.vote', 'Banana')

    @pyqtSlot()
    def on_chocolateButton_clicked(self):
        self.session.call(u'io.crossbar.demo.vote.vote', 'Chocolate')

    @pyqtSlot()
    def on_lemonButton_clicked(self):
        self.session.call(u'io.crossbar.demo.vote.vote', 'Lemon')


def main():
    parser = ArgumentParser(description='PyQt version of Crossbar Gauges demo.')
    parser.add_argument('--url',
                        type=unicode,
                        default=u'ws://127.0.0.1:8080/ws',
                        metavar='<url>',
                        help='WAMP router URL (default: ws://127.0.0.1:8080/ws).')
    args = parser.parse_args()

    app = QApplication(argv)
    qt5reactor.install()

    from twisted.internet import reactor

    def quit():
        if reactor.threadpool is not None:
            reactor.threadpool.stop()
        app.quit()

    window = VotesWindow(args.url, u'crossbardemo')
    window.closed.connect(quit)
    window.show()

    reactor.run()


if __name__ == '__main__':
    main()
