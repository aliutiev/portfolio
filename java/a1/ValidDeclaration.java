package cp213;
import java.util.Scanner;

public class ValidDeclaration {
	
	public static void main(String args[]) {
		
		String abc = "Fuckery";
		System.out.print(abc.substring(2, 3));
		if (abc.substring(2, 3) == "c") {
			System.out.println("true");
			
		}
		
		Scanner keyboard = new Scanner(System.in);
		boolean result;
		
		System.out.print("Enter a string: ");
		String a = keyboard.nextLine();
		
		result = isValid(a);
		
		

		
		if (result) {
			System.out.printf("'%s' is a valid Java variable definition.%n", a);
		} else {
			System.out.printf("'%s' is not a valid Java variable definition.%n", a);
		}
		
	}
	
	public static boolean isValid(final String statement) {
		
		int count = 0;
		int nextIndex;
		int length = statement.length();
		boolean result = true;
		
		if (statement == "") {
			result = false;
		} else if (statement.charAt(length - 1) != 59) {
			result = false;
		} else {
			
			// check 1 for spaces
			if (statement.charAt(count) == 32) { 
				while (statement.charAt(count) == 32) {
					count += 1;
					System.out.print(count);
				}
			}
			
//			if (statement.charAt(count) == ch));
//				System.out.print("OOF");
//			
			// getting next white space
//			nextIndex = count;
			

			
			
			// int byte long char, short, , , , float, double boolean.The
//			if ((count - nextIndex) == 3)
//			{
//				System.out.println("int type");
//			} else if ((count - nextIndex) == 4) {
//				System.out.println("4 letter type");
//			} else if ((count - nextIndex) == 5) {
//				System.out.println("5 letter type");
//			} else if ((count - nextIndex) == 6) {
//				System.out.println("6 letter type");
//			} else {
//				result = false;
//			}
			
		}
		
		
		
		
			
		
		
		return result;
		
	}
	
}



	
/*** Determines if the given string is a valid Java variable
 *  definition of the form “dataType variableName;”.
 *  Variables names must start with a letter or an underscore, but 
 *   cannot be an underscore alone.The rest of the variable name 
 *   may consist of letters, numbers andunderscores.Permitted data 
 *   types are byte, short, char, int, long, float, double and
 *   boolean.The statement must terminate at ‘;’.** 
 *   @param statement*            a string to test as a Java statement* 
 *   @return true ifstatementis a valid Java statement, false * otherwise*/
