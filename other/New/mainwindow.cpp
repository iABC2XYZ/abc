#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    const int constWidth=800, constHeight=600;

    this->setMaximumSize(constWidth,constHeight);
    this->setMinimumSize(constWidth,constHeight);
    this->setWindowTitle("973加速器束流软件");


}

MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_tabO_tabBarClicked(int index)
{

}
