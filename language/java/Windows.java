
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;
import java.util.StringTokenizer;

public final class Windows {
    private static final String OS = System.getProperty("os.name").toLowerCase();
    public static final String CRLF =System.getProperty("line.separator");
    public static String userHome(){
        return System.getProperty("user.home");
    }
    public static void printSystemProperties(){
        System.getProperties().list(System.out);
        System.out.println("-------system env------");
        for(String key:System.getenv().keySet()){
            System.out.println(key+"="+System.getenv(key));
        }
    }
    public static boolean isWindows(){
        return OS.contains("windows");
    }
    public static String getAdbPath() {
        Result result= execCmd("cmd /c wmic process list brief | findstr adb");
//        CommandUtils.Result result=CommandUtils.run("tasklist /fi \"imagename eq adb.exe\" /fo list");
        if(result.code==0){
            if(Ferba.MODE_MENU) System.out.println("[adb process list]:\n"+result.data);
            String[] row=result.data.split("\r\n")[0].split(" +");
            if(Ferba.MODE_MENU) System.out.println("[process id]:"+row[3]);
            result= execCmd("cmd /c wmic process where processid="+row[3]+" get executablepath");
            if(result.code==0){
                String[] split=result.data.split("(\r\n)+");
                return split.length>=2?split[1]:"adb";
            }
        }
        return "adb";
    }
    private  static Result execCmd(List<String> command, String charsetName) {
        if(Ferba.MODE_MENU) System.out.println("run:"+ command);
        Result result = new Result();
        InputStream is = null;
        try {
            Process process = new ProcessBuilder(command).redirectErrorStream(true).start();
            is = process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(is, charsetName));
            StringBuilder data = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                data.append(line).append(System.lineSeparator());
                //System.out.println( line);
            }
            result.code = process.waitFor();
            result.data = data.toString().trim();
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            //close stream
            try {
                is.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        return result;
    }
    private static Result execCmd(String command) {

        return execCmd(command, "UTF-8");
    }
    private static Result execCmd(String command, String charsetName) {
        StringTokenizer st = new StringTokenizer(command);
        String[] commandArray = new String[st.countTokens()];
        for (int i = 0; st.hasMoreTokens(); i++) {
            commandArray[i] = st.nextToken();
        }

        return execCmd(Arrays.asList(commandArray), charsetName);
    }
    private final static class Result {
        public int code;
        public String data;
    }
}
