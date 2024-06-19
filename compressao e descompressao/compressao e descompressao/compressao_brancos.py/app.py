def compressao_brancos(input_file, output_file):
        with open(input_file, 'r') as f:
            data = f.read()
        comprimido = ""
        count = 0

        for char in data:
            if char == " ":
                count += 1
            else:
                if count > 0:
                    comprimido += str(count)
                    count = 0
                comprimido += char

        if count > 0:
            comprimido += str(count)

        with open(output_file, 'w') as f:

            f.write("".join(["#" + char if char.isdigit() else char for char in comprimido]))

        print("Compressão concluída com sucesso!")

#rodar o código
compressao_brancos("texto.txt", "comprimido_brancos.txt")








