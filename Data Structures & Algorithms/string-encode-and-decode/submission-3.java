class Solution {

    // Given a list of strings, return a String such that each item 
    // in the list of strings is one string
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s.length()).append('#').append(s); //5#words
        }

        return sb.toString();
    }

    // Given a String, return a list of strings such that the items in 
    // each slots are seperated from that long string (with some seperator to know what is what)
    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();

        int i = 0;
        while (i < str.length()) {
            // find # to read length
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j)); // 5#words would be just 5 here (substring doesn't include j)

            // extract exactly the length characters 
            String s = str.substring(j + 1, j + 1 + length); // 5#words would be words() where () is the pointer as u need 1 more past for substring
            result.add(s);
            i = j + 1 + length;
        }

        return result;
    }
}
