#include <stdio.h>
#include <limits.h>
#include <vector>
#include <cmath>
#include <iostream>

using std::vector;

// 一共四次
#define TIME 4

// 顶点的数量
#define V 12

// OD 网格数量
#define TEST_CASE_COUNT 12

// minDistance: 从还没访问过的顶点中，获取一条最短的路径。
// sptSet 是顶点是否已经被「访问」的记录数组。

double minDistance(double dist[], bool sptSet[]) {
    // 最小值首先初始化为 INT_MAX（最大的整数），用来初始化
    double min = INFINITY;
    int    min_index;

    for (int v = 0; v < V; v++) {
        // 在找到一个未访问的顶点（sptSet[v] 为非）且距离小于当前的最小值的话
        if (sptSet[v] == false && dist[v] <= min) {
            // 就说明找到了一个更小的，记录下最小值 dist[v] 和最小值对应的顶点索引 min_index
            min = dist[v], min_index = v;
        }
    }
    // 把最小顶点索引返回
    return min_index;
}

// printSolution 只是用来打印最短路径的 没啥说的
void printSolution(double dist[], int n) {
    // printf("Vertex   Distance from Source\n");
    for (int i = 0; i < V; i++) {
        std::cout << dist[i] << '\t';
    }
    std::cout << '\n';
}

typedef vector<int> vector_int;
vector<vector_int>  visitedPath;

vector<int> getVisited(int toWhere) {
    return visitedPath[toWhere];
}

// dijkstra 函数是用来计算结果的。src 是起始顶点的索引。graph 是如图所示的有向图存储方式
void dijkstra(double graph[V][V], int src, bool printit = false) {
    visitedPath.clear();
    for (size_t i = 0; i < V; i++) {
        visitedPath.push_back(vector<int>());
        visitedPath[i].push_back(src);
    }

    double dist[V];  // dist[i] 保存着从起始点到 i 顶点的最小距离。

    bool sptSet[V];  // 如果我们找到的最短路径已经包括了顶点 i，那么就把 sptSet[i] 设置为 true。
                     // 否则，设置其为 false，代表这个点还没被加入「最短路径」之中。

    // 初始情况下，最小距离都未知，都设定为 INT_MAX（一个很大的无用值），sptSet 都设定为 false（都还没被加入到最短路径之中）
    for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, sptSet[i] = false;

    // src 是你指定的起始顶点位置
    dist[src] = 1.0;

    // 对于每一个顶点，都要找出一条最短路径
    for (double count = 0; count < V - 1; count++) {
        // 每一次，都找出当前情况下 距离最小的、不在「已选择集合」之中的顶点，记为 u
        int u = minDistance(dist, sptSet);

        // 并将 u 顶点 sptSet 设置为 True，也就是把它放到「已选择集合」之中，也就是把它视作最短路径的一员。
        sptSet[u] = true;

        // 由于一个顶点被加入到了最短路径里，因此最短路径可能会产生变化。我们需要更新所有顶点的最短路径
        for (int v = 0; v < V; v++) {

            // 只有那些尚未被纳入 sptSet 集合中的点才有更新的必要，已经加入最短路径集合里的点无需被更新。
            // 因此第一个条件就是 !sptSet[v]

            // 第二个条件：graph[u][v]，也就是他们之间的权值不是 0。是 0 只有可能在 u = v 时出现。不考虑

            // 第三个条件：dist[u] != INT_MAX：INT_MAX 是我们设定的一个无效标记，代表他们之间不连通。不连通的话也没有必要更新

            // 第四个条件：最重要的条件：dist[u] + graph[u][v] < dist[v]

            // 也就是：我从 src 点走到 u，再经过 u 走到 v 两段路程加起来比起直接走到 dist[v] 的路程更短，那才有更新的必要。

            // 我们要理解：为什么会产生最短路径的变化？因为新的顶点进入之后，可能出现绕路走反而距离更短的情况。也只有这种情况下才可能出现距离缩水。
            // 所以在四个条件全部满足时，
            // 将 dist[v] 缩小到“绕路”距离（其实比原来更短）dist[u] + graph[u][v]。

            if (!sptSet[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v]) {
                dist[v]        = dist[u] + graph[u][v];
                visitedPath[v] = visitedPath[u];
                visitedPath[v].push_back(v);
            }
        }
    }

    if (printit) {
        std::cout << '#' << src + 1 << '\t';
        // 最后打印就可以啦。
        printSolution(dist, V);
    }
}

