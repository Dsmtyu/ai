package com.gitee.jack20081117.frog;

import java.awt.Graphics;
import java.awt.Image;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import javax.imageio.ImageIO;

import com.gitee.jack20081117.frog.brain.Cell;
import com.gitee.jack20081117.frog.brain.Input;
import com.gitee.jack20081117.frog.brain.Output;
import com.gitee.jack20081117.frog.egg.CellGroup;
import com.gitee.jack20081117.frog.egg.Egg;
import com.gitee.jack20081117.frog.egg.Zone;
import com.gitee.jack20081117.frog.env.Application;
import com.gitee.jack20081117.frog.env.Env;

public class Frog {
    public float brainRadius;

    List<Cell> cells=new ArrayList<Cell>();

    public static Zone eye=new Zone(0,0,300);/* 眼睛暂时用不着，先忽略 */

    /* 运动细胞的输入区在脑中的坐标，先随便取就可以了，以后再考虑放到蛋里去进化 */
    public static Zone moveUp=new Zone(500,50,10);
    public static Zone moveDown=new Zone(500,100,10);
    public static Zone moveLeft=new Zone(500,150,10);
    public static Zone moveRight=new Zone(500,200,10);
    public static Zone moveRandom=new Zone(500,300,10);

    public int x;
    public int y;
    public long energy=10000;
    public Egg egg;
    public boolean alive=true; // set to false if dead
    public int moveCount=0; // how many times it moved

