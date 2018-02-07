import xlrd,codecs
from xml.dom import minidom,Node

#####生成音视频单期注册数据


date = xlrd.open_workbook(r"D:\PDRI_IssueOfPeriodical_Template_V1.0.xls")
periodical1 = date.sheet_by_index(0)
issn = date.sheet_by_index(1)

xpath =r'D:\PDRI_IssueOfPeriodical_Template_V1.0.xml'

doc = minidom.Document()
pdris = doc.createElement('pdris')
doc.appendChild(pdris)
def start():
    for j in range(1,issn.nrows):
        issn1 = issn.row_values(j)
        global issn1
        create_xml_issn()
    for i in range(1,periodical1.nrows):
        periodical2 = periodical1.row_values(i)
        global periodical2
        create_xml_periodical()

        # money = issn1[18].split(',')
        # print(money)

    # f =open(r"F:\Excel\Issue.xml",'a')
    # f.write(doc.toprettyxml())
    # f.close()
    # txt = doc.toprettyxml()
    # print(txt)
    # txt = txt.endcode("utf-8")
    # f.write(txt)
    # f=codecs.open(r"F:\Excel\PDRI_IssueOfPeriodical_Template_V1.0.xml",'a','utf-8-sig')
    f= codecs.open(xpath,'w','utf-8-sig')
    f.write(doc.toprettyxml())
    f.close()
def create_xml_periodical():
    # issue = doc.createElement('issue')
    # pdris.appendChild(issue)

    periodical=doc.createElement('periodical')
    pdris.appendChild(periodical)

    periodicalCount = doc.createElement('periodicalCount')
    periodicalCount.setAttribute('desc','*期数')
    periodicalCount.appendChild(doc.createTextNode(periodical2[0]))
    periodical.appendChild(periodicalCount)

    periodicalColumnNo = doc.createElement('periodicalColumnNo')
    periodicalColumnNo.setAttribute('desc','*卷号')
    periodicalColumnNo.appendChild(doc.createTextNode(periodical2[1]))
    periodical.appendChild(periodicalColumnNo)

    releaseDatetime = doc.createElement('releaseDatetime')
    releaseDatetime.setAttribute('desc','*发行日期')
    releaseDatetime.appendChild(doc.createTextNode(periodical2[2]))
    periodical.appendChild(releaseDatetime)

    planColumn = doc.createElement('planColumn')
    planColumn.setAttribute('desc','计划栏目')
    planColumn.appendChild(doc.createTextNode(periodical2[3]))
    periodical.appendChild(planColumn)

    location = doc.createElement('location')
    location.setAttribute('desc','解析地址')
    location.appendChild(doc.createTextNode(periodical2[4]))
    periodical.appendChild(location)

    md5Val = doc.createElement('md5Val')
    md5Val.setAttribute('desc','*资源摘要值')
    md5Val.appendChild(doc.createTextNode(periodical2[5]))
    periodical.appendChild(md5Val)

    issnNo = doc.createElement('issnNo')
    issnNo.setAttribute('desc','*ISSN')
    issnNo.appendChild(doc.createTextNode(periodical2[6]))
    periodical.appendChild(issnNo)
