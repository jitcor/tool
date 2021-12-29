
public class Binary {
    public static class LittleEndian {
        public static long asInt64(byte[] b) {
            return ((long) b[0] & 0xff) | ((long) b[1] & 0xff) << 8 | ((long) b[2] & 0xff) << 16 | ((long) b[3] & 0xff) << 24 |
                    ((long) b[4] & 0xff) << 32 | ((long) b[5] & 0xff) << 40 | ((long) b[6] & 0xff) << 48 | ((long) b[7] & 0xff) << 56;
        }

        public static int asInt32(byte[] b) {
            return ((int) b[0] & 0xff) | ((int) b[1] & 0xff) << 8 | ((int) b[2] & 0xff) << 16 | ((int) b[3] & 0xff) << 24;
        }

        public static byte[] asBytes(int v) {
            byte[] b = new byte[4];
            b[0] = (byte) (v&0xff);
            b[1] = (byte) ((v >> 8)&0xff);
            b[2] = (byte) ((v >> 16)&0xff);
            b[3] = (byte) ((v >> 24)&0xff);
            return b;
        }

        public static byte[] asBytes(long v) {
            byte[] b = new byte[8];
            b[0] = (byte) (v&0xff);
            b[1] = (byte) ((v >> 8)&0xff);
            b[2] = (byte) ((v >> 16)&0xff);
            b[3] = (byte) ((v >> 24)&0xff);
            b[4] = (byte) ((v >> 32)&0xff);
            b[5] = (byte) ((v >> 40)&0xff);
            b[6] = (byte) ((v >> 48)&0xff);
            b[7] = (byte) ((v >> 56)&0xff);
            return b;
        }

        public static void putInt32(byte[] b, int v) {
            b[0] = (byte) (v & 0xff);
            b[1] = (byte) ((v >> 8) & 0xff);
            b[2] = (byte) ((v >> 16) & 0xff);
            b[3] = (byte) ((v >> 24) & 0xff);
        }

        public static void putInt64(byte[] b, long v) {
            b[0] = (byte) (v&0xff);
            b[1] = (byte) ((v >> 8)&0xff);
            b[2] = (byte) ((v >> 16)&0xff);
            b[3] = (byte) ((v >> 24)&0xff);
            b[4] = (byte) ((v >> 32)&0xff);
            b[5] = (byte) ((v >> 40)&0xff);
            b[6] = (byte) ((v >> 48)&0xff);
            b[7] = (byte) ((v >> 56)&0xff);
        }
    }

    public static class BigEndian {
        public static int asInt32(byte[] b) {
            return ((int) b[3] & 0xff) | ((int) b[2] & 0xff) << 8 | ((int) b[1] & 0xff) << 16 | ((int) b[0] & 0xff) << 24;
        }

        public static long asInt64(byte[] b) {
            return ((long) b[7] & 0xff) | ((long) b[6] & 0xff) << 8 | ((long) b[5] & 0xff) << 16 | ((long) b[4] & 0xff) << 24 |
                    ((long) b[3] & 0xff) << 32 | ((long) b[2] & 0xff) << 40 | ((long) b[1] & 0xff) << 48 | ((long) b[0] & 0xff) << 56;
        }

        public static void putInt32(byte[] b, int v) {
            b[3] = (byte) (v&0xff);
            b[2] = (byte) ((v >> 8)&0xff);
            b[1] = (byte) ((v >> 16)&0xff);
            b[0] = (byte) ((v >> 24)&0xff);
        }

        public static void putInt64(byte[] b, long v) {
            b[7] = (byte) (v&0xff);
            b[6] = (byte) ((v >> 8)&0xff);
            b[5] = (byte) ((v >> 16)&0xff);
            b[4] = (byte) ((v >> 24)&0xff);
            b[3] = (byte) ((v >> 32)&0xff);
            b[2] = (byte) ((v >> 40)&0xff);
            b[1] = (byte) ((v >> 48)&0xff);
            b[0] = (byte) ((v >> 56)&0xff);
        }

        public static byte[] asBytes(int v) {
            byte[] b = new byte[4];
            b[3] = (byte) (v&0xff);
            b[2] = (byte) ((v >> 8)&0xff);
            b[1] = (byte) ((v >> 16)&0xff);
            b[0] = (byte) ((v >> 24)&0xff);
            return b;
        }

        public static byte[] asBytes(long v) {
            byte[] b = new byte[8];
            b[7] = (byte) (v&0xff);
            b[6] = (byte) ((v >> 8)&0xff);
            b[5] = (byte) ((v >> 16)&0xff);
            b[4] = (byte) ((v >> 24)&0xff);
            b[3] = (byte) ((v >> 32)&0xff);
            b[2] = (byte) ((v >> 40)&0xff);
            b[1] = (byte) ((v >> 48)&0xff);
            b[0] = (byte) ((v >> 56)&0xff);
            return b;
        }

    }
}
