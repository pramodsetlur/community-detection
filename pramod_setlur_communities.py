import networkx as nx
import sys
import community
import operator
import matplotlib.pyplot as plt

def read_input_to_graph(input_file):
    g = nx.Graph()

    with open(input_file) as file:
        for each_line in file:
            each_line = each_line.strip('\n').split()
            g.add_edge(each_line[0], each_line[1])
    file.close()

    return g

#Communities is a list of sets. Returns a list of lists instead.
def format_list(communities):
    formatted_communities = []
    for community in communities:
        char_community = sorted(list(community))

        #convert the character list to integer
        int_community = map(int, char_community)
        formatted_communities.append(sorted(list(int_community)))

    return sorted(formatted_communities)

#Converting the generator to a list
def convert_generator_list(connected_subgraphs):
    #Copying the items of the generator to a list
    connected_subgraphs_list = []
    for i in connected_subgraphs:
        connected_subgraphs_list.append(i)
    return connected_subgraphs_list

#Categorizing the nodes to a cluster number
def categorize_nodes(connected_subgraphs_list):
    community_number = 0
    community_dict = {}
    for subgraph in connected_subgraphs_list:
        community_number += 1
        for node in subgraph:
            community_dict[node] = community_number

    return community_dict

#Computes  the best community
def compute_best_community(original_g):
    max_modularity = -1
    total_nodes = nx.number_of_nodes(original_g)
    community_count = 1
    g = original_g
    communities = []

    #Generate all the communities: Loop thru taking the entire graph as 1 community to each node as a seperate community
    while community_count < total_nodes:
        betweenness = nx.edge_betweenness(g)
        max_betweenness = max(betweenness.iteritems(), key = operator.itemgetter(1))[0]
        g.remove_edge(max_betweenness[0], max_betweenness[1])
        connected_subgraphs = nx.connected_components(g)

        connected_subgraphs_list = convert_generator_list(connected_subgraphs)

        community_dict = categorize_nodes(connected_subgraphs_list)

        modularity = community.modularity(community_dict, original_g)

        if modularity > max_modularity:
            max_modularity = modularity
            communities = list(connected_subgraphs_list)
        community_count += 1

    communities = format_list(communities)

    return communities, max_modularity

def draw_graph(image, communities, graph):
    G=nx.cubical_graph()
    pos=nx.spring_layout(G) # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G,pos,
                           nodelist=[0,1,2,3,4],
                           node_color='r',
                           node_size=500,
                       alpha=0.8)
    # nx.draw_networkx_nodes(G,pos,
    #                        nodelist=[4,5,6,7],
    #                        node_color='b',
    #                        node_size=500,
    #                    alpha=0.8)

    # edges
    nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
    nx.draw_networkx_edges(G,pos,
                           edgelist=[(0,1),(1,2),(2,3),(3,0)],
                           width=8,alpha=0.5,edge_color='r')
    # nx.draw_networkx_edges(G,pos,
    #                        edgelist=[(4,5),(5,6),(6,7),(7,4)],
    #                        width=8,alpha=0.5,edge_color='b')


    # # some math labels
    # labels={}
    # labels[0]=r'$a$'
    # labels[1]=r'$b$'
    # labels[2]=r'$c$'
    # labels[3]=r'$d$'
    # labels[4]=r'$\alpha$'
    # labels[5]=r'$\beta$'
    # labels[6]=r'$\gamma$'
    # labels[7]=r'$\delta$'
    # nx.draw_networkx_labels(G,pos,labels,font_size=16)

    plt.axis('off')
    plt.savefig("labels_and_colors.png") # save as png
    plt.show() # display


def draw_graph2(graph):
    #nx.draw_networkx(graph)
    plt.axis('off')
    plt.savefig("labels_and_colors.png") # save as png
    plt.show() # display

def print_output(communities):
    for community in communities:
        print community

if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print "USAGE: python pramod_setlur_community.pdf [INPUT_FILE] [IMAGE]"
    else:
        input_file = sys.argv[1]
        image = sys.argv[2]

        graph = read_input_to_graph(input_file)
        communities, max_modularity = compute_best_community(graph)
        print_output(communities)
        #draw_graph(image, communities, graph)
        draw_graph2(graph)