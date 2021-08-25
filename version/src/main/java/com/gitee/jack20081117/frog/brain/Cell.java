package com.gitee.jack20081117.frog.brain;

/**
 * Cell is a brain nerve cell,which is the basic unit of frog's brain
 */

public class Cell {
    public int group;//this cell belongs to which group?
    public Input[] inputs;//inputs of cell,float array format like {(x1,y1),(x2,y2),...}
    public Output[] outputs;//outputs of cell,float array format like {(x1,y1),(x2,y2),...}

    public void activate(){
        for(Input xy:inputs){
        }
    }
}
