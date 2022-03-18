/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package edu.usc.irds.tensorflow.grpc;

import java.io.*;
import java.net.URL;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

/**
 * @author Thamme Gowda
 */
public class ImgFromUrl {

    public static void main(String[] args) throws Exception {
        args = Arrays.asList("localhost:9000", "https://cdn.discordapp.com/attachments/904857338853355540/954069669365575750/Screenshot_25.jpg").toArray(new String[1]);
        if (args.length != 2) {
            System.out.println("Invalid args");
            System.out.println("Usage: <host:port> <image>");
            System.out.println("\tExample: localhost:9090 ~/Pictures/cat.jpg");
            System.exit(1);
        }

        String[] parts = args[0].split(":");
        String server = parts[0];
        int port = Integer.parseInt(parts[1]);
        String imagePath = args[1];

        System.out.println("Image = " + imagePath);
        URL url = new URL(args[1]);
        InputStream in = new BufferedInputStream(url.openStream());
        OutputStream out = new BufferedOutputStream(new FileOutputStream("img.jpg"));

        for (int i; (i = in.read()) != -1; ) {
            out.write(i);
        }
        in.close();
        out.close();

        InputStream jpegStream = new FileInputStream("img.jpg");
        TensorflowObjectRecogniser recogniser = new TensorflowObjectRecogniser(server, port);
        List<Map.Entry<String, Double>> list = recogniser.recognise(jpegStream);
        System.out.println(list);
        recogniser.close();
        jpegStream.close();
    }

}
