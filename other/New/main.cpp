#include "mainwindow.h"
#include "o.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    //O o;
    //o.show();

    return a.exec();
}
