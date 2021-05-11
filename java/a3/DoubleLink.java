package cp213;

/**
 * The class for doubly-linked data structures. Provides attributes and
 * implementations for getLength, isEmpty, and toArray methods. The head
 * attribute is the first node in any doubly-linked list and last is the last
 * node.
 *
 * @author
 * @version 2019-10-08
 * 
 */
public class DoubleLink {

    // First node of double linked list
    private DoubleNode head = null;

    // Number of elements lastly stored in linked list
    private int length = 0;

    // Last node of double linked list.
    private DoubleNode last = null;

    /**
     * Adds a new Movie element to the list at the head position before the previous
     * head, if any. Increments the length of the List.
     *
     * @param value The value to be added at the head of the list.
     *
     * @return true if node is added successfully, else false.
     */
    public final boolean addNode(final Movie value) {

        DoubleNode newestHead =  head;
        
        DoubleNode oldestHead = new DoubleNode(value, null, newestHead);

        boolean added = false;

        if ( head != null) {
        	
            newestHead.setPrev(oldestHead);
            
        }

         head = oldestHead;

        if ( last == null) {
        	
             last = newestHead;
             
        }

        length += 1;
        
        added = true;

        return added;
        
    }

    /**
     * Removes the value at the front of this List.
     *
     * @return The value at the front of this List.
     */
    public Movie removeFront() {

        Movie value =  head.getValue();

        DoubleNode oldestHead =  head.getNext();

        if (oldestHead == null && length == 1) {
        	
            // only 1 item
        	 length = 0;
             head = null;
             last = null;
             
             
        } else {
        	
            // more than 1 item
             head = oldestHead;
             
             length -= 1;
             
        }

        return value;
        
    }

    /**
     * Returns the head element in the linked structure. Must be copy safe.
     *
     * @return the head node.
     */
    public final DoubleNode getHead() {
    	
        return  head;
        
    }

    /**
     * Returns the last number of elements in the linked structure.
     *
     * @return the value of length.
     */
    public final int getLength() {
    	
        return  length;
        
    }

    /**
     * Returns the last node in the linked structure. Must be copy safe.
     *
     * @return the last node.
     */
    public final DoubleNode getLast() {
    	
        return  last;
        
    }

    /**
     * Determines whether the double linked list is empty or not.
     *
     * @return true if list is empty, false otherwise.
     */
    public final boolean isEmpty() {
    	
        return  length == 0;
        
    }

    /**
     * Returns all the data in the list in the form of an array.
     *
     * @return The array of Movie elements. Must be copy safe
     */
    public final Movie[] toArray() {

        Movie[] bigMovies = new Movie[ getLength()];

        DoubleNode last =  getHead();
        
        int count = 0;

        while (count < length) {

            bigMovies[count] = last.getValue();

            if (last.getValue() != last.getValue()) {
            	
                last = last.getNext();
                
            }

            count++;
        }

        return bigMovies;

    }

}
