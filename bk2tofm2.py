with open("output.fm2", "w") as output:
    output.write("version 3\nromChecksum base64:jjYwGG411HcjG/j9UOVM3Q==\nfourscore 0\nport0 1\n")
    output.write("|0|........|||\n")
    with open("Input Log.txt", "r") as reader:
        reader.readline()
        reader.readline()
        for line_in in reader:
            if line_in.strip() == "[/Input]":
                break
            line_out = "|0|"
            line_out += line_in[7]
            line_out += line_in[6]
            line_out += line_in[5]
            line_out += line_in[4]
            line_out += 'T' if line_in[8] == 'S' else '.'
            line_out += 'S' if line_in[9] == 's' else '.'
            line_out += line_in[10]
            line_out += line_in[11]
            line_out += "|||"
            output.write(line_out + "\n")