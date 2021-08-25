package com.gitee.jack20081117.frog.utils;

import java.io.*;

public class FrogFileUtils {
    private FrogFileUtils(){
    }

    public static boolean deleteFile(String fileFullPath){
        File file=new File(fileFullPath);
        return file.delete();
    }

    public static void writeFile(String fileFullPath,byte[] byteArray){
        File file=new File(fileFullPath);
        if(!file.getParentFile().exists())
            file.getParentFile().mkdirs();
        FileOutputStream fos=null;
        try {
            fos=new FileOutputStream(file);
            fos.write(byteArray);
            fos.close();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if(fos!=null){
                try {
                    try {
                        fos.flush();
                    } catch (Exception e) {
                    }
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void writeFile(String fileFullPath,String text,String encoding){
        File file=new File(fileFullPath);
        if (!file.getParentFile().exists())
            file.getParentFile().mkdirs();
        FileOutputStream fos=null;
        try {
            fos=new FileOutputStream(file);
            byte[] bytes;
            bytes=text.getBytes(encoding);
            fos.write(bytes);
            fos.close();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (fos!=null) {
                try {
                    try {
                        fos.flush();
                    } catch (Exception e) {
                    }
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static String readFile(String fileFullPath,String encoding){
        InputStream inputStream;
        try {
            inputStream=new FileInputStream(new File(fileFullPath));
        } catch (FileNotFoundException e) {
            return null;
        }
        try {
            ByteArrayOutputStream result=new ByteArrayOutputStream();
            byte[] buffer=new byte[1024];
            int length;
            while ((length=inputStream.read(buffer))!=-1)
                result.write(buffer,0,length);
            String string=result.toString(encoding);
            return string;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        } finally {
            try {
                inputStream.close();
            } catch (IOException e) {
            }
        }
    }

    public static void appendFile(String fileName,String content) {
        FileOutputStream fos=null;
        try {
            fos=new FileOutputStream(fileName,true);
            fos.write(content.getBytes());
            fos.write("\r\n".getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fos!=null) {
                try {
                    try {
                        fos.flush();
                    } catch (Exception e) {
                    }
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
