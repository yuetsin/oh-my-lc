// written by @akshathaSreeramaprasad

type Node struct {
	Num  int
	Next *Node
}

type MyLinkedList struct {
	Length int
	Head   *Node
}


/** Initialize your data structure here. */
func Constructor() MyLinkedList {
    list := MyLinkedList{
		Length: 0,
		Head:   nil,
	}
	return list
}


/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (list *MyLinkedList) Get(index int) int {
	if index < 0 {
		return -1
	}

	if list.Head == nil {
		return -1
	}

	curNode := list.Head
	for i := 0; i <= index && curNode != nil; i++ {
		if i == index {
			return curNode.Num
		} else {
			curNode = curNode.Next
		}
	}
	return -1
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (list *MyLinkedList) AddAtHead(val int) {
	newNode := &Node{
		Num:  val,
		Next: nil,
	}
	// add to an empty list
	if list.Head == nil {
		list.Head = newNode
	} else {
		newNode.Next = list.Head
		list.Head = newNode
	}
	list.Length++
}

/** Append a node of value val to the last element of the linked list. */
func (list *MyLinkedList) AddAtTail(val int) {
	newNode := &Node{
		Num:  val,
		Next: nil,
	}
	//add to an empty list
	if list.Head == nil {
		list.Head = newNode
	} else {
		curNode := list.Head
		for curNode.Next != nil {
			curNode = curNode.Next
		}
		curNode.Next = newNode
		list.Length++
	}
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
  the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (list *MyLinkedList) AddAtIndex(index int, val int) {
	newNode := &Node{
		Num:  val,
		Next: nil,
	}
	curNode := list.Head
	if index == 0 {
		list.AddAtHead(val)
		return
	}
	if index != 0 && index == list.Length {
		list.AddAtTail(val)
		return
	}
	addBefore := list.GetNodeAtIndex(index)
	//if the index to be added at is at the beginning of the list
	if addBefore != nil && list.Head == addBefore {
		newNode.Next = addBefore
		list.Head = newNode
		list.Length++
	} else if addBefore != nil {
		// advance the curNode pointer to the node before the indexth node
		for curNode != nil && curNode.Next != nil && curNode.Next != addBefore {
			curNode = curNode.Next
		}
	}

	// add the new node before the indexth node
	if addBefore != nil && curNode.Next == addBefore {
		newNode.Next = addBefore
		curNode.Next = newNode
		list.Length++
	}
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (list *MyLinkedList) DeleteAtIndex(index int) {
	// invalid index
	if index < 0 {
		return
	}
	// invalid index
	if index >= list.Length {
		return
	}

	curNode := list.Head
	// add at head
	if index == 0 {
		list.Head = curNode.Next
		return
	}

	prevNode := list.GetNodeAtIndex(index - 1)
	// if there is only omne element in the list
	if prevNode == curNode && curNode.Next == nil {
		list.Length--
		list = nil
	} else {
		for i := 0; i < index; i++ {
			curNode = curNode.Next
			if i == index-1 {
				prevNode.Next = curNode.Next
			}
		}
		list.Length--
	}
}

func (list *MyLinkedList) GetNodeAtIndex(index int) *Node {
	currentNode := list.Head
	count := 0
	for count < index && currentNode != nil && currentNode.Next != nil {
		currentNode = currentNode.Next
		count++
	}
	if count == index {
		return currentNode
	} else if count == 0 {
		return currentNode
	}
	return nil
}