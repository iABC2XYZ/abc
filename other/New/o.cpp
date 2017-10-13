#include "o.h"

O::O()
{
    const int constWidth=800, constHeight=600;
    QTabWidget *tabO=new QTabWidget;
    tabO->setMaximumSize(constWidth/2,constHeight/2);
    tabO->setMinimumSize(constWidth/2,constHeight/2);
    //tabO->show();

}
