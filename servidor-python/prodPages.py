import os

#Atribuicao das strings a variaveis para facilitar 
project_name = 'qual_professor'
head = '<head>'
body = '<body>'

#Passando o HTML+... para String
def getProductionHtml(index, html, css, js):
        index_with_head = index.replace(head, head + '\n<style type="text/css">\n' + 
                        css + '\n</style>\n' + '<script type="text/javascript">\n' + 
                        js + '\n</script>\n')
        return index_with_head.replace(body, body + html)

def loadDist(pages_list):
    for page in pages_list:  
        # Armazenando o index
        h = open(project_name+'/index.html', 'r') 
        index_html = h.read()
        h.close()

        # Armazenando o pages
        h = open(project_name+'/pages/'+ page +'/'+ page +'.html', 'r')
        page_html = h.read()
        h.close() #encerra/fecha

        # Armazenando os arquivos javascript
        h = open(project_name+'/pages/'+ page +'/'+ page +'.js', 'r')
        page_js = h.read()
        h.close() #encerra/fecha

        # Armazenando os arquivos css
        h = open(project_name+'/pages/'+ page +'/'+ page +'.css', 'r')
        page_css = h.read()
        h.close() #encerra/fecha

        # Caso a pasta nao exista a pasta, criar a pasta 
        if not os.path.exists(project_name+'/dist'):
            os.makedirs(project_name+'/dist')

        # Abre o arquivo como Writing e caso nao exista o arquivo ele cria 
        h = open(project_name+'/dist/'+ page +'.html', 'w+')
        page_html = getProductionHtml(index_html, page_html, page_css, page_js)
        h.write(page_html) 
        h.close() #encerra/fecha

#Transforma a pag passada para bytes e retorna essa sequencia de bytes
def getBytesDistHtml(page):
        loadDist([page])
        h = open(project_name+'/dist/' + page + '.html', 'r')
        dist_page = h.read()
        h.close()
        header = ('HTTP/1.0 200 OK\r\n' +
                'Content-Type: text/html; charset=ISO-8859-1\r\n' +
                'Access-Control-Allow-Origin: *\r\n' +
                'Content-Length: ' + str(len(dist_page)) + '\r\n\r\n' +
                (dist_page))
        return bytes(header, 'utf-8')

#
def getIcon(icon):
        return bytes(('HTTP/1.0 200 OK\r\n' +
                'Content-Type: image/jpeg; charset=ISO-8859-1\r\n' +
                'Access-Control-Allow-Origin: *\r\n' +
                'Content-Length: ' + str(len(icon)) + '\r\n\r\n' +
                (icon) + ' charset=ISO-8859-1'), 'utf-8')