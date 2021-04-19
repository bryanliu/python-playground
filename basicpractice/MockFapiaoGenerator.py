import json
import random
import re
import time
import unittest
from json import JSONEncoder

import xlrd


class Fapiao():
    def __init__(self):
        self.invoiceCode = ''
        self.invoiceNumber = ''
        self.issueDate = ''
        self.checkCode = ''
        self.buyerAddrPhone = ''
        self.buyerBankAccount = ''
        self.buyerName = ''
        self.buyerTaxNumber = ''
        self.region = ''
        self.machineNumber = ''
        self.totalExTax = 100
        self.totalTax = 0
        self.totalInTax = 0
        self.supplierAddrPhone = ''
        self.supplierBankAccount = ''
        self.supplierName = ''
        self.supplierTaxNumber = ''
        self.note = ''
        self.itemList = []


class Fapiao_line():
    def __init__(self):
        self.name = ''
        self.model = ''
        self.unit = ''
        self.quantity = 1
        self.unitPrice = 1
        self.priceAmount = 1
        self.taxRate = 0.03
        self.taxAmount = 3


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


buyertaxNoMapping = {
    880: ['斯道拉恩索（广西）浆纸有限公司', '91450500090707025M'],
    881: ['斯道拉恩索（广西）林业有限公司', '914505000907070683'],
    885: ['广西斯道拉恩索林业有限公司', '91450500742060977F'],

}

sellertaxNoMapping = {
    '合浦县华赢超市设备经营部': '92450521MA5KY2U22J',
    '北海庞赛贸易有限公司': '914505006670409249',
    '中智广西人力资源服务有限公司': '91450000MA5NGWJA41'
}
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

normal_fapiao_code = '1234109121'
special_fapiao_code = '1234109321'


def generate_invoice_no():
    return "".join(map(str, random.sample(list, 8)))


def fapiao_type(note):
    if note.find("专票") >= 0:
        return "special"
    else:
        return "normal"


class MockFapiao:

    def __init__(self):
        # self.fapiaos = []
        pass

    def read_xml(self, name):
        xlsx = xlrd.open_workbook(name)
        table = xlsx.sheet_by_index(0)
        data = []
        print(table.nrows)
        for i in range(1, table.nrows):
            print(i)
            print(table.row_values(i))
            print(table.cell_value(i, 6))
            # self.generate_fapiao(table.row_values(i))
            data.append(table.row_values(i))
        return data

    def get_additional_in(self, additional, row_no):
        '''
        解析additional 中的 IN 节点的数据, 解析出来的节点数和 row_no一致，如果节点不够，用最后一个节点补齐。
        :param additional:
        :param row_no:
        :return:
        '''
        nodes = []
        nodestr = re.findall(r".*IN:(.*)$", additional, re.S)
        if not nodestr: return nodes
        nodes = nodestr[0].split()
        for i in range(len(nodes)):
            nodes[i] = re.sub(r"\D", "", nodes[i])
        if len(nodes) >= row_no:
            return nodes[:row_no]
        else:
            last_one = nodes[-1]
            for _ in range(row_no - len(nodes)):
                nodes.append(last_one)
            return nodes

    def generate_fapiao(self, row):
        if not row: return
        note = row[8]
        additional = row[7]
        fapiaos = []
        lines = self.parse_note(note)
        nodes = self.get_additional_in(additional, len(lines))
        # 每行都生成一张发票，也就是每张发票都是一行
        for i, line in enumerate(lines):
            f = Fapiao()
            f.supplierName = row[6]
            f.invoiceCode = special_fapiao_code if fapiao_type(note) == "special" else normal_fapiao_code
            f.invoiceNumber = generate_invoice_no()
            f.issueDate = time.strftime("%Y-%m-%d")
            f.checkCode = '12345678901234567890'
            f.supplierTaxNumber = sellertaxNoMapping[row[6]]
            f.note = row[8] + " IN:" + nodes[i]
            f.buyerName = buyertaxNoMapping[int(row[3])][0]
            f.buyerTaxNumber = buyertaxNoMapping[int(row[3])][1]
            f.itemList.append(line)
            f.totalExTax = line.priceAmount
            f.totalTax = line.taxAmount
            f.totalInTax = line.taxAmount + line.priceAmount
            # print(f.supplierName)
            fapiaos.append(f)
        return fapiaos

    def parse_note(self, note):
        '''
        根据 NOTE 解析出有几个发票Line
        :param note:
        :return: List Fapiao_line
        '''
        if not note: return []
        linelist = []
        if re.match(r'.*不含税金额.*', note):
            amoutlist = re.findall(r'\D*(\d+?)元', note)
            taxlist = re.findall(r'.*税率(\d+)%', note)
            taxrate = 0.06 if not taxlist else int(taxlist[0]) / 100
            for amount in amoutlist:
                amount = int(amount)
                line = Fapiao_line()
                line.name = "测试"
                line.priceAmount = amount
                line.taxRate = taxrate
                line.taxAmount = amount * taxrate
                line.unitPrice = amount
                line.quantity = 1
                linelist.append(line)
        elif re.match(r".*普票.*", note):
            # normal invoide
            amoutlist = re.findall(r'\D*(\d+?)元', note)
            taxlist = re.findall(r'.*税率(\d+)%', note)
            taxrate = 0.06 if not taxlist else int(taxlist[0]) / 100
            for amountwithtax in amoutlist:
                amountwithtax = int(amountwithtax)
                line = Fapiao_line()
                withouttax = amountwithtax / (1 + taxrate)
                line.priceAmount = withouttax
                line.name = "测试"
                line.taxRate = taxrate
                line.taxAmount = amountwithtax - withouttax
                line.unitPrice = withouttax
                line.quantity = 1
                linelist.append(line)

        return linelist

    def get_mock_fapiao(self, filename):
        # f = Fapiao()
        # l1 = Fapiao_line()
        # f.itemList.append(l1)
        # #正常类无法直接JSON 序列化，自定义一个Encoder，返回o.__dict__
        # print(json.dumps(f, cls=Encoder))
        # print(Encoder().encode(l1))
        # print(Encoder().encode(f))
        allrows = self.read_xml(filename)
        fapiaos = []
        for onerow in allrows:
            fapiaos += self.generate_fapiao(onerow)
        for f in fapiaos:
            print(json.dumps(f, cls=Encoder, ensure_ascii=False))
        print(f"total generated {len(fapiaos)} fapiaos")


