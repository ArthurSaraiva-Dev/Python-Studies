arquivo_write = open("dados_write.txt", "w", encoding='utf-8') # criando arquivo txt

arquivo_write.write("Conteúdo da primeira linha") #escrevendo no arquivo
arquivo_write.write("\nConteúdo da segunda linha")
arquivo_write.close

linhas = ["Conteúdo linha 1",
          "\nConteúdo linha 2"] #array simples

arquivo_writelines = open("dados_writelines.txt", "w", encoding="utf-8")
arquivo_writelines.writelines(linhas) # adicionando o conteúdo do array no txt
arquivo_writelines.close #fechando o arquivo

arquivo_writelines = open("dados_writelines.txt", "a", encoding="utf-8")
arquivo_writelines.write("\nConteúdo terceira linha") #add mais conteúdo utilizando o append "a"

