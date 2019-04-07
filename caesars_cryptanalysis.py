import ngram_score as ns
import caesar_cipher as cc

fitness = ns.ngram_score('data/english_quadgrams.txt')


def break_cipher(ciphertext, keys):
    max_fitness_score = float('-inf') 
    for key in keys:
        plaintext = cc.caesar_decipher(ciphertext, key)
        fitness_score = fitness.score(plaintext)
        if fitness_score > max_fitness_score:
            max_fitness_score = fitness_score
            most_accurate_plaintext = plaintext
            most_accurate_key = key
        print(f'Key = {key}\tPlaintext = {plaintext}\tFitness = {fitness_score}')
    print(f'\nMost accurate key = {most_accurate_key}\tMost accurate plantext = {most_accurate_plaintext}\tFitness = {max_fitness_score}\n')

break_cipher('YMJHFJXFWHNUMJWNXTSJTKYMJJFWQNJXYPSTBSFSIXNRUQJXYHNUMJWX', range(1,26))
break_cipher('VHFUHW', [3,5])