package com.gitee.jack20081117.frog.egg;

import java.io.Serializable;
import java.util.Random;

public class Egg implements Serializable{
    private static final long serialVersionUID=2L;
    public static final int CELL_GROUP_QTY=30;
    public float brainRadius=1000;
    public CellGroup[] cellgroups;

    public static Egg createBrandNewEgg(){
        Egg egg=new Egg();
        Random r=new Random();
        egg.cellgroups=new CellGroup[CELL_GROUP_QTY];
        for(int i=0;i<CELL_GROUP_QTY;i++){
            CellGroup cellGroup=new CellGroup();
            egg.cellgroups[i]=cellGroup;
            cellGroup.groupInputZone=new Zone(r.nextFloat()*egg.brainRadius,r.nextFloat()*egg.brainRadius,
                    (float)(r.nextFloat()*egg.brainRadius*.01));
            cellGroup.groupOutputZone=new Zone(r.nextFloat()*egg.brainRadius,r.nextFloat()*egg.brainRadius,
                    (float)(r.nextFloat()*egg.brainRadius*.01));
            cellGroup.cellQty=r.nextInt(10);
            cellGroup.cellInputRadius=(float)(r.nextFloat()*0.001);
            cellGroup.cellOutputRadius=(float)(r.nextFloat()*0.001);
            cellGroup.inputQtyPerCell=r.nextInt(10);
            cellGroup.outputQtyPerCell=r.nextInt(5);
        }
        return egg;
    }
}
