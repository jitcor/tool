import java.io.InputStream;
import java.io.OutputStream;

public class StreamUtils {
    public static void copy(InputStream inputStream, OutputStream outputStream,boolean close){
        byte[] buffer=new byte[1024];
        int n=0;
        try {
            while ((n = inputStream.read(buffer)) > 0) {
                outputStream.write(buffer, 0, n);
                outputStream.flush();
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        if(close){
            try {
                inputStream.close();
                outputStream.close();
            }catch (Exception e){
                e.printStackTrace();
            }
        }
    }
    public static void copyN(InputStream inputStream, OutputStream outputStream,int length,boolean close){
        if(length<=0)return;
        byte[] buffer=new byte[Math.min(length,1024)];
        int n=0;
        try {
            while ((n = inputStream.read(buffer)) > 0) {
                outputStream.write(buffer, 0, n);
                outputStream.flush();
                length-=n;
                if(length<1024){
                    buffer=new byte[length];
                }
            }
        }catch (Exception e){
            e.printStackTrace();
        }
        if(close){
            try {
                inputStream.close();
                outputStream.close();
            }catch (Exception e){
                e.printStackTrace();
            }
        }
    }
}
