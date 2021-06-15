import os,json

def removePadding(paddedEncodedText):
        paddedInfo = paddedEncodedText[:8]
        extraPadding = int(paddedInfo,2)

        padEncodedText = paddedEncodedText[8:]
        encodedText = padEncodedText[:-1*extraPadding]
        return encodedText

def decodedText(encodedText,reverseMapping):
        curCode = ""
        decodedText = ""

        for bit in encodedText:
            curCode += bit
            if (curCode in reverseMapping):
                character = reverseMapping[curCode]
                decodedText += character
                curCode = ""
        return decodedText

def decompress(inputPath):
        filename, file_extension = os.path.splitext(inputPath)
        outputPath = filename + "_decompressed" + ".txt"

        with open(inputPath, 'rb') as file, open(outputPath, 'w') as output:
            bit_string = ""
            lines = next(file)
            #Later use for reverse mapping
            mapping = json.loads(lines.decode('utf-8'))
            # print(mapping)
            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = removePadding(bit_string)

            decompressed_text = decodedText(encoded_text,mapping)
            
            output.write(decompressed_text)

        return outputPath