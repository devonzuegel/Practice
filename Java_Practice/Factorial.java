import java.util.*;
import java.io.*;

public class Factorial {

	public static void main(String args[]) {
		print("Enter '-1' when you're done.\n");

		int x = 0;
		while (x != -1) {
			x = get_input_num();
			if (x == -1)		print("See you later!");
			else 						print(x + "! = " + factorial(x));
		}
	}

	private static int get_input_num() {
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {

			try {  // catches exceptions for unsuccessful line read
				print("Please enter a positive number: ");
				String line = br.readLine();

				try {  // catches exception for poorly-formed strings (not in integer format)
					int x = Integer.parseInt(line);
					if (x>=-1)		return x;
				} catch (NumberFormatException e) {}
				
			} catch (IOException ioe) {}

		}

	}

	private static int factorial(int x) {
		// BASE CASES
		if (x < 0)		return -1; // accounts for the case where the input is negative
		if (x == 0)		return 1;  // when we've reached 1, stop!
		
		// RECURSIVE CALL
		return x * factorial(x - 1);
	}

	// to avoid having to write out System.out.println()
	private static void print(String s) {
		System.out.println(s);
	}
}