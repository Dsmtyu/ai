package com.gitee.jack20081117.frog.utils;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.gitee.jack20081117.frog.Frog;
import com.gitee.jack20081117.frog.egg.Egg;
import com.gitee.jack20081117.frog.env.*;

public class EggTool {

    public static final boolean JSON_FILE_FORMAT=false;//是否存储为JSON格式

    /**
     *利用Java串行机制存盘，只有能量多的frog才有资格下蛋，进行下一轮运行，能量少的frog没有下蛋的资格
     */
    public static void layEggs(Env env) {
        sortFrogsOrderByEnergyDesc(env);//根据能量多少对Frog进行排序
        System.out.print("First frog energy="+env.frogs.get(0).energy);
        System.out.print(",  Last frog energy="+env.frogs.get(env.frogs.size()-1).energy+",  ");
        for (Frog frog:env.frogs){
            System.out.print(frog.energy+",");
        }
        System.out.println();
        try {
            List<Egg> newEggs=new ArrayList<Egg>();
            for (int i=0;i<env.EGG_QTY;i++)
                newEggs.add(env.frogs.get(i).layEgg());

            if (JSON_FILE_FORMAT) {//json
                String newEggsString=JSON.toJSONString(newEggs);
                FrogFileUtils.writeFile(Application.CLASSPATH+"eggs.json",newEggsString,"utf-8");
            } else {//ser
                FileOutputStream fo=new FileOutputStream(Application.CLASSPATH+"eggs.ser");
                ObjectOutputStream so=new ObjectOutputStream(fo);
                so.writeObject(newEggs);
                so.close();
            }
            env.eggs=newEggs;
            System.out.println("Saved "+env.eggs.size()+" eggs to file '"+Application.CLASSPATH+"eggs.ser"+"'");
        } catch (IOException e) {
            System.out.println(e);
        }
    }

    private static void sortFrogsOrderByEnergyDesc(Env env) {
        Collections.sort(env.frogs,new Comparator<Frog>() {
            public int compare(Frog a,Frog b) {
                if (a.energy>b.energy)
                    return -1;
                else if (a.energy==b.energy)
                    return 0;
                else
                    return 1;
            }
        });
    }

    /**
     * 从磁盘读入一批Egg
     */
    @SuppressWarnings("unchecked")
    public static void loadEggs(Env env) {
        boolean errorfound=false;
        if (JSON_FILE_FORMAT) {//json
            String eggsString=FrogFileUtils.readFile(Application.CLASSPATH+"eggs.json","utf-8");
            if (eggsString!=null) {
                List<JSONObject> jsonEggs=(List<JSONObject>) JSON.parse(eggsString);
                env.eggs=new ArrayList<Egg>();
                for (JSONObject json:jsonEggs) {
                    Egg egg=json.toJavaObject(Egg.class);
                    env.eggs.add(egg);
                }
                System.out.println("Loaded "+env.eggs.size()+" eggs from file '"+Application.CLASSPATH+"eggs.json"+"'.");
            } else
                errorfound=true;
        } else {//ser
            try {
                FileInputStream eggsFile=new FileInputStream(Application.CLASSPATH+"eggs.ser");
                ObjectInputStream eggsInputStream=new ObjectInputStream(eggsFile);
                env.eggs=(List<Egg>) eggsInputStream.readObject();
                System.out.println("Loaded "+env.eggs.size()+" eggs from file '"+Application.CLASSPATH+"eggs.ser"+"'.");
                eggsInputStream.close();
            } catch (Exception e) {
                errorfound=true;
            }
        }
        if (errorfound) {//找不到文件，那么就新建一批Egg
            System.out.println("No eggs files ' "+Application.CLASSPATH+" found, created "+env.EGG_QTY+" new eggs to do test.");
            env.eggs=new ArrayList<Egg>();
            for (int i=0;i<env.EGG_QTY;i++)
                env.eggs.add(Egg.createBrandNewEgg());
        }
    }

    /**
     * 删除Egg
     */
    public static void deleteEggs() {
        System.out.println("Delete exist egg file: '"+Application.CLASSPATH+"eggs.ser'");
        FrogFileUtils.deleteFile(Application.CLASSPATH+"eggs.ser");
    }

}
