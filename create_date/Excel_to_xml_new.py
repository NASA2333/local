import xlrd
from xml.dom import minidom,Node

# data = xlrd.open_workbook(r"F:\Exct\PDRI_Newspaper_Template_V1.0.xls")
data = xlrd.open_workbook(r"F:\Exct\book2.xls")
table = data.sheet_by_index(0)
'''
rows = table.nrows          #行数
cols = table.ncols          #列
table1 = table.row_values(2)

# for i in table1:
#     print(i)
# print(table1)
# print(rows,cols)
'''


rows = table.nrows


doc = minidom.Document()
pdris = doc.createElement('pdris')
doc.appendChild(pdris)
xpath =r'F:\newspaper.xml'
# print(doc.toprettyxml())

##   读取Excel文档
def start():
    for i in range(1,rows):
        table1 =table.row_values(i)
        # print(table1[1])
        global  table1
        create_xml(xpath)
    f= open(xpath,'a')
    f.write(doc.toprettyxml())
    f.close()

####  创建xml
def create_xml(xpath):

    # doc = minidom.Document()
    newspaper= doc.createElement('newspaper')
    pdris.appendChild(newspaper)

    cn = doc.createElement('cn ')
    cn.setAttribute("desc","*cn")
    # isbn.appendChild(doc.createTextNode("ISRC CN-C18-90-91-6"))
    cn.appendChild(doc.createTextNode(table1[0]))
    newspaper.appendChild(cn)

    periodicalSerialNo = doc.createElement('periodicalSerialNo')
    periodicalSerialNo.setAttribute('desc','*期数 ')
    periodicalSerialNo.appendChild(doc.createTextNode(table1[1]))
    newspaper.appendChild(periodicalSerialNo)

    editionNumber = doc.createElement('editionNumber')
    editionNumber.setAttribute('desc','*报纸板数')
    editionNumber.appendChild(doc.createTextNode(table1[2]))
    newspaper.appendChild(editionNumber)
	
    pdriPublisher = doc.createElement('pdriPublisher')
    pdriPublisher.setAttribute('desc','*发行日期')
    pdriPublisher.appendChild(doc.createTextNode(table1[3]))
    newspaper.appendChild(pdriPublisher)

    newspaperName = doc.createElement('newspaperName')
    newspaperName.setAttribute('desc','*报纸名称')
    newspaperName.appendChild(doc.createTextNode(table1[4]))
    newspaper.appendChild(newspaperName)

    newspaperType = doc.createElement('newspaperType')
    newspaperType.setAttribute('desc','*报纸类别')
    newspaperType.appendChild(doc.createTextNode(table1[5]))
    newspaper.appendChild(newspaperType)

    publicationSDatetime = doc.createElement('publicationSDatetime')
    publicationSDatetime.setAttribute('desc','*创报年份')
    publicationSDatetime.appendChild(doc.createTextNode((table1[6])))
    newspaper.appendChild(publicationSDatetime)

    releaseArea = doc.createElement('releaseArea')
    releaseArea.setAttribute('desc','*发行范围')
    releaseArea.appendChild(doc.createTextNode(table1[7]))
    newspaper.appendChild(releaseArea)

    periodical = doc.createElement('periodical')
    periodical.setAttribute('desc','*刊期')
    periodical.appendChild(doc.createTextNode(table1[8]))
    newspaper.appendChild(periodical)

    domesticDistributor = doc.createElement('domesticDistributor')
    domesticDistributor.setAttribute('desc','*语种')
    domesticDistributor.appendChild(doc.createTextNode(table1[9]))
    newspaper.appendChild(domesticDistributor)

    pdriPublisher = doc.createElement('pdriPublisher')
    pdriPublisher.setAttribute('desc','*出版者')
    pdriPublisher.appendChild(doc.createTextNode(table1[10]))
    newspaper.appendChild(pdriPublisher)

    publishAddress = doc.createElement('publishAddress')
    publishAddress.setAttribute('desc','*出版地')
    publishAddress.appendChild(doc.createTextNode(table1[11]))
    newspaper.appendChild(publishAddress)

    hostUnit = doc.createElement('hostUnit')
    hostUnit.setAttribute('desc','*主办单位')
    hostUnit.appendChild(doc.createTextNode(table1[12]))
    newspaper.appendChild(hostUnit)

	
	
    supervisorUnit = doc.createElement('supervisorUnit')
    supervisorUnit.setAttribute('desc','*主管单位')
    supervisorUnit.appendChild(doc.createTextNode(table1[13]))
    newspaper.appendChild(supervisorUnit)

    keyword = doc.createElement('keyword')
    keyword.setAttribute('desc','关键词')
    keyword.appendChild(doc.createTextNode(table1[14]))
    newspaper.appendChild(keyword)

    color = doc.createElement('color')
    color.setAttribute('desc','印色')
    color.appendChild(doc.createTextNode(table1[15]))
    newspaper.appendChild(color)

    domesticDistributor = doc.createElement('domesticDistributor')
    domesticDistributor.setAttribute('desc','*国内发行单位')
    domesticDistributor.appendChild(doc.createTextNode(table1[16]))
    newspaper.appendChild(domesticDistributor)

    domPostalNumber = doc.createElement('domPostalNumber')
    domPostalNumber.setAttribute('desc','*国内邮发代号')
    domPostalNumber.appendChild(doc.createTextNode(table1[17]))
    newspaper.appendChild(domPostalNumber)

    overseasDistributor = doc.createElement('overseasDistributor')
    overseasDistributor.setAttribute('desc','国外发行单位')
    overseasDistributor.appendChild(doc.createTextNode(table1[18]))
    newspaper.appendChild(overseasDistributor)

    forPostalNumber = doc.createElement('forPostalNumber')
    forPostalNumber.setAttribute('desc','国外邮发代号')
    forPostalNumber.appendChild(doc.createTextNode(table1[19]))
    newspaper.appendChild(forPostalNumber)

	
	
	
	
    price = doc.createElement('price')
    price.setAttribute('desc','定价')
    # price.appendChild(doc.createTextNode(table1[20]))
    newspaper.appendChild(price)

    money=table1[20].split(',')
    # print(list(m))
    label = doc.createElement('label')
    label.setAttribute('desc','货币符号')
    label.appendChild(doc.createTextNode(money[0]))
    price.appendChild(label)

    price.price = doc.createElement('price')
    price.price.setAttribute('desc','价格')
    price.price.appendChild(doc.createTextNode(money[1]))
    price.appendChild(price.price)


	
	
	
    

    resolutionUrl = doc.createElement('resolutionUrl')
    resolutionUrl.setAttribute('desc','*解析地址')
    resolutionUrl.appendChild(doc.createTextNode(table1[21]))
    newspaper.appendChild(resolutionUrl)

    md5Val = doc.createElement('md5Val')
    md5Val.setAttribute('desc','*资源摘要值')
    md5Val.appendChild(doc.createTextNode(table1[22]))
    newspaper.appendChild(md5Val)




if __name__=="__main__":
    start()


