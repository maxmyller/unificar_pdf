import os
from PyPDF2 import PdfFileReader, PdfFileMerger

cnpj = '00000000000000'
nomePastaEmpresa = '00000000000000_NOME_EMPRESA'
ano = '2020'
competencia = '09_SETEMBRO'
mes = '09'
caminhoPasta = 'W:\\{}\\{}\\{}\\SEFIP'.format(nomePastaEmpresa, ano, competencia)

pdf_files = [f for f in os.listdir(caminhoPasta) if f.startswith("Analítico") or f.startswith("Comprovante") or f.startswith("RE") or (f.startswith(cnpj) and f.endswith("pdf"))]
merger = PdfFileMerger()

for filename in pdf_files:
    merger.append(PdfFileReader(os.path.join(caminhoPasta, filename), "rb"))
    print(filename)

merger.write(os.path.join(caminhoPasta, f"{mes} {ano} SEFIP.pdf"))