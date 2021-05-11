package cp213;

import java.util.Scanner;

public class Movie {

	public final int FIRST_YEAR = 1800;
	public final String[] GENRES = {"science fiction", "fantasy", "drama", "romance", "comedy", "zombie", "action", "historical", "horror", "war" };
	public final double MAX_RATING = 10;
	public final double MIN_RATING = 0;

	public String title;
	public String director;
	
	public int year;
	public int genre;
	public double rating;

	public static void main(String[] args) {

		Movie obj1 = new Movie();
		Movie obj2 = new Movie("Dellamorte Dellamore", 1994, "Michele Soavi", 7.2, 3);
		Movie obj3 = new Movie("Zulu", 2013, " Jérôme Salle", 6.7, 2);

		System.out.println();
		System.out.println(obj1.toString());
		System.out.println();
		System.out.println(obj2.toString());
		System.out.println();
		System.out.println(obj3.toString());
		System.out.println();

		System.out.println(obj1.compareTo(obj1));
		System.out.println(obj3.compareTo(obj1));
		System.out.println(obj1.compareTo(obj2));

	}
	
// accessors

	public int getFirstYear() {
		
		return FIRST_YEAR;
		
	}

	public String[] getGenres() {
		
		return GENRES;
		
	}

	public double getMaxRating() {
		
		return MAX_RATING;
		
	}

	public double getMinRating() {
		
		return MIN_RATING;
		
	}

	public String getTitle() {
		
		return title;
		
	}

	public String getDirector() {
		
		return director;
		
	}

	public int getYear() {
		
		return year;
		
	}

	public int getGenre() {
		
		return genre;
		
	}

	public double getRating() {
		
		return rating;
		
	}

// mutators
	
	public String setTitle(final String arg) {
		
		title = arg;
		
		return getTitle();
		
	}

	public String setDirector(final String arg) {
		
		director = arg;
		
		return getDirector();
		
	}

	public int setYear(final int arg) {
		
		year = arg;
		
		return getYear();
		
	}

	public int setGenre(final int arg) {

		
		genre = arg;
		
		return getGenre();
		
	}
	
	public double setRating(final double arg) {
		
		rating = arg;
		
		return getRating();
		
	}

// additional public methods
	
	public String genreToName(final int genreNum) {
		
		String name = getGenres()[genreNum];
		
		return name;
		
	}

	public String genreMenu() {
		
		String choices = "0: science fiction \n1: fantasy \n2: drama \n3: romance \n4: comedy \n5: zombie \n6: action \n7: historical \n8: horror \n9: war \n";
		
		return choices;
		
	}

	public String toString() {
		String genreName = genreToName(genre);
		
		String theText = "Title: " + title + "\nYear: " + year + " \nDirector: " + director + "\nRating: " + rating + "\nGenre: " + genreName;
		
		return theText;
	
	}

	public int compareTo(Movie secondMovie) {

		int value = 0;

		if (getYear() != secondMovie.getYear()) {
			
			value = getYear() - secondMovie.getYear();
		
		} else {
			
			if (!getTitle().equalsIgnoreCase(secondMovie.getTitle())) {
				
				value = getFirstYear();
			
			}

			if (!getDirector().equalsIgnoreCase(secondMovie.getDirector())) {
				
				value = getFirstYear();
			
			}

			if (getGenre() != secondMovie.getGenre()) {
				
				value = getFirstYear();
			
			}

			if (getRating() != secondMovie.getRating()) {
				
				value = getFirstYear();
			
			}

		}

		return value;

	}

	public Movie() {
		
		Scanner keyboard = new Scanner(System.in);
		
		int inputYear;
		int inputGenre;
		double inputRating;		
		
		String director;

		// title
		System.out.print("Title: ");
		setTitle(keyboard.nextLine());

		
		// year
		System.out.print("Year: ");
		inputYear = keyboard.nextInt();
		
		while (inputYear < getFirstYear()) {
			
			System.out.print("Please enter a valid year (after 1800): ");
			
			inputYear = keyboard.nextInt();
			
		}
		
		setYear(inputYear);
		
		// fuck this catch for the line
		keyboard.nextLine();
		
		// director
		System.out.print("Director: ");
		director = keyboard.nextLine();
		setDirector(director);

		// rating
		System.out.print("Rating (0-10): ");
		inputRating = keyboard.nextDouble();
		
		while (inputRating < getMinRating() || inputRating > getMaxRating()) {
			
			System.out.print("Rating (0-10): ");
			inputRating = keyboard.nextDouble();
			
		}
		setRating(inputRating);
		
		// genre
		System.out.println("\n" + genreMenu());
		System.out.print("Genre: ");
		
		inputGenre = keyboard.nextInt();
		while (inputGenre > getGenres().length - 1 || inputGenre < 0) {
			
			System.out.print("Genre (0-8): ");
			inputGenre = keyboard.nextInt();
			
		}
		
		setGenre(inputGenre);

		// close keyboard
		keyboard.close();

	}

	public Movie(String arg1, int arg2, String arg3, double arg4, int arg5) {

		setTitle(arg1);
		
		if (arg2 >= getFirstYear()) {
			
			setYear(arg2);
			
		} else {
			
			System.out.println("Invalid year");
			
		}
		
		setDirector(arg3);
		
		if (arg4 <= getMaxRating() && arg4 >= getMinRating() ) {
			
			setRating(arg4);
			
		} else {
			
			System.out.println("Invalid rating");
			
		}

		if (arg5 < getGenres().length && arg5 >= 0) {
			
			setGenre(arg5);
			
		} else {
			
			System.out.println("Invalid genre");
			
		}

		

	}

}