def create_xml_issn():
    issue = doc.createElement('issue')
    pdris.appendChild(issue)

    issnNo = doc.createElement('issnNo')
    issnNo.setAttribute('desc','*ISSN')
    issnNo.appendChild(doc.createTextNode(str(issn1[0])))
    issue.appendChild(issnNo)

    cnNo = doc.createElement('cnNo')
    cnNo.setAttribute('desc','*CN')
    cnNo.appendChild(doc.createTextNode(issn1[1]))
    issue.appendChild(cnNo)

    pdriTitle = doc.createElement('pdriTitle')
    pdriTitle.setAttribute('desc','*期刊名称')
    pdriTitle.appendChild(doc.createTextNode(issn1[2]))
    issue.appendChild(pdriTitle)

    hostUnit = doc.createElement('hostUnit')
    hostUnit.setAttribute('desc','*主办单位')
    hostUnit.appendChild(doc.createTextNode(issn1[3]))
    issue.appendChild(hostUnit)

    supervisorUnit = doc.createElement('supervisorUnit')
    supervisorUnit.setAttribute('desc','*主管单位')
    supervisorUnit.appendChild(doc.createTextNode(issn1[4]))
    issue.appendChild(supervisorUnit)

    pdriPublisher = doc.createElement('pdriPublisher')
    pdriPublisher.setAttribute('desc','*出版单位')
    pdriPublisher.appendChild(doc.createTextNode(issn1[5]))
    issue.appendChild(pdriPublisher)

    publishAddress = doc.createElement('publishAddress')
    publishAddress.setAttribute('desc','*出版地')
    publishAddress.appendChild(doc.createTextNode(issn1[6]))
    issue.appendChild(publishAddress)

    periodical = doc.createElement('periodical')
    periodical.setAttribute('desc','*刊期')
    periodical.appendChild(doc.createTextNode(issn1[7]))
    issue.appendChild(periodical)

    size = doc.createElement('size')
    size.setAttribute('desc','尺寸')
    size.appendChild(doc.createTextNode(issn1[8]))
    issue.appendChild(size)

    publicationSDatetime = doc.createElement('publicationSDatetime')
    publicationSDatetime.setAttribute('desc','*创刊年')
    publicationSDatetime.appendChild(doc.createTextNode(issn1[9]))
    issue.appendChild(publicationSDatetime)

    publicationEDatetime = doc.createElement('publicationEDatetime')
    publicationEDatetime.setAttribute('desc','停刊年')
    publicationEDatetime.appendChild(doc.createTextNode(issn1[10]))
    issue.appendChild(publicationEDatetime)

    publicationType = doc.createElement('publicationType')
    publicationType.setAttribute('desc','出版物类型')
    publicationType.appendChild(doc.createTextNode(issn1[11]))
    issue.appendChild(publicationType)

    classification = doc.createElement('classification')
    classification.setAttribute('desc','*分类号')
    classification.appendChild(doc.createTextNode(issn1[12]))
    issue.appendChild(classification)

    keywordCn = doc.createElement('keywordCn')
    keywordCn.setAttribute('desc','*关键字（中文）')
    keywordCn.appendChild(doc.createTextNode(issn1[13]))
    issue.appendChild(keywordCn)

    keywordEn = doc.createElement('keywordEn')
    keywordEn.setAttribute('desc','关键字（英文）')
    keywordEn.appendChild(doc.createTextNode(issn1[14]))
    issue.appendChild(keywordEn)

    subject = doc.createElement('subject')
    subject.setAttribute('desc','学科')
    subject.appendChild(doc.createTextNode(issn1[15]))
    issue.appendChild(subject)

    researchField = doc.createElement('researchField')
    researchField.setAttribute('desc','研究领域')
    researchField.appendChild(doc.createTextNode(issn1[16]))
    issue.appendChild(researchField)

    postalNumber = doc.createElement('postalNumber')
    postalNumber.setAttribute('desc','邮发代号')
    postalNumber.appendChild(doc.createTextNode(issn1[17]))
    issue.appendChild(postalNumber)

    periodicalPrice = doc.createElement('periodicalPrice')
    periodicalPrice.setAttribute('desc','定价')
    issue.appendChild(periodicalPrice)

    money = issn1[18].split(',')

    label = doc.createElement('label')
    label.setAttribute('desc','钱币符号')
    label.appendChild(doc.createTextNode(str(money[0])))
    periodicalPrice.appendChild(label)

    price = doc.createElement('price')
    price.setAttribute('desc','价格')
    price.appendChild(doc.createTextNode(str(money[1])))
    periodicalPrice.appendChild(price)



if __name__=="__main__":
    start()