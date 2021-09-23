#!/usr/bin/env python
# encoding: utf-8
"""
treepy.py

Created by Diego Ceccarelli on 2010-09-24.
Copyright (c) 2010 ISTI CNR. All rights reserved.
"""

import sys
import getopt

help_message = '''
The help message goes here.
'''


class Tree:
    "implements a tree, nodes[i]->edge label,node_id"

    def __init__(self, label=""):
        self.ROOT = 0
        self.size = 0
        self.labels = {}
        self.nodes = {}
        self.last_id = -1
        self.size = 1
        self.nodes[self.ROOT] = []
        self.last_id = self.ROOT
        if (label != ""):
            self.labels[self.ROOT] = label

    def getLabel(self, node_id):
        if (node_id in self.labels):
            return self.labels[node_id]
        else:
            return ""

    def addNode(self, src_id=-1, edge_label="", dest_label=""):
        dest_id = self.size
        self.nodes[src_id].append((edge_label, dest_id))
        self.nodes[dest_id] = []
        self.last_id = dest_id
        if (dest_label != ""): self.labels[self.size] = dest_label
        self.size += 1
        return self.last_id

    """ A tree is rappresented by a string, with this code:
        a 
       /c \
      /	    \
     b		 d 
    ;0;a;(c;1;b;())(;2;d;())
    """

    def strNode(self, node_id):
        desc = str(node_id) + ";" + self.getLabel(node_id) + ";"
        for (lab, child_id) in self.nodes[node_id]:
            desc += "([" + lab + "];" + self.strNode(child_id) + ")"
        return desc

    def read(self, input_file):
        """
        read description from an input file:
        each line reports all the nodes at the same level, children of different nodes are divided by tab
        siblings are divided by |
        e.g. the previous example is coded as:
        a
        c;b|;d

        """
        desc_file = open(input_file)

        node_ids = {}  # line -> nodeId1, nodeId2 ...
        lines = desc_file.readlines()
        self.labels[self.ROOT] = lines[0].strip()
        node_ids[0] = [self.ROOT]
        # for each line consider iterate on each node s_i
        for j in range(1, len(lines)):
            if (lines[j][0] == '#'): continue
            node_ids[j] = []
            dest_siblings = lines[j].split("@")
            count = 0
            for s in node_ids[j - 1]:
                if count < len(dest_siblings):
                    dest_nodes = dest_siblings[count].split("|")

                    # print dest_nodes
                    for d in dest_nodes:
                        if d.strip('\xc2\xa0 \n\t') == "": continue
                        # print d.strip()
                        try:
                            (edge_label, node_label) = d.split(";")
                        except:
                            print >> sys.stderr, "Error: reading line " + str(j) + " elem " + d + "(" + str(
                                len(d.strip())) + ")"
                            sys.exit()
                        node_ids[j].append(self.addNode(s, edge_label.strip(), node_label.strip()))
                    count += 1

        desc_file.close()

    def getNodeTex(self, node_id):
        count = 0
        desc = self.getLabel(node_id)
        if (node_id == self.ROOT):
            tex = "\\node[punkt] {$" + desc + "$}"
        else:
            tex = "node[punkt] {$" + desc + "$}"
        for (lab, child_id) in self.nodes[node_id]:
            tex += "\n\tchild {" + self.getNodeTex(child_id) + "\n"
            lab = lab.strip()
            if count % 2 == 0:
                rev = lab  # [::-1]
                tex += "edge from parent\n node[kant,right,pos=.4]{$" + rev + "$}}"
        # else:
        #	lab = lab.replace("$","\$")
        #	tex+= "edge from parent\n node[kant,below,pos=.4]{\\texttt{"+lab+"}}}"
        # count+=1
        return tex

    def replace(self, str):
        result = str
        dic = {"toRight": "\\rightarrow", "toLeft": "\leftarrow",
               "double": "\leftrightarrow", "or": " \\vee", "and": " \wedge ",
               "not": "\\neg", "sblue": "\\textcolor{blue}{", "eblue": "}",
               "sred": "\\textcolor{red}{", "ered": "}",
               "smag": "\\textcolor{magenta}{", "emag": "}", "space": "\ "}
        for i in dic:
            result = result.replace(i, dic.get(i))
            # print("replace  " + i)
            # print("result: "+result)
        return result

    def getTex(self):
        desc = ""
        desc += self.getNodeTex(self.ROOT) + ";"
        # desc += "\\end{tikzpicture}\n}\n \end{document}"
        desc = self.replace(desc)
        return desc

    # for each block of nodes at the next level take the block i and for each node d in i
    # addNode(s,d,label_d)

    def __str__(self):
        return self.strNode(self.ROOT)


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error as msg:
            raise Usage(msg)

        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value

    except Usage as err:
        print(sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg))
        print(sys.stderr, "\t for help use --help")
        return 2
    t = Tree()
    t.read(sys.argv[1])

    with open(sys.argv[1] + "_result.txt", 'w') as f:
        print(f.write(t.getTex()))
    # print(t.getTex())


if __name__ == "__main__":
    sys.exit(main())
