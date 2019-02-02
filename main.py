# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import subprocess
import requests
import MySQLdb
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, -10, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.wordpress_input = QtWidgets.QLineEdit(self.centralwidget)
        self.wordpress_input.setGeometry(QtCore.QRect(50, 170, 321, 40))
        self.wordpress_input.setObjectName("wordpress_input")
        self.laravel_input = QtWidgets.QLineEdit(self.centralwidget)
        self.laravel_input.setGeometry(QtCore.QRect(50, 280, 321, 41))
        self.laravel_input.setObjectName("laravel_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 250, 66, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 81, 17))
        self.label_3.setObjectName("label_3")
        self.html_input = QtWidgets.QLineEdit(self.centralwidget)
        self.html_input.setGeometry(QtCore.QRect(50, 400, 321, 40))
        self.html_input.setText("")
        self.html_input.setObjectName("html_input")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 370, 91, 17))
        self.label_4.setObjectName("label_4")
        self.progress_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.progress_display.setGeometry(QtCore.QRect(410, 170, 341, 271))
        self.progress_display.setObjectName("progress_display")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 140, 66, 17))
        self.label_5.setObjectName("label_5")
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.setGeometry(QtCore.QRect(50, 480, 95, 27))
        self.go_button.setFlat(False)
        self.go_button.setObjectName("go_button")
        #self.show_folders_button = QtWidgets.QPushButton(self.centralwidget)
        #self.show_folders_button.setGeometry(QtCore.QRect(160, 480, 131, 27))
        #self.show_folders_button.setFlat(False)
        #self.show_folders_button.setObjectName("show_folders_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.go_button.clicked.connect(self.create_projects)
        #self.show_folders_button.clicked.connect(self.show_folders)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rz Project Creator"))
        self.label.setText(_translate("MainWindow", "Rz Project Creator"))
        self.wordpress_input.setPlaceholderText(_translate("MainWindow", "name"))
        self.laravel_input.setPlaceholderText(_translate("MainWindow", "name"))
        self.label_2.setText(_translate("MainWindow", "Laravel"))
        self.label_3.setText(_translate("MainWindow", "Wordpress"))
        self.html_input.setPlaceholderText(_translate("MainWindow", "name"))
        self.label_4.setText(_translate("MainWindow", "Html Css Js"))
        self.label_5.setText(_translate("MainWindow", "Progress"))
        self.go_button.setText(_translate("MainWindow", "Go"))
        #self.show_folders_button.setText(_translate("MainWindow", "Show folders"))


    # MY functions
    def create_projects(self):

        # default folders
        address_wordpress = "/var/www/html/projects-wp/"
        address_laravel = "/var/www/html/projects-laravel/"
        address_html = "/home/reza/Documents/design/foroosh/"

        # step 1 check inputs
        self.progress_display.append("=> Starting...")
        iswordpress = self.wordpress_input.text()
        islaravel = self.laravel_input.text()
        ishtml = self.html_input.text()
        if(iswordpress != ""):
            self.progress_display.append("=> You want wordpress project.")
        if(islaravel != ""):
            self.progress_display.append("=> You want laravel project.")
        if(ishtml != ""):
            self.progress_display.append("=> You want html project.")

        if(islaravel != iswordpress):

            if(iswordpress != ""):

                # download and save file
                self.progress_display.append("=> Downloading https://wordpress.org/latest.zip")
                app.processEvents()
                r = requests.get("https://wordpress.org/latest.zip", allow_redirects=True)
                app.processEvents()
                #if download failed
                #if(r.status_code == 200):
                #self.progress_display.append("=> Download failed. using local file instead")
                open(address_wordpress + iswordpress + ".zip", 'wb').write(r.content)

                # extract file
                self.progress_display.append("=> Extracting latest.zip")
                res = subprocess.check_output(["unzip", address_wordpress + iswordpress + ".zip", "-d", address_wordpress])
                #else:
                #    self.progress_display.append("=> Extracting latest.zip")
                #    res = subprocess.check_output(["unzip", "files/latest.zip", "-d", address_wordpress])

                # rename extracted folder
                self.progress_display.append("=> Renaming folder")
                res = subprocess.check_output(["mv", address_wordpress + "wordpress", address_wordpress + iswordpress])

                # mysql database
                self.progress_display.append("=> Creating mysql database for project")
                conn = MySQLdb.connect(host='localhost', user='root', passwd='1111')
                cursor = conn.cursor()
                cursor.execute('Create database ' + iswordpress + ' CHARACTER SET utf8 COLLATE utf8_general_ci;')

                # wordpress config file
                self.progress_display.append("=> Edit wordpress config file")
                with open(address_wordpress + iswordpress + '/wp-config-sample.php', 'r') as myfile:
                    data = myfile.read()
                myfile.close()
                data = data.replace("define('DB_NAME', 'database_name_here');", "define('DB_NAME', '" + iswordpress + "');")
                data = data.replace("define('DB_USER', 'username_here');", "define('DB_USER', 'root');")
                data = data.replace("define('DB_PASSWORD', 'password_here');", "define('DB_PASSWORD', '1111');")
                data = data.replace("define('DB_COLLATE', '');", "define('DB_COLLATE', '');\ndefine('FS_METHOD', 'direct');\ndefine( 'WP_AUTO_UPDATE_CORE', false );")
                file = open(address_wordpress + iswordpress + '/wp-config.php', 'w+')
                file.write(data)
                file.close()


                #for line in res.splitlines():
                #    self.progress_display.append(line)
                self.progress_display.append("=> Wordpress project created successfully :)")
                #time.sleep(5)
                #res = subprocess.check_output(["chromium-browser", "http://localhost/projects-wp/" + iswordpress])

            if(islaravel != ""):

                # start creating with composer
                self.progress_display.append("=> Composer create-project --prefer-dist laravel/laravel " + islaravel)
                #res = subprocess.check_output(["cd", "/var/www/html/projects-laravel"])
                app.processEvents()
                res = subprocess.check_output(["composer", "create-project", "--prefer-dist", "laravel/laravel", address_laravel + islaravel])
                app.processEvents()
                #for line in res.splitlines():
                #   self.progress_display.append(str(line))

                # mysql database
                self.progress_display.append("=> Creating mysql database for project")
                conn = MySQLdb.connect(host='localhost', user='root', passwd='1111')
                cursor = conn.cursor()
                cursor.execute('Create database ' + islaravel + ' CHARACTER SET utf8 COLLATE utf8_general_ci;')

                # laravel config file
                self.progress_display.append("=> Edit laravel config file")
                with open(address_laravel + islaravel + '/.env', 'r') as myfile:
                    data = myfile.read()
                myfile.close()
                data = data.replace("APP_URL=http://localhost", "APP_URL=http://localhost/projects-laravel/" + islaravel)
                data = data.replace("DB_DATABASE=homestead", "DB_DATABASE=" + islaravel)
                data = data.replace("DB_USERNAME=homestead", "DB_USERNAME=root")
                data = data.replace("DB_PASSWORD=secret", "DB_PASSWORD=1111")
                data = data.replace("APP_NAME=Laravel", "APP_NAME=" + islaravel)

                file = open(address_laravel + islaravel + '/.env', 'w')
                file.write(data)
                file.close()

                self.progress_display.append("=> Laravel project created successfully :)")
                #res = subprocess.check_output(["chromium-browser", "http://localhost/projects-laravel/" + islaravel + "/public"])

        else:
            self.progress_display.append("=> laravel and Wordpress project names should be different!")

            if(ishtml != ""):
                # extract file
                self.progress_display.append("=> Extracting html.zip to Documents/design/foroosh/" + ishtml)
                res = subprocess.check_output(["unzip", 'files/html.zip', "-d", address_html + ishtml])
                self.progress_display.append("=> Html project created successfully :)")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
