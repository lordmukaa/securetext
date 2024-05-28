# Codificador de Mensagens

Este projeto implementa um codificador e decodificador de mensagens utilizando a Cifra de César e o algoritmo RC4. Ele também inclui uma interface gráfica construída com a biblioteca `tkinter` para facilitar a interação do usuário com as funcionalidades de codificação e decodificação.

## Funcionalidades

- Codificação e decodificação de mensagens utilizando a Cifra de César.
- Codificação e decodificação de mensagens utilizando o algoritmo RC4.
- Interface gráfica para facilitar a entrada e saída de dados.

## Como Funciona

### Cifra de César

A Cifra de César é uma técnica de criptografia de substituição onde cada letra do texto é substituída por outra letra que está um número fixo de posições à frente no alfabeto.

#### Codificação
A função `Encode_Cesar` realiza a codificação da mensagem. Ela utiliza uma chave de codificação (um número inteiro) para deslocar as letras no alfabeto.

```python
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
