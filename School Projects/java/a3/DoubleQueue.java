package cp213;

/**
 * A queue structure of Movie objects. Only the Movie values contained in the
 * queue are visible through the standard queue methods. The Movie values are
 * stored in a DoubleLink object provided in class as attribute.
 *
 * @author
 *
 * @version 2019-10-08
 *
 * @param Movie this data structure value type.
 */
public class DoubleQueue {

    // First node of the queue
    private DoubleLink values = null;

    /**
     * Combines the contents of the left and right Queues into the current Queue.
     * Moves nodes only - does not move value or call the high-level methods insert
     * or remove. left and right Queues are empty when done. Nodes are moved
     * alternately from left and right to this Queue.
     *
     * @param source1 The front Queue to extract nodes from.
     * @param source2 The second Queue to extract nodes from.
     */
    public void combine(final DoubleQueue source1, final DoubleQueue source2) {
        // your code here
    }

    /**
     * Adds value to the rear of the queue.
     *
     * @param value The value to added to the rear of the queue.
     */
    public void insert(final Movie value) {

        DoubleLink listNew = new DoubleLink();

        if (values != null) {

            if (!values.isEmpty()) {

                Movie oldTemp = values.removeFront();
                listNew.addNode(oldTemp);

            }

            values.addNode(value);

            while (!listNew.isEmpty()) {
                Movie newTemp = listNew.removeFront();
                values.addNode(newTemp);
            }

        } else {

            values = new DoubleLink();
            values.addNode(value);

        }

    }

    /**
     * Returns the front value of the queue and removes that value from the queue.
     * The next node in the queue becomes the new front node.
     *
     * @return The value at the front of the queue.
     */
    public Movie remove() {

        Movie result = null;
        if (values != null) {
            result = values.removeFront();
        }
        return result;

    }

    /**
     * Returns the value at the front. Must be copy safe
     *
     * @return the value at the front.
     */
    public Movie peekFront() {

        Movie result = null;
        if (values != null) {
            DoubleNode head = values.getHead();
            result = head.getValue();
        }

        return result;

    }

    /**
     * Returns the value at the rear. Must be copy safe.
     *
     * @return the value at the rear.
     */
    public Movie peekRear() {

        Movie result = null;
        if (values != null) {
            DoubleNode head = values.getLast();
            result = head.getValue();
        }

        return result;

    }

    /**
     * Returns all the data in the queue in the form of an array.
     *
     * @return The array of Movie elements. Must be copy safe
     */
    public final Movie[] toArray() {

        Movie[] newMovie;

        if (values != null) {
        	newMovie = values.toArray();
        } else {
        	newMovie = new Movie[0];
        }

        return newMovie;
    }

}
