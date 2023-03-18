def gen_weights_array():
    pol_alfabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o",
                   "ó", "p", "q", "r", "s", "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż"]

    with open('pan-tadeusz.txt', 'r', encoding="utf8") as file:
        data = file.read()

    ile_liter = [0] * len(pol_alfabet)
    for i in range(len(data)):
        for j in range(len(pol_alfabet)):
            if pol_alfabet[j] == data[i].lower():
                ile_liter[j] += 1

    zip_array = zip(ile_liter, pol_alfabet)
    zip_array = sorted(zip_array)

    sorted_weights = [y for y, x in zip_array]
    sorted_alphabet = [x for y, x in zip_array]

    return sorted_weights[::-1], sorted_alphabet[::-1]


def binary_tree(weights, alphabet, alphabetArray, finalArray):
    chances = 0
    when_slice = 0
    for i in range(len(weights)):
        chances += weights[i]
    for i in range(len(weights)):
        when_slice2 = when_slice
        when_slice += (weights[i])
        if chances / 2 >= when_slice:
            continue
        else:
            if abs(chances / 2 - when_slice) > abs(chances / 2 - when_slice2):
                i -= 1
            if i == 0:
                i = 1
            if len(weights) == 1:
                finalArray[alphabetArray.index(alphabet[0])] += "0"
                return finalArray
            if len(weights) == 2:
                finalArray[alphabetArray.index(alphabet[0])] += "0"
                finalArray[alphabetArray.index(alphabet[1])] += "1"
                return finalArray
            else:
                left_alphabet = alphabet[:i]
                right_alphabet = alphabet[i:]
                left_weights = weights[:i]
                right_weights = weights[i:]
                for x in range(i):
                    finalArray[alphabetArray.index(left_alphabet[x])] += "0"
                for z in range(len(right_alphabet)):
                    finalArray[alphabetArray.index(right_alphabet[z])] += "1"
                binary_tree(left_weights, left_alphabet, alphabetArray, finalArray)
                binary_tree(right_weights, right_alphabet, alphabetArray, finalArray)
                return finalArray


if __name__ == '__main__':
    weightsArray1, alphabetArray1 = gen_weights_array()
    alphabetArray2 = alphabetArray1
    finalArray1 = [""] * len(alphabetArray1)
    finalArray1 = (binary_tree(weightsArray1, alphabetArray1, alphabetArray2, finalArray1))
    for i in range(len(finalArray1)):
        finalArray1[i] = ''.join([alphabetArray1[i], ": ", finalArray1[i]])
    for i in finalArray1:
        print(i)
