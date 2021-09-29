PYTHON = python

JGRAPH = /home/jplank/bin/LINUX/jgraph
PS2PDF = ps2pdf - 
CONVERT = convert -density 300 - -quality 100

TOJPG = ${JGRAPH} | ${PS2PDF} | ${CONVERT}

run:
	${PYTHON} maze_gen.py 20 20 | ${TOJPG} graphs/20_20.jpg
	${PYTHON} maze_gen.py 50 50 -c red | ${TOJPG} graphs/50_50_red.jpg
	${PYTHON} maze_gen.py 100 100 -c blue | ${TOJPG} graphs/100_100_blue.jpg
	${PYTHON} maze_gen.py 200 200 -c green | ${TOJPG} graphs/200_200_green.jpg
	${PYTHON} maze_gen.py 400 400 | ${TOJPG} graphs/400_400.jpg
	${PYTHON} maze_gen.py 100 50 -c orange | ${TOJPG} graphs/100_50_orange.jpg

clean:
	rm graphs/*