class UT(unittest.TestCase):

    def setUp(self) -> None:
        self.f = MockFapiao()

    def test_parse_special_line_empty(self):
        res = self.f.parse_note("")
        self.assertEqual(0, len(res))

    def test_parse_special_line_one_line_not_include_tax(self):
        res = self.f.parse_note("mock一张专票，不含税金额1000元，税率6%")
        self.assertEqual(1, len(res))
        line = res[0]
        self.assertEqual(1000, line.priceAmount)
        self.assertEqual(0.06, line.taxRate)
        self.assertEqual(60, line.taxAmount)
        self.assertEqual(1, line.quantity)
        self.assertEqual(1000, line.unitPrice)

    def test_parse_special_line_3_lines_not_include_tax(self):
        res = self.f.parse_note("mock三张专票，不含税金额分别为1000元，2000元和5000元，税率13%")
        self.assertEqual(3, len(res))
        line = res[0]
        self.assertEqual(1000, line.priceAmount)
        self.assertEqual(0.13, line.taxRate)
        self.assertEqual(130, line.taxAmount)
        self.assertEqual(1, line.quantity)
        self.assertEqual(1000, line.unitPrice)

        line2 = res[1]
        self.assertEqual(2000, line2.priceAmount)
        self.assertEqual(0.13, line2.taxRate)
        self.assertEqual(260, line2.taxAmount)
        self.assertEqual(1, line2.quantity)
        self.assertEqual(2000, line2.unitPrice)

        line3 = res[2]
        self.assertEqual(5000, line3.priceAmount)
        self.assertEqual(0.13, line3.taxRate)
        self.assertEqual(650, line3.taxAmount)
        self.assertEqual(1, line3.quantity)
        self.assertEqual(5000, line3.unitPrice)

    # @unittest.skip
    def test_parse_normal_oneline(self):
        lines = self.f.parse_note("mock一张普票，含税金额980元")
        self.assertEqual(1, len(lines))
        line1 = lines[0]

        self.assertEqual(924.5283018867924, line1.priceAmount)
        self.assertEqual(0.06, line1.taxRate)
        self.assertEqual(55.471698113207594, line1.taxAmount)
        self.assertEqual(1, line1.quantity)
        self.assertEqual(924.5283018867924, line1.unitPrice)

    def test_parse_normal_multiple_line(self):
        lines = self.f.parse_note("一个IN各mock一张普票，含税金额分别为100元和110元")
        self.assertEqual(2, len(lines))
        line1 = lines[0]
        self.assertEqual(94.33962264150944, line1.priceAmount)
        self.assertEqual(0.06, line1.taxRate)
        self.assertEqual(5.660377358490564, line1.taxAmount)
        self.assertEqual(1, line1.quantity)
        self.assertEqual(94.33962264150944, line1.unitPrice)
        line2 = lines[1]
        self.assertEqual(103.77358490566037, line2.priceAmount)
        self.assertEqual(0.06, line2.taxRate)
        self.assertEqual(6.226415094339629, line2.taxAmount)
        self.assertEqual(1, line2.quantity)
        self.assertEqual(103.77358490566037, line2.unitPrice)

    def test_gen_invoice_no(self):
        res = generate_invoice_no()
        print(f'generated invoice number {res}')
        self.assertIsNotNone(res)

    def test_get_additional(self):
        additional = """
        "PO: 4503291947
GR: 5034410407/5034410408
IN: 202100011264
     202100011265"
        """
        res = self.f.get_additional_in(additional, 2)
        self.assertEqual(2, len(res))
        self.assertEqual("202100011264", res[0])
        self.assertEqual("202100011265", res[1])

    def test_get_additional_one_add_two_row(self):
        additional = """
        "PO: 4503291947
GR: 5034410407/5034410408
IN: 202100011264"
        """
        res = self.f.get_additional_in(additional, 2)
        self.assertEqual(2, len(res))
        self.assertEqual("202100011264", res[0])
        self.assertEqual("202100011264", res[1])

    def test_get_additional_two_add_one_row(self):
        additional = """
        "PO: 4503291947
GR: 5034410407/5034410408
IN: 202100011264
     202100011265"
        """
        res = self.f.get_additional_in(additional, 1)
        self.assertEqual(1, len(res))
        self.assertEqual("202100011264", res[0])


if __name__ == "__main__":
    # MockFapiao().get_mock_fapiao()
    mockfapiao = MockFapiao()
    mockfapiao.get_mock_fapiao('/Users/admin/Downloads/mock 发票20210330_all.xls')
    #unittest.main()
