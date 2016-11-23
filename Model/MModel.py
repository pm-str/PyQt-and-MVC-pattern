from datetime import datetime
from urllib.request import urlopen
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractListModel
import random


class Schedule:
    def __init__(self, type, table_number, capacity, dt, issms, phone, order_number):
        self.type = str(type)
        self.table_number = str(table_number)
        self.capacity = str(capacity)
        self.dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')
        self.issms = str(issms)
        self.phone = str(phone)
        self.order_number = str(order_number)


class InfoTable:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity


class Model(QAbstractListModel):
    def __init__(self, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self._details = []

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._details)

    def data(self, QModelIndex, int_role=None):
        if int_role == QtCore.Qt.DisplayRole:
            row = QModelIndex.row()
            value = self._details[row]

            return value

    def insertRows(self, p_int=0, p_int_1=0, QModelIndex_parent=QtCore.QModelIndex(), *args, **kwargs):
        self.beginInsertRows(QModelIndex_parent, p_int, p_int + p_int_1 - 1)
        self._details.append("№{}\n{}\n\n".format(len(self._details)+1, kwargs['text']))
        self.endInsertRows()

        return True

    def to_book(self, type, capacity, dt, issms, phone):
        def send_sms(phone, order_number):
            # you have to get your api address on this site or one another
            line = 'http://sms.ru/sms/send?api_id=12345678-D15A-7057-1F15-1234567nm96BD&to={}&text=your+order+-+{}'
            http = line.format(phone.replace('+', '').replace('-', ''), order_number)
            with urlopen(http) as r:
                pass
            print(http)

        def apply_changes(orders):
            with open('schedule.db', 'w') as fin:
                output = ''
                for i in orders:
                    output += ' / '.join([
                        i.type,
                        i.table_number,
                        i.capacity,
                        i.dt.isoformat(sep=' ')[:16],
                        i.issms,
                        i.phone,
                        i.order_number
                    ]
                    ) + '\n'
                fin.write(output)

        def get_info_tables():
            tables = []
            with open('infoTables.db') as fin:
                for i in fin:
                    if not i.startswith('#') and i.strip():
                        tables.append(InfoTable(*i.split(' / ')))
            return tables

        def get_schedule():
            orders = []
            with open('schedule.db') as fin:
                for i in fin:
                    if not i.startswith('#') and i.strip():
                        orders.append(Schedule(*i.split(' / ')))
            return orders

        # getting info from database about later ordered tables
        info_tables = get_info_tables()
        orders = get_schedule()
        order_number = str(random.random())[2:]
        if type == 1:
            if len(list(filter(lambda x: x.dt.date() == dt.date(), orders))):
                self.insertRows(text='На это число заказ не доступен.')
                return
            else:
                table_number = 0
                dt = dt.toString('yyyy-MM-dd hh:mm')
                orders.append(Schedule(type, table_number, capacity, dt, issms, phone, order_number))
                self.insertRows(text='Номер заказа - ' + order_number)

        if type == 2:
            current = list(filter(lambda x: x.dt.date() == dt.date(), orders))
            for i in current:
                if i.type == '1':
                    self.insertRows(text='На это число заказ не доступен.')
                    return

            for i in current:
                for j in range(len(info_tables)):
                    if i.table_number == info_tables[j].table_number:
                        del[info_tables[j]]
                        break

            if not len(info_tables):
                self.insertRows(text='На это число нет свободных мест.')
                return

            convenient = list(filter(lambda x: int(x.capacity) >= int(capacity), info_tables))
            if not len(convenient):
                self.insertRows(text='Столы на данное количество персон отстутствуют.')
                return

            table_number = convenient[0].table_number
            dt = dt.toString('yyyy-MM-dd hh:mm')
            orders.append(Schedule(type, table_number, capacity, dt, issms, phone, order_number))
            self.insertRows(text='Заказ на {} человек(а)\nНомер стола - {}\nНомер заказа - {}'.format(
                capacity, table_number, order_number
            ))

        apply_changes(orders)
        if issms:
            send_sms(phone, order_number)

