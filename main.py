# Regression analysis
# Calculation of regression analysis and output of results in the graphical interface
import pandas as pd
import statsmodels.api as sm
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog

Form, Window = uic.loadUiType("regression.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_click_1():
    qf = QFileDialog()
    file = qf.getOpenFileName(None, "Open File", "/",
                              "Document(*.xlsx *.xls)")[0]
    form_1 = [i for i in str(file).split("/")]
    if form_1[-1].endswith(".xlsx") or form_1[-1].endswith(".xls"):
        form.label.setText(file)
        file_1 = str(file)
        global data
        data = pd.read_excel(file_1)
        regression = str(data.corr())
        print(data.corr())
        form.label_2.setText(regression)
        form.pushButton_2.clicked.connect(on_click_2)
    else:
        form.label.setText("Choose the right format")
        form.label_2.setText("")


def on_click_2():
    col = [i for i in form.lineEdit.text().split()]
    X = data[col]
    Y = data["Y"]
    X = sm.add_constant(X)
    reg = sm.OLS(Y, X)
    res = reg.fit()
    correlation = str(res.summary())
    form.label_3.setText(correlation)
    print(correlation)


form.pushButton.clicked.connect(on_click_1)
app.exec()
