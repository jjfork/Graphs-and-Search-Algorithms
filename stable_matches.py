import networkx as nx
import matplotlib.pyplot as plt
import random


def grindr(top_preferences, bot_preferences):
    n = len(top_preferences)
    dominated = []
    top_list = list(range(n))
    bot_list = list(range(n))
    free_tops = top_list[:]

    while free_tops:
        top = free_tops[0]
        preferences = top_preferences[top]

        for bot in preferences:
            if bot not in dominated:
                dominated.append(bot)
                free_tops.remove(top)
                break
            else:
                current_top = dominated[dominated.index(bot) - 1]
                bots_preferences = bot_preferences[bot]
                if bots_preferences.index(top) < bots_preferences.index(current_top):
                    dominated.remove(current_top)
                    free_tops.append(current_top)
                    dominated.append(bot)
                    free_tops.remove(top)
                    break
    matches = [(bot_list.index(bot), top) for top, bot in enumerate(dominated)]
    return matches


def plot_matches(matches):
    gr = nx.Graph()

    for bot, top in matches:
        gr.add_edge(f"Bot {bot}", f"Top {top}")

    # Separate top and bot nodes into two lists
    top_nodes = [node for node in gr.nodes if node.startswith('Top')]
    bot_nodes = [node for node in gr.nodes if node.startswith('Bot')]

    pos = nx.bipartite_layout(gr, top_nodes)

    edge_colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'pink', 'cyan', 'brown', 'gray']

    random.shuffle(edge_colors)

    nx.draw_networkx_nodes(gr, pos, nodelist=top_nodes, node_color='lightblue', node_size=800)
    nx.draw_networkx_nodes(gr, pos, nodelist=bot_nodes, node_color='pink', node_size=800)
    nx.draw_networkx_edges(gr, pos, edge_color=edge_colors)
    nx.draw_networkx_labels(gr, pos, font_size=10, font_weight='bold')

    plt.title('Stable Marriage Matches')
    plt.axis('off')
    plt.show()


# Example usage
top_preferences = [[1, 2, 3, 4, 5, 6, 0], [6, 0, 5, 2, 3, 4, 1], [1, 5, 2, 6, 4, 0, 3],
                   [3, 1, 4, 2, 0, 6, 5], [0, 4, 6, 3, 1, 5, 2], [3, 2, 5, 4, 0, 1, 6], [1, 2, 3, 4, 5, 6, 0]]
bot_preferences = [[6, 5, 2, 1, 4, 3, 0], [0, 6, 1, 3, 2, 4, 5], [6, 5, 3, 0, 2, 4, 1],
                   [1, 2, 4, 3, 0, 6, 5], [4, 3, 0, 2, 1, 6, 5], [6, 0, 4, 2, 5, 3, 1], [6, 0, 5, 3, 4, 1, 2]]

matches = grindr(top_preferences, bot_preferences)
for bot, top in matches:
    print(f"Bot {bot} matches with Top {top}")

plot_matches(matches)
