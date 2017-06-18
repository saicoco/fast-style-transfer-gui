# coding=utf-8
__author__ = 'JiaGeng'
from neural_windows.ui import Ui_MainWindow
from PyQt4.QtCore import  *
from PyQt4.QtGui import *
import sys, os
from mx_transfer.segement import segement
from mx_transfer.style import ffwd
from skimage import io
from mx_transfer import make_image
import gc

class neural_style_transfer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(neural_style_transfer, self).__init__(parent)
        self.setupUi(self)
        QObject.connect(self.shanshui, SIGNAL("clicked()"), self.fshanshui)
        QObject.connect(self.youhua, SIGNAL("clicked()"), self.fyouhua)
        QObject.connect(self.shuimohua, SIGNAL("clicked()"), self.fshuimohua)
        QObject.connect(self.contentButton, SIGNAL("clicked()"), self.show_contDialog)
        QObject.connect(self.runButton, SIGNAL("clicked()"), self.transfer)
        QObject.connect(self.resetButton, SIGNAL("clicked()"), self.reset)
        QObject.connect(self.localButton, SIGNAL("clicked()"), self.local_style)
        QObject.connect(self.waveButton, SIGNAL("clicked()"), self.wave)
        QObject.connect(self.museButton, SIGNAL("clicked()"), self.muse)

        QObject.connect(self.grilButton, SIGNAL("clicked()"), self.gril)
        QObject.connect(self.headButton, SIGNAL("clicked()"), self.head)
        QObject.connect(self.gril2Button, SIGNAL("clicked()"), self.gril2)
        QObject.connect(self.sailButton, SIGNAL("clicked()"), self.sail)
        QObject.connect(self.sumiaoButton, SIGNAL("clicked()"), self.sumiao)

        self.ckpt = ""
        self.style_weight = 0.
        self.content_weight = 1e-3
        self.content_img = None
        self.out_path = './out'
        self.outputs = []
        self.mask = None
        self.style_img = None
        self.basepath = 'mx_transfer/ckpt/'
        self.content_size = None

    def reset(self):
        self.content_label.setPixmap(QPixmap(self.content_img))

    def local_style(self):
        self.mask = segement(self.content_img)
        print "segement complete"

    def fshanshui(self):
        self.ckpt = "".join([self.basepath, 'rain_princess/rain_princess'])
        self.style_img = "".join([self.basepath, 'rain_princess/rain_princess.jpg'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def fyouhua(self):
        self.ckpt = "".join([self.basepath, 'the_scream/the_scream'])
        self.style_img = "".join([self.basepath, 'the_scream/the_scream.jpg'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def fshuimohua(self):
        self.ckpt = "".join([self.basepath, 'xiangrikui/xiangrikui'])
        self.style_img = "".join([self.basepath, 'xiangrikui/xiangrikui.png'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def wave(self):
        self.ckpt = "".join([self.basepath, 'wave/wave'])
        self.style_img = "".join([self.basepath, 'wave/wave.jpg'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def muse(self):
        self.ckpt = "".join([self.basepath, 'la_muse/la_muse'])
        self.style_img = "".join([self.basepath, 'la_muse/la_muse.jpg'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def gril(self):
        self.ckpt = "".join([self.basepath, 'gril/gril'])
        self.style_img = "".join([self.basepath, 'gril/gril.png'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def head(self):
        self.ckpt = "".join([self.basepath, 'head/head'])
        self.style_img = "".join([self.basepath, 'head/head.jpg'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def sumiao(self):
        self.ckpt = "".join([self.basepath, 'sumiao/sumiao'])
        self.style_img = "".join([self.basepath, 'sumiao/sumiao.png'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def sail(self):
        self.ckpt = "".join([self.basepath, 'sail/sail'])
        self.style_img = "".join([self.basepath, 'sail/sail.jpg'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def gril2(self):
        self.ckpt = "".join([self.basepath, 'gril2/gril2'])
        self.style_img = "".join([self.basepath, 'gril2/gril2.png'])
        self.style_label.setPixmap(QPixmap(self.style_img))

    def show_contDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'open file', './')
        assert filename.split('.')[-1] in ['jpg', 'png']
        self.content_img = str(filename)
        self.content_label.setPixmap(QPixmap(filename))

    # def init_maker(self):
    #     maker = make_image.Maker(self.ckpt, self.content_size)
    #     return maker

    def transfer(self):
        if not os.path.isdir(self.out_path):
            os.mkdir(self.out_path)
        # device = '/cpu:0'
        out_path = self.out_path + '/out' + self.content_img.split('/')[-1]
        content_img = io.imread(self.content_img)
        content_size = content_img.shape[:2]
        ckpt = self.ckpt
        def init_maker():
            maker = make_image.Maker(ckpt, content_size)
            outputs = ffwd(maker=maker, content=self.content_img, outpath=out_path, mask=self.mask)
            del maker
            return outputs
        outputs = init_maker()
        # outputs = ffwd(maker=maker, content=self.content_img, outpath=out_path, mask=self.mask)
        # self.outputs = ffwd_to_img(self.content_img, out_path, self.ckpt, device=device, mask=self.mask)
        self.content_label.setPixmap(QPixmap(out_path))
        del outputs
        del content_img
        gc.collect()

if __name__=='__main__':
    app = QApplication(sys.argv)
    neural_st = neural_style_transfer()
    neural_st.show()
    app.exec_()
    # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());