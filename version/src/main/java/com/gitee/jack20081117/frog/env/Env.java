package com.gitee.jack20081117.frog.env;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import javax.swing.JPanel;

import com.gitee.jack20081117.frog.Frog;
import com.gitee.jack20081117.frog.egg.Egg;
import com.gitee.jack20081117.frog.utils.EggTool;

/**
 * Env模块：模拟的生物生存区域，将由Programmer全权控制，随着Frog的脑进化变得越来越复杂。
 */
@SuppressWarnings("serial")
public class Env extends JPanel {
    public static int SHOW_SPEED=1;//Speed of test:1~1000

    public static int STEPS_PER_ROUND=5000;

    public static final boolean DELETE_EGGS=true;//每次运行是否先删除保存的蛋

    public int ENV_XSIZE=300;//屏幕的宽度

    public int ENV_YSIZE=300;//屏幕的高度

    public byte[][] foods=new byte[ENV_XSIZE][ENV_YSIZE];//食物区域

    public int FOOD_QTY=2000;//食物总数，会在屏幕上随机出现

    public int EGG_QTY=80;

    public List<Frog> frogs=new ArrayList<Frog>();//frogs
    public List<Egg> eggs;//eggs

    static{
        System.out.println("Abrabrabra!");
        if (DELETE_EGGS)
            EggTool.deleteEggs();//运行先删除保存的蛋
    }

    public Env(){
        super();
        this.setLayout(null);
        this.setBounds(100,100,ENV_XSIZE,ENV_YSIZE);
    }

    private void rebuildFrogAndFood(){
        frogs.clear();
        for (int i=0;i<ENV_XSIZE; i++){// clear foods
            for (int j=0;j<ENV_YSIZE;j++){
                foods[i][j]=0;
            }
        }
        Random rand=new Random();
        for (int i=0;i<eggs.size();i++){ // 1个Egg生出4个Frog
            for (int j=0;j<4;j++){
                frogs.add(new Frog(ENV_XSIZE/2+rand.nextInt(90),ENV_YSIZE/2+rand.nextInt(90),eggs.get(i)));
            }
        }
        System.out.println("Created "+4*eggs.size()+" frogs");
        for (int i=0;i<FOOD_QTY;i++)//总共生成FOOD_QTY个food
            foods[rand.nextInt(ENV_XSIZE-3)][rand.nextInt(ENV_YSIZE-3)]=1;
    }

    private void drawFood(Graphics g){
        for (int x=0;x<ENV_XSIZE;x++)
            for (int y=0;y<ENV_YSIZE;y++)
                if (foods[x][y]>0){
                    g.fillOval(x,y,4,4);//画食物
                }
    }

    public void run() throws InterruptedException {
        EggTool.loadEggs(this);// 从磁盘加载egg，或新建一批egg
        int round=1;//运行次数
        Image buffImg=createImage(this.getWidth(),this.getHeight());
        Graphics g=buffImg.getGraphics();
        long t1,t2;
        do {
            t1=System.currentTimeMillis();//运行开始时间
            rebuildFrogAndFood();
            boolean allDead=false;
            for (int i=0;i<STEPS_PER_ROUND;i++){
                if(allDead)//循环提前解除的条件是frog全部死亡
                    break;
                allDead=true;
                for (Frog frog:frogs){
                    if (frog.active(this))//本frog还活着
                        allDead=false;//frog并没有全部死亡
                    if (frog.alive&&frog.moveCount==0&&i>100){// 如果不移动就死!
                        frog.alive=false;//frog死亡
                    }
                }
                if (i%SHOW_SPEED!=0)// 画frog会拖慢速度
                    continue;
                // 开始画frog
                g.setColor(Color.white);
                g.fillRect(0,0,this.getWidth(),this.getHeight());
                g.setColor(Color.BLACK);
                for (Frog frog:frogs)
                    frog.show(g);
                drawFood(g);//画食物
                Graphics graphics=this.getGraphics();
                graphics.drawImage(buffImg,0,0,this);
                Thread.sleep(10);
            }
            EggTool.layEggs(this);
            t2=System.currentTimeMillis();//运行结束时间
            Application.mainFrame.setTitle("Frog test round: "+round+", time used: "+(t2-t1)+" ms");//本次运行用时
            round++;
        } while (true);
    }
}