// 最后在 main 函数里调用一下就可以了。
int main() {

    int    src_point = 0;
    double QValue[V][V];

    for (size_t i = 0; i < V; i++) {
        for (size_t j = 0; j < V; j++) {
            // 首先大家都没有拥堵。所以
            // Q 全部设置为 0
            QValue[i][j] = 0.0;
        }
    }

    double QCoe[V][V] = { { 0.0, 0.02, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 1 */
                          { 0.02, 0.0, 0.03, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 },  /* Node 2 */
                          { 0.0, 0.03, 0.0, 0.0, 0.0, 0.06, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 3 */
                          { 0.01, 0.0, 0.0, 0.0, 0.04, 0.0, 0.0, 0.03, 0.0, 0.0, 0.0, 0.0 },  /* Node 4 */
                          { 0.0, 0.05, 0.0, 0.0, 0.0, 0.05, 0.0, 0.04, 0.0, 0.0, 0.0, 0.0 },  /* Node 5 */
                          { 0.0, 0.0, 0.06, 0.03, 0.0, 0.0, 0.0, 0.0, 0.05, 0.0, 0.0, 0.0 },  /* Node 6 */
                          { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0 },    /* Node 7 */
                          { 0.0, 0.0, 0.0, 0.0, 0.04, 0.0, 0.06, 0.0, 0.0, 0.0, 0.01, 0.0 },  /* Node 8 */
                          { 0.0, 0.0, 0.0, 0.0, 0.0, 0.05, 0.0, 0.04, 0.0, 0.0, 0.0, 0.01 },  /* Node 9 */
                          { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.05, 0.0 },   /* Node 10 */
                          { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.05, 0.0, 0.03 },  /* Node 11 */
                          { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.03, 0.0 } }; /* Node 12 */

    int    time           = 0;
    double time_cnt[TIME] = { 0.4, 0.3, 0.2, 0.1 };
    /* 注意 graph 的调用方式。graph[i][j] 代表顶点 i 到顶点 j 的边权值。0 意味着不连通。 */
    double graph[V][V] = { { 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 1 */
                           { 3.0, 0.0, 2.0, 0.0, 1.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 2 */
                           { 0.0, 2.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 3 */
                           { 2.0, 0.0, 0.0, 0.0, 2.5, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 4 */
                           { 0.0, 1.5, 0.0, 0.0, 0.0, 1.5, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0 },   /* Node 5 */
                           { 0.0, 0.0, 1.0, 3.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0 },   /* Node 6 */
                           { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0 },   /* Node 7 */
                           { 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.5, 0.0, 0.0, 0.0, 3.0, 0.0 },   /* Node 8 */
                           { 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 3.5, 0.0, 0.0, 0.0, 3.0 },   /* Node 9 */
                           { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0 },   /* Node 10 */
                           { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 1.0, 0.0, 3.5 },   /* Node 11 */
                           { 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 3.5, 0.0 } }; /* Node 12 */
    double real_graph[V][V];

    const int startPoints[4]       = { 1, 3, 10, 12 };
    const int endPoints[4]         = { 1, 3, 10, 12 };
    const int ODDistribution[4][4] = { { 0, 300, 400, 500 }, { 300, 0, 100, 250 }, { 400, 100, 0, 600 }, { 500, 250, 600, 0 } };
    while (time < TIME) {
        std::cout << "\n\n\n==== 报告 =====\n\n\n这是第 " << time + 1 << "次 OD 迭代。此次分配系数为 " << time_cnt[time] << "。" << std::endl;

        for (size_t i = 0; i < V; i++) {
            for (size_t j = 0; j < V; j++) {
                // 计算真正权值。
                real_graph[i][j] = graph[i][j] + QValue[i][j] * QCoe[i][j];
                if (real_graph[i][j] != 0.0) {
                    std::cout << "信息：这次 #" << i + 1 << "到 #" << j + 1 << " 的权值为 " << real_graph[i][j] << "。\n";
                }
            }
        }
        for (int i = 0; i < 4; ++i) {
            dijkstra(graph, startPoints[i] - 1);
            for (int j = 0; j < 4; ++j) {
                if (i == j) {
                    continue;
                }
                vector<int> visit_path = getVisited(j);
                if (visit_path.size() > 1) {
                    std::cout << "\n发现拥塞路径。";
                    for (int k = 0; k < visit_path.size(); ++k) {
                        std::cout << "=> #" << visit_path[k] + 1;
                    }
                    std::cout << "。下次将更新他们的权值。\n";
                    for (int im = 0; im < visit_path.size() - 1; ++im) {
                        // 找到了这条拥挤路径！这条路上的 ODDistribution 全部设置。
                        QValue[visit_path[im]][visit_path[im + 1]] = time_cnt[time] * double(ODDistribution[i][j]);

                        std::cout << "从点 #" << visit_path[im] + 1 << " 到点 #" << visit_path[im + 1] + 1 << " 之间的 Q 值被设置为 " << QValue[visit_path[im]][visit_path[im + 1]] << "。\n";
                    }
                }
            }
        }
        std::cout << "\n===== 报告 ===== \n此次迭代之后，各点之间的最短路径长是：\n";
        for (int i = 0; i < V; ++i) {
            std::cout << "\t#" << i + 1;
        }
        std::cout << '\n';
        for (int i = 0; i < V; ++i) {
            dijkstra(real_graph, i, true);
        }
        ++time;
    }
    return 0;
}