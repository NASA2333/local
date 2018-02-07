import xlrd,codecs
from xml.dom import minidom,Node

#打开Excel，并读取第一页表的值
data = xlrd.open_workbook(r'D:\PDRI_PieceofPeriodical_Template_V1.0.xls')
table = data.sheet_by_index(0)
#创建Xml
doc = minidom.Document()
pdris = doc.createElement('pdris')
doc.appendChild(pdris)

xpath = r"D:\PDRI_PieceofPeriodical_Template_V1.0.xml"

def start():
    for i in range(1,table.nrows):
        table1 = table.row_values(i)
        global table1
        create_xml()
    f= codecs.open(xpath,'a','utf-8-sig')
    f.write(doc.toprettyxml())
    f.close()

def create_xml():
    piece = doc.createElement('piece')
    pdris.appendChild(piece)

    periodicalPdriCode = doc.createElement('periodicalPdriCode ')
    periodicalPdriCode.setAttribute("desc","*单期PDRI")
    # periodicalPdriCode.appendChild(doc.createTextNode("ISRC CN-C18-90-91-6"))
    periodicalPdriCode.appendChild(doc.createTextNode(table1[0]))
    piece.appendChild(periodicalPdriCode)

    pieceSerialNo = doc.createElement('pieceSerialNo')
    pieceSerialNo.setAttribute('desc','*篇编号')
    pieceSerialNo.appendChild(doc.createTextNode(str(table1[1])))
    piece.appendChild(pieceSerialNo)

    doi = doc.createElement('doi')
    doi.setAttribute('desc','DOI')
    doi.appendChild(doc.createTextNode(table1[2]))
    piece.appendChild(doi)

    pdriTitle = doc.createElement('pdriTitle')
    pdriTitle.setAttribute('desc','*题名')
    pdriTitle.appendChild(doc.createTextNode(table1[3]))
    piece.appendChild(pdriTitle)

    pdriTitleEn = doc.createElement('pdriTitleEn')
    pdriTitleEn.setAttribute('desc','题名（英文）')
    pdriTitleEn.appendChild(doc.createTextNode(table1[4]))
    piece.appendChild(pdriTitleEn)

    author = doc.createElement('author')
    author.setAttribute('desc','*作者')
    author.appendChild(doc.createTextNode(table1[5]))
    piece.appendChild(author)
	
    date =table1[6].split(',')
	
    piecePages = doc.createElement('piecePages')
    piecePages.setAttribute('desc','*起止页码')
   # piecePages.appendChild(doc.createTextNode(table1[6]))
    piece.appendChild(piecePages)

    start = doc.createElement('start')
    start.setAttribute('desc','*开始页码')
    start.appendChild(doc.createTextNode(date[0]))
    piecePages.appendChild(start)

    end = doc.createElement('end')
    end.setAttribute('desc','*结束页码')
    end.appendChild(doc.createTextNode(date[1]))
    piecePages.appendChild(end)

    pieceDocumentCode = doc.createElement('pieceDocumentCode')
    pieceDocumentCode.setAttribute('desc','*文献标识码')
    pieceDocumentCode.appendChild(doc.createTextNode(table1[7]))
    piece.appendChild(pieceDocumentCode)

    pieceKeywordCn = doc.createElement('pieceKeywordCn')
    pieceKeywordCn.setAttribute('desc','*关键字')
    pieceKeywordCn.appendChild(doc.createTextNode(table1[8]))
    piece.appendChild(pieceKeywordCn)

    pieceKeywordEn = doc.createElement('pieceKeywordEn')
    pieceKeywordEn.setAttribute('desc','关键字（英文）')
    pieceKeywordEn.appendChild(doc.createTextNode(table1[9]))
    piece.appendChild(pieceKeywordEn)

    pieceSummaryCn = doc.createElement('pieceSummaryCn')
    pieceSummaryCn.setAttribute('desc','*摘要')
    pieceSummaryCn.appendChild(doc.createTextNode(table1[10]))
    piece.appendChild(pieceSummaryCn)

    pieceSummaryEn = doc.createElement('pieceSummaryEn')
    pieceSummaryEn.setAttribute('desc','摘要（英文）')
    pieceSummaryEn.appendChild(doc.createTextNode(table1[11]))
    piece.appendChild(pieceSummaryEn)

    researchDirection = doc.createElement('researchDirection')
    researchDirection.setAttribute('desc','研究方向')
    researchDirection.appendChild(doc.createTextNode(table1[12]))
    piece.appendChild(researchDirection)

    fundType = doc.createElement('fundType')
    fundType.setAttribute('desc','基金类别')
    fundType.appendChild(doc.createTextNode(table1[13]))
    piece.appendChild(fundType)

    pieceReferences = doc.createElement('pieceReferences')
    pieceReferences.setAttribute('desc','*参考文献')
    pieceReferences.appendChild(doc.createTextNode(table1[14]))
    piece.appendChild(pieceReferences)

    location = doc.createElement('location')
    location.setAttribute('desc','解析地址')
    location.appendChild(doc.createTextNode(table1[15]))
    piece.appendChild(location)

    md5Val = doc.createElement('md5Val')
    md5Val.setAttribute('desc','*资源摘要值')
    md5Val.appendChild(doc.createTextNode(table1[16]))
    piece.appendChild(md5Val)

if __name__=="__main__":
    start()