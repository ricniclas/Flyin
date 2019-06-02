import pickle
file = pickle.load(open("top_scores", "rb"))

def mostrarPlacar(Pontos):
    D = ""
    for key in Pontos:
        # print(key)
        C = "Nome : "
        A = (key['Nome'])
        B = (key['Pontos'])
        # C = ("Nome: ",A, "Pontos: ",B)
        # print(A)
        # print(B)
        C += A
        C += " Pontos: "
        C += str(B)
        D += C
        D += "\n"

    return D




my_string = mostrarPlacar(file)
len_my_string = len(my_string)
print ("Sua mensagem é:")
print(my_string)
print ("Sua informação tem",len_my_string*7,"bits de tamanho")

letters =[]
only_letters =[]
for letter in my_string:
    if letter not in letters:
        freq = my_string.count(letter)
        letters.append(freq)
        letters.append(letter)
        only_letters.append(letter)

nodes = []
while len(letters)>0:
    nodes.append(letters[0:2])
    letters = letters[2:]
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)


def combine (nodes):
    pos=0
    newnode=[]
    if len(nodes)>1:
        nodes.sort()
        nodes[pos].append("0")
        nodes[pos+1].append("1")
        combined_node1 = (nodes[pos][0]+nodes[pos+1][0])
        combined_node2 = (nodes[pos][1]+nodes[pos+1][1])
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes=[]
        newnodes.append(newnode)
        newnodes = newnodes+nodes[2:]
        nodes=newnodes
        huffman_tree.append(nodes)
        combine(nodes)
    return huffman_tree

newnodes = combine(nodes)

huffman_tree.sort(reverse=True)

print ("Aqui está a árvore Huffman mostrando os módulos emergidos e os caminhos binários.")

checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)

count=0
for level in huffman_tree:
    print ("Level",count,":",level)
    count +=1

print()

letter_binary = []
if len(only_letters)==1:
    letter_code = [only_letters[0],"0"]
    letter_binary.append(letter_code*len(my_string))
else:
    for letter in only_letters:
        lettercode=""
        for node in checklist:
            if len(node)>2 and letter in node [1]:
                lettercode = lettercode + node[2]
        letter_code = [letter,lettercode]
        letter_binary.append(letter_code)

print("Seus códigos binários são:")
for letter in letter_binary:
    print(letter[0],letter[1])

bitstring =""
for character in my_string:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]

binary = ((bin(int(bitstring, base=2))))

uncompressed_file_size = len(my_string)*7
compressed_file_size = len(binary)-2

print("Seu arquivo original tinha",uncompressed_file_size,"bits, o comprimido tem",compressed_file_size)
print("Isso economizou",uncompressed_file_size-compressed_file_size,"bits")

print("sua mensagem em binário é:")
print(binary)

bitsrtring = str(binary[2:])
umcompressed_string = ""
code = ""

for digit in bitstring:
    code = code+digit
    pos = 0
    for letter in letter_binary:
        if code == letter[1]:
            umcompressed_string = umcompressed_string+letter_binary[pos][0]
            code =""
        pos +=1

print ("Sua informação descomprimida é: ")
print(umcompressed_string)