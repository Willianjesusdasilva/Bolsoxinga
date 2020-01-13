import random

classificador = [
    'pessoa',
    'criatura',
    'criatura'
]

xingneutro = [
	'imbecil',
	'idiota',
	'palerma',
	'pateta',
	'boçal',
	'ignorante',
	'besta',
	'torpe',
	'canalha',
	'vigarista',
	'mau-caráter',
	'indecente',
	'imoral',
	'sem-vergonha',
	'parasita',
	'patife',
	'desprezível',
	'infame',
	'execrável',
	'repugnante',
	'imprestável',
	'abominável']
	
exagero = [
	'que eu já vi',
	'do mundo',
	'da face da Terra',
	'de todos os tempos',
	'que este país já viu',
	'que eu tive o desprazer de conhecer',
	'que já existiu']
	
qualificador = [
	'demais',
	'de marca maior',
	'a dar com pau',
	'além da conta',
	'pra caramba',
	'pra cacete']

conclusao = [
	'Não presta.',
	'Nunca fez nada que preste.',
	'Não me engana, tá OK?',
	'Não engana ninguém.',
	'O povo brasileiro tem consciência disso.',
	'Nunca me enganou.',
    'Ninguém fala isso daí.',
    'Todo mundo sabe disso.',
    'Eu sempre disse isso.',
    'Isso não é segredo pra ninguém.',
    'Alguém tinha que falar isso, tá OK?',
    'Com toda a certeza.',
	'Envergonha o povo brasileiro.',
	'Quer destruir a nossa nação.',
	'É impressionante isso daí.',
	'Cara de pau.',
	'Precisa pegar uma cana.']


def set_xing(nome):
    return (f' {nome} é a {random.choice(classificador)} mais {random.choice(xingneutro)} {random.choice(exagero)}. {random.choice(conclusao)}')

print(set_xing('willian'))
