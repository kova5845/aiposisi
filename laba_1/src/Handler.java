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
            String requestType = this.getRequestType(requestText);
            String requestUrl = this.getRequestUrl(requestText);
            System.out.println(requestType + " " + requestUrl);
            switch (requestType){
                case "POST":
                    System.out.println("server handle post request");
                    break;
                case "GET":
                    Path filePath = Path.of(this.directory + requestUrl);
                    if(Files.exists(filePath) && !Files.isDirectory(filePath)){
                        String extension = this.getFileExtension(filePath);
                        String type = CONTENT_TYPES.get(extension);
                        byte[] fileBytes = Files.readAllBytes(filePath);
                        this.sendHeader(output, 200, "OK", type, fileBytes.length);
                        output.write(fileBytes);
                    } else{
                        String type = CONTENT_TYPES.get("text");
                        this.sendHeader(output, 404, "Not Found", type, NOT_FOUND_MESSAGE.length());
                        output.write(NOT_FOUND_MESSAGE.getBytes());
                    }
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
        var reader = new Scanner(input).useDelimiter("\r\n");
        var line = reader.next();
        String[] arr = line.split(" ");
        return arr[0] + " " + arr[1];
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

    private void sendHeader(OutputStream output, int statusCode, String statusText, String type, long length){
        var ps = new PrintStream(output);
        ps.printf("HTTP/1.1 %s %s%n", statusCode, statusText);
        ps.printf("Content-Type: %s%n", type);
        ps.printf("Content-Length: %s%n%n", length);
    }
}
