// written by @lxy1015545250

struct AvlNode {
    int      val;
    AvlNode* left;
    AvlNode* right;
    int      height;
    AvlNode( int val ) : val( val ), left( nullptr ), right( nullptr ), height( 1 ) {}
    ~AvlNode() {
        left  = nullptr;
        right = nullptr;
    }
};

class AvlTree {
private:
    int      i;
    AvlNode* root;

public:
    AvlTree() : root( nullptr ), i( 1 ) {}
    bool find( int v );
    bool insert( int v );
    bool remove( int v );

private:
    bool find( int v, AvlNode* node, AvlNode* parent );
    bool insert( int v, AvlNode*& node );
    bool remove( int v, AvlNode*& node );
    int  get_min_val( AvlNode* node );

    void        balance( AvlNode*& node );
    static void lrotate( AvlNode*& left, AvlNode*& parent );
    static void rrotate( AvlNode*& parent, AvlNode*& right );

    static int get_new_height( AvlNode* node );
    static int max( int a, int b );
    static int diff( AvlNode* l, AvlNode* r );
};

bool AvlTree::find( int v ) {
    i++;
    if ( root == nullptr )
        return false;
    for ( AvlNode* iter = root; iter != nullptr; ) {
        if ( iter->val == v )
            return true;
        if ( iter->val < v ) {
            iter = iter->right;
        }
        else {
            iter = iter->left;
        }
    }
    return false;
}

bool AvlTree::insert( int v ) {
    i++;
    bool ret = insert( v, root );
    if ( ret == true ) {
        balance( root );
    }
    return ret;
}

bool AvlTree::remove( int v ) {
    i++;
    bool ret = remove( v, root );
    if ( ret == true ) {
        balance( root );
    }
    return ret;
}

bool AvlTree::insert( int v, AvlNode*& node ) {
    if ( node == nullptr ) {
        node = new AvlNode( v );
        return true;
    }
    if ( node->val == v ) {
        return false;
    }
    if ( node->val < v ) {
        bool ret = insert( v, node->right );
        if ( ret ) {
            balance( node->right );
            return true;
        }
        return false;
    }
    if ( node->val > v ) {
        bool ret = insert( v, node->left );
        if ( ret ) {
            balance( node->left );
            return true;
        }
        return false;
    }
    return false;
}

bool AvlTree::remove( int v, AvlNode*& node ) {
    if ( node == nullptr ) {
        return false;
    }
    if ( node->val == v ) {

        AvlNode *l = node->left, *r = node->right;

        if ( l == nullptr && r == nullptr ) {  // 没有孩子
            delete node;
            node = nullptr;
            return true;
        }

        if ( l != nullptr && r != nullptr ) {  // 两个孩子
            // Attention! `n = node` is really really important, becacuse
            // when we remove the successor
            // the whole tree may mutate, and change *& node bacause it's a reference.
            // Debug this for hours.
            AvlNode* n     = node;
            int      value = get_min_val( node->right );

            remove( value );  // 这个被删除节点一定是单孩子情况
            n->val = value;

            return true;
        }

        {  // 一个孩子
            auto child = ( node->left != nullptr ) ? ( node->left ) : ( node->right );
            delete node;
            node = child;
            return true;
        }
    }
    if ( node->val < v ) {
        bool ret = remove( v, node->right );
        if ( ret == true ) {
            balance( node );
        }
        return ret;
    }
    else {  // node->val > v
        bool ret = remove( v, node->left );
        if ( ret == true ) {
            balance( node );
        }
        return ret;
    }
}

/**
 * 这个节点的右子树层数最高为1，删除这个节点，一定造成其父节点左子树高度减少1。
 * 删除这个结点可能造成全树结构改变，单独写一个函数比较麻烦。
 */
int AvlTree::get_min_val( AvlNode* node ) {
    if ( node == nullptr )
        return -1;
    while ( node->left != nullptr ) {
        node = node->left;
    }
    return node->val;
}

void AvlTree::balance( AvlNode*& node ) {
    if ( node == nullptr )
        return;
    AvlNode*& left  = node->left;
    AvlNode*& right = node->right;
    if ( diff( left, right ) == 2 ) {
        if ( diff( left->left, left->right ) > 0 ) {  // LL
            // cout << "LL rotate" << endl;
            lrotate( left, node );
        }
        else if ( diff( left->left, left->right ) < 0 ) {  // LR
            // cout << "LR rotate" << endl;
            rrotate( left, left->right );
            lrotate( left, node );
        }
        else {
            cerr << "balance error" << endl;
            return;
        }
    }
    else if ( diff( left, right ) == -2 ) {
        if ( diff( right->left, right->right ) < 0 ) {  // RR
            rrotate( node, right );
        }
        else if ( diff( right->left, right->right ) > 0 ) {  // RL
            lrotate( right->left, right );
            rrotate( node, right );
        }
        else {
            cerr << "balance error" << endl;
        }
    }
}

// 注意，这里传入的left和parent是耦合的。。
void AvlTree::lrotate( AvlNode*& left, AvlNode*& parent ) {
    AvlNode* new_parent = left;
    AvlNode* lr         = left->right;
    left->right         = parent;
    left                = lr;
    parent              = new_parent;
    get_new_height( parent->right );
    get_new_height( parent );
}

void AvlTree::rrotate( AvlNode*& parent, AvlNode*& right ) {
    AvlNode* new_parent = right;
    AvlNode* rl         = right->left;
    right->left         = parent;
    right               = rl;
    parent              = new_parent;
    get_new_height( parent->left );
    get_new_height( parent );
}

inline int AvlTree::max( int a, int b ) {
    return a > b ? a : b;
}

inline int AvlTree::get_new_height( AvlNode* node ) {
    auto l = node->left;
    auto r = node->right;
    int  lh, rh;
    if ( l == nullptr )
        lh = 0;
    else
        lh = l->height;

    if ( r == nullptr )
        rh = 0;
    else
        rh = r->height;

    node->height = max( lh, rh ) + 1;
    return node->height;
}

inline int AvlTree::diff( AvlNode* l, AvlNode* r ) {
    int lh, rh;
    if ( l == nullptr )
        lh = 0;
    else
        lh = l->height;

    if ( r == nullptr )
        rh = 0;
    else
        rh = r->height;

    return lh - rh;
}

class MyHashSet {
private:
    AvlTree* avl;

public:
    /** Initialize your data structure here. */
    MyHashSet() {
        avl = new AvlTree();
    }

    void add( int key ) {
        avl->insert( key );
    }

    void remove( int key ) {
        avl->remove( key );
    }

    /** Returns true if this set contains the specified element */
    bool contains( int key ) {
        return avl->find( key );
    }
};