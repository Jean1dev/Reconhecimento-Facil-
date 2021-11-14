package edu.usc.irds.tensorflow.grpc;

import java.io.*;
import java.nio.file.Files;
import java.util.List;
import java.util.Map;

public class ChecarImagem {

    public static void main(String[] args) throws Exception {
        File file = new File("img.jpg");
        TensorflowObjectRecogniser recogniser = new TensorflowObjectRecogniser("localhost", 9000);

        while (true) {
            if (file.exists()) {
                System.out.println("arquivo existe");

                System.out.println("Image = " + file.getAbsolutePath());
                InputStream jpegStream = new FileInputStream(file.getAbsolutePath());
                List<Map.Entry<String, Double>> list = recogniser
                        .recognise(jpegStream);

                Writer arquivo = new BufferedWriter(new FileWriter("output.txt", true));
                arquivo.append(String.valueOf(list));
                arquivo.append("\n");
                arquivo.close();
                System.out.println(list);
                jpegStream.close();
//                System.exit(0);
                if (!file.delete()) {
                    Files.delete(file.toPath());
                }
            }
        }
    }
}
