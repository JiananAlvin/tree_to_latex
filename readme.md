# TranslateToLatexTree #

This is a python script file that translates tree-graph information stored in a .txt file to complicated LaTeX code, which can be compiled into a pretty tree graph in LaTeX editor (ex. Overleaf).

## Basic usage

If you want to draw this tree:


![Banana tree](https://github.com/diegoceccarelli/treepy/raw/master/examples/banana.png)

Then you should create a .txt file where each line describes a level of the tree, starting from the root:

```txt
line 1: v
```

In the second line you want to describe 4 nodes. Each node description is separated by the others with the symbol '|' and contains the label of the incoming edge (if any) and the label of the node, encoded with this syntax: 

```txt
[label of the incoming edge] ; [label of the node]
```

Then the second will be: 

```
line 2: a;u | banana$;1 | $;7 | na;z
```

In the third line, you have nodes with different parents: the description you will put at the beginning of the line will refer to the leftmost node at the upper level (in this case *u*). <u>You can change the parent node using the symbol '@': the parent will become the next parent node on the right</u> (in this case *1*). If the next parent node does not  have child nodes, leave the description empty.

Third line will be: 	

```txt
line 3: $;6	| na;v @  @  @ $;5 | na$;3
```

Same for the fourth level/line, you have to specify the parent for each description, considering the node that you 
created in the previous level: the previous level contains four nodes and only the second has child, then:

```txt
line 4: @ $;4 | na$;2 @ @ 
```



## Special Syntax for Discrete Mathematical Formula

I want to generate some Formula of Discrete Mathematic. There are a lot of special sign here. Hence I defined some Syntax especially:

```python
        dic = {"toRight": "\\rightarrow",
               "toLeft": "\\leftarrow",
               "double": "\\leftrightarrow",
               "or": "\\vee",
               "and": "\\wedge ",
               "not": "\\neg",
               "all": "\\forall",
               "exists": "\\exists",
               "cross": "\\times",
               "circle": "\\bigcirc",
               "sblue": "\\textcolor{blue}{", "eblue": "}",
               "sred": "\\textcolor{red}{", "ered": "}",
               "spink": "\\textcolor{magenta}{", "epink": "}",
               "space": "\\ ",
               "nextLine": "$\\\\$",
               "$$": " "}
```

An example of tree-graph information written in a .txt file:

``` txt
sred 1 ered space all x (H(x) toRight T(x)):T nextLine sred 2 ered space sblue H(m):T eblue nextLine sred 3 ered space sblue T(m):F eblue
all T space on space 1 ; sred 4 ered space H(m) toRight T(m):T
; sred 5 ered space sblue H(m):F eblue nextLine cross | toRight T space on space 4 ; sred 6 ered space sblue T(m):T eblue nextLine cross
```

The generated graph:

![image-20211026225356097](https://raw.githubusercontent.com/JiananAlvin/ImageBed/master/202110262253136.png)

## How to run this script ##

My folder looks like this:

![image-20210923042034398](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230420476.png)

In folder `example`, there is a `.txt` file which is used to describe a tree. Its content is mentioned above:

```txt
sred 1 ered space all x (H(x) toRight T(x)):T nextLine sred 2 ered space sblue H(m):T eblue nextLine sred 3 ered space sblue T(m):F eblue
all T space on space 1 ; sred 4 ered space H(m) toRight T(m):T
; sred 5 ered space sblue H(m):F eblue nextLine cross | toRight T space on space 4 ; sred 6 ered space sblue T(m):T eblue nextLine cross
```

Then I would try the command following:

```bas
{Python_path} .\treepy.py {tree_description_file}
```

![image-20210923041905791](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230419856.png)

Run it, and you see:

![image-20210923042250478](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230422553.png)

A `xxx_result.txt` file has been generated:

![image-20210923042336812](https://raw.githubusercontent.com/gggdttt/ImageBeds/master/img/202109230423880.png)

The generated Latex code in `xxx_result.txt` looks like:

```latex
\node[punkt] {$\textcolor{red}{ 1 } \  \forall x (H(x) \rightarrow T(x)):T $\\$ \textcolor{red}{ 2 } \  \textcolor{blue}{ H(m):T } $\\$ \textcolor{red}{ 3 } \  \textcolor{blue}{ T(m):F }$}
	child {node[punkt] {$\textcolor{red}{ 4 } \  H(m) \rightarrow T(m):T$}
	child {node[punkt] {$\textcolor{red}{ 5 } \  \textcolor{blue}{ H(m):F } $\\$ \times$}
edge from parent
 node[kant,right,pos=.4]{$\textcolor{magenta}{}$}}
	child {node[punkt] {$\textcolor{red}{ 6 } \  \textcolor{blue}{ T(m):T } $\\$ \times$}
edge from parent
 node[kant,right,pos=.4]{$\textcolor{magenta}{\rightarrow T \  on \  4}$}}
edge from parent
 node[kant,right,pos=.4]{$\textcolor{magenta}{\forall T \  on \  1}$}};
```

Copy it and paste it to your overleaf in the following way:

```latex
\begin{center}
\begin{tikzpicture}[
grow=down,
level 1/.style={sibling distance=5cm,level distance=2.5cm},
level 2/.style={sibling distance=4cm, level distance=2cm},
level 3/.style={sibling distance=4cm, level distance=2cm},
kant/.style={ text centered},
every node/.style={text ragged, inner sep=2mm,align=center},
punkt/.style={ shade, top color=white,
bottom color=white, draw=white, very thick }
]

% Insert generated Latex code here%

\end{tikzpicture}
\end{center}

%end here
```

The tree is drawn using the [tikz package](http://www.texample.net/tikz/). You will have to import the package *tikz*. As you can see the preamble of tikzpicture allows you to personalize your tree .




> @ Author: WenjieDTU & JiananAlvin
>
> Ref: https://github.com/diegoceccarelli/treepy

