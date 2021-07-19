## DSA NOTES From William Fiset's YT Channel

1. Abstract data type vs data structures: ADT is only an interface to a DS. Does not outline how the DS is implemented in which language. Eg: one ADT is list, and its DS can be dynamic array or linked list.
2. Static arrays: fixed container, indexable, sequential storage. Used in IO routines, buffers, dynamic prog etc.
3. Dynamic arrays can be implemented using static array - if capacity during insertion reached, make new static array of double size. And so on.
4. Dot(.) and arrow(->) operator difference: arrow is used when we are referring to attributes of a pointer to an object, dot when referring to attribute of object itself. ptr->name is the same as (*ptr).name.
5. Queue used for BFS, stack for DFS.
6. All heaps must be trees i.e. cannot contain cycles.