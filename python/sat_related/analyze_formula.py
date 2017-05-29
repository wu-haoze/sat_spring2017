import community
import networkx as nx
import sys


def main():
    num_var = 0
    num_clause = 0
    content = []
    with open(sys.argv[1], 'r') as in_file:
        for line in in_file:
            if line[0] == "c":
                continue
            elif line[0] == 'p':
                line = line.split()
                num_var = int(line[2])
                num_clause = int(line[3])
            elif line != '':
                content.append(map(int, line.split())[:-1])
    
    VIG = nx.Graph()
    VIG.add_nodes_from(range(num_var+1)[1:])
    VCG = nx.Graph()
    VCG.add_nodes_from(range(num_var + num_clause + 1)[1:])

    # Build a Variable Interaction Graph
    preprocess_VIG(content, VIG)
    # Build a Variable Cluase Graph
    preprocess_VCG(content, VCG, num_var)
    
    dic_VCG = nx.degree(VCG)
    dic_VIG = nx.degree(VIG)

    # Print VCG degrees
    degs = []
    for i in range(1,num_var + 1):
        degs.append(dic_VIG[i])
    with open("degrees.txt", 'a') as out_file:
        out_file.write(sys.argv[1] + " " + " ".join(map(str, degs)) + "\n");

    print "VIG: ", degs

    # Print VIG degrees
    degs = []
    for i in range(1,num_var + 1):
        degs.append(dic_VCG[i])
    print "VCG: ", degs

    # Calculate the ratio of positive literal to negative literal for each variable,
    #  and the occurrence of each variable
    pos_negs, occurrence = get_posneg(content, num_var)

    print "Pos_neg: ", pos_negs
    print "Occurrence: ", occurrence


def get_posneg(content, num_var):
    occ_dic = {}
    pos_dic = {}
    for i in range(1, num_var + 1):
        occ_dic[i] = 0
        pos_dic[i] = 0
    for line in content:
        for lit in line:
            occ_dic[abs(lit)] += 1
            if lit > 0:
                pos_dic[abs(lit)] += 1
    occurrence = []
    pos_negs = []
    for i in range(1, num_var + 1):
        occurrence.append(occ_dic[i]) 
        if occ_dic[i] != 0:
            pos_negs.append(abs(occ_dic[i] - 2.0 * pos_dic[i])/occ_dic[i])
        else:
            pos_negs.append(0)
    assert(num_var == len(pos_negs))
    return pos_negs, occurrence

def preprocess_VIG(formula, VIG):
    """                                                               
    Transforms a formula into int matrix
    Builds VIG.
    """
    for cn in range(len(formula)):
        for i in range(len(formula[cn])-1):
            for j in range(len(formula[cn]))[i+1:]:
                VIG.add_edge(abs(formula[cn][i]), abs(formula[cn][j]))

def preprocess_VCG(formula, VCG, num_var):
    """                      
    Builds VCG
    """
    for cn in range(len(formula)):
        for var in formula[cn]:
            VCG.add_edge(abs(var), cn + num_var + 1)

if __name__ == "__main__":
    main()
