# Sieve Challenge

Make sure you're connected to the Interwebs, then run:

	$ python script.py

And you should see my answer to the challenge :)

## A few notes
* The ``Price`` class (implemented in ``price.py``) is responsible for price parsing;
* A small suite of tests is provided in ``test_price.py``;
* Networking is done via the [Requests](http://docs.python-requests.org/en/latest) library;
* Python 2.7.3 is required;
* Developed in Ubuntu 12.10;

## Output
From ``output.txt``:
````
DESAFIO SIEVE - Gabriel Vieira

NIVEL 1: http://hughes.sieve.com.br:9090/level1
Texto: <p> <div>Preco baratinho para toda a familia. So R$ 44,99 pra mamae e pra titia!</p>
Preco: R$44,99


NIVEL 2: http://hughes.sieve.com.br:9090/level2
Texto: <p> <div> Vamos falar de coisa boa? Vamos falar de tekpix por apenas R$ 3.999,00?? So hoje! </div> </p>
Preco: R$3,99


NIVEL 3: http://hughes.sieve.com.br:9090/level3
Texto: parabens! Voce ganhou um mini system de R$ 499,00
Preco: R$499,0


NIVEL 4: http://hughes.sieve.com.br:9090/level4
Texto: Preco atual = R$ 4 5 0 ,0 0
Preco: R$450,0


NIVEL 5: http://hughes.sieve.com.br:9090/level5%2525
Texto: Ok, mais um preco pra voce!!! R$ 40 0,0 0
Preco: R$400,0
````
