import re
import os
from tkinter import *

#Cifra de Cesar

#Codificador em Cifra de Cesar
def Encode_Cesar():
    Alpha_Orig = "abcdefghijklmnopqrstuvwxyz "
    Msg_Input = Text_Box_Msg_Encode.get()
    Key_Input = int(Text_Box_Key_1.get())
    Indx_Encode = 0
    Msg_Encode = ""
    Size_Alpha = len(Alpha_Orig)
    Size_Msg = len(Msg_Input)

    
    while Indx_Encode != Size_Msg:
        i = Alpha_Orig.find(Msg_Input[Indx_Encode])
        i_2 = (i + Size_Alpha + Key_Input) % Size_Alpha
        Msg_Encode += Alpha_Orig[i_2]
        Indx_Encode += 1

    Text_Out_Encode_Cesar["text"] = Msg_Encode

#Decodificador em Cifra de Cesar
def Decode_Cesar():
    Alpha_Orig = "abcdefghijklmnopqrstuvwxyz "
    Alpha_New = ""
    Msg_Input = Text_Box_Msg_Decode.get()
    Key_Input = int(Text_Box_Key_1.get())
    Indx_Decode = 0
    Msg_Decode = ""
    Size_Alpha = len(Alpha_Orig)
    Size_Msg = len(Msg_Input)
    Encode = Size_Alpha - (( Key_Input + Size_Alpha ) % Size_Alpha)


    while len(Alpha_New) != Size_Alpha:
        i = (len(Alpha_New) + Size_Alpha + Encode) % Size_Alpha
        Alpha_New += Alpha_Orig[i]
    
    while Indx_Decode != Size_Msg:
        i_2 = Alpha_New.find(Msg_Input[Indx_Decode])
        i_3 = (i_2 + Size_Alpha - Key_Input) % Size_Alpha
        Msg_Decode += Alpha_New[i_3]
        Indx_Decode += 1

    Text_Out_Decode_Cesar["text"] = Msg_Decode



# RC4

def Inicializa_s_Box(chave):
    s_box = list(range(256))
    j = 0

    for i in range(256):
        j = (j + s_box[i] + chave[i % len(chave)]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]

    return s_box


def Gera_Stream(chave, texto):
    s_box = Inicializa_s_Box(chave)
    i = 0
    j = 0
    stream = []

    for byte in texto:
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        k = s_box[(s_box[i] + s_box[j]) % 256]
        stream.append(k)

    return bytes(stream)


def Cifra_rc4(chave, texto):

    chave = chave.encode('utf-8')
    texto = texto.encode('utf-8')
    stream = Gera_Stream(chave, texto)
    texto_cifrado = bytes([x ^ y for x, y in zip(texto, stream)])
    Text_Out_Encode_2["text"] = texto_cifrado.hex()
    return texto_cifrado


def Decifra_rc4(chave, texto_cifrado):
    texto_cifrado = bytes.fromhex(texto_cifrado)
    texto = Gera_Stream(chave.encode('utf-8'), texto_cifrado)
    texto_decifrado = bytes([x ^ y for x, y in zip(texto_cifrado, texto)])
    Text_Out_Decode_2["text"] = texto_decifrado.decode('utf-8')
    return texto_decifrado


def Call_Cifra():
    chave = Text_Box_Key_2.get()
    texto_original = Text_Box_Msg_Encode_2.get()
    Cifra_rc4(chave, texto_original)


def Call_Decifra():
    chave = Text_Box_Key_2.get()
    texto_original = Text_Box_Msg_Decode_2.get()
    Decifra_rc4(chave, texto_original)



# Interface

window = Tk()
window.title("Codificador")
window.geometry("620x400")
window.configure(background = "#555555")


Text_Into = Label(window, text = "Codifique em Cifra de Cesar:", background = "#555555")
Text_Into.grid(column = 1, row = 0)


Text_Info_Encode = Label(window, text = "Coloque a mensagem a ser codificada:", background = "#555555")
Text_Info_Encode.grid(column = 0, row = 1)


Text_Info_Key = Label(window, text = "Coloque a chave de codificação:", background = "#555555")
Text_Info_Key.grid(column = 0, row = 2)


Text_Info_Decode = Label(window, text = "Coloque a mensagem a ser decodificada:", background = "#555555")
Text_Info_Decode.grid(column = 0, row = 3)


Text_Box_Msg_Encode = Entry(window)
Text_Box_Msg_Encode.grid(column = 1, row = 1)


Text_Box_Msg_Decode = Entry(window)
Text_Box_Msg_Decode.grid(column = 1, row = 3)


Text_Box_Key_1 = Entry(window)
Text_Box_Key_1.grid(column = 1, row = 2)


Button_1 = Button(window, text = "Converter", command = Encode_Cesar, background = "#4444ff")
Button_1.grid(column = 2, row = 1)


Button_2 = Button(window, text = "Des-Converter", command = Decode_Cesar, background = "#4444ff")
Button_2.grid(column = 2, row = 3)


Text_Out_Encode_Cesar = Label(window, text = "")
Text_Out_Encode_Cesar.grid(column = 3, row = 1)


Text_Out_Decode_Cesar = Label(window, text = "")
Text_Out_Decode_Cesar.grid(column = 3, row = 3)


Text_Intro_2 = Label(window, text = "Codifique em RC4" , background = "#555555")
Text_Intro_2.grid(column = 1, row = 5)


Text_Info_Encode_2 = Label(window, text = "Coloque a mensagem a ser codificada:", background = "#555555")
Text_Info_Encode_2.grid(column = 0, row = 6)


Text_Info_Key_2 = Label(window, text = "Coloque a chave de codificação:", background = "#555555")
Text_Info_Key_2.grid(column = 0, row = 7)


Text_Info_Decode_2 = Label(window, text = "Coloque a mensagem a ser decodificada:", background = "#555555")
Text_Info_Decode_2.grid(column = 0, row = 8)


Text_Box_Msg_Encode_2 = Entry(window)
Text_Box_Msg_Encode_2.grid(column = 1, row = 6)


Text_Box_Key_2 = Entry(window)
Text_Box_Key_2.grid(column = 1,row = 7)


Text_Box_Msg_Decode_2 = Entry(window)
Text_Box_Msg_Decode_2.grid(column = 1, row = 8)


Button_3 = Button(window, text = "Converter", command = Call_Cifra, background = "#4444ff")
Button_3.grid(column = 2, row = 6)


Button_4 = Button(window, text = "Des-Converter", command = Call_Decifra, background = "#4444ff")
Button_4.grid(column = 2, row = 8)


Text_Out_Encode_2 = Label(window, text = "")
Text_Out_Encode_2.grid(column = 3, row = 6)


Text_Out_Decode_2 = Label(window, text = "")
Text_Out_Decode_2.grid(column = 3, row = 8)


end = Button(window, text = "Finalizar", command = window.destroy, background = "#4444ff")
end.grid(column = 1, row = 10)


window.mainloop()