    static final Random r=new Random();
    static Image frogImg;
    static {
        try {
            frogImg=ImageIO.read(new FileInputStream(Application.CLASSPATH+"frog.png"));//生成Frog 图像
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public Frog(int x,int y,Egg egg) {
        this.x=x;
        this.y=y;
        if (egg.cellgroups==null)
            throw new IllegalArgumentException("Illegal egg cellgroups argument!");
        this.brainRadius=egg.brainRadius;
        for (int k=0;k<egg.cellgroups.length;k++) {
            CellGroup g=egg.cellgroups[k];
            for (int i=0;i<g.cellQty;i++) {// 开始根据蛋来创建脑细胞
                Cell c=new Cell();
                c.inputs=new Input[g.inputQtyPerCell];
                for (int j=0;j<g.inputQtyPerCell;j++) {
                    c.inputs[j]=new Input();
                    c.inputs[j].cell=c;
                    Zone.copyXY(randomPosInZone(g.groupInputZone),c.inputs[j]);
                    c.inputs[j].radius=g.cellInputRadius;
                }
                c.outputs=new Output[g.outputQtyPerCell];
                for (int j=0;j<g.outputQtyPerCell;j++) {
                    c.outputs[j]=new Output();
                    c.outputs[j].cell=c;
                    Zone.copyXY(randomPosInZone(g.groupInputZone),c.outputs[j]);
                    c.outputs[j].radius=g.cellOutputRadius;
                }
                cells.add(c);
            }
        }
        this.egg=egg;// 保留一份蛋，如果没被淘汰掉，将来下蛋时要用这个蛋来下新蛋
    }

    /** Active a frog, if frog is dead return false */
    public boolean active(Env env) {
        if (!alive)
            return false;
        if (x<0||x>=env.ENV_XSIZE||y<0||y>=env.ENV_YSIZE) {// 超出边界的青蛙死去
            alive=false;
            return false;
        }

        // move
        for (Cell cell:cells) {
            for (Output output:cell.outputs) {
                if (moveUp.nearby(output))
                    moveUp(env);
                if (moveDown.nearby(output))
                    moveDown(env);
                if (moveLeft.nearby(output))
                    moveLeft(env);
                if (moveRight.nearby(output))
                    moveRight(env);
                if (moveRandom.nearby(output))
                    moveRandom(env);
            }
        }
        return true;
    }

    /** 如果青蛙位置与food重合，吃掉它 */
    private void checkFoodAndEat(Env env) {
        boolean eatedFood=false;
        if (x>=0 && x<env.ENV_XSIZE && y>0 && y<env.ENV_YSIZE)
            if (env.foods[x][y]>0) {
                env.foods[x][y]=0;
                energy=energy+1000;// 吃掉food，能量增加
                eatedFood=true;
            }
        // 奖励
        if (eatedFood) {
        }
    }

    private void moveRandom(Env env) {//随机进行运动
        int ran=r.nextInt(4);
        if (ran==0)
            moveUp(env);
        if (ran==1)
            moveDown(env);
        if (ran==2)
            moveLeft(env);
        if (ran==3)
            moveRight(env);
    }

    private void moveUp(Env env) {//向上运动
        y+=1;
        if (y<0||y>=env.ENV_YSIZE) {
            alive=false;
            return;
        }
        checkFoodAndEat(env);
    }

    private void moveDown(Env env) {//向下运动
        y-=1;
        if (y<0||y>=env.ENV_YSIZE) {
            alive=false;
            return;
        }
        checkFoodAndEat(env);
    }

    private void moveLeft(Env env) {//向左运动
        x-=1;
        if (x<0||x>=env.ENV_XSIZE) {
            alive=false;
            return;
        }
        checkFoodAndEat(env);
    }

    private void moveRight(Env env) {//向右运动
        x+=1;
        if (x<0||x>=env.ENV_XSIZE) {
            alive=false;
            return;
        }
        checkFoodAndEat(env);
    }

    private boolean allowVariation=false;//是否允许变异

    private float percet1(float f) {//变异后差别控制在1%
        if (!allowVariation)
            return f;
        return (float)(f*(0.99f+r.nextFloat()*0.02));
    }

    private float percet5(float f) {//变异后差别控制在5%
        if (!allowVariation)
            return f;
        return (float)(f*(0.95f+r.nextFloat()*0.10));
    }

    private static Zone randomPosInZone(Zone z) {
        return new Zone(z.x-z.radius+z.radius*2*r.nextFloat(),z.y-z.radius+z.radius*2*r.nextFloat(),0);
    }

    public Egg layEgg() {
        if (r.nextInt(100)>25) // 变异率先固定在25%
            allowVariation=false;// 如果不允许变异，下的蛋就相当于克隆原来的蛋
        else
            allowVariation=true;
        Egg newEgg=new Egg();
        newEgg.brainRadius=percet5(egg.brainRadius);
        CellGroup[] cellgroups=new CellGroup[egg.cellgroups.length];
        newEgg.cellgroups=cellgroups;
        for (int i=0;i<cellgroups.length;i++) {
            /*oldGp指的是原来egg的cellgroup
            * cellGroup是新的egg的cellgroup*/
            CellGroup cellGroup=new CellGroup();
            cellgroups[i]=cellGroup;
            CellGroup oldGp=egg.cellgroups[i];
            cellGroup.groupInputZone=new Zone(percet5(oldGp.groupInputZone.x),percet5(oldGp.groupInputZone.y),
                    percet5(oldGp.groupInputZone.radius));
            cellGroup.groupOutputZone=new Zone(percet5(oldGp.groupOutputZone.x),percet5(oldGp.groupOutputZone.y),
                    percet5(oldGp.groupOutputZone.radius));
            cellGroup.cellQty=Math.round(percet5(oldGp.cellQty));
            cellGroup.cellInputRadius=percet1(oldGp.cellInputRadius);
            cellGroup.cellOutputRadius=percet1(oldGp.cellOutputRadius);
            cellGroup.inputQtyPerCell=Math.round(percet5(oldGp.inputQtyPerCell));
            cellGroup.outputQtyPerCell=Math.round(percet5(oldGp.outputQtyPerCell));
        }
        return newEgg;
    }

    public void show(Graphics g) {
        if (!alive)
            return;
        g.drawImage(frogImg,x-8,y-8,16,16,null);
    }
}
