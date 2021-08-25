package com.gitee.jack20081117.frog.env;

import java.io.File;

import javax.swing.JFrame;

/**
 * Application模块：项目的启动、关闭等基础服务
 */
public class Application {
    public static final String CLASSPATH;//项目路径，在我的电脑上是C:\Users\admin\Desktop\AI
    static {
        String classpath=new File("").getAbsolutePath();
        int i=classpath.indexOf("\\AI\\");
        CLASSPATH=classpath.substring(0,i)+"\\AI\\";//Windows
    }
    public static JFrame mainFrame=new JFrame();

    public static void main(String[] args) throws InterruptedException {
        mainFrame.setLayout(null);
        mainFrame.setSize(520,550); // 窗口大小
        mainFrame.setTitle("Frog test round: 0, time used: ? ms");
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 关闭时退出程序
        Env env=new Env();//虚拟环境
        mainFrame.add(env);
        mainFrame.setVisible(true);
        env.run();
    }
}
