import networkx as nx
import sys
import community
import operator

def read_input_to_graph(input_file):
    g = nx.Graph()

    with open(input_file) as file:
        for each_line in file:
            each_line = each_line.strip('\n').split()
            g.add_edge(each_line[0], each_line[1])
    file.close()

    return g

def compute_best_community(original_g):
    max_modularity = -1
    total_nodes = nx.number_of_nodes(original_g)
    community_count = 1
    g = original_g
    communities = []

    while community_count < total_nodes:
        betweenness = nx.edge_betweenness(g)
        max_betweenness = max(betweenness.iteritems(), key = operator.itemgetter(1))[0]
        g.remove_edge(max_betweenness[0], max_betweenness[1])
        connected_subgraphs = nx.connected_components(g)

        community_dict = {}
        community_number = 0
        for subgraph in connected_subgraphs:
            community_number += 1
            for node in subgraph:
                community_dict[node] = community_number

        modularity = community.modularity(community_dict, original_g)
        if modularity > max_modularity:
            max_modularity = modularity
            communities = connected_subgraphs

            print "max modularity increased"
            for i in connected_subgraphs:
                print i

        community_count += 1

    print max_modularity


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print "USAGE: python pramod_setlur_community.pdf [INPUT_FILE] [IMAGE]"
    else:
        input_file = sys.argv[1]
        #image = sys.argv[2]

        g = read_input_to_graph(input_file)
        compute_best_community(g)