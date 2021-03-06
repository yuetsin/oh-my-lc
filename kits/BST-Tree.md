# BST

> ~~Best Suicide Time~~ Binary Search Tree

二叉搜索树。AVL 树、红黑树都是 BST 的特殊形式。

## Definition

如果某一棵树符合以下条件之一，则称之为 BST：

1. 是空树。
2. 具有下列性质的二叉树：
	1. 任意有左子树的节点，其左子树上所有节点的值都小于其节点的值；
	2. 任意有右子树的节点，其右子树上所有节点的值都大于**等于**其节点的值。

BST 的任意子树也都是 BST。

## Search

BST 最好的性质，就是「可以以 $O(k)$ 的时间完成搜索」。

> $k$ 是树的深度。

> 最好情况下，如果我们能始终维持一棵树的「平衡」（去看 AVL 树那节中关于「平衡」的说明），即使得 $k \approx \log n$，就能以 $O(\log n)$ 的时间完成一次搜索。

> 当然，如果 BST 实在太不平衡，以至于其退化成了一个排序好元素组成的链表的话，那就是 $k \approx n$，即搜索需要花上 $O(n)$ 的时间了。

找的方式也好简单。从根节点开始。如果目标值小于当前节点的值，你就往左。否则，你就往右。

> 是 不 是 很 简 单 呢 ？