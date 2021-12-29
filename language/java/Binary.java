
public class Binary {
    public static class LittleEndian {
        public static long asInt64(byte[] b){
            return ((long)b[0])| ((long)b[1])<<8| ((long)b[2])<<16| ((long)b[3])<<24|
                    ((long)b[4])<<32| ((long)b[5])<<40| ((long)b[6])<<48| ((long)b[7])<<56;
        }
        public static int asInt32(byte[] b){
            return ((int)b[0])| ((int)b[1])<<8| ((int)b[2])<<16| ((int)b[3])<<24;
        }
        public static byte[] asBytes(int v){
            byte[] b=new byte[4];
            b[0]= (byte) v;
            b[1]= (byte) (v>>8);
            b[2]= (byte) (v>>16);
            b[3]= (byte) (v>>24);
            return b;
        }
        public static byte[] asBytes(long v){
            byte[] b=new byte[8];
            b[0]= (byte) v;
            b[1]= (byte) (v>>8);
            b[2]= (byte) (v>>16);
            b[3]= (byte) (v>>24);
            b[4]= (byte) (v>>32);
            b[5]= (byte) (v>>40);
            b[6]= (byte) (v>>48);
            b[7]= (byte) (v>>56);
            return b;
        }

        public static void putInt32(byte[] b,int v){
            b[0]= (byte) v;
            b[1]= (byte) (v>>8);
            b[2]= (byte) (v>>16);
            b[3]= (byte) (v>>24);
        }
        public static void putInt64(byte[] b,long v){
            b[0]= (byte) v;
            b[1]= (byte) (v>>8);
            b[2]= (byte) (v>>16);
            b[3]= (byte) (v>>24);
            b[4]= (byte) (v>>32);
            b[5]= (byte) (v>>40);
            b[6]= (byte) (v>>48);
            b[7]= (byte) (v>>56);
        }
    }
    public static class BigEndian {
        public static int asInt32(byte[] b){
            return ((int)b[3])| ((int)b[2])<<8| ((int)b[1])<<16| ((int)b[0])<<24;
        }
        public static long asInt64(byte[] b){
            return ((long)b[7])| ((long)b[6])<<8| ((long)b[5])<<16| ((long)b[4])<<24|
                    ((long)b[3])<<32| ((long)b[2])<<40| ((long)b[1])<<48| ((long)b[0])<<56;
        }
        public static void putInt32(byte[] b,int v){
            b[3]= (byte) v;
            b[2]= (byte) (v>>8);
            b[1]= (byte) (v>>16);
            b[0]= (byte) (v>>24);
        }
        public static void putInt64(byte[] b,long v){
            b[7]= (byte) v;
            b[6]= (byte) (v>>8);
            b[5]= (byte) (v>>16);
            b[4]= (byte) (v>>24);
            b[3]= (byte) (v>>32);
            b[2]= (byte) (v>>40);
            b[1]= (byte) (v>>48);
            b[0]= (byte) (v>>56);
        }
        public static byte[] asBytes(int v){
            byte[] b=new byte[4];
            b[3]= (byte) v;
            b[2]= (byte) (v>>8);
            b[1]= (byte) (v>>16);
            b[0]= (byte) (v>>24);
            return b;
        }
        public static byte[] asBytes(long v){
            byte[] b=new byte[8];
            b[7]= (byte) v;
            b[6]= (byte) (v>>8);
            b[5]= (byte) (v>>16);
            b[4]= (byte) (v>>24);
            b[3]= (byte) (v>>32);
            b[2]= (byte) (v>>40);
            b[1]= (byte) (v>>48);
            b[0]= (byte) (v>>56);
            return b;
        }

    }
}
