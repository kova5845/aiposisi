import java.io.*;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Handler extends Thread{

    private static final Map<String, String> CONTENT_TYPES = new HashMap<>(){{
        put("png", "image/png");
        put("html", "text/html");
        put("css", "text/css");
        put("txt", "text/plain");
        put("js", "text/javascript");
        put("svg", "image/svg+xml");
        put("", "text/plain");
    }};

    private static final String NOT_FOUND_MESSAGE = "NOT FOUND";
    private Socket socket;
    private String directory;

    public Handler(Socket socket, String directory) {
        this.socket = socket;
        this.directory = directory;
    }

    @Override
    public void run() {
        try {
            InputStream input = this.socket.getInputStream();
            OutputStream output = this.socket.getOutputStream();
            String requestText = this.getRequestText(input);
            System.out.println(requestText);
            String requestType = this.getRequestType(requestText);
            String requestUrl = this.getRequestUrl(requestText);
            switch (requestType){
                case "POST":
                    System.out.println("server handle post request");
                    break;
                case "GET":
                    Path filePath = Path.of(this.directory + requestUrl);
                    String answerText = "";
                    if(Files.exists(filePath) && !Files.isDirectory(filePath)){
                        String extension = this.getFileExtension(filePath);
                        String type = CONTENT_TYPES.get(extension);
                        byte[] fileBytes = Files.readAllBytes(filePath);
                        answerText = this.sendHeader(output, 200, "OK", type, fileBytes.length, requestType);
                        output.write(fileBytes);
                    } else{
                        String type = CONTENT_TYPES.get("text");
                        answerText = this.sendHeader(output, 404, "Not Found", type, NOT_FOUND_MESSAGE.length(), requestType);
                        output.write(NOT_FOUND_MESSAGE.getBytes());
                    }
                    this.writeLog(requestText, answerText);
                    break;
                case "OPTIONS":
                    System.out.println("server handle option request");
                    break;
                default:
                    System.out.println("DEFAULT");
            }

        } catch (IOException e){
            e.printStackTrace();
        }
    }

    private String getRequestText(InputStream input) throws IOException{
        Scanner reader = new Scanner(input);
        String line = "";
        int i = 10;
        while (reader.hasNext() && i > 0) {
            line += reader.nextLine() + "\n";
            i--;
        }
        return line;
    }

    private String getRequestType(String input){
        return input.split(" ")[0];
    }

    private String getRequestUrl(String input){
        return input.split(" ")[1];
    }

    private String getFileExtension(Path path){
        String name = path.getFileName().toString();
        int extensionStart = name.lastIndexOf(".");
        return  extensionStart == -1 ? "" : name.substring(extensionStart + 1);
    }

    private String sendHeader(OutputStream output, int statusCode, String statusText, String type, long length, String requestType){
        PrintStream ps = new PrintStream(output);
        String answer = "";
        File file = new File("D://aiposisi//laba_1//Config.txt");
        try (FileInputStream fin = new FileInputStream(file)) {
            answer = new String(fin.readAllBytes());
            answer = String.format(answer, statusCode, statusText, type, length, "localhost", requestType);
            System.out.println(answer);
            output.write(answer.getBytes());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return answer;
    }

    private void writeLog(String requestText, String answerText) {
        try{
            File file = new File("D://aiposisi//laba_1//file.log");
            file.createNewFile();
            FileOutputStream fout = new FileOutputStream(file, false);
            byte[] bufferRequest = requestText.getBytes();
            fout.write(bufferRequest, 0, bufferRequest.length);
            fout.write("\n\n".getBytes());
            byte[] bufferAnswer = answerText.getBytes();
            fout.write(bufferAnswer, 0, bufferAnswer.length);


        } catch(IOException e){
            System.out.println(e);
        }

    }
}
