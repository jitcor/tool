
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class ByteStream {
    public static void copy(byte[] data, OutputStream outputStream) {
        InputStream inputStream = new ByteArrayInputStream(data);
        byte[] buffer = new byte[1024];
        int n = 0;
        try {
            while ((n = inputStream.read(buffer)) > 0) {
                outputStream.write(buffer, 0, n);
                outputStream.flush();
            }
        } catch (Exception e) {
            e.printStackTrace();

        }
    }

    public static void copy(InputStream inputStream, byte[] data) {
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        int len = data.length;
        byte[] buffer = new byte[1024];
        int n = 0;
        try {
            while ((n = inputStream.read(buffer)) > 0) {
                outputStream.write(buffer, 0, n);
                outputStream.flush();
                len-=n;
                if(len==0)break;
                if(len<1024){
                    buffer=new byte[len];
                }
            }
        } catch (Exception e) {
            e.printStackTrace();

        }
    }

}
