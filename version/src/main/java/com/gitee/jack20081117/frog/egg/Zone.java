package com.gitee.jack20081117.frog.egg;

import java.io.Serializable;

public class Zone implements Serializable{
    private static final long serialVersionUID=3L;
    public float x;
    public float y;
    public float radius;

    public Zone(){
    }

    public Zone(float x,float y,float radius){
        this.x=x;
        this.y=y;
        this.radius=radius;
    }

    public boolean nearby(Zone z){
        float distance=radius+z.radius;
        if(Math.abs(x-z.x)<distance && Math.abs(y-z.y)<distance)
            return true;
        return false;
    }

    public int roundX(){
        return Math.round(x);
    }

    public int roundY(){
        return Math.round(y);
    }

    public static void copyXY(Zone from,Zone to){
        to.x=from.x;
        to.y=from.y;
    }
}
