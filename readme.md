# TranslateToLatexTree #

This is a python script that compiles a simple text representation of a tree in a pretty latex figure.

## Basic usage

Let's say you want to draw this tree:


![Banana tree](https://github.com/diegoceccarelli/treepy/raw/master/examples/banana.png)

Then you should create a txt file where each line describes a level of the tree, starting from the root:

	line 1: v

In the second line you want to describe 4 nodes. Each node description is separated by the others with the symbol '|' and contains the label of the incoming edge (if any) and the label of the node, encoded with this syntax: 

	[label of the incoming edge] ; [label of the node]

Then the second will be: 
	line 2: a;u| banana$;1 | $;7 | na;z

In the third line, you have nodes with different parents: the description you will put at the beginning of the line will refer to the leftmost node at the upper level (in this case *u*). <u>You can change the parent node using the symbol '@': the parent will become the next parent node on the right</u> (in this case *1*). If the next parent node does not  have child nodes, leave the description empty.

Third line will be: 	

	line 3: $;6	|na;v @  @  @ $;5 | na$;3

Same for the fourth level/line, you have to specify the parent for each description, considering the node that you 
created in the previous level: the previous level contains four nodes and only the second has child, then:

	line 4: @ $;4| na$;2 @ @ 



## Special Syntax for Discrete Mathematical Formula

I want to generate some Formula of Discrete Mathematic. There are a lot of special sign here. Hence I defined some Syntax especially:

```python
        dic = {"toRight": "\\rightarrow",
               "toLeft": "\leftarrow",
               "double": "\leftrightarrow", 
               "or": "\vee ", 
               "and": "\wedge ",
               "not": "\\neg", 
               "sblue": "\\textcolor{blue}{", "eblue": "}",
               "sred": "\\textcolor{red}{", "ered": "}", "space": "\ ","nextLine":"$\\\\$"
               "largeSpace": "\quad", "$$": " "}
```

An example:

``` txt
1.(p toRight r) and (q toRight not r):T largeSpace 2.(p toLeft r) or (q double not r):F
;3.p toRight r:T | sblue not  T space on space 1 eblue;4.q toRight p:T
@ ;sred 5. p toRight r :T ered| not  T space on space 1;6.q toRight p:T

```

The generated graph:

![image-20210923040952696](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230409776.png)

## How to run this script ##

My folder looks like this:

![image-20210923042034398](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230420476.png)

In folder `example`, there is a `txt` file which is used to describe a tree.

So I would try the command following:

```bas
{Python_path} .\treepy.py {tree_description_file}
```



![image-20210923041905791](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230419856.png)

Run it, and you see:

![image-20210923042250478](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230422553.png)

A `xxx_result.txt` file has been generated:

![image-20210923042336812](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230423880.png)

The code in `xxx_result.txt` looks like:

```latex
\node[punkt] {$1.(p \rightarrow r)  \wedge  (q \rightarrow \neg r):T \quad 2.(p \leftarrow r)  \vee (q \leftrightarrow \neg r):F$}
	child {node[punkt] {$3.p \rightarrow r:T$}
edge from parent
 node[kant,above,pos=.4]{ }}
	child {node[punkt] {$4.q \rightarrow p:T$}
	child {node[punkt] {$\textcolor{red}{ 5. p \rightarrow r :T }$}
edge from parent
 node[kant,above,pos=.4]{ }}
	child {node[punkt] {$6.q \rightarrow p:T$}
edge from parent
 node[kant,above,pos=.4]{$\neg  T \  on \  1$}}
edge from parent
 node[kant,above,pos=.4]{$\textcolor{blue}{ \neg  T \  on \  1 }$}};
```

Copy it and paste it to your overleaf in the following way:

```latex
%start from here
\begin{tikzpicture}[
grow=down,
level 1/.style={sibling distance=5cm,level distance=4cm},
level 2/.style={sibling distance=4cm, level distance=4cm},
level 3/.style={sibling distance=4cm, level distance=4cm},
kant/.style={ text centered, sloped},
every node/.style={text ragged, inner sep=2mm,align=center},
punkt/.style={ shade, top color=white,
bottom color=white, draw=white, very thick }
]

% Insert generated code here%

\end{tikzpicture}

%end here
```

The tree is drawn using the [tikz package](http://www.texample.net/tikz/). You will have to import the package *tikz*. As you can see the preamble of tikzpicture allows you to personalize your tree .




> @ Author : WenjieDTU&JiananAlvin
>
> Ref: https://github.com/diegoceccarelli/treepy

