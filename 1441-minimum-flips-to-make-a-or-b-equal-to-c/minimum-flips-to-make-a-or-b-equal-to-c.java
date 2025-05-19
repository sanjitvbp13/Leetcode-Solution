class Solution {
    public int minFlips(int a, int b, int c) {
        int flips = 0;

        for (int i = 0; i < 32; i++) {
            int a_bit = (a >> i) & 1;
            int b_bit = (b >> i) & 1;
            int c_bit = (c >> i) & 1;

            int or_bit = a_bit | b_bit;

            if (or_bit != c_bit) {
                if (c_bit == 1) {
                    flips += 1; 
                } else {
                    flips += a_bit + b_bit; 
                }
            }
        }

        return flips;
    }
}
