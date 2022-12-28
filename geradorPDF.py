from reportlab.pdfgen import canvas

def GeneratePDF(lista):
    try:
        nome_pdf = input('Inofrme o nome do documento PDF')
        pdf= canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x,'{} : {}'.format(nome, idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Arial", 12)
        pdf.drawString(245,750, 'Lista de Clientes')
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{}.pdf Criado com sucesso!!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))

    produtos = {"arroz": [4.90, "alto"], "feijão": [8.80,"médio"]}