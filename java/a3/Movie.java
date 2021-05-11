package cp213;

import java.util.Scanner;

public class Movie {
	
	static final int FIRST_YEAR = 1800;
	static final String [] GENRES = {"science fiction", "fantasy", "drama", "romance", "comedy",
			"zombie", "action", "historical", "horror", "war"};
	static final double MAX_RATING = 10.0;
	static final double MIN_RATING = 0.0;
	
	private String title;
	private String director;
	private int year;
	private int genre;
	private double rating;

	public static void main(final String[] args) {
	// Movie testing
		DoubleQueue movies = new DoubleQueue();

		movies.insert(new Movie("Dellamorte Dellamore", "Michele Soavi", 1994, 3, 7.2));
		
		movies.insert(new Movie("Zulu", "Jerome Salle", 2013, 2, 6.7));

		movies.insert(new Movie("Zulu", "Cy Endfield", 1964, 9, 7.8));
		
		Movie [] moviesArray = movies.toArray();
		
		System.out.println(movies.peekFront());
		
		System.out.println(movies.peekFront());

		System.out.println(movies.remove());

		System.out.println(movies.peekFront());
		
		System.out.println(movies.peekFront());		

		movies.insert(new Movie("Zulu", "Jerome Salle", 2013, 2, 6.7));

		movies.insert(new Movie("Zulu", "Cy Endfield", 1964, 9, 7.8));
		
    }
	
	public int getFirstYear() {
		return FIRST_YEAR;
	}
	
	public String [] getGenres() {
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

	public void setTitle(final String arg) {
		title = arg;
	}
	
	public void setDirector(final String arg) {
		director = arg;
	}
	
	public void setYear(final int arg) {
		year = arg;
	}
	
	public void setGenre(final int arg) {
		genre = arg;
	}
	
	public void setRating(final double arg) {
		rating = arg;
	}

	public String genreToName(int arg) {
		return getGenres()[arg];
	}

	public String genreMenu() {
		String menu = new String();
		for (int i=0; i<getGenres().length; i++)
			menu = menu.concat(""+i+": "+getGenres()[i]+"\n");
		return menu;
	}

	public String toString() {
		return "Title: "+getTitle()+"\nYear: "+getYear()+"\nDirector: "+getDirector()+"\nRating: "+
				getRating()+"\nGenre: "+genreToName(getGenre());
	}

	public int compareTo(Movie arg) {
		if( (getTitle().compareToIgnoreCase(arg.getTitle()))!=0 )
			return getYear()==arg.getYear()?getFirstYear():getYear()-arg.getYear();

		if( getYear()!=arg.getYear() )
			return getYear()-arg.getYear();

		if( (getDirector().compareToIgnoreCase(arg.getDirector()))!=0 )
			return getYear()==arg.getYear()?getFirstYear():getYear()-arg.getYear();

		if( getRating()!=arg.getRating() )
			return getYear()==arg.getYear()?getFirstYear():getYear()-arg.getYear();

		if( getGenre()!=arg.getGenre() )
			return getYear()==arg.getYear()?getFirstYear():getYear()-arg.getYear();
		
		return 0;
	}

	public Movie() {
		Scanner keyboard = new Scanner(System.in);
		
		System.out.print("Title: ");
		String arg = keyboard.nextLine();
		setTitle(arg);

		System.out.print("Year: ");
		arg = keyboard.nextLine();
		setYear(Integer.parseInt(arg));
		
		System.out.print("Director: ");
		arg = keyboard.nextLine();
		setDirector(arg);

		do {
			System.out.print("Rating: ");
			arg = keyboard.nextLine();
			setRating(Double.parseDouble(arg));
		}while(Double.parseDouble(arg)>10.0 || Double.parseDouble(arg)<0.0);
		
		do {
			System.out.print(genreMenu());
			System.out.print("Genre: ");
			arg = keyboard.nextLine();
			setGenre(Integer.parseInt(arg));
		}while(Integer.parseInt(arg)>9 || Integer.parseInt(arg)<0);
		keyboard.close();
	}
	
	public Movie(String arg1, String arg2, int arg3, int arg4, double arg5) {
		setTitle(arg1);
		setDirector(arg2);
		setYear(arg3);
		setGenre(arg4);
		setRating(arg5);
	}
}
