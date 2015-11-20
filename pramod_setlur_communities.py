import networkx as nx
import sys
import community
import operator
import matplotlib

def read_input_to_graph(input_file):
    g = nx.Graph()

    with open(input_file) as file:
        for each_line in file:
            each_line = each_line.strip('\n').split()
            g.add_edge(each_line[0], each_line[1])
    file.close()

    return g

def format_list(communities):
    formatted_communities = []
    for community in communities:
        char_community = sorted(list(community))
        int_community = map(int, char_community)
        formatted_communities.append(sorted(list(int_community)))

    return sorted(formatted_communities)

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

        #Copying the items of the generator to a list
        connected_subgraphs_list = []
        for i in connected_subgraphs:
            connected_subgraphs_list.append(i)

        community_dict = {}
        community_number = 0

        for subgraph in connected_subgraphs_list:
            community_number += 1
            for node in subgraph:
                community_dict[node] = community_number

        modularity = community.modularity(community_dict, original_g)
        if modularity > max_modularity:
            max_modularity = modularity
            communities = list(connected_subgraphs_list)
        community_count += 1

    communities = format_list(communities)

    return communities, max_modularity

def draw_graph(image, communities, g):
    print "test"

if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print "USAGE: python pramod_setlur_community.pdf [INPUT_FILE] [IMAGE]"
    else:
        input_file = sys.argv[1]
        image = sys.argv[2]

        g = read_input_to_graph(input_file)
        communities, max_modularity = compute_best_community(g)
        draw_grap(image, communities, g)