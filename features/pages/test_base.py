from applitools.common import MatchLevel
from selenium import webdriver
from features.browser import Browser
import time
from datetime import datetime
import os, re, os.path
from os import listdir
from fpdf import FPDF
import csv
from features.resources.test_config.my_config import APP_NAME

dirpath = os.getcwd()


class TestBase(Browser):
    # Login Page Actions

    def takesScreenshot(self):
        screenshotFile = datetime.now().strftime("%a-%b-%d-%Y-%H-%M-%S")
        screenShotPath = dirpath + r'/features/resources/screenshots/'
        self.driver.get_screenshot_as_file(screenShotPath + screenshotFile + r'.png')
        time.sleep(3)

    def cleanScreenShotFolder(self):
        screenShotPath = dirpath + r'/features/resources/screenshots/'
        for root, dirs, files in os.walk(screenShotPath):
            for file in files:
                os.remove(os.path.join(root, file))
        print('===== Screnshot folder cleared ====')

    def storeAllSceenshotsIntoPDFFile(self, senario_name):
        currenttime = datetime.now().strftime("%a-%b-%d-%Y-%H-%M-%S").replace("-", "_")
        pdf_filename = dirpath + r'/features/resources/screenshotDocs/' + senario_name + r'_' + currenttime + r'_' + r'.pdf'
        screenShotPath = dirpath + r'/features/resources/screenshots/'

        imagelist = listdir(screenShotPath)  # get list of all images
        pdf = FPDF('P', 'mm', 'A4')  # create an A4-size pdf document
        x, y, w, h = 15, 20, 180, 130

        for image in imagelist:
            pdf.add_page()
            imagePath = image
            pdf.image(screenShotPath + image, x, y, w, h)
            pdf.set_font("Arial", 'B', size=11)
            pdf.cell(50, 20, txt=imagePath, ln=1, align='C')
        pdf.output(pdf_filename, "F")

    def getCurrentDateTime(self):
        current_time = datetime.now().strftime("%Y/%m/%d %H:%M")
        return current_time

    def generateResultCSV(self, scenario, ctn, timstamp):
        result_path = dirpath + r'/features/resources/testResult/'
        timedate = timstamp.replace('/', '_').replace(' ', '_').replace(':', '_')
        csvpath = result_path + scenario + r'_Result(' + timedate + r').csv'
        with open(csvpath, mode='w', newline='') as result_file:
            result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result_writer.writerow(['scenario', 'ctn', 'searchdatetime'])
            result_writer.writerow([scenario, ctn, timstamp])

    def storeCurrentWindow(self):
        currentWindow = self.driver.current_window_handle
        return currentWindow

    def switchToNewWindow(self):
        allWindow = self.driver.window_handles
        for window in allWindow:
            # if (window != parentWindow):
            self.driver.switch_to_window(window)
            time.sleep(5)

    def switchBackToMainWindow(self, parentWindow):
        self.driver.switch_to_window(parentWindow)

    def closeCurrentBowserWindow(self):
        self.driver.close()

    def getCurrentSystemUser(self):
        currentUser = os.environ.get('USERNAME')
        return currentUser
