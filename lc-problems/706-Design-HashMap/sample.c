
// written by @balban

#include <stdio.h>
#include <stdlib.h>

struct link {
    struct link* next;
    struct link* prev;
    int          key;
    int          val;
};

void list_init( struct link* l ) {
    l->prev = l;
    l->next = l;
}

int list_empty( struct link* l ) {
    return ( l->prev == l && l->next == l );
}

void list_add( struct link* list, struct link* l ) {
    struct link* next = list->next;

    list->next = l;
    l->prev    = list;

    l->next    = next;
    next->prev = l;
}

void list_remove( struct link* l ) {
    struct link *prev, *next;
    if ( list_empty( l ) ) {
        return;
    }
    prev = l->prev;
    next = l->next;

    prev->next = next;
    next->prev = prev;
    l->prev    = l;
    l->next    = l;

    return;
}

#define ENTRIES 50000
typedef struct {
    struct link array[ ENTRIES ];
} MyHashMap;

// 10001107 -> prime number.

/** Initialize your data structure here. */

MyHashMap* myHashMapCreate() {
    MyHashMap* m = malloc( sizeof( MyHashMap ) );

    for ( int i = 0; i < ENTRIES; i++ ) {
        list_init( &m->array[ i ] );
    }
    return m;
}

int hash( int key ) {
    return key % ENTRIES;
}

struct link* myHashMapGetRef( MyHashMap* obj, int key );

/** value will always be non-negative. */
void myHashMapPut( MyHashMap* obj, int key, int value ) {
    int          index = hash( key );
    struct link* l;
    struct link* ref;

    ref = myHashMapGetRef( obj, key );

    if ( ref == NULL ) {
        l = malloc( sizeof( struct link ) );
        list_init( l );
        l->key = key;
        l->val = value;
        list_add( &obj->array[ index ], l );
    }
    else {
        ref->val = value;
    }
}

/** Created a version that returns the reference to the linked list element, if it exists. I needed it for same-key updates. */
struct link* myHashMapGetRef( MyHashMap* obj, int key ) {
    int          index = hash( key );
    struct link* list  = &obj->array[ index ];
    struct link* l     = list->next;

    // Iterate on the list for that key, return value if key matches to a list element.
    while ( l != list ) {
        if ( l->key == key ) {
            return l;
        }
        l = l->next;
    }
    return NULL;
}

/** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
int myHashMapGet( MyHashMap* obj, int key ) {
    int          index = hash( key );
    struct link* list  = &obj->array[ index ];
    struct link* l     = list->next;

    // Iterate on the list for that key, return value if key matches to a list element.
    while ( l != list ) {
        if ( l->key == key ) {
            return l->val;
        }
        l = l->next;
    }

    return -1;
}

/** Removes the mapping of the specified value key if this map contains a mapping for the key */
void myHashMapRemove( MyHashMap* obj, int key ) {
    int          index = hash( key );
    struct link* list  = &obj->array[ index ];
    struct link* l     = list->next;

    // Iterate on the list for that key, return value if key matches to a list element.
    while ( l != list ) {
        if ( l->key == key ) {
            list_remove( l );
            free( l );
            return;
        }
        l = l->next;
    }

    return -1;
}

void myHashMapFree( MyHashMap* obj ) {
    for ( int i = 0; i < ENTRIES; i++ ) {
        struct link* list = &obj->array[ i ];
        struct link* l;
        struct link* cur;

        if ( !list_empty( list ) ) {
            l = list->next;

            while ( l != list ) {
                cur = l;
                l   = l->next;
                list_remove( cur );
                free( cur );
            }
        }
    }
    free( obj );
}

/**
 * Your MyHashMap struct will be instantiated and called as such:
 * MyHashMap* obj = myHashMapCreate();
 * myHashMapPut(obj, key, value);

 * int param_2 = myHashMapGet(obj, key);

 * myHashMapRemove(obj, key);

 * myHashMapFree(obj);
*/