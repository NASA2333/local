import xlrd
from xml.dom import minidom,Node
import codecs

data = xlrd.open_workbook(r"D:\PDRI_Audio&Video_Template_V1.0.xls")
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
xpath =r"D:\PDRI_Audio&Video_Template_V1.01.xml"


##   读取Excel文档
def start():
    for i in range(1,rows):
        table1 =table.row_values(i)
        global  table1
        create_xml(xpath)
    f= codecs.open(xpath,'a','utf-8-sig')
    f.write(doc.toprettyxml())
    f.close()

####  创建xml
def create_xml(xpath):

    # doc = minidom.Document()
    audio = doc.createElement('audio')
    pdris.appendChild(audio)

    isbn = doc.createElement('isbn ')
    isbn.setAttribute("desc","*标识符")
    # isbn.appendChild(doc.createTextNode("ISRC CN-C18-90-91-6"))
    isbn.appendChild(doc.createTextNode(table1[0]))
    audio.appendChild(isbn)

    worksName = doc.createElement('worksName')
    worksName.setAttribute('desc','*作品名称')
    worksName.appendChild(doc.createTextNode(table1[1]))
    audio.appendChild(worksName)

    worksNameEn = doc.createElement('worksNameEn')
    worksNameEn.setAttribute('desc','外文名')
    worksNameEn.appendChild(doc.createTextNode(table1[2]))
    audio.appendChild(worksNameEn)

    producer = doc.createElement('producer')
    producer.setAttribute('desc','创作者及责任方式')
    producer.appendChild(doc.createTextNode(table1[3]))
    audio.appendChild(producer)

    # responsibilityWay = doc.createElement('responsibilityWay')
    # responsibilityWay.setAttribute('desc','创作者责任方式')
    # responsibilityWay.appendChild(doc.createTextNode(table1[4]))
    # audio.appendChild(responsibilityWay)

    title = doc.createElement('title')
    title.setAttribute('desc','*主题')
    title.appendChild(doc.createTextNode(table1[4]))
    audio.appendChild(title)

    description = doc.createElement('description')
    description.setAttribute('desc','*描述')
    description.appendChild(doc.createTextNode(table1[5]))
    audio.appendChild(description)

    pdriPublisher = doc.createElement('pdriPublisher')
    pdriPublisher.setAttribute('desc','*出版者')
    pdriPublisher.appendChild(doc.createTextNode(table1[6]))
    audio.appendChild(pdriPublisher)

    otherPdriIsbn = doc.createElement('otherPdriIsbn')
    otherPdriIsbn.setAttribute('desc','其他责任者及责任方式')
    otherPdriIsbn.appendChild(doc.createTextNode(table1[7]))
    audio.appendChild(otherPdriIsbn)

    # otherResponsibilityWay = doc.createElement('otherResponsibilityWay')
    # otherResponsibilityWay.setAttribute('desc','其他责任者责任方式')
    # otherResponsibilityWay.appendChild(doc.createTextNode(table1[9]))
    # audio.appendChild(otherResponsibilityWay)

    releaseDatetime = doc.createElement('releaseDatetime')
    releaseDatetime.setAttribute('desc','发行日期')
    releaseDatetime.appendChild(doc.createTextNode(table1[8]))
    audio.appendChild(releaseDatetime)

    resourceType = doc.createElement('resourceType')
    resourceType.setAttribute('desc','*资源类型')
    resourceType.appendChild(doc.createTextNode(table1[9]))
    audio.appendChild(resourceType)

    eType = doc.createElement('eType')
    eType.setAttribute('desc','格式')
    eType.appendChild(doc.createTextNode(table1[10]))
    audio.appendChild(eType)

    productLink = doc.createElement('productLink')
    productLink.setAttribute('desc','关联产品及解析地址')
    productLink.appendChild(doc.createTextNode(table1[11]))
    audio.appendChild(productLink)

    # resolutionUrlProductLink = doc.createElement('resolutionUrlProductLink')
    # resolutionUrlProductLink.setAttribute('desc','关联产品解析地址')
    # resolutionUrlProductLink.appendChild(doc.createTextNode(table1[14]))
    # audio.appendChild(resolutionUrlProductLink)

    eSource = doc.createElement('eSource')
    eSource.setAttribute('desc','*来源')
    eSource.appendChild(doc.createTextNode(table1[12]))
    audio.appendChild(eSource)

    langCode = doc.createElement('langCode')
    langCode.setAttribute('desc','*语种')
    langCode.appendChild(doc.createTextNode(table1[13]))
    audio.appendChild(langCode)

    scopeTimeSpace = doc.createElement('scopeTimeSpace')
    scopeTimeSpace.setAttribute('desc','时空范围')
    scopeTimeSpace.appendChild(doc.createTextNode(table1[14]))
    audio.appendChild(scopeTimeSpace)

    ePrivilege = doc.createElement('ePrivilege')
    ePrivilege.setAttribute('desc','权限')
    ePrivilege.appendChild(doc.createTextNode(table1[15]))
    audio.appendChild(ePrivilege)

    version = doc.createElement('version')
    version.setAttribute('desc','版本')
    version.appendChild(doc.createTextNode(table1[16]))
    audio.appendChild(version)

    audience = doc.createElement('audience')
    audience.setAttribute('desc','受众')
    audience.appendChild(doc.createTextNode(table1[17]))
    audio.appendChild(audience)

    sourceCarrier = doc.createElement('sourceCarrier')
    sourceCarrier.setAttribute('desc','源载体')
    sourceCarrier.appendChild(doc.createTextNode(table1[18]))
    audio.appendChild(sourceCarrier)

    resolutionUrl = doc.createElement('resolutionUrl')
    resolutionUrl.setAttribute('desc','*解析地址')
    resolutionUrl.appendChild(doc.createTextNode(table1[19]))
    audio.appendChild(resolutionUrl)

    md5Val = doc.createElement('md5Val')
    md5Val.setAttribute('desc','*资源摘要值')
    md5Val.appendChild(doc.createTextNode(table1[20]))
    audio.appendChild(md5Val)




if __name__=="__main__":
    start()


