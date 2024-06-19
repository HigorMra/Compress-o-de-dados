def descompressao_brancos(input_file, output_file):
        with open(input_file, 'r') as f:
            data = f.read()

        decomprimido = ""
        i = 0

        while i < len(data):
            if data[i].isdigit():
                decomprimido += " " * int(data[i])
            else:
                decomprimido += data[i]
            i += 1

        with open(output_file, 'w') as f:
            f.write(decomprimido)

        print("Descompressão concluída com sucesso!")

#rodar o codigo
descompressao_brancos("texto.txt", "descomprimido.txt")
