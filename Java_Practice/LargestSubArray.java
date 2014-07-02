import java.util.*;
import java.io.*;

public class LargestSubArray {

	public static void main(String args[]) {
		// ArrayList<Integer> a = new ArrayList<Integer>();
		// a.add(2);
		int[] arr = {1, 2, 3, -1};
		print(LargestSubArray(arr));
	}

	private static ArrayList<Integer> LargestSubArray(int[] arr) {
		ArrayList<Integer> subArr = new ArrayList<Integer>();
		return subArr;
	}

	// to avoid having to write out System.out.println()
	private static void print(String s) {
		System.out.println(s);
	}

	private static void print(int i) {
		System.out.println(i);
	}

	private static void print(ArrayList<Integer> arr) {
		for (int i = 0; i < arr.size(); i++)
			System.out.println(arr.get(i));
	}
}