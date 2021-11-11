import sys, math

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,'

def main():
    message = 'RSA is a public key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.'
    keySize = 1024
    pubkey = (14118956157108293655346808051133433894091646039538312006923399735362493605263203702497585893776717003286326229134304078204210728995962809448233282087726441833718356477474042405336332872075207334696535304102256981804931805888502587515310873257966538377740407422137907772437613376342940374815839154897315760145075243071401233858428232725214391295151698044147558454184807105787419519119343953276836694146614061330872356766933442169358208953710231872729486994792595105820069351163066330362191163434473421951082966346860965671789280887020440983279967498480147232734401682910892741619433374703999689201536556462802829353073, 100718103971294791099836725874012546370680926012185805765401052276262582385715159775366446162659948559753647672663811614813769790164114531293175203029620427243719599468958551745636665558941526164523429965489703529940030465646848449715020479155556561228677211251598560502855023412904336022230634725973056990069)
    
    encryptedText = encryption(keySize, pubkey, message)

    print('Encrypted text:')
    print(encryptedText)

def getBlocksFromText(message, blockSize):
    blockInts = []
    for blockStart in range(0, len(message), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(message))):
            blockInt += (SYMBOLS.index(message[i])) * (len(SYMBOLS) ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts

def encryptMessage(message, n, e, blockSize):
    encryptedBlocks = []

    for block in getBlocksFromText(message, blockSize):
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks

def encryption(keySize, pubkey, message):
    n, e = pubkey
    blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))

    encryptedBlocks = encryptMessage(message, n, e, blockSize)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ''.join(encryptedBlocks)

    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    return encryptedContent

if __name__ == '__main__':
    main()
