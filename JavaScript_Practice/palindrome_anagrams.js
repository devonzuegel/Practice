function solution(S) {
    // creates a map of the character frequences in string S
    var map = char_frequencies(S);
    
    // checks to make sure that at most 1 character occurs an odd # of times
    one_odd = false;
    for (var x in map) {
        if (map[x]%2 == 1) {
            if (one_odd)  return 0; /* if this is the second time we've found
                                     * an odd-frequency character, we know that
                                     * it can't be an anagram of a palindrome */
            
            else    one_odd = true; /* if this is the first time we've found an
                                     * odd-frequency char, we set the flag so
                                     * that, if we find another, we return 0 */
        }
    }
    return 1;
}

function char_frequencies(S) {
    var map = {};
    for (var i = 0; i < S.length; i++) {
        if (S[i] in map)    map[S[i]]++;
        else                map[S[i]] = 1;
    }
    return map;
}