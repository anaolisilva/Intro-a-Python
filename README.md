<h1>Introdução à programação com Python</h1>
<p>Coleção de exercícios-programa (EPs) feitos na disciplina MAC0110 - Introdução à Programação (IME-USP) no primeiro semestre de 2021, ministrada pelos professores Carlos Hitoshi e José Coelho (a quem são atribuídos os enunciados), onde trabalhei com conceitos de lógica de programação aplicado em Python, utilizando elementos como laços condicionais, de repetição, listas, dicionários, etc. </p>
<p>Este README está dividido de acordo com os EPs realizados na disciplina. A complexidade aumenta conforme o número do EP. Resumos dos enunciados e tópicos de estudo abordados estão <a href="#lista">listados abaixo.</a> O enunciado completo, com exemplos, está em comentário no arquivo do exercício.</p>
<p>Alguns exercícios já vieram com determinadas funções implementadas - quando isso ocorre, está indicado também em comentário. </p>
<strong>Clique no número da atividade para ver a resolução que eu bolei!</strong><br><br>

<div align="left">
	<p>Tecnologias:</p>
	<table>
			<tr>
        <td><img width="60px" src="https://raw.githubusercontent.com/devicons/devicon/9f4f5cdb393299a81125eb5127929ea7bfe42889/icons/python/python-original-wordmark.svg" alt="Python"></td>
      </tr>
	</table>
</div>
<hr>
<h3>Exercícios-programa</h3>
<ul id="lista">

  <li><a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/ep01.py" target="_blank">EP01</a> e <a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/tipos.py" target="_blank">EP02</a> - trabalhar conceitos simples, como variáveis, seus valores e tipos e expressões.</li>
	<br>
	<img align="left" height="250px" src="https://github.com/anaolisilva/Intro-a-Python/blob/main/Recursos/carinhaimg.png?raw=true" alt="carinha"> <br><br>
  <li align="center"><a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/tipos.py" target="_blank">EP03</a> - Escrever um programa que leia uma cordenada (x,y) e imprima a cor que a coordenada atinge, considerando o mapa ao lado:
        <br> <br>
        <p><em>Objetivo: Praticar o pensamento aplicado a resolução de problemas computacionais por meio do pensamentos lógico e aritmético e pensamentos alternativos.</em></p> <br><br><br>
  </li>
	<br>
  <li><a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/digitos.py" target="_blank">EP04</a> - Escrever um programa que lê um número n e imprime seus dígitos verificadores de acordo com a lógica (semelhante à lógica dos DVs do CPF):<br>
		dv1 = resto da divisão (1 × d1 + 2 × d2 + 3 × d3 + ⋯ + k × dk)/11<br>
		dv2 = resto da divisão (0 × d1 + 1 × d2 + 2 × d3 + 3 × d4 + ⋯ + (k − 1) × dk + k × dv1)/11<br>
		(caso o resto de alguma das divisões seja 10, o dv é 0)
 </li>
	<br>
	<li><a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/pitagoreano.py" target="_blank">EP05</a> - Escrever um programa que lê um número n e define se ele é a soma de um trio pitagoreano. <br>
		Três números inteiros positivos a, b e c, a < b < c, formam um trio pitagoreano se a2 + b2 = c2.
	<br>	Alguns números inteiros positivos podem ser escritos como a soma de um trio pitagoreano. Chamamos esses número de pitagoreanos. Por exemplo, 12 é um número pitagoreago ja que 12 = 3 + 4 + 5 e 3, 4 e 5 é um trio pitagoreano.
	</li>
	<br>
	<li> <a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/funcoes.py" target="_blank">EP06</a> - Escrever um programa com 4 funções:<br>
		<strong>- primo()</strong> - recebe um número inteiro p e define se p é primo.<br>
		<strong>- goldbach()</strong> - recebe um inteiro positivo n e define se n é a soma de dois números primos.<br>
		<strong>- exponencial()</strong> - deve retornar um número inteiro, a partir da seguinte explicação:
		<br> <img height="100px" src="https://github.com/anaolisilva/Intro-a-Python/blob/main/Recursos/exponencial.png?raw=true" alt="explicação exponencial"><br>
		<img height="20px" src="https://github.com/anaolisilva/Intro-a-Python/blob/main/Recursos/exponencial02.png?raw=true" alt="no dia d o número de infectados é nd = (1 + e × p) elevado a d, tudo * n0"><br>
		<strong>- logistica()</strong> - deve retornar um número inteiro, a partir da seguinte explicação: <br>
		A função logistica leva em consideração o fato de que na prática funções exponenciais não são encontradas, e coloca um limite de número n de indivíduos na população.<br>
		<img height="20px" src="https://github.com/anaolisilva/Intro-a-Python/blob/main/Recursos/logistica.png?raw=true" alt="no dia d o número de infectados é nd=(1+ e × p × (1−(nd−1)/n)) × n de d-1">
	</li>
	<br>
	<li> <a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/area.py" target="_blank">EP07</a> - Implementar 2 funções:<br>
		<strong>- area_por_retangulos(f, a, b, k)</strong> - Fazer uma aproximação da área de um gráfico de função a partir do método dos retângulos. Recebe uma função f, dois números a e b e um inteiro k. Retorna uma aproximação da área sob a função f no intervalo [a,b] usando k retângulos. <br>
		<img height="140px" src="https://github.com/anaolisilva/Intro-a-Python/blob/main/Recursos/aproxretangulos.gif?raw=true" alt="Imagem ilustrando o método de aproximação por retângulos"> <br>
		<strong>- area_aproximada(f, a, b, eps=EPSILON)</strong> - Função que determina melhor k para que área aproximada tenha o menor erro relativo. Recebe uma função f, dois números a, b, eps. Retorna um inteiro k e uma aproximação da área sob a função f no intervalo [a,b] usando k retângulo, de modo que o erro relativo seja menor que eps.
	</li>
	<br>
	<li>
		<a href="https://github.com/anaolisilva/Intro-a-Python/blob/main/amigos.py" target="_blank">EP08</a> - Implementar 2 funções:<br>
		<strong>- circular(amigo_de) </strong> - recebe uma lista amigo_de[] e retorna True se a lista é circular e retorna False em caso contrário. Uma lista é circular se permite que os presentes sejam distribuídos em um único ciclo.<br>
		<img height="110px" src="https://github.com/anaolisilva/Intro-a-Python/blob/main/Recursos/listacircular.png?raw=true" alt="Imagem ilustrando lista circular x não-circular"> <br>
		<strong>- experimento(N, T, debug=False) </strong> - recebe dois inteiros, N e T, e um booleano debug. A função realiza T sorteios de listas aleatórias de tamanho N (número de pessoas no grupo) contendo os inteiros 0, 1, …, N-1. A função retorna uma estimativa para probabilidade p(N) de uma lista de tamanho N ser circular. Essa estimativa é razão S/T entre o número observado de listas circulares e o número T de listas sorteadas. 
	</li>

</ul>


