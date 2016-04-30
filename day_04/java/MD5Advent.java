import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;


public class MD5Advent {

    private static void findMinimumSatisfyingNumber(String token) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        int i = 1;
        while (true) {
            md.update(String.format("%s%d", token, i++).getBytes(StandardCharsets.US_ASCII));
            byte[] digest = md.digest();

            StringBuilder sb = new StringBuilder();
            for (byte b : digest) {
                sb.append(String.format("%02X", b));
            }
            if (sb.toString().startsWith("00000")) {
                System.out.println(i - 1);
                break;
            }
        }
    }

    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException {
        findMinimumSatisfyingNumber("yzbqklnj");
    }
}
