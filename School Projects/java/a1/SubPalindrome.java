package cp213;
import java.util.Scanner;

public class SubPalindrome {
	
	public static void main(String[] args) {
		// test code here}
		/*** Determines and displays if any substrings of s are palindromes.
		 * The method tests all substrings of length minLen and more. *
		 * If any substrings are found to be palindromes, 
		 * the message is displayed in the form "Following substring(s) of the string '...' are
		 * palindrome(s): '..', '..'”. If none of the substrings are
		 * palindrome, the output is:"No substrings of the string '..' are palindrome."
		 */
		
		Scanner keyboard = new Scanner(System.in);
		
		System.out.print("Enter a string of size 1-10 characters:");
		String a = keyboard.nextLine();
		int length = a.length();
		
		if (length == 0) {
			System.out.println("'' is not a valid input, size less than 1");
		} else if (length > 10) {
			System.out.printf("'%s' not a valid input, size more than 10%n", a);
		} else {
			testSubPalindromes(a, length);			
		}		
	}
	
	public static void testSubPalindromes(final String s, int minLen) {
		// stating values
		String finalString = "";
		int leftIndex;
		int rightIndex = minLen - 1;
		
		// getting indices
		if (rightIndex % 2 == 0) {
			leftIndex = rightIndex / 2;
			rightIndex = leftIndex;
		} else {
			leftIndex = (rightIndex - 1) / 2;
			rightIndex = leftIndex + 1;
		}
		
		// loop for each substring
		while (leftIndex >= 0) {
			String sNew = s.substring(leftIndex, rightIndex + 1);
			
			// handle exceptions
			sNew = sNew.toLowerCase();
			
			int length = sNew.length();	
			
			System.out.print(leftIndex + " " + rightIndex + " | " + sNew + " ");	
			
			leftIndex -= 1;
			rightIndex += 1;
			
			boolean result = isPalindrome(sNew);
			
		}
	}
	
		
	
	
	/*** Determines if s is a palindrome. Ignores case, spaces, digits,
	 * and punctuation in the string parameter s.** 
	 @param s a string
	 @return true if s is a palindrome, false otherwise
	 */
	
	public static boolean isPalindrome(final String s) {
		// method code here
		
		return true;
		
	}

}
